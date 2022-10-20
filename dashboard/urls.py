from django.urls import path
from . import views

urlpatterns = [
    path('pivot', views.dashboard_with_pivot, name='dashboard_with_pivot'),
    # path('data', views.pivot_data, name='pivot_data'),
    path('farmers',views.farmer_Form,name="farmers"),
    path('farmerslist',views.farmers_list,name="farmerslist"),
]