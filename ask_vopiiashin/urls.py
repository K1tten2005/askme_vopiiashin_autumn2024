from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from ask_vopiiashin import settings
from askme import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('askme/', views.askme, name='home'),
    path('ask/', views.ask, name='home'),
    path('question/', views.question, name='home'),
    path('tag/', views.tag, name='home'),
    path('settings/', views.settings, name='home'),
    path('login/', views.login, name='home'),
    path('signup/', views.signup, name='home'),

]
