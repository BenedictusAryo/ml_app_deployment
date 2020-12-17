from django.shortcuts import render
from django.http import JsonResponse
from django.utils import timezone
import pandas as pd 
from .models import PredResults
from django.contrib.auth.decorators import login_required
import os
import pickle

################  Model File and Folder Location  ###################
MODEL_FILE = 'iris_model.pkl'
MODEL_PATH = os.path.abspath(os.path.join(os.path.dirname(os.path.realpath(__file__)), os.pardir, os.pardir, MODEL_FILE))


####################  Model Class  #############################
class IrisModel:
    def __init__(self, model_path):
        self.model = pickle.load(open(model_path, 'rb'))

    def predict(self, features):
        return self.model.predict(features)[0]

model = IrisModel(MODEL_PATH)  

# Create your views here.

@login_required
def predict(request):
    return render(request, 'predict.html')

def predict_chances(request):
    if request.POST.get('action') == 'post':

        # Receive data from client
        sepal_length = float(request.POST.get('sepal_length'))
        sepal_width = float(request.POST.get('sepal_width'))
        petal_length = float(request.POST.get('petal_length'))
        petal_width = float(request.POST.get('petal_width'))

        # Make Prediction
        result = model.predict([[sepal_length, sepal_width, petal_length, petal_width]])

        classification = result.capitalize()

        PredResults.objects.create(pred_date=timezone.now(),sepal_length=sepal_length, sepal_width=sepal_width,
                                   petal_length=petal_length, petal_width=petal_width,
                                   classification=classification)

        return JsonResponse(
            {
                'result': classification,
                'sepal_length':sepal_length,
                'sepal_width':sepal_width,
                'petal_length':petal_length,
                'petal_width':petal_width
            },
            safe=False)


def view_results(request):
    # Submit prediction and show all
    data = {'dataset':PredResults.objects.all()}
    return render(request, 'results.html', data)