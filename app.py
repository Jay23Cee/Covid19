from flask import Flask , render_template, url_for, request, redirect
from flask_sqlalchemy import SQLAlchemy
from flask_assets import Environment, Bundle
from datetime import datetime
from routes import *





app = Flask(__name__ )
assests = Environment(app)

js = Bundle('main.js', 'https://cdn.plot.ly/plotly-1.2.0.min.js' , ' jquery-2.1.4.js', filters='jsmin', output='gen/packed.js' )
assests.register('js_all', js)

app.register_blueprint(routes)

 

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
#app.static_folder= 'static'

db=  SQLAlchemy(app)


class Todo(db.Model) :

   

    id = db.Column(db.Integer, primary_key = True)
    content = db.Column(db.String(200), nullable= False)
    date_created = db.Column(db.DateTime, default = datetime.utcnow)
    print(date_created)
    def __repr__(self):
        return '<Task %r>' % self.id

@app.route('/' , methods = ['POST', 'GET'])
def index():
    Table_json = search.get_json_all_data()

    search.get_json_all_data()
    if request.method =='POST':
        task_content = request.form['content']
        new_task = Todo(content = task_content)

        # try:
            
        #     return redirect('/')
        # except:
            

    else:
        tasks = Todo.query.order_by(Todo.date_created).all()
        
      #  return render_template('index.html', tasks=tasks)
        
        return render_template('index.html', a = Table_json)

# @app.route('/delete/<int:id>'  , methods = ['POST', 'GET'])
# def delete(id):



# @app.route('/update/<int:id>', methods =['GET', 'POST'])
# def update(id):
    
    





if __name__ ==  "__main__":
    app.run(debug=True)