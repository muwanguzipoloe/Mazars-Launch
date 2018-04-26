from django.urls import path
from company import views

urlpatterns = [
    path('', views.Invitees_form.as_view(), name='info_form'),
    path('table/', views.Invitees_table, name='table')
]
