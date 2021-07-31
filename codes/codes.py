''' get all habs/towns with infra and Hh
'''
from work.models import Site, getHabID
from work.functions import genCode
from django.db.models import Q, F, Count
def getScopeSites():
    sites =Site.objects.exclude(consumer=None, progressqty=None, progressqty__status='canceled')
    # sites =Site.objects.exclude(progressqty=None, progressqty__status='canceled')
    # sites =Site.objects.exclude(progressqty=None, progressqty__status='canceled', consumer_set=None)
    ss = sites.values('hab_id','village', 'census','habitation','block','district','progressqty__ht', 'progressqty__lt_3p', 'progressqty__lt_1p'
    , 'progressqty__dtr_100', 'progressqty__dtr_63', 'progressqty__dtr_25').annotate(hh=Count('consumer'))

def assignDaughters():

    daughters = Site.objects.exclude(village=F('habitation'))
    daughters1 = [d for d in daughters if (genCode(d.village)!=genCode(d.habitation))]
    for d in daughters1:
        parents = Site.objects.filter(census = d.census)
        parent = [p for p in parents if (genCode(p.village)==genCode(p.habitation))]
        if(len(parent)>0):
            d.daughter_of = parent[0]
            d.save()
from work.models import Project
import pandas as pd
def getEvProjectwise():
    f = '/Users/ronsair/mspdcl/hab_town_infra_hh4.xlsx'
    df = pd.read_excel(f)
    habids = df['hab_id'].values
    projects = Project.objects.all()
    
    sites = []
    for hid in habids:
        site = Site.objects.get(hab_id=hid)
        sites.append(site)
    evcounts = {projects[0].code:0, projects[1].code:0}
    evs = [s for s in sites if genCode(s.village)==genCode(s.habitation)]
    for ev in evs:
        evcounts[ev.project.code] += 1
    print(evcounts)
    habscount = {projects[0].code:0, projects[1].code:0}
    daughters = [s for s in sites if genCode(s.village)!=genCode(s.habitation)]
    for daughter in daughters:
        habscount[daughter.project.code] += 1    
    print(habscount)
    
# def setProject():
    # nonProject = [d for d in daughters if d.project==None]
    # for daughter in nonProject:
    #     if(not(getattr(daughter, 'progressqty', None))):
    #         daughter.project = projects[0]
    #         daughter.save()
# def setProjectForSaub():
#     for daughter in daughters:
