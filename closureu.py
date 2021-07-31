'''
1. check the list of infra habitations
2. check missing hh habitations if any
3. check hh numbers for all habs
'''

'''
input file: macro
field map:
'''
from work.models import Loa, ProgressQty, Site
import pandas as pd
from work.controller import getSite, getHabID
from work.controller import getSiteProgressdf
from consumers.models import Consumer
from django.db.models import Count, F, Q
from pprint import pprint

def run():
    skip_rows = 5

    HT = 'Weasel Conductor on Steel Tubular Poles'
    LT1P = '1X35+1X25'
    LT3P = '3X50+1X35'
    NONE = 'None'
    DTR25 = '25 KVA (3 Ph)'
    DTR63 = '63 KVA (3 Ph)'
    DTR100 = '100 KVA (3 Ph)'

    columns = dict(sn=0,
                village=1,
                census=2,
                habitation=1,
                hhv=3,
                htst=4,
                htsv=5,
                htwt=6,
                htwv=7,
                htrt=8,
                htrv=9,
                ltt1=10,
                lt1v=11,
                ltt2=12,
                lt2v=13,
                kvat1=14,
                kva1v=15,
                kvat2=16,
                kva2v=17)






    # print(columns.values())
    fd = 'closure_review'
    f = input('Macro file: ')
    # f = '/Users/ronsair/mspdcl/Closure submissions/submissionofclosuretemplatedatafortheexecutedquantit/Bishnupur_275_0.xlsm'
    dfMacro = pd.read_excel(f, sheet_name='Proposed', engine='openpyxl')
    district = str.upper(dfMacro.iloc[0, 1])

    dfMacroSites = dfMacro[skip_rows:].iloc[:, list(columns.values())].fillna(0)
    # print(df1)
    dfMacroSites.columns = list(columns.keys())


    dfNilHab = (dfMacroSites['habitation'] == 0) & (dfMacroSites['census'] == 0)
    dfMacroSites = dfMacroSites.loc[~dfNilHab]

    df = dfMacroSites


    wrongHtt = [x for x in df['htst'] if x not in [NONE, 0]]
    if(len(wrongHtt) > 0):
        print(f'ERROR: HT Infra type out of scope')
    wrongHtt = [x for x in df['htrt'] if x not in [NONE, 0]]
    if(len(wrongHtt) > 0):
        print(f'ERROR: HT Infra type out of scope')
    wrongHtt = [x for x in df['htwt'] if x not in [HT, NONE, 0]]
    if(len(wrongHtt) > 0):
        print(f'ERROR: HT Infra Type not in {[HT, NONE]}')
    wrongLTC1 = [x for x in df['ltt1'] if x not in [LT1P, LT3P, NONE, 0]]
    if(len(wrongLTC1) > 0):
        print(f'ERROR: LTC1 Infra Type', wrongLTC1)
    wrongLTC2 = [x for x in df['ltt2'] if x not in [LT1P, LT3P, NONE, 0]]
    if(len(wrongLTC2) > 0):
        print(f'ERROR: LTC2 Infra Type')

    for i, row in df.iterrows():
        ht = row['htwv']
        ltt1 = row['ltt1']
        ltt2 = row['ltt2']
        if((ltt1 == ltt2) and ltt1 not in [0, NONE]):
            print('ERROR: duplicate LT Infra')
        dtr1 = row['kvat1']
        dtr2 = row['kvat2']
        if((dtr1 == dtr2) and dtr1 not in [0, NONE]):
            print('ERROR: duplicate DTR Infra')


    macrohab_ids = []
    flag = 1
    for i, row in dfMacroSites.iterrows():
        site, extra = getSite(census=row['census'], habitation=row['habitation'])
        if(site):
            macrohab_ids.append(site.hab_id)
        else:
            hab_id = getHabID(census=row['census'], habitation=row['habitation'])
            # macrohab_ids.append(hab_id)
            macrohab_ids.append(f'{flag}-{hab_id}')
            flag += 1

    dfMacroSites['hab_id'] = macrohab_ids

    vcols = [lbl for lbl in dfMacroSites.columns if lbl[-1] == 'v']
    dfMacroSites['infraSum'] = dfMacroSites[vcols[1:]].sum(axis=1)

    dfProgressSites = getSiteProgressdf(district)
    # print(type(dfProgressSites['census']))
    dfProgressSites = dfProgressSites[dfProgressSites['census'].astype(
        int) > 799999]
    dfProgressSites.to_excel(f'{fd}/{district}_urban_prog_sites.xlsx')

    certs = dfProgressSites.set_index('hab_id')['progressqty__cert']
    dfMacroSites = dfMacroSites.join(certs, on='hab_id')

    dfMacroSites.to_excel(f'{fd}/{district}_urban_macro.xlsx')
    dfMacroWithInfra = dfMacroSites[dfMacroSites['infraSum'] > 0]

    dfMacroWithInfra.to_excel(f'{fd}/{district}_urban_macroHabIdWithInfra.xlsx')

    duplicateMacroSites = dfMacroSites.duplicated(subset=['hab_id'],keep=False)
    dfduplicateMacroSites = dfMacroSites[duplicateMacroSites]
    if(len(dfduplicateMacroSites) > 0):
        dfduplicateMacroSites.sort_values(['hab_id'], inplace=True)
        print('Duplicate sites in macros')
        for i, row in dfduplicateMacroSites.iterrows():
            print(round(row['infraSum'],2), row['hab_id'],row['census'], row['habitation'])
        dfduplicateMacroSites.to_excel(f'{fd}/{district}_urban_duplicates.xlsx')
        input('continue?')

    missingProgressSitesHid = set(dfProgressSites['hab_id']) - set(dfMacroWithInfra['hab_id'])
    if(missingProgressSitesHid):
        print('missingProgressSites')
        dfmissingProgressSites = dfProgressSites[dfProgressSites['hab_id'].isin(missingProgressSitesHid)]
        print(dfmissingProgressSites.iloc[:,1:5])
        dfmissingProgressSites.to_excel(f'{fd}/{district}_urban_missingProgressSites.xlsx')
        input('continue?')
    dfmacromissingcensus = pd.read_excel('missing_census_macro_habs.xlsx', engine='openpyxl')
    pendingMacrocensus  = set(dfmacromissingcensus['hab_id']).intersection(dfProgressSites['hab_id'])
    if(pendingMacrocensus):
        print('\npending macro census update')
        print(pendingMacrocensus)

    extraMacroInfraSites = set(dfMacroWithInfra['hab_id']) - set(dfProgressSites['hab_id'])
    if(extraMacroInfraSites):
        print('extraMacroInfraSites')
        df = dfMacroWithInfra[dfMacroWithInfra['hab_id'].isin(extraMacroInfraSites)]
        print(df.iloc[:,1:5])
        df.to_excel(f'{fd}/{district}_urban_extraMacroInfraSites.xlsx')
        input('continue?')


    # 1: get all hh habs
    cs = Consumer.objects.filter(
        site__district=district).exclude(site__census__lt=799999)
    # cshabs = cs.values('site__origin__hab_id','site__hab_id','site__census', 'site__habitation', )\
    #     .annotate(apl=Count(Q(F('habitation')=='APL')))
    cshabs = cs.values('site__hab_id', 'site__village', 'site__census', 'site__habitation', )\
        .annotate(
            bplv=Count('apl_bpl', filter=Q(apl_bpl='BPL')),
            aplv=Count('apl_bpl', filter=Q(apl_bpl='APL')))


    # 2: are all habs present in macro?
    dfcshabs = pd.DataFrame(cshabs)
    dfcshabs['hhv'] = dfcshabs['aplv'] + dfcshabs['bplv']
    dfcshabs.to_excel(f'{fd}/{district}_rural_cshabs.xlsx')

    # sitesToAdd = [x for i, x in dfcshabs.iterrows() if ((x['site__hab_id'] not in dfMacroSites['hab_id'].values) and (
    #     (x['site__origin__hab_id'] == None or x['site__origin__hab_id'] not in dfMacroSites['hab_id'].values)))]
    csitesToAdd = set(dfcshabs['site__hab_id']) - set(dfMacroSites['hab_id'])
    if(csitesToAdd):
        dfcsitesToAdd = dfcshabs[dfcshabs['site__hab_id'].isin(csitesToAdd)]
        dfcsitesToAdd.sort_values('site__census', inplace=True)
        print('\n*** Missing Consumer Sites in Macro')
        dfcsitesToAdd.to_excel(f'{fd}/{district}_rural_sites_to_add_macro.xlsx')
        print(dfcsitesToAdd[['site__village','site__census','site__habitation']])
        input('continue?')

    # s_cs_count = dfcsi
    dfcscounts = dfcshabs.groupby('site__hab_id').sum()

    dfMacroSites = dfMacroSites.set_index('hab_id')
    
    print(f"total hh (macro): {sum(dfMacroSites['hhv'])}")
    print(f"total hh (report): {sum(dfcshabs['hhv'])}")

    dfMacroSites[['hhv', 'aplv', 'bplv']] = 0
    dfMacroSites.update(dfcscounts)
    print(f"total hh (update): {sum(dfMacroSites['hhv'])}")
    dfMacroSites.to_excel(f'{fd}/{district}_urban_data.xlsx')




    formatteddata = []
    for i, row in dfMacroSites.iterrows():
        ht = row['htwv'] + row['htsv'] + row['htrv']
        ltt1 = row['ltt1']
        ltt2 = row['ltt2']
        lt1 = 0.0
        lt3 = 0.0
        if(ltt1 == LT1P):
            lt1 += row['lt1v']
        if(ltt1 == LT3P):
            lt3 += row['lt1v']
        if(ltt2 == LT1P):
            lt1 += row['lt2v']
        if(ltt2 == LT3P):
            lt3 += row['lt2v']
        dtr1 = row['kvat1']
        dtr2 = row['kvat2']
        dtr25 = 0
        dtr63 = 0
        dtr100 = 0
        if(dtr1 == DTR25):
            dtr25 += row['kva1v']
        if(dtr1 == DTR63):
            dtr63 += row['kva1v']
        if(dtr1 == DTR100):
            dtr100 += row['kva1v']

        if(dtr2 == DTR25):
            dtr25 += row['kva2v']
        if(dtr2 == DTR63):
            dtr63 += row['kva2v']
        if(dtr2 == DTR100):
            dtr100 += row['kva2v']
        hh = row['hhv']
        rec = {}
        if(hh > 0 or row['infraSum'] > 0):
            rec = {
                'village': row['village'],
                'census': row['census'],
                'habitation': row['habitation'],
                'hhv': row['hhv'], HT: ht, LT3P: lt3, LT1P: lt1,
                DTR100: dtr100, DTR63: dtr63, DTR25: dtr25,
                'infra': row['infraSum'] > 0,
                'hab_id': i
            }
            formatteddata.append(rec)

    dfFormatted = pd.DataFrame(formatteddata)
    dfFormatted = dfFormatted.join(certs, on='hab_id')

    dfFormatted.to_excel(f'{fd}/{district}_urban_formatted.xlsx')


    sExecutedSum = dfFormatted[['hhv', HT, LT3P, LT1P, DTR100, DTR63, DTR25]].sum()
    sExecutedSum['infra_habs'] = len(dfFormatted[dfFormatted['infra']])
    sExecutedSum['total_habs'] = len(dfFormatted)
    sExecutedSum.name = 'executed'
    pqty_maps = {'ht': HT, 'lt_3p': LT3P, 'lt_1p': LT1P, 'dtr_100': DTR100, 'dtr_63': DTR63, 'dtr_25': DTR25}
    pfields = {'progressqty__'+f:pqty_maps[f] for f in pqty_maps}
    # if(len(missingProgressSitesHid) > 0):
    #     sMissingSum = dfmissingProgressSites[list(pfields.keys())].sum()
    #     sMissingSum.index = [pfields[x] for x in sMissingSum.index]
    #     sScopeSum = sMissingSum + sExecutedSum
    # else:
    #     sScopeSum = sExecutedSum.copy()
    # sScopeSum['hhv'] = sum(dfcshabs['hhv'])
    # sScopeSum['infra_habs'] = len(dfProgressSites)
    # sScopeSum['total_habs'] = len(dfFormatted)
    # sScopeSum.name = 'Scope'

    # dfExecutedSum = pd.DataFrame([sExecutedSum, sScopeSum])
    sExecutedSum.to_excel(f'{fd}/{district}_urban_summary.xlsx')

    s_report_psum = pd.Series({pfields[f]: dfProgressSites[f].sum() for f in pfields}, name='report_sum')
    s_report_psum['infra_habs'] = len(dfProgressSites)
    s_report_psum['total_habs'] = '--'
    s_report_psum['hhv'] = '--'
    print(pd.DataFrame([s_report_psum, sExecutedSum]).transpose())

    ifUpdate = input('Update? (Y)')
    if(ifUpdate == 'Y'):
        alreadycanceled = []
        updated = []
        canceled = []
        missingmacrocensus=[]
        ps = ProgressQty.objects.filter(site__district=district, site__census__gt= 790000)
        dfmacromissingcensus = pd.read_excel('missing_census_macro_habs.xlsx', engine='openpyxl')
        dff = dfFormatted.set_index('hab_id')
        dff = dff[dff['infra']>0]
        for p in ps:
            if(p.site.hab_id in dff.index):
                s = dff.loc[p.site.hab_id]
                # print('updating', p.site.hab_id)
                p.ht = s[HT]
                p.lt_1p = s[LT1P]
                p.lt_3p = s[LT3P]
                p.dtr_25 = s[DTR25]
                p.dtr_63 = s[DTR63]
                p.dtr_100 = s[DTR100]
                p.status = 'completed'
                updated.append(p)
            else:
                if(p.status == 'canceled'):
                    alreadycanceled.append([p, p.cert])
                else:
                    if(p.site.hab_id in pendingMacrocensus):
                        continue
                    else:
                        # print('canceling', p.site.hab_id)
                        p.remark = 'canceled in June 2021'
                        p.status = 'canceled'
                        canceled.append([p, p.cert])

            p.save()
        pprint('')
        pprint('updated')
        pprint(updated)
        pprint('')
        pprint('canceled')
        pprint(canceled)
        pprint('')
        pprint('already canceled')
        pprint(alreadycanceled)
        pprint('')

if(__name__ == '__main__'):
    run()