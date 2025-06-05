from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///checklists.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Checklist(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    items = db.relationship('Item', backref='checklist', lazy=True, cascade='all, delete-orphan')

class Item(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(200), nullable=False)
    done = db.Column(db.Boolean, default=False)
    checklist_id = db.Column(db.Integer, db.ForeignKey('checklist.id'), nullable=False)


with app.app_context():
    db.create_all()

@app.route('/')
def index():
    lists = Checklist.query.all()
    return render_template('index.html', lists=lists)

@app.route('/new', methods=['GET', 'POST'])
def new_checklist():
    if request.method == 'POST':
        name = request.form['name']
        raw_items = request.form.getlist('items')
        checklist = Checklist(name=name)
        for text in raw_items:
            if text.strip():
                checklist.items.append(Item(text=text.strip()))
        db.session.add(checklist)
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('new.html')

@app.route('/list/<int:list_id>', methods=['GET', 'POST'])
def view_list(list_id):
    checklist = Checklist.query.get_or_404(list_id)
    if request.method == 'POST':
        for item in checklist.items:
            item.done = (str(item.id) in request.form)
        db.session.commit()
        return redirect(url_for('view_list', list_id=list_id))
    return render_template('view.html', checklist=checklist)

@app.route('/delete/<int:list_id>', methods=['POST'])
def delete_list(list_id):
    checklist = Checklist.query.get_or_404(list_id)
    db.session.delete(checklist)
    db.session.commit()
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
