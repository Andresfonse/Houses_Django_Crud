from django.urls import path, include
from . import views
from django.contrib import admin

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('nosotros', views.nosotros, name='nosotros'),
    path('accounts/profile/', views.propiedades, name='propiedades'),
    path('propiedades/crear', views.crear_propiedad, name='crear'),
    path('propiedades/editar', views.editar_propiedad, name='editar'),
    path('eliminar/<int:id>', views.eliminar, name='eliminar'),
    path('propiedades/editar/<int:id>', views.editar_propiedad, name='editar'),
    path('account/', include('django.contrib.auth.urls')),
    path('salir/', views.salir, name='salir'),
    path('user/', views.propuser, name='user'),
    path('agenda/editar', views.agenda, name='agenda'),
    path('agenda/editar/<int:id>', views.agenda, name='agenda'),
    path('agendados', views.agendados, name='agendados'),
    path('eliminarDatos/<int:id>', views.eliminarDatos, name='eliminarDatos')
]