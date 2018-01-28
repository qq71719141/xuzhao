from django.shortcuts import render, redirect
from django.http import JsonResponse
from df_user.models import Passport
from df_user.models import Passport, Address
from utils工具.get_hash import get_hash
from django.core.mail import send_mail
from df_user.tasks import send_email


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
    Passport.objects.add_user(name, get_hash(pwd), email)
    send_email.delay(name=name, email=email)
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
            request.session['is_login'] = True
            request.session['name'] = name
            request.session['post_id'] = user.id
            if request.session.has_key('prev_url'):
                next = request.session['prev_url']
            else:
                next = '/index/'
            return JsonResponse({'ret': next})
        else:
            return JsonResponse({'ret': 2})


def index(request):
    return render(request, 'df_user/index.html')

def user_center_info(request):
    if request.session.has_key('name'):
        addr = Address.objects.get_address(passport_id=request.session['post_id'])
        return render(request, 'df_user/user_center_info.html', {'page': 1, 'addr':addr})
    else:
        return redirect('/login/')


def user_center_order(request):
    if request.session.has_key('name'):
        return render(request, 'df_user/user_center_order.html', {'page': 2})
    else:
        return redirect('/login/')


def cart(request):
    if request.session.has_key('name'):
        return render(request, 'df_user/cart.html')
    else:
        return redirect('/login/')


def detail(request):
    return render(request, 'df_user/detail.html')


def list(request):
    return render(request, 'df_user/list.html')


def place_order(request):
    return render(request, 'df_user/place_order.html')


def login_out(request):
    request.session.flush()
    return redirect('/index/')


def user_center_site(request):
    if request.method == 'POST':
        print('post')
        name = request.POST['name']
        addr = request.POST['addr']
        zip_code = request.POST['zip']
        phone = request.POST['phone']
        Address.objects.add_info(request.session['post_id'], name, addr, zip_code, phone)
        return redirect('/user_center_site/')
    else:
        addr = Address.objects.get_address(passport_id=request.session['post_id'])
        return render(request, 'df_user/user_center_site.html', {'addr': addr, 'page': 0})