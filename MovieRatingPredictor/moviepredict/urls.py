from django.urls import path

from . import views

app_name = 'moviepredict'
urlpatterns = [
    path('', views.index, name='index'),
    path('result/<int:budget>', views.result, name='result'),
    path('makeprediction/', views.makeRatingPrediction, name='makepredict')
]