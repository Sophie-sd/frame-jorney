from django.shortcuts import render
# Видаляємо невикористовуваний HttpResponse
# from django.http import HttpResponse 

# Create your views here.

def home(request):
    # Рендеримо єдиний шаблон home.html
    return render(request, 'core/home.html')

# Видаляємо непотрібні views
# def about(request):
#     return render(request, 'core/about.html')
# 
# def portfolio(request):
#     return render(request, 'core/portfolio.html')
# 
# def reviews(request):
#     return render(request, 'core/reviews.html')
# 
# def services(request):
#     return render(request, 'core/services.html')
# 
# def contact(request):
#     return render(request, 'core/contact.html') 