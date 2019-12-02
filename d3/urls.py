from django.urls import include, path

from . import views

urlpatterns = [
    path('', views.viewbarlinegraph, name='barline'),
    path('bar', views.viewbargraph, name='bar'),
    path('groupedbar', views.viewgroupedbargraph, name='groupedbar'),
    path('histogram', views.viewhistogramgraph, name='histogram'),
]
