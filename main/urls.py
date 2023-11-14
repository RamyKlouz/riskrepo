from . import views
from django.urls import path

app_name = 'main'

urlpatterns = [
    path('', views.index, name='index'),
    path('cursus/', views.cursus, name='cursus'),
    path('cv/', views.cv, name='cv'),
    path('cursuscv/', views.cursuscv, name='cursuscv'),
    path('courses/<str:categorie>/', views.courses, name='courses'),
    path('diplomes_details/<int:id>/', views.diplomes_details, name='diplomes_details'),
    path('save_avis/', views.save_avis, name='save_avis'),
    path('save_Payment/', views.save_Payment, name='save_Payment'),
    path('chat/', views.chat, name='chat'),
]