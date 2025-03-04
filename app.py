from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///G:/Program Files/Flask/todo.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    decs = db.Column(db.String(200), nullable=False)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)

    
    
    def __repr__(self) -> str:
        return f"{self.sno} - {self.title}"
    
@app.route('/', methods=['GET', 'POST'])
def hello_world():
    if request.method=='POST':
        title = request.form['title']
        desc = request.form['desc']
        todo = Todo (title=title, decs=desc)
        db.session.add(todo)
        db.session.commit()
        
    allTodo = Todo.query.all()
    return render_template('index.html', allTodo = allTodo)

@app.route('/show')
def products():
    allTodo = Todo.query.all()
    print(allTodo)
    return'this is products page'  

@app.route('/update/<int:sno>')
def update(sno):
    todo = Todo.query.filter_by(sno=sno).first()
    return render_template('update.html', todo = todo)

app.route('/delete/<int:sno>')
def delete(sno):
    todo = Todo.query.filter_by(sno=sno).first()
    db.session.delete(todo)
    db.session.commit()
    return redirect("/")
 

if __name__ == "__main__":
    app.run(debug=True, port=8000)   