from django.shortcuts import render
from .models import Doctor


# Create your views here.

def index(request):
    doctors = Doctor.objects.all()
    print(doctors)
    param = {'doctors': doctors}
    return render(request, 'records/index.html', param)


def add_new_doctor(request):
    if request.method == 'POST':
        if request.POST.get('doctor_name') and request.POST.get('specialization'):
            doctors = Doctor()
            doctors.doctor_name = request.POST.get('doctor_name')
            doctors.specialization = request.POST.get('specialization')
            doctors.save()

            return render(request, 'records/add-doctor.html')

    else:
        return render(request, 'records/add-doctor.html')


def delete_doctor(request):
    doctors = Doctor.objects.all()
    param = {'doctors': doctors}

    if request.method == 'POST':
        if request.POST.get('doc_to_delete'):
            del_doc = Doctor.objects.get(doctor_id=request.POST.get('doc_to_delete'))
            del_doc.delete()

            return render(request, 'records/delete-doctor.html', param)
    else:

        return render(request, 'records/delete-doctor.html', param)


def edit_doctor(request):
    doctors = Doctor.objects.all()
    param = {'doctors': doctors}

    return render(request, 'records/edit-doctor.html', param)


def edit_view(request):
    edit_doc = Doctor.objects.get(doctor_id=request.GET.get('doc_to_edit'))
    param = {'doctor_name': edit_doc.doctor_name, 'specialization': edit_doc.specialization}

    if request.method == 'POST':
        if request.POST.get('new_doctor_name'):
            edit_doc.doctor_name = request.POST.get('new_doctor_name')

        if request.POST.get('new_specialization'):
            edit_doc.specialization = request.POST.get('new_specialization')

        edit_doc.save()

        edited_param = {'doctor_name': edit_doc.doctor_name, 'specialization': edit_doc.specialization}

        return render(request, 'records/edit-view.html', edited_param)
    else:
        return render(request, 'records/edit-view.html', param)
