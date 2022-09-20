from django.shortcuts import render, redirect
from apps.scp_base.models import SCPEuclid
from django.views.generic import View


def add_euclid(request):
    if request.method == 'GET':
        return render(
            request=request,
            template_name='primary/protect.html',
            context={}
        )
    else:
        title_object = request.POST.get('title_object')
        description = request.POST.get('description')
        file = request.FILES.get('euclid_file')
        scp_euclid = SCPEuclid.objects.create(title_object=title_object, description=description, image=file)
        return redirect('/scp/add/')


def euclid(request):
    if request.method == "GET":
        scp_euclid = SCPEuclid.objects.all()
        return render(
            request=request,
            template_name="primary/euclid_base.html",
            context={'scp_euclid': scp_euclid}
        )


def del_euclid(request, id):
    euclid_del = SCPEuclid.objects.get(pk=id)
    euclid_del.delete()
    return redirect('add_euclid')
