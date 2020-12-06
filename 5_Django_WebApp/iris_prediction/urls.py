from django.urls import path
from . import views

app_name = 'iris_prediction'

urlpatterns = [
    path('', views.predict, name='iris_prediction_form'),
    path('predict/', views.predict_chances, name='submit_prediction'),
    path('results/', views.view_results, name='results'),
]