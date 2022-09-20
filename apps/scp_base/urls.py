from django.urls import path
from apps.scp_base.views import *
from apps.scp_base import views
from apps.scp_base import euclid, ketter, thaumiel


urlpatterns = [
    path('add/', views.add_scp, name='add'),
    path('scp/', views.scp, name='scp'),
    path('olx/', view=views.add_img, name='olx'),
    path('save_delete/<id>', views.scp_save, name='save-delete'),

    path('euclid_info/', views.scp_euclid, name='euclid'),
    path('euclid_base/', euclid.add_euclid, name='add_euclid'),
    path('euclid/', view=euclid.euclid, name='euclid_data'),
    path('euclid_delete/<id>', euclid.del_euclid, name='euclid-delete'),

    path('keter_info/', ketter.scp_keter, name='keter'),
    path('keter_base/', ketter.add_keter, name='add_keter'),
    path('keter/', view=ketter.keter, name='keter_data'),
    path('delete_keter/<id>', ketter.delete_keter, name='delete-keter'),

    path('thaumiel_base/', thaumiel.add_thaumiel),
    path('thaumiel/', thaumiel.thaumiel),
    path('thaumiel_info/', thaumiel.scp_thaumiel, name='thaumiel_info'),
]
