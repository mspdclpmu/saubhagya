import pandas as pd
from work.models import ProgressQty


def checkConsistency():
    # check correct infra type
    f = input('Infra File: ')
    df = pd.read_excel(f)
    HT = 'Weasel Conductor on Steel Tubular Poles'
    LT1P = '1X35+1X25'
    LT3P = '3X50+1X35'
    NONE = 'None'
    DTR25 = '25 KVA (3 Ph)'
    DTR63 = '63 KVA (3 Ph)'
    DTR100 = '100 KVA (3 Ph)'
    wrongHtt = [x for x in df['htwt'] if x not in [HT, NONE]]
    if(len(wrongHtt) > 0):
        print(f'ERROR: HT Infra Type not in {[HT, NONE]}')
        return
    wrongLTC1 = [x for x in df['ltt1'] if x not in [LT1P, LT3P, NONE]]
    if(len(wrongLTC1) > 0):
        print(f'ERROR: LTC1 Infra Type')
        return
    wrongLTC2 = [x for x in df['ltt2'] if x not in [LT1P, LT3P, NONE]]
    if(len(wrongLTC2) > 0):
        print(f'ERROR: LTC2 Infra Type')
        return

    for i, row in df.iterrows():
        habid = row['hab_id']
        ht = row['htwv']
        ltt1 = row['ltt1']
        ltt2 = row['ltt2']
        if((ltt1 == ltt2) and ltt1 != NONE):
            print('ERROR: duplicate LT Infra')
            return
        lt1 = 0.0
        lt3 = 0.0
        if(ltt1 == LT1P):
            lt1 += row['lt1v']
        if(ltt2 == LT1P):
            lt1 += row['lt1v']
        if(ltt1 == LT3P):
            lt3 += row['lt1v']
        if(ltt2 == LT3P):
            lt3 += row['lt1v']
        dtr1 = row['kvat1']
        dtr2 = row['kvat2']
        if((dtr1 == dtr2) and dtr1 != NONE):
            print('ERROR: duplicate DTR Infra')
            return        
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
        print(habid)
        if(input()=='x'):
            break
        # progress = ProgressQty.objects.get(hab_id=habid)
        # progress.ht = ht
        # progress.lt_1p = lt1
        # progress.lt_3p = lt3
        # progress.dtr_25 = dtr25
        # progress.dtr_63 = dtr63
        # progress.dtr_100 = dtr100

        # progress.save()

checkConsistency()