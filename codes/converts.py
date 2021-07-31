HT = 'Weasel Conductor on Steel Tubular Poles'
LT1P = '1X35+1X25'
LT3P = '3X50+1X35'
NONE = 'None'
DTR25 = '25 KVA (3 Ph)'
DTR63 = '63 KVA (3 Ph)'
DTR100 = '100 KVA (3 Ph)'

def macroInfraToCol(row):
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
    return (ht, lt3, lt1, dtr100, dtr63, dtr25)