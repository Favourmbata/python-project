sample = {'name': 'kelly',
          'age': 25,
          'salary': 8000,
          'city': 'new york'}
keys = ['name', 'salary']

sample = {k: sample[k] for k in sample.keys() - keys}
print(sample)
