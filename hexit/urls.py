
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name="colors-page"),
    path('hex-to-rgb-and-rgb-to-hex-converter', views.converter, name="colour-code-converter-page"),
]
