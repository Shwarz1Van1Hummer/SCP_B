from django.shortcuts import render, redirect
from apps.scp_base.models import SCPThaumiel


def add_thaumiel(request):
    if request.method == 'GET':
        return render(
            request=request,
            template_name='primary/protect.html',
            context={}
        )
    else:
        title_object = request.POST.get('title_object')
        description = request.POST.get('description')
        file = request.FILES.get('thaumiel_file')
        scp_thaumiel = SCPThaumiel.objects.create(title_object=title_object, description=description, image=file)
        return redirect('/scp/add/')


def thaumiel(request):
    if request.method == "GET":
        scp_thaumiel = SCPThaumiel.objects.all()
        return render(
            request=request,
            template_name='primary/thaumiel_base.html',
            context={'scp_thaumiel': scp_thaumiel}
        )


def scp_thaumiel(request):
    if request.method == 'GET':
        return render(
            request=request,
            template_name='primary/thaumiel_info.html',
            context={}
        )



    # Подредактирорвать форму таумиеля