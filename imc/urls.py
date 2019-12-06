from django.urls import path
from . import views


urlpatterns = [
	path('',views.index,name='index'),
	path('servicios.html',views.servicios,name='servicios'),
	path('planes.html',views.planes,name='planes'),
	path('imc.html',views.imc,name='imc'),
	path('imc2.html',views.imc2,name='imc2'),
	path('faq.html',views.faq,name='faq'),
	path('contacto.html',views.contacto,name='contacto'),
	path('acerca.html',views.acerca,name='acerca'),
	path('404.html',views.cuatrocerocuatro,name='cuatrocerocuatro'),
]