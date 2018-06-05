
from django.conf.urls import url
from django.urls import path
from . import views


urlpatterns = [
    # mas adelante se creara el index
    # path('', views.Index.as_view(), name='index'),
    path('', views.AveListView.as_view(), name='index'),
    path('aves/<int:pk>', views.AveDetailView.as_view(), name='ave-detail'),
    path('api/aves', views.AvesList.as_view(), name='api-ave-list'),
    path('api/clase', views.ClaseList.as_view(), name='api-clase-list'),
    path('api/orden', views.OrdenList.as_view(), name='api-orden-list'),
    path('api/familia', views.FamiliaList.as_view(), name='api-familia-list'),
    path('api/genero', views.GeneroList.as_view(), name='api-genero-list'),
    path('api/especie', views.EspecieList.as_view(), name='api-especie-list'),
]
