from django.shortcuts import render, redirect
from crud.models import Details
from .forms import DetailsForm
from django.contrib import messages


def index(request):
    return render(request, 'index.html')


def create(request):
    if request.method == "POST":
        name = request.POST['name']
        age = request.POST['age']
        address = request.POST['address']
        obj = Details.objects.create(name=name, age=age, address=address)
        obj.save()
        messages.success(request, "Data Inserted successfully..")
    return redirect('/')


def retrieve(request):
    details = Details.objects.all()
    return render(request, 'retrieve.html', {'details': details})


def edit(request, id):
    object = Details.objects.get(id=id)
    return render(request, 'edit.html', {'object': object})


def update(request, id):
    object = Details.objects.get(id=id)
    form = DetailsForm(request.POST, instance=object)
    if form.is_valid():
        form.save()
        messages.success(request, "Updated Successfully")
        object = Details.objects.all()
        return redirect('retrieve')


def delet(request, id):
    Details.objects.filter(id=id).delete()
    messages.warning(request, "Deleted Successfully")
    return redirect('retrieve')
