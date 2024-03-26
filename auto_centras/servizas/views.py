from django.shortcuts import render, redirect
from . import forms
from django.shortcuts import render, get_object_or_404
from .models import ClientData, Mechanic
from .forms import ClientDataForm
from django.db.models import Sum


def create_client_data(request):
    if request.method == 'POST':
        form = forms.ClientDataForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')  
    else:
        form = forms.ClientDataForm() 
    return render(request, 'servizas/create_client_data.html', {'form': form})

def create_mechanic(request):
    if request.method == "POST":
        form = forms.MechanicForm(request.POST)
        if form.is_valid():
            form.save()
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

def mechanic_list(request):
    mechanics = Mechanic.objects.all()
    return render(request, 'servizas/mechanic_list.html', {'mechanics': mechanics})

def client_print(request, pk):
    client = get_object_or_404(ClientData, pk=pk)
    return render(request, 'servizas/client_print.html', {'client': client})


def top_month_mechanic(request):
    top_mechanics = []

    for month in range(1, 13):
        mechanics_profit = ClientData.objects.filter(
            created_date__month=month
        ).values('mechanic__name').annotate(
            total_profit=Sum('labor_cost') + Sum('ordered_parts_price')
        ).order_by('-total_profit')

        if mechanics_profit:
            top_mechanic = mechanics_profit[0]
            top_mechanics.append({'month': month, 'top_mechanic': top_mechanic})

    return render(request, 'servizas/top_month_mechanic.html', {'top_mechanics': top_mechanics})