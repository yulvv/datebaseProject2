from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User



def navigation(request):
    return render(request, 'navigation.html')


# login
def loginPage(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("/")
        else:
            return HttpResponse("ERROR Password")
    if request.method == 'GET':
        return render(request, 'login.html')

# logout
def logoutPage(request):
    logout(request)
    return redirect("/")

# 注册
def registerPage(request):
    if request.method == 'POST':
        try:
            username = request.POST['username']
            password = request.POST['password']
            person = User.objects.filter(username=username)
            if any(person):
                return HttpResponse("您输入的用户名已存在！")
            user = User.objects.create_user(username, '', password)
            user.save()
            return HttpResponse("注册成功！")
        except:
            return HttpResponse("Invild Input")
    if request.method == 'GET':
        return render(request, 'register.html')

