from django.urls import path
from . import views as cus_views
urlpatterns =[

    path('',cus_views.show_transations, name='transations'),
    path('new_transation/',cus_views.new_transation, name='new_transation'),
    path('details/<int:id>/',cus_views.details_customer, name='details_customer'),
    # path('delete/<int:id>/',cus_views.delete_customer, name='delete_customer'),
    # path('exa/',cus_views.matltiplae, name='exa'),

]
