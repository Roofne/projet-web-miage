from django.urls import path

from . import views

urlpatterns = [
    path('', views.index       , name='index'),
    path('index', views.index  , name='index'),
    path('benef', views.benef  , name='benef'),
    path('listebenef',views.listebenef,name='listebenef'),
    path('modifierbenef/<id_benef>',views.modifierbenef,name='modifierbenef'),
    path('delete_benef/<id_benef>',views.delete_benef,name='delete_benef')
]
