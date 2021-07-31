from django.db import models
from work.models import Site
import re

CFIELDS = ['site__village','site__census','site__habitation','name','consumer_no','edate2','status','aadhar','meter_no','apl_bpl','mobile_no','voter_no','tariff','pdc_date','address1','address2','site__district', 'site__division','remark', 'cinfra_type']


def genCode(value):
    return re.sub('[\W]+', '', str(value)).upper()


def getHabID(**kwargs):
    return re.sub('[\W]+', '', "{}{}".format(kwargs['census'], kwargs['habitation'])).upper()


def formatString(string=""):
    return " ".join(str(string).split()).upper()


def getConsumerID(census, consumer_no, name):
    return genCode("{}{}{}".format(census, consumer_no, name))


class Timestamp(models.Model):
    created_at = models.DateTimeField(
        auto_now_add=True,  blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True,  blank=True, null=True)

    class Meta:
        abstract = True


class Common(Timestamp):
    changeid = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        abstract = True


class Consumer(Common):
    def __str__(self):
        return "{} - {} - ({}) - {} portal({})".format(self.name, self.consumer_no, self.habitation, self.census, self.isInPortal)

    # class Meta:
    #     unique_together = ('census', 'habitation', 'name', 'consumer_no')
    site = models.ForeignKey(
        Site, on_delete=models.SET_NULL, null=True, blank=True)
    hab_id = models.CharField(max_length=50, null=True, blank=True)
    village = models.CharField(max_length=50, null=True, blank=True)
    census = models.IntegerField(null=True, blank=True)
    habitation = models.CharField(max_length=50,  null=True, blank=True)
    name = models.CharField(max_length=50, null=True, blank=True)
    consumer_no = models.CharField(max_length=50, null=True, blank=True)
    edate = models.CharField(max_length=50, null=True, blank=True)
    status = models.CharField(max_length=20, null=True, blank=True)
    aadhar = models.CharField(max_length=50, null=True, blank=True)
    meter_no = models.CharField(max_length=50, null=True, blank=True)
    apl_bpl = models.CharField(max_length=3, null=True, blank=True)
    mobile_no = models.CharField(max_length=20, null=True, blank=True)
    voter_no = models.CharField(max_length=20, null=True, blank=True)
    tariff = models.CharField(max_length=20, null=True, blank=True)
    pdc_date = models.CharField(max_length=20, null=True, blank=True)
    address1 = models.CharField(max_length=100, null=True, blank=True)
    address2 = models.CharField(max_length=100, null=True, blank=True)
    remark = models.CharField(max_length=100, null=True, blank=True)
    isInPortal = models.BooleanField(null=True, blank=True)
    district = models.CharField(max_length=20, null=True, blank=True)
    consumer_id = models.CharField(max_length=200, unique=True, null=True, blank=True)
    division = models.CharField(max_length=50, null=True, blank=True)
    cinfra_type = models.CharField(max_length=50, null=True, blank=True)
    edate2 = models.DateField(blank=True, null=True)

    def save(self, *args, **kwargs):
        self.habitation = formatString(self.habitation)
        # self.village = formatString(self.village)
        self.name = formatString(self.name)
        # self.district = formatString(self.district)
        self.consumer_no = genCode(self.consumer_no)
        self.hab_id = getHabID(census=self.census, habitation=self.habitation)
        self.consumer_id = getConsumerID(self.census, self.consumer_no,self.name)
        # print('saving... ', self.hab_id, self.consumer_id)
        super(Consumer, self).save(*args, **kwargs)


class Group(models.Model):
    name = models.CharField(max_length=30)
    consumer = models.ForeignKey(Consumer, on_delete=models.CASCADE)