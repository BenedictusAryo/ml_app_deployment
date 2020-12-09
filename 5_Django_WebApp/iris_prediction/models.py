from django.db import models

# Create your models here.
class PredResults(models.Model):
    pred_date = models.DateTimeField('prediction date')
    sepal_length = models.FloatField()
    sepal_width = models.FloatField()
    petal_length = models.FloatField()
    petal_width = models.FloatField()
    classification = models.CharField(max_length=30)

    def __str__(self):
        return self.classification