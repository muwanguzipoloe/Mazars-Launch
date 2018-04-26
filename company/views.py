from django.shortcuts import render
from company.models import Invitees
from company.forms import InviteesForm
from django.urls import reverse_lazy
from django import views
from django.views import generic

class Invitees_form(generic.CreateView):
    form_class = InviteesForm
    success_url = reverse_lazy('info_form')
    template_name = 'info_form.html'
    # if request.method =='POST':
    #     form = InviteesForm(request.POST)
    #     if form.is_valid():
    #         model_instance = form.save(commit=False)
    #         model_instance.save()
    #         return redirect('Invitees_form')
    # else:
    #     form = InviteesForm()
    # return render(request, 'info_form.html', {'form': form})


def Invitees_table(request):
    table_items = Invitees.objects.all
    context = {
               'name':table_items.name,
               'company':table_items.company,
    }
    return render(request, 'table.html', context)
