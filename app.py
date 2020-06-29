from flask import Flask , render_template, url_for, request, redirect

from flask_assets import Environment, Bundle
from datetime import datetime
from routes import *





app = Flask(__name__ )
assests = Environment(app)

js = Bundle('main.js', 'https://cdn.plot.ly/plotly-1.2.0.min.js' , ' jquery-2.1.4.js', filters='jsmin', output='gen/packed.js' )
assests.register('js_all', js)

app.register_blueprint(routes)

 




   


@app.route('/' , methods = ['POST', 'GET'])
def index():
    covid_data = search.get_json_all_data()

        
    return render_template('index.html', a = covid_data)

# @app.route('/delete/<int:id>'  , methods = ['POST', 'GET'])
# def delete(id):



# @app.route('/update/<int:id>', methods =['GET', 'POST'])
# def update(id):
    
    





if __name__ ==  "__main__":
    
    app.run(debug=True)