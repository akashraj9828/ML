import pandas as pd
from sklearn import svm
import pickle

# load trained model from disk
model = pickle.load(open('model.dat', 'rb'))

# function to check testing data
# returns predicted outcome and its probability
def check(flour, milk):
    if(model.predict([[flour, milk]]) == 0):
        return 'muffin', model.predict_proba([[flour, milk]])
    else:
        return 'cupcake', model.predict_proba([[flour, milk]])


# load testing data
test_data = pd.read_csv('test.csv')
# extract first 2 features as we trained it for 2 features only
l = test_data[['type', 'flour', 'milk']].values
# print(l)
# iterate through test data and check it
for data in l:
    type = data[0]
    flour = data[1]
    milk = data[2]
    res = check(flour, milk)
    prediction = res[0]
    prob = res[1][0]
    prob0=prob[0]
    prob1=prob[1]

    if prediction == type:        
        print('{}\t{} flour:{} milk:{} {}({}) \tConfidence::- [ {:.2f} , {:.2f} ]'.format(
            '-'*4, prediction == type, flour, milk, prediction, type, prob0, prob1))

    else:
        print('{}\t{} flour:{} milk:{} {}({}) \tConfidence::- [ {:.2f} , {:.2f} ]'.format(
            'X'*4, prediction == type, flour, milk, prediction, type, prob0, prob1))
