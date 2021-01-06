from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import StudentForm
from .models import News


def student_info(request):
    if request.method == 'GET':
        context = {
            'form': StudentForm()
        }
        return render(request, 'student.html', context)
    else:
        form = StudentForm(request.POST, request.FILES)
        if form.is_valid():
            data = form.save(commit=False)
            data.user_id = request.user.id
            try:
                data.save()
                return redirect('after_login')
            except:
                messages.add_message(request, messages.ERROR, 'Failed To Update Please Try Again')
                return redirect('student_info')
        else:
            context1 = {
                'form': form
            }
            return render(request, 'student.html', context1)


# def showNews(request):
#     s = News.objects.all()
#     context = {
#         'news': s,
#     }
#     print(context, 'all data successfully arrived')
#     return render(request, 'student_dashboard.html', context)


def news(request):
        s = News.objects.all()
        b = len(s)
        c = s[0]
        c1 = s[1]
        c2 = s[2]
        c3 = s[3]
        context = {
            'news': s,
            'item': b,
            'sixth': c,
            'first': c1,
            'routine': c2,
            'tour': c3,

        }
        return render(request, 'afterlogin.html', context)



