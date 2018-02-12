
from django.conf.urls import url
from django.urls import path
from . import views


urlpatterns = [
    # mas adelante se creara el index
    # path('', views.Index.as_view(), name='index'),
    path('', views.AveListView.as_view(), name='index'),
    path('aves/<int:pk>', views.AveDetailView.as_view(), name='ave-detail'),
]
