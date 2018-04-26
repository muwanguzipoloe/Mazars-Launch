from django.contrib import admin
from company.models import Invitees
from import_export.resources import ModelResource
from import_export.admin import ImportExportMixin, ImportMixin, ExportActionModelAdmin

admin.site.site_header = "MAZARS BRJ LAUNCH PAD"

class InviteesResource(ModelResource):
    class Meta:
        model = Invitees

# class InfoAdmin(admin.ModelAdmin):
#     change_list_template = 'admin/info_change_list.html'
#     date_hierarchy = 'created'
#     list_display = ('')

class InviteesAdmin(ImportExportMixin, admin.ModelAdmin):
    resource_class = InviteesResource
    list_display =('name','company','designation','status','date_of_update','telephone_contact','email_address','comments')
    import_order =('name','company','designation','status','date_of_update','telephone_contact','email_address','comments')

# admin.site.register(Info)
admin.site.register(Invitees,InviteesAdmin)
