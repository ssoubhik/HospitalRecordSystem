from django.urls import path

from .views import HomepageView, DoctorRecordsView, AddDoctorView, DeleteDoctorView, EditDoctorView, PatientRecordsView, \
    AddPatientView, EditPatientView, DeletePatientView

urlpatterns = [
    path('', HomepageView.as_view(), name="HRSHome"),
    path('doctor-records', DoctorRecordsView.as_view(), name="DoctorRecords"),
    path('add-doctor', AddDoctorView.as_view(), name="AddNewDoctor"),
    path('delete-doctor/<int:pk>', DeleteDoctorView.as_view(), name="DeleteDoctor"),
    path('edit-doctor/<int:pk>', EditDoctorView.as_view(), name="EditDoctor"),
    path('patient-records', PatientRecordsView.as_view(), name="PatientRecords"),
    path('add-patient', AddPatientView.as_view(), name="AddPatient"),
    path('edit-patient/<int:pk>', EditPatientView.as_view(), name="EditPatient"),
    path('delete-patient/<int:pk>', DeletePatientView.as_view(), name="DeletePatient"),
]
