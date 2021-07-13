from django.urls import path
from . import views

urlpatterns = [
    path('demo', views.index, name='demo'),
    path('new_interaction', views.new_interaction, name='new_interaction'),
    path('save_share', views.save_share, name='save_share'),
    path('help', views.help, name='help'),
    path('library', views.library, name='library')
]
