from django.shortcuts import render
from django.http import JsonResponse
from df_user.models import Passport
from df_user.models import Passport
# Create your views here.
def register(request):
    return render(request, 'df_user/register.html')

def check_register(request):
    name = request.POST.get('user_name')
    try:
        Passport.objects.get(username=name)
        return JsonResponse({'ret': 0})
    except Exception as i:
        return JsonResponse({'ret': 1})

def register_handle(request):
    name = request.POST.get('user_name')
    pwd = request.POST.get('pwd')
    email = request.POST.get('email')
    Passport.objects.add_user(name, pwd, email)
    return render(request, 'df_user/login.html')

def login(request):
    return render(request, 'df_user/login.html')

def check_login(request):
    name = request.POST['name']
    pwd = request.POST['pwd']
    try:
        user = Passport.objects.get(username=name)
    except Exception as i:
        return JsonResponse({'ret': 0})
    else:
        if name == user.username and pwd == user.password:
            print('ojbk')
            return JsonResponse({'ret': 1})
        else:
            return JsonResponse({'ret': 2})