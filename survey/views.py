from django.shortcuts import render, HttpResponse
from .models import Survey
from .forms import SurveyForm, NameForm, P1Form, P2Form


def survey(request):
    if request.method == "POST":
        print('post')
        form = SurveyForm(request.POST)
        if form.is_valid():
            print('valid')
            form.save()
        context = {'form': form}
        return HttpResponse("Thanks for participating in survey")
    else:
        form = SurveyForm
        context = {'form': form}
        return render(request, 'Survey/survey.html',context )


def review(request):
    if request.method == "POST":
        print('post')
        form = NameForm(request.POST)
        form2 = P1Form(request.POST)
        form3 = P2Form(request.POST)
        if form.is_valid() and form2.is_valid() and form3.is_valid():
            print('valid')
            a = form.save()
            b = form2.save(commit=False)
            c = form3.save(commit=False)
            b.name = a
            c.name = a
            b.save()
            c.save()

        return HttpResponse("Thanks for participating in survey")
    else:
        form = NameForm
        form1 = P1Form
        form2 = P2Form
        context = {'form': form,'form1':form1,'form2':form2}
        return render(request, 'Survey/review.html',context )
