import numpy as np
import pandas as pd

from sklearn import svm

import matplotlib.pyplot as plt
import seaborn as sns
import pickle
import joblib
import cloudpickle
sns.set(font_scale=1)

# for jupyter notebook
# get_ipython().run_line_magic('matplotlib', 'inline')

# load training data
recipies = pd.read_csv('data.csv')
print(recipies.head())


# plot graph
# sns.lmplot("flour","sugar",data=recipies,markers='*',size=6,order=0,scatter=True,fit_reg=False)
sns.lmplot(x="flour",
           y="sugar",
           data=recipies,
           size=6,
        #    aspect=1,
           markers=["x",'*'],
           hue='type',
           palette='Set1',
           fit_reg=False,
           scatter_kws={'s': 50},
           )
plt.show()

# convert labels to 0 or 1 [muffin=0,cupcake=1]
type_label = np.where(recipies['type'] == 'muffin', 0, 1)
# print(type_label)

# features['flour', 'milk', 'sugar', 'butter', 'egg', 'baking powder', 'vanilla', 'salt']
# recipie_features = recipies.columns.values[1:].tolist()
# print(recipie_features)


# extract 2 features for now which we will use to train
ingredients = recipies[['flour', 'sugar']].values

# make a SVC(support vector classifier) object
model = svm.SVC(kernel='linear', probability=True)
# train the svc object
model.fit(ingredients, type_label)

# save the model/object to disk for later use
pickle.dump(model,open('model.dat','wb'))
