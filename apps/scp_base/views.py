from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpRequest
from django.views.generic import CreateView, TemplateView, FormView, DetailView, ListView

from apps.scp_base.models import SCP


def add_scp(request):
        if request.method == 'GET':
            return render(
                request=request,
                template_name='primary/protect.html',
                context={}
              )
        else:
            title_object = request.POST.get('title_object')
            description = request.POST.get('description')
            file = request.FILES.get('file')
            scps = SCP.objects.create(title_object=title_object, description=description, image=file)
            return redirect('/scp/add/')


def scp(request):
    if request.method == "GET":
        scps = SCP.objects.all()
        return render(
            request=request,
            template_name="primary/protect_save.html",
            context={'scps': scps}
            )


def add_img(request):
    if request.method == 'GET':
        return render(
            request=request,
            template_name='primary/olx.html',
            context={
                'scp': scp
            }
        )


def scp_euclid(request):
    if request.method == 'GET':
        return render(
            request=request,
            template_name='primary/euclid_info.html',
            context={
                'scp': scp
            }
        )


def scp_save(request, id):
    save = SCP.objects.get(pk=id)
    save.delete()
    return redirect('scp')