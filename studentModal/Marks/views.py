from django.shortcuts import render, redirect
from .models import SixthSem, FirstSem, SecondSem
from django.contrib import messages


def search_marks(request):
    try:
        if request.method == 'GET':
            return render(request, 'student_dashboard.html')
        else:
            result = request.POST.get('roll_no')
            e = SixthSem.objects.get(roll_no=result)
            a = e.webTech
            b = e.compiler
            c = e.rts
            d = e.software
            f = e.dot_net
            g = e.e_commerce
            list1 = [a, b, c, d, f, g]
            for item in list1:
                if item == None:
                    list1.remove(None)
                    total = sum(list1)
                    i = len(list1)
                    avg = (total / i)
                    if avg <= 40:
                        a = 'not a good result'
                    elif 40 <= avg <= 59:
                        a = 'satisfactory result, second division'
                    elif 60 <= avg <= 75:
                        a = 'good result'
                    elif 75 <= avg <= 89:
                        a = 'Very Good'
                    elif avg >= 90:
                        a = 'Outstanding Result'
            context = {
                'marks': e,
                'total': total,
                'avg': avg,
                'remarks': a
            }

            return render(request, 'showresult.html', context)
    except:
        messages.add_message(request, messages.ERROR, 'Record not Found')
        return redirect('student_dashboard')


def first_sem(request):
    try:
        if request.method == 'GET':
            return render(request, 'firstsem/firstSearch.html')
        else:
            result1 = request.POST.get('roll_no')
            h = FirstSem.objects.get(roll=result1)
            a = h.Physics
            c = h.math
            d = h.C_programming
            f = h.Digital
            g = h.F_it
            list1 = [a, c, d, f, g]
            for item in list1:
                if item == None:
                    list1.remove(None)
                else:
                    total = sum(list1)
                    i = len(list1)
                    avg = (total / i)
                    if avg <= 40:
                        a = 'Your result is not good practice well again'
                    elif 40 <= avg <= 59:
                        a = 'satisfactory result, second division'
                    elif 60 <= avg <= 75:
                        a = 'good result'
                    elif 75 <= avg <= 89:
                        a = 'Very Good'
                    elif avg >= 90:
                        a = 'Outstanding Result'
            context = {
                'marks': h,
                'total': total,
                'avg': avg,
                'remarks': a
            }

            return render(request, 'firstsem/firstsem.html', context)
    except:
        messages.add_message(request, messages.ERROR, 'Record not Found')
        return redirect('first_sem')


def second_sem(request):
    try:
        if request.method == 'GET':
            return render(request, 'secondsem/secondSearch.html')
        else:
            result = request.POST.get('roll_no')
            h = SecondSem.objects.get(roll_no=result)
            a = h.discrete
            c = h.math_ii
            d = h.micro
            f = h.stat_i
            g = h.oop
            list1 = [a, c, d, f, g]
            print(list1)
            for item in list1:
                if item == None:
                    list1.remove(None)
                else:
                    total = sum(list1)
                    i = len(list1)
                    avg = (total / i)
                    if avg <= 40:
                        a = 'Your result is not good practice well again'
                    elif 40 <= avg <= 59:
                        a = 'satisfactory result, second division'
                    elif 60 <= avg <= 75:
                        a = 'good result'
                    elif 75 <= avg <= 89:
                        a = 'Very Good'
                    elif avg >= 90:
                        a = 'Outstanding Result'
            context = {
                'marks': h,
                'total': total,
                'avg': avg,
                'remarks': a
            }

            return render(request, 'secondsem/secondsem.html', context)
    except:
        messages.add_message(request, messages.ERROR, 'Record not Found')
        return redirect('second_sem')