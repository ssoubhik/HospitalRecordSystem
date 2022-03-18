from django.urls import reverse_lazy
from .models import Doctor, Patient
from django.views.generic import TemplateView, ListView, CreateView, UpdateView, DeleteView


# home page view
class HomepageView(TemplateView):
    template_name = 'records/index.html'


# doctors list view
class DoctorRecordsView(ListView):
    model = Doctor
    template_name = 'records/doctor-records.html'


# add doctor view
class AddDoctorView(CreateView):
    model = Doctor
    fields = '__all__'
    success_url = reverse_lazy("DoctorRecords")
    template_name = 'records/add-doctor.html'


# delete doctor view
class DeleteDoctorView(DeleteView):
    model = Doctor
    success_url = reverse_lazy("DoctorRecords")
    template_name = 'records/delete-doctor.html'


# edit doctor view
class EditDoctorView(UpdateView):
    model = Doctor
    fields = '__all__'
    success_url = reverse_lazy("DoctorRecords")
    template_name = 'records/edit-doctor.html'


# patient records view
class PatientRecordsView(ListView):
    model = Patient
    template_name = 'records/patient-records.html'


# add patient view
class AddPatientView(CreateView):
    model = Patient
    fields = '__all__'
    success_url = reverse_lazy("PatientRecords")
    template_name = 'records/add-patient.html'


# edit patient view
class EditPatientView(UpdateView):
    model = Patient
    fields = '__all__'
    success_url = reverse_lazy("PatientRecords")
    template_name = 'records/edit-patient.html'


# delete patient view
class DeletePatientView(DeleteView):
    model = Patient
    success_url = reverse_lazy("PatientRecords")
    template_name = 'records/delete-patient.html'
