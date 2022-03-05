from django.shortcuts import render
from .models import Doctor


# doctors list view
def index(request):
    # creating an array of Doctor
    doctors = Doctor.objects.all()

    param = {'doctors': doctors}
    return render(request, 'records/index.html', param)


# add doctor view
def add_new_doctor(request):
    if request.method == 'POST':
        # check if doctor_name & specialization are not null
        if request.POST.get('doctor_name') and request.POST.get('specialization'):
            # create a new instance of doctor model
            doctors = Doctor()

            # add doctor_name & specialization
            doctors.doctor_name = request.POST.get('doctor_name')
            doctors.specialization = request.POST.get('specialization')

            # save doctor
            doctors.save()

            # add doctor template
            return render(request, 'records/add-doctor.html')

    else:
        # add doctor template
        return render(request, 'records/add-doctor.html')


# delete doctor view
def delete_doctor(request):

    # create an array of Doctor
    doctors = Doctor.objects.all()
    param = {'doctors': doctors}

    # perform on click delete button
    if request.method == 'POST':
        if request.POST.get('doc_to_delete'):
            # get the doctor object to delete
            del_doc = Doctor.objects.get(doctor_id=request.POST.get('doc_to_delete'))

            # delete doctor
            del_doc.delete()

            # delete doctor template
            return render(request, 'records/delete-doctor.html', param)
    else:
        # delete doctor template
        return render(request, 'records/delete-doctor.html', param)


# edit doctor list view
def edit_doctor(request):
    # create an array of Doctor
    doctors = Doctor.objects.all()
    param = {'doctors': doctors}

    # edit doctor template
    return render(request, 'records/edit-doctor.html', param)


# edit doctor view
def edit_view(request):
    # get the doctor object to edit
    edit_doc = Doctor.objects.get(doctor_id=request.GET.get('doc_to_edit'))

    param = {'doctor_name': edit_doc.doctor_name, 'specialization': edit_doc.specialization}

    # perform on click done button
    if request.method == 'POST':
        # check if doctor name has been edited or not
        if request.POST.get('new_doctor_name'):
            edit_doc.doctor_name = request.POST.get('new_doctor_name')

        # check if specialization has been edited or not
        if request.POST.get('new_specialization'):
            edit_doc.specialization = request.POST.get('new_specialization')

        # save changes
        edit_doc.save()

        edited_param = {'doctor_name': edit_doc.doctor_name, 'specialization': edit_doc.specialization}

        # edit view template
        return render(request, 'records/edit-view.html', edited_param)
    else:
        # edit view template
        return render(request, 'records/edit-view.html', param)
