import pandas as pd
from .models import Consumer
def all():
    consumers = Consumer.objects.all()
    fields = ['site__village', 'site__census', 'site__habitation', 'name', 'consumer_no', 'edate', 'status', 'aadhar', 'meter_no', 'apl_bpl', 'mobile_no', 'voter_no', 'tariff', 'pdc_date', 'address1', 'address2', 'site__district', 'remark']
    # df = pd.DataFrame(consumers.values(*CFIELDS))
    df = pd.DataFrame(consumers.values(*fields))
    df = df.fillna('')
    df.to_excel('outputs/saub_consumers.xlsx')
    
def divwise():
    divs = Consumer.objects.values('site__division').distinct()
    for div in divs:
        division = div['site__division']
        consumers = Consumer.objects.filter(site__division = division)
        fields = ['id','site__village', 'site__census', 'site__habitation', 'name', 'consumer_no', 'edate2', 'status', 'aadhar', 'meter_no', 'apl_bpl', 'mobile_no', 'voter_no', 'tariff', 'pdc_date', 'address1', 'address2', 'site__district', 'remark']
        df = pd.DataFrame(consumers.values(*fields))
        df = df.fillna('')
        df.to_excel(f'outputs/saub_consumers_div_{division}.xlsx')
def distwise():
    dists = Consumer.objects.values('site__district').distinct()
    for div in dists:
        district = div['site__district']
        consumers = Consumer.objects.filter(site__district = district)
        fields = ['id','site__village', 'site__census', 'site__habitation', 'name', 'consumer_no', 'edate2', 'status', 'aadhar', 'meter_no', 'apl_bpl', 'mobile_no', 'voter_no', 'tariff', 'pdc_date', 'address1', 'address2', 'site__district', 'site__division', 'remark']
        df = pd.DataFrame(consumers.values(*fields))
        df = df.fillna('')
        df.to_excel(f'outputs/saub_consumers_dist_{district}.xlsx')
def fordist(district):
    consumers = Consumer.objects.filter(site__district = district)
    fields = ['id','site__village', 'site__census', 'site__habitation', 'name', 'consumer_no', 'edate2', 'status', 'aadhar', 'meter_no', 'apl_bpl', 'mobile_no', 'voter_no', 'tariff', 'pdc_date', 'address1', 'address2', 'site__district', 'site__division', 'remark']
    df = pd.DataFrame(consumers.values(*fields))
    df = df.fillna('')
    df.to_excel(f'outputs/saub_consumers_dist_{district}.xlsx')
    
def fordiv(divs):
    # divs = Consumer.objects.values('site__division').distinct()
    for division in divs:
        consumers = Consumer.objects.filter(site__division = division)
        fields = ['site__village', 'site__census', 'site__habitation', 'name', 'consumer_no', 'edate2', 'status', 'aadhar', 'meter_no', 'apl_bpl', 'mobile_no', 'voter_no', 'tariff', 'pdc_date', 'address1', 'address2', 'site__district', 'remark']
        df = pd.DataFrame(consumers.values(*fields))
        df = df.fillna('')

        df.to_excel(f'outputs/saub_consumers_div_{division}.xlsx')

# fordiv()