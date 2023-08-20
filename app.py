from flask import Flask,request,render_template
import requests
import json



app=Flask(__name__)

@app.route('/')
def main():
    return render_template('index.html')


@app.route('/predict',methods=['POST','GET'])
def predict():
    if request.method=='POST':
        city=request.form['input_text']
        url=f"https://api.weatherapi.com/v1/current.json?key=89a4c16fc3704719955142152231508&q={city}"

        r=requests.get(url)

        # print(r.text)

        wdic=json.loads(r.text)

        
        try:
        
            return render_template("index.html",temperature="The temperature is {} degree Celcius".format(str(wdic['current']['temp_c'])) ,Condition=" The Condition of the sky is {}".format(str(wdic['current']['condition']['text'])),wind="The Speed of the wind is {} kmph".format(str(wdic['current']['wind_kph'])) ,humidity="The humidity of the area is {} ".format(str(wdic['current']['humidity'])),location="The Location is : {}".format(str(wdic['location']['name'])) + " , {}".format(str(wdic['location']['region']))+", {}".format(str(wdic['location']['country'])),presure="The Presure od the area is {} MB".format(str(wdic['current']['pressure_mb'])) ,time="Time is : {}".format(str(wdic['location']['localtime'])))
        
        except:
            
            return render_template('error.html',location="Sorry , {}!!! Please enter correct location ".format(str(wdic['error']['message'])))

        
        
        
        


    return render_template("index.html")


if __name__=='__main__':
    app.run(debug=True)