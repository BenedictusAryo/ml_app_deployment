from django.contrib import admin
from django.apps import apps

# Register your models here.
for model in apps.get_app_config('iris_prediction').get_models():
    admin.site.register(model)