from work.controller import getSite
import pandas as pd
from work.models import Site, ProgressQty
from converts import macroInfraToCol
import os

f = input('Extra macro sites file: ')

def process(file):
    df = pd.read_excel(file, engine='openpyxl')
    for i,r in df.iterrows():
        census = r['census']
        habitation = r['habitation']
        s, x = getSite(census=census, habitation=habitation)
        if(x):
            print('Variation exists', x)
            return
        if(s):
            print('Existing site',s)
        else:
            s = Site()
            s.census = census
            s.village = r['village']
            s.habitation = habitation
            s.block = r['block']
            s.district = os.path.basename(f).split('_')[0]
            sr = Site.objects.filter(census=s.census)
            if(sr):
                s.division = sr.first().division
            s.remark = 'added in macro recently'
            s.category = 'II' if (r['kva1v']+r['kva2v']) > 0 and r['htwv']>1 else 'III'
            s.save()
        p = ProgressQty()
        p.ht, p.lt_3p, p.lt_1p, p.dtr_100, p.dtr_63, p.dtr_25 = macroInfraToCol(r)
        p.status = 'completed'
        p.cert = True
        p.site = s
        p.save()
    
if(not 'extraMacroInfraSites' in f):
    print('Provide extraMacroInfraSites file')
else:
    process(file=f)