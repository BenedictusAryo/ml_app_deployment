# Python Script Deployment

Model Deployment using Console Script is the most easiest and common method to serve the functionality of the program.

Script usualy purposed to do automation or scheduling which doesn't need UI Interface.

Script usually taking arguments alogside the script when running, in this case, our **Iris Flower Prediction Script** may take argument as features to predict the Iris Flower class.

When we running 
```python
python iris_prediction.py
```

We will see error help like this:

```python
Iris Flower Prediction

optional arguments:
  -h, --help            show this help message and exit

required named arguments:
  -sl SEPAL_LENGTH, --sepal_length SEPAL_LENGTH
                        Sepal Length of Iris Flower
  -sw SEPAL_WIDTH, --sepal_width SEPAL_WIDTH
                        Sepal Width of Iris Flower
  -pl PETAL_LENGTH, --petal_length PETAL_LENGTH
                        Petal Length of Iris Flower
  -pw PETAL_WIDTH, --petal_width PETAL_WIDTH
                        Petal Width of Iris Flower
```                        

Since our Script will need required Arguments like Sepal Length, Sepal Width, Petal Length, and Petal width as Features to predict the Iris Flower Class.

So we can run the script with argument like:

```python
python iris_prediction.py --sepal_length=5.56 --sepal_width=2.78 --petal_length=3.0 --petal_width=21.7
```
So that the script will output:
```python
Iris Flower Prediction

Input Features:  [5.56, 2.78, 3.0, 21.7]
Result:  Versicolor
```