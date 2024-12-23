from django.shortcuts import render, HttpResponse

# Create your views here.
def main(request):
    return render(request, 'wowtyr/main.html', {'title':'Главная страница'})

def registration(request):
    return render(request, 'wowtyr/registration.html', {'title':'Регистрация'})

def aboutus(request):
    return render(request, 'wowtyr/aboutus.html',{'title':'О нас'})

def reviews(request):
    return render(request, 'wowtyr/reviews.html', {'title':'Отзывы'})

def tours(request):
    return render(request, 'wowtyr/tours.html', {'title':'Туры'})

def error(request):
    return render(request, 'wowtyr/error.html', {'title':'Ошибка 404'})