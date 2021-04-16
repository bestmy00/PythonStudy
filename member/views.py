from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.hashers import make_password, check_password

from .models import BoardMember


def home(request):
    user_id = request.session.get('user')
    if user_id:
        member = BoardMember.objects.get(pk=user_id)
        return HttpResponse(member.username)

    return HttpResponse('Home!')


def register(request):
    if request.method == "GET":
        return render(request, 'register.html')
    elif request.method == "POST":
        username = request.POST.get('username', None)
        email = request.POST.get('email', None)
        password = request.POST.get('password', None)
        re_password = request.POST.get('re_password', None)
        res_data = {}
        if not (username and email and password and re_password):
            res_data['error'] = '모든 값을 입력해야 합니다.'
        if password != re_password:
            res_data['error'] = '비밀번호가 다릅니다.'
        else:
            member = BoardMember(
                username=username,
                password=make_password(password),
                email=email,
            )
            member.save()
        return render(request, 'register.html', res_data)


def login(request):
    form = LoginForm()
    return render(request, 'login.html', {'form': form})
    '''
    if request.method == "GET":
       return render(request, 'login.html')
    elif request.method == "POST":
        username = request.POST.get('username', None)
        password = request.POST.get('password', None)
        res_data = {}
        if not (username and password):
            res_data['error'] = '모든 값을 입력하세요!'
        else:
            member = BoardMember.objects.get(username=username)
            if check_password(password, member.password):
                pass
                request.session['user'] = member.id
                return redirect('/')
            else:
                res_data['error'] = '비밀번호가 다릅니다.'

        return render(request, 'login.html', res_data)
    '''



def logout(request):
    if request.session.get('user'):
        del(request.session['user'])

    return redirect('/')
