from django.contrib import messages
from django.http import HttpResponseRedirect
from django.http import HttpResponse

from django.template  import loader
from django.shortcuts import render
from django.shortcuts import redirect
from .models import beneficiaire

# Create your views here.
def welcome(request):
    return render(request, 'users/welcome.html')

def index(request):
    return render(request, 'users/index.html', {'data': [1, 2, 3, 4,5,6,7,8]})

def listebenef(request):
    benefs=beneficiaire.objects.order_by('Nom')
    return render(request,'users/listebenef.html',{'benefs':benefs})

def modifierbenef(request, id_benef):
    ID_benef=beneficiaire.objects.get(pk=id_benef)
    if (request.method=="POST"):
        if request.POST.get('Nom'):
            ID_benef.Nom=request.POST.get('Nom')
        if request.POST.get('prenom'):
            ID_benef.prenom=request.POST.get('prenom')
        if request.POST.get('mail'):
            ID_benef.mail=request.POST.get('mail')
        if request.POST.get('telephone'):
            ID_benef.telephone=request.POST.get('telephone')
        if request.POST.get('postale'):
            ID_benef.postale=request.POST.get('postale')
        if request.POST.get('nb_parts'):
            ID_benef.nb_parts=request.POST.get('nb_parts')
        if request.POST.get('mot_mairie'):
            ID_benef.mot_mairie=request.POST.get('mot_mairie')
        if request.POST.get('carte_donnee'):
            ID_benef.carte_donnee=request.POST.get('carte_donnee')
        if request.POST.get('presence_aux_distributions'):
            ID_benef.presence_aux_distributions=request.POST.get('presence_aux_distributions')
        if request.POST.get('champ_remarque'):
            ID_benef.champ_remarque=request.POST.get('champ_remarque')
        ID_benef.save()
        benefs=beneficiaire.objects.order_by('Nom')
        return render(request,'users/listebenef.html',{'benefs':benefs})
    else:
        return render(request,'users/modifierbenef.html',{'benefs':ID_benef})

def delete_benef(request, id_benef):
    beneficiaire.objects.filter(id=id_benef).delete()
    return redirect('/users/listebenef')

def benef(request):
    if (request.method=="POST"):
        saverecord=beneficiaire()
        if request.POST.get('Nom'):
            saverecord.Nom=request.POST.get('Nom')
        if request.POST.get('prenom'):
            saverecord.prenom=request.POST.get('prenom')
        if request.POST.get('mail'):
            saverecord.mail=request.POST.get('mail')
        if request.POST.get('telephone'):
            saverecord.telephone=request.POST.get('telephone')
        if request.POST.get('postale'):
            saverecord.postale=request.POST.get('postale')
        if request.POST.get('nb_parts'):
            saverecord.nb_parts=request.POST.get('nb_parts')
        if request.POST.get('mot_mairie'):
            saverecord.mot_mairie=request.POST.get('mot_mairie')
        if request.POST.get('carte_donnee'):
            saverecord.carte_donnee=request.POST.get('carte_donnee')
        if request.POST.get('presence_aux_distributions'):
            saverecord.presence_aux_distributions=request.POST.get('presence_aux_distributions')
        if request.POST.get('champ_remarque'):
            saverecord.champ_remarque=request.POST.get('champ_remarque')
        saverecord.save()
        return redirect('/users/listebenef')
    else:
        return render(request,"users/benef.html")
