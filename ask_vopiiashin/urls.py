from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from ask_vopiiashin import settings
from askme import views

urlpatterns = [
    path('admin/', admin.site.urls, name='admin'),
    path('', include('askme.urls')),
]
