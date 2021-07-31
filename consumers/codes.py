import pandas as pd
from consumers.models import Consumer, genCode, formatString, getConsumerID
from django.db.models import Count
import os

def uploadConsumerPortalPartial(path):
    filesd = []
    for folder, folders, files in os.walk(path):
        for file in files:
            parts = file.split('.')
            district = ' '.join(parts[0].split(' ')[1:]).upper()
            filesd.append([os.path.join(folder,file), district])

    for file in filesd:
        district = file[1]
        ix = 0
        existing = 0
        new = 0
        df = pd.read_excel(file[0])
        for i, row in df.iloc[ix:].iterrows():
            print(i, row['Census Code'], row['Name'], row['Consumer No'])
            consumer = Consumer()
            ix = i
            consumer.consumer_no = genCode(row['Consumer No'])
            consumer.census = row['Census Code']
            consumer.village = row['Village']
            consumer.name = formatString(row['Name'])
            consumerid = getConsumerID(consumer.census, consumer.consumer_no, consumer.name)
            existingConsumer = Consumer.objects.filter(consumer_id = consumerid)
            if(existingConsumer):
                print('existing')
                ex = existingConsumer.first()
                if(ex.census == consumer.census):
                    Consumer.objects.filter(census=consumer.census, district=None).update(district=district)
                existing += 1
                continue
            consumer.remark = 'missing details'
            consumer.isInPortal = True
            consumer.habitation = ""
            consumer.district = district
            consumer.save()
            new += 1
            print('updated')

CFIELDS = ['village','census','habitation','name','consumer_no','edate','status','aadhar','meter_no','apl_bpl','mobile_no','voter_no','tariff','pdc_date','address1','address2','district', 'remark']

NULLFIELDS = ["", None, "nan",0, '0', False]

def fill(target, source):
    changes = False
    for k in CFIELDS:
        print('checking field', k)
        tk = getattr(target,k) in NULLFIELDS
        sk = getattr(source,k) not in NULLFIELDS
        if(tk and sk):
            # target[k] = source[k]
            setattr(target,k, getattr(source,k))
            changes = True
    # if(changes):
    #     target.save()
    return target, changes
    

def completionLevel(record):
    return sum([1 for k in record if not record[k] in NULLFIELDS])

def deleteDuplicate():
    # duplicate consumers
    cs = Consumer.objects.values('consumer_id').annotate(count=Count('consumer_id')).filter(count__gt=1)
    for c in cs.values('consumer_id').distinct():
        print(c['consumer_id'])
        dcs = Consumer.objects.filter(consumer_id=c['consumer_id'])
        largest = 0
        last_largest = None
        changes = False
        for dc in dcs:
            reward = completionLevel(dc.__dict__)
            if(reward > largest):
                largest = reward
                if(last_largest):
                    last_largest, nc = fill(last_largest, dc)
                    changes = changes or nc
                    dc.delete()
                else:
                    last_largest = dc
            else:
                dc.delete()
        if(changes):
            last_largest.save()
        


