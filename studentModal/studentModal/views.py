from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from Student.models import Student

from django.http import HttpResponse
from django.template.loader import get_template
from django.views.generic import View
from .utils import render_to_pdf


class GeneratePDF(View):
    def get(self, request, *args, **kwargs):
        template = get_template('showresult.html')
        # html = template.render()
        pdf = render_to_pdf('showresult.html')
        if pdf:
            response = HttpResponse(pdf, content_type='application/pdf')
            filename = "result.pdf"
            content = "inline; filename='%s'" % filename
            download = request.GET.get("download")
            if download:
                content = "attachment; filename='%s'" % filename
            response['Content-Disposition'] = content
            return response
        return HttpResponse("Not found")


def home(request):
    return render(request, 'master.html')


@login_required(login_url='login')
def after_login(request):
    global context
    s = is_student(request.user.id)
    if s == 1:
        e = Student.objects.get(user_id=request.user.id)
        context = {
            'student': e
        }
    return render(request, 'afterlogin.html', context)


def courses(request):
    return render(request, 'courses.html')


def logout_(request):
    logout(request)
    return redirect('master')


def login_(request):
    if request.method == 'GET':
        return render(request, 'login.html')
    else:
        u = request.POST.get('username')
        p = request.POST.get('pass')
        user = authenticate(username=u, password=p)
        if user is not None:
            login(request, user)
            a = is_student(request.user.id)
            if a == 1:
                return redirect('after_login')
            else:
                return redirect('student_info')
        else:
            messages.add_message(request, messages.ERROR, 'username or password not correct')
            return redirect('login')


def signup(request):
    if request.method == 'GET':
        return render(request, 'signup.html')
    else:
        u = request.POST.get('username')
        p1 = request.POST.get('password1')
        p2 = request.POST.get('password2')
        if p1 == p2:
            try:
                user = User(username=u)
                user.set_password(p2)
                user.save()
                return redirect('login')
            except:
                messages.add_message(request, messages.ERROR, 'Username already exist please choose another')
                return redirect('signup')
        else:
            messages.add_message(request, messages.ERROR, 'password doesnot match')
            return render(request, 'signup.html')


@login_required(login_url='login')
def student_dashboard(request):
        return render(request, 'student_dashboard.html')


@login_required(login_url='login')
def profile(request):
    s = is_student(request.user.id)
    if s == 1:
        e = Student.objects.get(user_id=request.user.id)
        context1 = {
            'student': e
        }
        return render(request, 'profile.html', context1)
    else:
        redirect('student_dashboard')


def is_student(id):
    try:
        a = Student.objects.get(user_id=id)
        return 1

    except:
        return 0
