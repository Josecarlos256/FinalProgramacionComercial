from django.conf.urls import url
from django.urls.resolvers import URLPattern
from . import views

urlpatterns = [
    url('curso/nuevo/', views.curso_nuevo, name='curso_nuevo'),
]