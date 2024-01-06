import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import pickle

df = pd.read_csv('data/drug.csv')
print(df)

df.drop_duplicates(inplace = True)

from sklearn import preprocessing
lb_enc = preprocessing.LabelEncoder()
df['BP'] = lb_enc.fit_transform(df['BP'])
df['Cholesterol'] = lb_enc.fit_transform(df['Cholesterol'])
df['Drug'] = lb_enc.fit_transform(df['Drug'])

df = df.replace({'F' :0, 'M':1})

# from sklearn.preprocessing import MinMaxScaler
# mm = MinMaxScaler()
# df['Na_to_K'] = mm.fit_transform(df[['Na_to_K']].values)
# #df['Age'] = mn.fit_transform(df[['Age']].values)

from sklearn.model_selection import train_test_split

X = df.drop(columns = ['Drug'])
y = df['Drug']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.01, random_state=6,shuffle = True )

# from sklearn import svm
# sv = svm.SVC(kernel= 'linear')

# sv.fit(X_train,y_train)

from sklearn.tree import DecisionTreeRegressor
dtr = DecisionTreeRegressor()

dtr.fit(X_train, y_train)


# filenmae = 'drugg.pkl'
# with open(filenmae, 'wb') as file:
#     pickle.dump(sv, file)

pickle.dump(dtr, open('model/drugg.pkl', 'wb'))

# dtr = pickle.load(open('drug.pkl', 'rb'))
# y_pred = dtr.predict(X_train)
# accuracy = accuracy_score(y_train, y_pred)
# print(accuracy*100)



