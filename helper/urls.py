from django.urls import path
from . import views

from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('', views.index, name='home_helper'),
    path('<int:pk>', views.Detail.as_view(), name='quest-detail'),
    path('adder/', views.index, name='adder_helper'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)