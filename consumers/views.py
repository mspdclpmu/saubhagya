from django.shortcuts import render, HttpResponseRedirect, reverse
from django.views.decorators.csrf import ensure_csrf_cookie
from django.http import JsonResponse
from numpy.core.numeric import NaN
import pandas as pd
from django.contrib import messages
from .models import Consumer
from work.models import Site
from work.functions import getHabID
from django.db.models import F, Sum, Count, Q, FileField
from .codes import CFIELDS
from consumers.models import formatString, genCode, getConsumerID


@ensure_csrf_cookie
def index(request):
    data = getData()
    return render(request, "consumers/index.html", {'data': data})


def getData():
    cs = Consumer.objects.all()
    crural = cs.filter(census__lt=799999).values(
        'site__district').annotate(
            no_habs = Count('site__habitation', distinct=True),
            bpl=Count('apl_bpl', filter=Q(apl_bpl='BPL')), 
            apl=Count('apl_bpl', filter=Q(apl_bpl='APL')), 
            unknown=Count('apl_bpl', filter=Q(apl_bpl=None)))
    df = pd.DataFrame(crural).fillna('None')
    df.set_index('site__district', inplace=True)
    # curban = Consumer.objects.filter(census__gt=799999).values(
    #     'site__district', 'apl_bpl').annotate(records=Count('site__hab_id'))
    curban = cs.filter(census__gt=799999).values(
        'site__district').annotate(
            no_habs = Count('site__habitation', distinct=True),
            bpl=Count('apl_bpl', filter=Q(apl_bpl='BPL')), 
            apl=Count('apl_bpl', filter=Q(apl_bpl='APL')), 
            unknown=Count('apl_bpl', filter=Q(apl_bpl=None)))
    df2 = pd.DataFrame(curban).fillna('None')
    df2.set_index('site__district', inplace=True)
    # c = Consumer.objects.filter(isInPortal=True).values(
    #     'district').annotate(count=Count('name'))
    # dfp = pd.DataFrame(c).fillna('None')
    # dfp.set_index('district', inplace=True)
    # df['in portal '] = dfp
    dfdiv = pd.DataFrame(cs.values('site__division').annotate(hh=Count('consumer_no')))
    return '<div style="display: flex;"><div>Rural<br>' + df.to_html() + '</div><div>Urban<BR>' + df2.to_html() +'</div><div>'+ dfdiv.to_html()+ '</div></div>'


def upload(request):
    # TODO: find site first and update
    if(not request.method == 'POST'):
        return render(request, "consumers/index.html")
    file = request.FILES['file']
    upid = request.POST['upid']
    df = pd.read_excel(file, 'upload')
    df = df.fillna('')
    df_template = pd.read_excel('files/template_consumer_details.xlsx')
    cols = df_template.columns
    truths = [col in df.columns for col in df_template.columns]
    ifmatch = all(truths)
    ncreated = 0
    nupdated = 0
    if(not ifmatch):
        notmatch = [df_template.columns[i]
                    for i, col in enumerate(truths) if not col]
        messages.error(request, "Field not found– ")
        messages.error(request, notmatch)
        return HttpResponseRedirect(reverse('consumers:index'))
    for index, row in df.iterrows():
        # unique_together = ('census', 'habitation', 'name', 'consumer_no')
        # print('Processing..')
        # print(row)
        census = row[cols[0]]
        habitation = " ".join(str(row[cols[1]]).split()).upper()
        name = " ".join(str(row[cols[3]]).split()).upper()
        consumer_no = str(row[cols[7]]).replace(" ", "").upper()
        consumer, created = Consumer.objects.get_or_create(
            consumer_id=getConsumerID(census, consumer_no, name)
        )
        if(created):
            ncreated += 1
        else:
            nupdated += 1
        # consumer.village = row[cols[]]
        changed = False
        if(census):
            changed = True
            consumer.census = census
        if(habitation):
            changed = True
            consumer.habitation = habitation
        if(name):
            changed = True
            consumer.name = name
        if(consumer_no):
            changed = True
            consumer.consumer_no = consumer_no
        if(row[cols[2]]):
            consumer.edate = row[cols[2]]
            changed = True
        if(row[cols[11]]):
            consumer.status = row[cols[11]]
            changed = True
        if(row[cols[5]]):
            consumer.aadhar = row[cols[5]]
            changed = True
        if(row[cols[8]]):
            consumer.meter_no = row[cols[8]]
            changed = True
        if(row[cols[6]]):
            consumer.apl_bpl = row[cols[6]]
            changed = True
        if(row[cols[4]]):
            consumer.mobile_no = row[cols[4]]
            changed = True
        if(row[cols[9]]):
            consumer.voter_no = row[cols[9]]
            changed = True
        if(row[cols[10]]):
            consumer.tariff = row[cols[10]]
            changed = True
        if(row[cols[12]]):
            consumer.pdc_date = row[cols[12]]
            changed = True
        if(row[cols[13]]):
            consumer.address1 = row[cols[13]]
            changed = True
        if(row[cols[14]]):
            consumer.address2 = row[cols[14]]
            changed = True
        if(row[cols[15]]):
            consumer.remark = row[cols[15]]
            changed = True

        censusSite = Site.objects.filter(census=row[cols[0]]).first()
        if(censusSite):
            consumer.district = censusSite.district
            consumer.village = censusSite.village

        consumer.changeid = upid
        hab_id = getHabID(census=row[cols[0]], habitation=row[cols[1]])
        consumer.hab_id = hab_id
        if(Site.objects.filter(hab_id=hab_id).exists()):
            site = Site.objects.get(hab_id=hab_id)
            consumer.site = site
        if(changed):
            try:
                consumer.save()
            except Exception as ex:
                messages.error(request, ex.__str__())
                print('Processing..')
                print(row)
                print(ex)
    messages.success(request, '{} updated. {} uploaded of {} records'.format(
        nupdated, ncreated, len(df)))
    return HttpResponseRedirect(reverse('consumers:index'))


def api_getConsumers(request):
    if(request.method != 'POST'):
        return JsonResponse(
            'nothing to do'
        )
    filterString = {}

    habid = request.POST.get('habid', None)
    if(habid):
        filterString['site__hab_id__icontains'] = habid
        print(habid)

    address = request.POST.get('address', None)
    if(address):
        filterString['address1__icontains'] = address

    name = request.POST.get('name', None)
    if(name):
        filterString['name__icontains'] = formatString(name)

    consumer_no = request.POST.get('consumer_no', None)
    if(consumer_no):
        filterString['consumer_no__icontains'] = genCode(consumer_no)

    consumer_id = request.POST.get('consumer_id', None)
    if(consumer_id):
        filterString['consumer_id__exact'] = genCode(consumer_id)

    habid_exact = request.POST.get('habid_exact', None)
    if(habid_exact):
        filterString['site__hab_id__exact'] = genCode(habid_exact)

    inPortal = request.POST.get('inPortal', None)
    if(inPortal):
        filterString['isInPortal'] = True

    village = request.POST.get('village', None)
    if(village):
        filterString['site__village__icontains'] = formatString(village)

    consumers = Consumer.objects.filter(
        **filterString).order_by('name', 'site__census')
    header = consumers.values('site__village', 'site__census', 'site__habitation', 'site__district', 'site__division').order_by(
    ).annotate(count=Count('site__habitation'))
    dfheader = pd.DataFrame(header)
    fields = ['site__village', 'site__census', 'site__habitation', 'name', 'consumer_no', 'edate2', 'status', 'aadhar', 'meter_no',
              'apl_bpl', 'mobile_no', 'voter_no', 'tariff', 'pdc_date', 'address1', 'address2', 'site__district','site__division', 'remark']
    # df = pd.DataFrame(consumers.values(*CFIELDS))
    df = pd.DataFrame(consumers.values(*fields, 'id'))
    # print(df.head())
    if(not df.empty):
        df = df.fillna('')
        df = df.applymap(lambda x: '' if x=='nan' else x)
        df['edit'] = df.loc[:, 'id'].map(
            lambda x: '<a target="_blank" href=/admin/consumers/consumer/' + str(x) + '>edit</a>')
        df['delete'] = df.loc[:, 'id'].map(
            lambda x: '<a target="_blank" href=/admin/consumers/consumer/' + str(x) + '/delete/>delete</a>')
        # df.head()
        df1 = df.loc[:, [*fields, 'edit', 'delete',]]
        df1.iloc[:, :-3].to_excel('outputs/filtered_consumers.xlsx')
        datajson = list(df1.T.to_dict().values())
        # print(df1.iloc[:,5:].head())
        # print(datajson)
        return JsonResponse({'consumers': datajson, 'count': len(df1), 'header': dfheader.to_html()})
    else:
        return JsonResponse({'status': "no data"})
