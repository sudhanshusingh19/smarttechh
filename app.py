from flask import Flask, render_template
from geopy.geocoders import Nominatim

geolocator = Nominatim(user_agent="my_geocoder")


app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/transport')
def transport():
   '''
    s=input("enter source : ")
    location = geolocator.geocode(s)
    latitude = location.latitude
    longitude = location.longitude
    my_dict = {'latitude':latitude,'longitude':longitude}
    '''
   return render_template('transport.html')

@app.route('/waste')
def waste():
    return render_template('waste.html')

@app.route('/service')
def service():
    return render_template('service.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/eda1')
def output():
    return render_template('output.html')

@app.route('/eda2')
def output1():
    return render_template('output1.html')

if __name__ == '__main__':
    app.run(debug=True)
