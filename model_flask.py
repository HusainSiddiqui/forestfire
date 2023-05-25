from flask import Flask, render_template, request
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression,Lasso,Ridge
import pickle

ridge=pickle.load(open('C:/Users/Admin/Documents/Python_Program/assingment/ex/templates/ridge_model.pickle','rb'))
scale=pickle.load(open('C:/Users/Admin/Documents/Python_Program/assingment/ex/templates/scaler.pickle','rb'))
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('model_html.html')

@app.route('/pridectdata', methods=['GET', 'POST'])

def predict_datapoint():
    
    if request.method == 'POST':
        num1 = float(request.form.get('temp'))
        num2 = float(request.form.get('rh'))
        num3 = float(request.form.get('ws'))
        num4 = float(request.form.get('rain'))
        num5 = float(request.form.get('ffmc'))
        num6 = float(request.form.get('dmc'))
        num7 = float(request.form.get('region'))
        
        new_scale=scale.transform([[num1,num2,num3,num4,num5,num6,num7]])
        print('***********',new_scale,'**************')
        
        result=ridge.predict(new_scale)
        print('++++++++++',result,'++++++++++++')
        
        return render_template('model_html.html' ,result=result)

    else:
        return render_template('model_html.html')

if __name__ == '__main__':
    app.run()
