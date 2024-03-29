from django.contrib import admin
from simple_history.admin import SimpleHistoryAdmin

# Register your models here.
from .models import Site, SurveyQty, ShiftedQty, ProgressQty, SiteExtra, ShiftedQtyExtra, ProgressQtyExtra, DprQty, Resolution, Loa, Log, Project, BOQ, Rate, Billing
from consumers.models import Consumer, Group

# admin.site.register(Site)
# admin.site.register(SurveyQty, SimpleHistoryAdmin)
admin.site.register(ShiftedQty, SimpleHistoryAdmin)
# admin.site.register(ProgressQty)
# admin.site.register(SiteExtra)
admin.site.register(ShiftedQtyExtra, SimpleHistoryAdmin)
# admin.site.register(ProgressQtyExtra)
# admin.site.register(DprQty, SimpleHistoryAdmin)
admin.site.register(Log)
admin.site.register(Group)
admin.site.register(Loa)
admin.site.register(Project)
admin.site.register(BOQ)
admin.site.register(Rate)
admin.site.register(Billing)


class ResolulationAdmin(SimpleHistoryAdmin):
    # list_display = ('name', 'country',)
    list_filter = ('status',)
admin.site.register(Resolution, ResolulationAdmin)

class ConsumerAdmin(SimpleHistoryAdmin):
    # list_display = ('name', 'country',)
    list_filter = ('isInPortal','remark')
    search_fields = ('census','name')
    raw_id_fields = ('site',)
admin.site.register(Consumer, ConsumerAdmin)

class DprQtyAdmin(SimpleHistoryAdmin):
    # list_display = ('name', 'country',)
    search_fields = ('site__hab_id', 'site__habitation','site__village')
admin.site.register(DprQty, DprQtyAdmin)

class SiteAdmin(SimpleHistoryAdmin):
    # list_display = ('name', 'country',)
    search_fields = ('hab_id', 'habitation','village')
admin.site.register(Site, SiteAdmin)

class SiteExtraAdmin(SimpleHistoryAdmin):
    # list_display = ('name', 'country',)
    search_fields = ('hab_id', 'habitation','village')
admin.site.register(SiteExtra, SiteExtraAdmin)

class ProgressAdmin(SimpleHistoryAdmin):
    # list_display = ('site__district',)
    search_fields = ('site__hab_id','site__district')
admin.site.register(ProgressQty, ProgressAdmin)

class ProgressQtyExtraAdmin(SimpleHistoryAdmin):
    # list_display = ('name', 'country',)
    # search_fields = ('changeid',)
    search_fields = ('site__hab_id',)
admin.site.register(ProgressQtyExtra, ProgressQtyExtraAdmin)

class SurveyQtyAdmin(SimpleHistoryAdmin):
    # list_display = ('name', 'country',)
    # search_fields = ('changeid',)
    search_fields = ('site__hab_id',)
admin.site.register(SurveyQty, SurveyQtyAdmin)