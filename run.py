pip install pypmml
from pypmml import Model
model = Model.fromFile('/content/test2.0.pmml')
sample_input = {
    'Car Model = BMW X5': 1,
    'Car Model = Mercedez Benz C class': 0,
    'Mileage': 69000,
    'Age(yrs)': 6,
}

result = model.predict(sample_input)

print(result)
