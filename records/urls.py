from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="HospitalRecordsHome"),
    path('add-doctor', views.add_new_doctor, name="AddNewDoctor"),
    path('delete-doctor', views.delete_doctor, name="DeleteDoctor"),
    path('edit-doctor', views.edit_doctor, name="EditDoctor"),
]
