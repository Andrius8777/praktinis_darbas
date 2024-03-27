from django.shortcuts import render, redirect, get_object_or_404
from . import forms
from .models import ClientData, Mechanic
from .forms import ClientDataForm, ClientDataFilterForm
from django.db.models import Q
from django.utils import timezone


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
    created_data_list = ClientData.objects.all().order_by('-created_date')   
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

def mechanic_list(request):
    mechanics = Mechanic.objects.all()
    return render(request, 'servizas/mechanic_list.html', {'mechanics': mechanics})

def client_print(request, pk):
    client = get_object_or_404(ClientData, pk=pk)
    return render(request, 'servizas/client_print.html', {'client': client})

def top_month_mechanic(request):
    month_names = {
        1: 'Sausis',
        2: 'Vasaris',
        3: 'Kovas',
        4: 'Balandis',
        5: 'Gegužė',
        6: 'Birželis',
        7: 'Liepa',
        8: 'Rugpjūtis',
        9: 'Rugsėjis',
        10: 'Spalis',
        11: 'Lapkritis',
        12: 'Gruodis',
    }

    selected_month = request.GET.get('selected_month')
    if selected_month:
        selected_month = int(selected_month)
    else:
        selected_month = timezone.now().month

    mechanics_data = {}

    client_data = ClientData.objects.filter(created_date__month=selected_month)
    for data in client_data:
        mechanic_name = data.mechanic.name
        labor_cost = data.labor_cost
        if mechanic_name in mechanics_data:
            mechanics_data[mechanic_name] += labor_cost
        else:
            mechanics_data[mechanic_name] = labor_cost

    sorted_mechanics = sorted(mechanics_data.items(), key=lambda x: x[1], reverse=True)

    top_mechanics = [{'mechanic_name': mechanic, 'total_labor_cost': labor_cost} for mechanic, labor_cost in sorted_mechanics]

    return render(request, 'servizas/top_month_mechanic.html', {'current_month': month_names[selected_month],
        'selected_month': selected_month, 'top_mechanics': top_mechanics, 'month_names': month_names})

def home(request):
    queryset = None
    count = None

    if request.method == 'POST':
        form = ClientDataFilterForm(request.POST)
        if form.is_valid():
            start_date = form.cleaned_data.get('start_date')
            end_date = form.cleaned_data.get('end_date')
            query = form.cleaned_data.get('query')

            queryset = ClientData.objects.all()

            if start_date and end_date:
                queryset = queryset.filter(created_date__range=(start_date, end_date))

            if query:
                queryset = queryset.filter(
                    Q(client_name__icontains=query) |
                    Q(model__icontains=query) |
                    Q(make__icontains=query) |
                    Q(number_plate__icontains=query) |
                    Q(mechanic__name__icontains=query)
                )

            queryset = queryset.order_by('-created_date')
            count = queryset.count()

    else:
        form = ClientDataFilterForm()

    return render(request, 'base.html', {'form': form, 'queryset': queryset, 'count': count})