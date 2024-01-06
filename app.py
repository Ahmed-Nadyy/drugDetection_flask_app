from flask import Flask,request ,render_template
import pickle
import numpy as np


dtr = pickle.load(open('model/drugg.pkl','rb'))
# dtr = pickle.load(open('drug.pkl', 'rb'))
app = Flask(__name__)

@app.route('/')
def man():
    return render_template('homee.html')

@app.route('/predict', methods=['POST'])
def home():
    data1 = request.form['a']
    data2 = request.form['b']
    data2= data2.upper()
    if(data2 == "F"):
        data22 = 0

    else : 
        data22 = 1
        

    data3 = request.form['c']
    data2= data3.upper()
    if(data3 == 'HIGH') :
        data33 = 0
        
    elif (data3 == 'LOW') :
        data33 = 1
        
    else :
        data33 = 2
        # data3 = float(data3)

    data4 = request.form['d']
    data2= data4.upper()
    if(data4 == 'HIGH') :
        data44 = 0
        # data44 = float(data4)
    else : 
        data44 = 1
        # data44 = float(data4)
     
    data5 = request.form['e']
    # from sklearn.preprocessing import MinMaxScaler
    # mm = MinMaxScaler()
    # data55 = mm.fit_transform(data5.values)

    arr = np.array([[data1, data22, data33, data44, data5]])
    print (arr)
    pred = dtr.predict(arr)
    return render_template('afterr.html', data= pred)




if __name__ == '__main__':
     app.run(debug=True)