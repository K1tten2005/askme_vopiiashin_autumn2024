from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from ask_vopiiashin import settings
from askme import views

app_name = 'askme'

urlpatterns = [
    path('', views.askme, name='main_page'),
    path('hot/', views.hot, name='hot'),
    path('tag/<str:tag_name>', views.tag, name='tag'),
    path('question/<int:question_id>', views.question, name='question'),
    path('question/<int:question_id>/answer/', views.add_answer, name='add_answer'),
    path('question_like/<int:question_id>/', views.question_like, name='question_like'),
    path('answer_like/<int:answer_id>/', views.answer_like, name='answer_like'),
    path('answer/rate_correct/<int:answer_id>/', views.rate_correct, name='rate_correct'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('signup/', views.signup, name='signup'),
    path('ask/', views.ask, name='ask'),
    path('settings/', views.settings, name='settings'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.BASE_DIR / 'static')
