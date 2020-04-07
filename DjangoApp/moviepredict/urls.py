from django.urls import path

from . import views

app_name = 'moviepredict'
urlpatterns = [
    path('', views.index, name='index'),
    path('makeprediction/', views.makeRatingPrediction, name='makepredict')
]