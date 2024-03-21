from django.shortcuts import render, redirect
from . import forms
from django.contrib import messages
from django.shortcuts import render, get_object_or_404
from .models import ClientData, Mechanic
from .forms import ClientDataForm


def create_client_data(request):
    if request.method == 'POST':
        form = forms.ClientDataForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Įrašas sėkmingai sukurtas')
            return redirect('home')  
    else:
        form = forms.ClientDataForm() 
    return render(request, 'servizas/create_client_data.html', {'form': form})

def create_mechanic(request):
    if request.method == "POST":
        form = forms.MechanicForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Darbuotojas sėkmingai sukurtas')
            if request.GET.get('next'):
                return redirect(request.GET.get('next'))
            return redirect('home')
    else:
        form = forms.MechanicForm() 
    return render(request, 'servizas/create_mechanic.html', {'form': form})

def created_client_detail(request, client_id):
    client = get_object_or_404(ClientData, pk=client_id)
    return render(request, 'servizas/created_client_detail.html', {'client': client})

def created_data_list(request):
    created_data_list = ClientData.objects.all()  
    return render(request, 'servizas/created_data_list.html', {'created_data_list': created_data_list})

def edit_client(request, client_id):
    client = get_object_or_404(ClientData, pk=client_id)
    if request.method == 'POST':
        form = ClientDataForm(request.POST, instance=client)
        if form.is_valid():
            form.save()
            return redirect('created_client_detail', client_id=client_id)
    else:
        form = ClientDataForm(instance=client)
    return render(request, 'servizas/edit_client.html', {'form': form})

def delete_client(request, client_id):
    client = get_object_or_404(ClientData, pk=client_id)
    if request.method == 'POST':
        client.delete()
        return redirect('created_data_list')  
    return render(request, 'servizas/delete_client.html', {'client': client})

def home(request):
    return render(request, 'base.html')

def delete_mechanic(request, mechanic_id):
    mechanic = get_object_or_404(Mechanic, pk=mechanic_id)
    if request.method == 'POST':
        mechanic.delete()
        return redirect('mechanic_list')  
    return render(request, 'servizas/delete_mechanic.html', {'mechanic': mechanic})

def mechanic_list(request):
    mechanics = Mechanic.objects.all()
    return render(request, 'servizas/mechanic_list.html', {'mechanics': mechanics})

