from django.shortcuts import render, HttpResponse
from .models import Survey
from .forms import SurveyForm


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
