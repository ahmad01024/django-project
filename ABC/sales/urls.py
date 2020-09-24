from django.urls import path
from django.conf.urls import url
from . import views
from .views import *

app_name = 'my_sales'
urlpatterns = [
    path('new_invoice/', views.new_invoice, name='new_invoice'),
    path('create_invoice/', views.create_invoice, name='create_invoice'),
    path('list_invoices/', views.list_invoices, name='list_invoices'),
    path('show_invoice/<int:invoice_number>/', views.show_invoice, name='show_invoice'),

    path('get_customer_data/', views.get_customer_data, name='get_customer'),
    path('list_invoices_data/', views.list_invoices_data, name='list_invoices_data'),

    path('pdf/<int:invoice_number>/', views.show_pdf),

]
