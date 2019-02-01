import pandas as pd
from sklearn import svm
import pickle
# from create_data import create_test_data

# create_test_data()
# load trained model from disk
model = pickle.load(open('model.dat', 'rb'))

# function to check testing data
# returns predicted outcome and its probability


def check(ingredients):
    if(model.predict([ingredients]) == 0):
        return 'muffin', model.predict_proba([ingredients])
    else:
        return 'cupcake', model.predict_proba([ingredients])


# load testing data
test_data = pd.read_csv('test.csv')
# extract first 2 features as we trained it for 2 features only
l = test_data[['type', 'flour', 'milk', 'sugar', 'butter','egg', 'baking powder', 'vanilla', 'salt']].values.tolist()
# print(l)
# iterate through test data and check it
for data in l:
    type = data[0]
    ingredients=data[1:]
    res = check(ingredients)
    prediction = res[0]
    prob = res[1][0]
    prob0=prob[0]
    prob1=prob[1]

    if prediction == type:        
        print('{}\t{} data:{} \t {}({}) \tConfidence::- [ {:.2f} , {:.2f} ]'.format(
            '-'*4, prediction == type, ingredients, prediction, type, prob0, prob1))

    else:
        print('{}\t{} data:{} \t {}({}) \tConfidence::- [ {:.2f} , {:.2f} ]'.format(
            'X'*4, prediction == type, ingredients, prediction, type, prob0, prob1))
