import django_tables2 as table_items
from django_tables2.utils import A
from .models import Invitees

class InviteesTable(tables.Table):
    class Meta:
        model = Invitees
        fields -= '__all__'
        attrs = {"class": "table-striped table-bordered"}
            
