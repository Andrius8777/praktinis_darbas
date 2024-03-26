from django.shortcuts import render

def main_page(request):
    return render(request, 'main_page.html')

def about_page(request):
    return render(request, 'web_page/about_page.html')

def services_page(request):
    return render(request, 'web_page/services.html')

def shop_page(request):
    return render(request, 'web_page/shop.html')