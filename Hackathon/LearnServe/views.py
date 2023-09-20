from django.shortcuts import render
from django.http import HttpResponse,Http404,HttpResponseRedirect
from .models import TestModel,TeachingRegistration
from .forms import NameForm,VolenteerForm
from django.urls import reverse

def home(request):
    return render(request, "LearnServe/home.html")


def volenteer_info(request):
    return HttpResponse("uve reached Scouting")

def get_volenteering(request):
    context = {}
    form = VolenteerForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        url = reverse('volenteer_info')
        return HttpResponseRedirect(url)
    else:
        form = VolenteerForm()
        # print("hello world")
    context['forms'] = form
    context['variable'] = 'volenteering'
    return render(request, "LearnServe/forms.html", context)



def teaching_info(request):
    return HttpResponse("Uve reached teaching Information")


def teachers(request):
    context = {}
    form = NameForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        url = reverse('teaching_info')
        return HttpResponseRedirect(url)
    else:
        form = NameForm()
        # print("hello world")
    context['forms'] = form
    context['variable'] = 'teaching'
    return render(request, "LearnServe/forms.html", context)


def education(request):
    return HttpResponse("Uve reached education")
def details(request,question_id):
    question = get_object_or_404(Question, pk=question_id)
    render(request, "LearnServe/details.html",{"question":question})
