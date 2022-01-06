from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
from django.shortcuts import redirect

from .models import Produits
from .forms import ProductForm

# Create your views here.
def index(request):
    produits = Produits.objects.all()
    context = {'produits': produits}
    return render(request, 'products/index.html', context)

def formulaire(request):
  if(request.method == 'POST'):
    if(request.POST.get('nom') and request.POST.get('qty') and request.POST.get('category')):
        new_entity = Produits()
        new_entity.nom = request.POST.get('nom')
        new_entity.qty = request.POST.get('qty')
        new_entity.category = request.POST.get('category')
        new_entity.save()
        print('Success : Entity Added')
    else:
        print('Error : Bad Data Sent')
    return redirect('/products/index')
  else:
    return render(request, 'products/formulaire.html')
