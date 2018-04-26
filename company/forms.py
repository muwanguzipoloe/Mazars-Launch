from django.forms import ModelForm
from company.models import Invitees

class InviteesForm(ModelForm):
    class Meta:
        model = Invitees
        fields = '__all__'
