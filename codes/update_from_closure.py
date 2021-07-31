'''
1. check the list of infra habitations
2. check missing hh habitations if any
3. check hh numbers for all habs
'''

'''
input file: macro
field map:
'''

HT = 'Weasel Conductor on Steel Tubular Poles'
DTR100 = '100 KVA (3 Ph)'
DTR63 = '63 KVA (3 Ph)'
DTR25 = '25 KVA (3 Ph)'
AB1P = '1X35+1X25'
AB3P = '3X50+1X35'

columns = dict(sn=0,
               block=1,
               village=2,
               census=3,
               habitation=4,
               bplv=6,
               free_aplv=7,
               aplv=8,
               hhv=9,
               htst=11,
               htsv=12,
               htwt=13,
               htwv=14,
               htrt=15,
               htrv=16,
               ltt1=17,
               lt1v=18,
               ltt2=19,
               lt2v=20,
               kvat1=21,
               kva1v=22,
               kvat2=23,
               kva2v=24)

division = None
district = input('[input] district: ')
file = input('Rural_macroHabIdWithInfra: ')

import pandas as pd
df = pd.read_excel(file)

from work.controller import getSite
from work.models import Site, ProgressQty

for i, row in df.iterrows():
    village = row['village']
    census = row['census']
    habitation = row['habitation']
    block = row['block']
    print(f'[updating] {village}, {census}, {habitation}')
    site, _ = getSite(census=row['census'], habitation=habitation)
    if(site == None):
        # add site
        refSite = Site.objects.filter(census = census).first()
        if(refSite == None):
            division = input(f'[input] division for {village}, {census}, {habitation}: ')
            # district = input(f'[input] district  for {village}, {census}, {habitation}: ')
        else:
            division = refSite.division
            # district = refSite.district
        site = Site()
        site.village = village
        site.census = census
        site.habitation = habitation
        site.division = division
        site.district = district
        site.block = block
        site.save()
        print(f'[added] {village} {census}, {habitation}')

    p, created = ProgressQty.objects.get_or_create(site=site)
    p.ht = row['htwv']

    if(row['ltt1']==AB1P):
        p.lt_1p = row['lt1v'] or 0
    elif(row['ltt1']==AB3P):
        p.lt_3p = row['lt1v'] or 0

    if(row['ltt2']==AB1P):
        p.lt_1p = row['lt2v'] or 0
    elif(row['ltt2']==AB3P):
        p.lt_3p = row['lt2v'] or 0
    
    if(row['kvat1']==DTR100):
        p.dtr_100 = row['kva1v'] or 0
    elif(row['kvat1']==DTR63):
        p.dtr_63 = row['kva1v'] or 0
    elif(row['kvat1']==DTR25):
        p.dtr_25 = row['kva1v'] or 0

    if(row['kvat2']==DTR100):
        p.dtr_100 = row['kva2v'] or 0
    elif(row['kvat2']==DTR63):
        p.dtr_63 = row['kva2v'] or 0
    elif(row['kvat2']==DTR25):
        p.dtr_25 = row['kva2v'] or 0

    p.save()