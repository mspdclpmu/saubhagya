
import pandas as pd
# get all progress sites
from work.controller import getSiteProgressdf
dfProgressSites = getSiteProgressdf()

# 1: get all hh habs
from consumers.models import Consumer
from django.db.models import Count, F, Q
cs = Consumer.objects.all()
# cshabs = cs.values('site__origin__hab_id','site__hab_id','site__census', 'site__habitation', )\
#     .annotate(apl=Count(Q(F('habitation')=='APL')))
cshabs = cs.values('site__origin__hab_id', 'site__hab_id','site__village', 'site__census', 'site__habitation','site__district', 'site__division' )\
    .annotate(
        bpl=Count('apl_bpl', filter=Q(apl_bpl='BPL')),
        apl=Count('apl_bpl', filter=Q(apl_bpl='APL')))

# 2: are all habs present in macro?
dfcshabs = pd.DataFrame(cshabs)
dfcshabs['hh'] = dfcshabs['apl'] + dfcshabs['bpl']

df_all = dfProgressSites.merge(dfcshabs, how='outer', left_on='hab_id', right_on='site__hab_id')

print(df_all.head())