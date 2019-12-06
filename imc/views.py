from django.shortcuts import render
from .models import ket
from .forms import PostForm

def index(request):

	num_visitas=request.session.get('num_visitas', 0)
	num_visitas=request.session['num_visitas']=num_visitas+1

	return render(
		request,
		'index.html',
		context={'ketcount':ket.contar(ket), 'promedioIMC':ket.promedioIMC(ket), 'num_visitas':num_visitas})

def faq(request):
	return render(
		request,
		'faq.html')

def servicios(request):
	return render(
		request,
		'servicios.html')

def planes(request):
	return render(
		request,
		'planes.html')

def imc(request):
	return render(
		request,
		'imc.html')

def imc2(request):
	form = PostForm()

	if request.method == "POST":
		form = PostForm(request.POST)
		if form.is_valid():
			post = form.save(commit=False)
			post.save()
	else:
		form = PostForm()
	return render(request,'imc2.html',{'form': form})



def contacto(request):
	return render(
		request,
		'contacto.html')

def acerca(request):
	return render(
		request,
		'acerca.html')

def cuatrocerocuatro(request):
	return render(
		request,
		'404.html')

from django.views.generic.edit import CreateView, UpdateView, DeleteView
from . models import ket

class ketCreate(CreateView):
	model = ket
	fields = '__all__'

class ketUpdate(UpdateView):
	model = ket
	fields = ['nombre','peso','estatura','edad','sexo']

class ketDelete(DeleteView):
	model = ket
