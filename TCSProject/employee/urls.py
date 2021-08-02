from django.urls import path
from . import views



urlpatterns=[
    path('',views.employee_from,name="newemployee"),
    path('<int:id>/',views.employee_from,name="update"),
    path('delete/<int:id>/',views.employee_delete,name="delete"),
    path('list/',views.employee_list,name="all_list"),
]