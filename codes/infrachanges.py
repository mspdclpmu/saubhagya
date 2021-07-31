

source = input('Macro file with updated qty: ')
target = input('File to be updated: ')

skip_rows = 5
HT = 'Weasel Conductor on Steel Tubular Poles'
DTR63 = '63 KVA (3 Ph)'
DTR25 = '25 KVA (3 Ph)'
DTR100 = '100 KVA (3 Ph)'
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


import pandas as pd

# from work.controller import getSite

dfMacro = pd.read_excel(source, sheet_name='Proposed', skiprows=skip_rows)
dfTarget = pd.read_excel(target)


# df1.set_index([0,1]).update(df2.set_index([0,1]))
# for i,r in dfTarget.iterrows():
index_cols = list(dfMacro.columns[3:5])

dfUpdated = dfTarget.set_index(['census','habitation'])
for i in range(columns['htst'], columns['kva2v']+1):
    col = dfMacro.columns[i]
    s = dfMacro.set_index(index_cols)[col]
    datacol = list(columns.keys())[list(columns.values()).index(i)]
    s.name = datacol
    dfUpdated.update(s)

dfUpdated.to_excel('updated_ccpur.xlsx')
