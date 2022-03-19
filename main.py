from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__, template_folder='templates')
app.config['SECRET_KEY'] = 'helloitstrackerbasedatabase'

"""
    sqlalchemy .db location (for sqlite)
"""
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
SQLALCHEMY_TRACK_MODIFICATIONS = True
db = SQLAlchemy(app)

"""
    Two classes has been creater one is used to store the number of Tracker and the other class that
    is visitor to store values against tracker
"""



class Tracker(db.Model):
    __tablename__ = 'tracker'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=False)

    def __init__(self, name):
        self.name = name

class Visitor(db.Model):
    __tablename__ = 'visitors'
    id = db.Column(db.Integer, primary_key=True)
    visitors = db.Column(db.String(300))
    sales = db.Column(db.String(300))
    tracker_id = db.Column(db.Integer, db.ForeignKey('tracker.id', ondelete="CASCADE"), nullable=False)

    def __init__(self, visitors, sales, tracker_id):
        self.visitors = visitors
        self.sales = sales
        self.tracker_id = tracker_id


db.create_all()
db.session.commit()

track = 'Tracker 1'
entry = Tracker(name=track)
db.session.add(entry)
db.session.commit()

track = 'Tracker 2'
entry = Tracker(name=track)
db.session.add(entry)
db.session.commit()

track = 'Tracker 3'
entry = Tracker(name=track)
db.session.add(entry)
db.session.commit()

track = 'Tracker 4'
entry = Tracker(name=track)
db.session.add(entry)
db.session.commit()

track = 'Tracker 5'
entry = Tracker(name=track)
db.session.add(entry)
db.session.commit()

track = 'Tracker 6'
entry = Tracker(name=track)
db.session.add(entry)
db.session.commit()

track = 'Tracker 7'
entry = Tracker(name=track)
db.session.add(entry)
db.session.commit()

track = 'Tracker 8'
entry = Tracker(name=track)
db.session.add(entry)
db.session.commit()

track = 'Tracker 9'
entry = Tracker(name=track)
db.session.add(entry)
db.session.commit()

track = 'Tracker 10'
entry = Tracker(name=track)
db.session.add(entry)
db.session.commit()

visitor = 50000
sale = 100000
trac_id = 1
entry = Visitor(visitors=visitor, sales=sale, tracker_id=trac_id)
db.session.add(entry)
db.session.commit()

visitor = 67000
sale = 500000
trac_id = 2
entry = Visitor(visitors=visitor, sales=sale, tracker_id=trac_id)
db.session.add(entry)
db.session.commit()

visitor = 697000
sale = 170000
trac_id = 3
entry = Visitor(visitors=visitor, sales=sale, tracker_id=trac_id)
db.session.add(entry)
db.session.commit()

visitor = 6567000
sale = 2000
trac_id = 4
entry = Visitor(visitors=visitor, sales=sale, tracker_id=trac_id)
db.session.add(entry)
db.session.commit()

labels = [
    'Number of Visitor', 'Sales'
]

values = [
    967, 1190.89
]

colors = [
    "#F7464A", "#46BFBD"]


@app.route('/', methods=['POST', 'GET'])
def index():
    tracker = Tracker.query.all()

    trackeroptions = request.form.get('trackeroptions')

    try:
        visitor = Visitor.query.filter_by(tracker_id=trackeroptions).first()
        values[0] = visitor.visitors
        values[1] = visitor.sales
    except:
        pass

    return render_template('index.html', title='Number of Visitors and Sales', max=17000,
                           set=zip(values, labels, colors), tracker=tracker)


@app.route('/about')
def about():
    visitor = Visitor.query.all()

    return render_template('about.html', title='Number of Visitors and Sales', max=17000,
                           set=zip(values, labels, colors), visitor=visitor, item=values, label=labels, colors=colors)


@app.route('/post')
def post():
    return render_template('post.html')


@app.route('/contact')
def contact():
    return render_template('contact.html')


@app.route('/addtracker', methods=['POST', 'GET'])
def addtracker():
    if request.method == 'POST':
        tracker = request.form.get('tracker')
        print(tracker)
        entry = Tracker(name=tracker)
        db.session.add(entry)
        db.session.commit()
        return redirect('/')
    return render_template('addtracker.html')


if __name__ == '__main__':
    app.run(debug=True)
