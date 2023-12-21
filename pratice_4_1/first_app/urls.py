from django.urls import path
from . import views
urlpatterns = [
    path('', views.home , name='home'),
    path('forms/',views.forms , name = 'forms'),
    path('models/',views.models_view , name = 'models'),
]