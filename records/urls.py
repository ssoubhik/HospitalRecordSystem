from django.urls import path
from . import views
from .views import PatientRecordsView, AddPatientView, EditPatientView, DeletePatientView

urlpatterns = [
    path('', views.index, name="HRSHome"),
    path('doctor-records', views.doctor_records, name="DoctorRecords"),
    path('add-doctor', views.add_new_doctor, name="AddNewDoctor"),
    path('delete-doctor', views.delete_doctor, name="DeleteDoctor"),
    path('edit-doctor', views.edit_doctor, name="EditDoctor"),
    path('patient-records', PatientRecordsView.as_view(), name="PatientRecords"),
    path('add-patient', AddPatientView.as_view(), name="AddPatient"),
    path('edit-patient', EditPatientView.as_view(), name="EditPatient"),
    path('delete-patient', DeletePatientView.as_view(), name="DeletePatient"),
]
