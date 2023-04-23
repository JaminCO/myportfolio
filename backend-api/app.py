from flask import Flask, render_template, request, jsonify
from flask_sqlalchemy import SQLAlchemy
import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///messages.db'
db = SQLAlchemy(app)

class Message(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    email = db.Column(db.String(50))
    message = db.Column(db.Text)
    date = db.Column(db.DateTime)

@app.route('/')
def home():
    return "THERE IS NOTHING TO SEE HERE, KEEP GOING"


@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        # data = request.get_json()
        # name = data['name']
        # email = data['email']
        # message = data['message']
        name = request.form['name']
        email = request.form['email']
        message = request.form['message']
        new_message = Message(name=name, email=email, message=message, date=datetime.datetime.utcnow())
        db.session.add(new_message)
        db.session.commit()
        return jsonify({"msg":"Message Done"})

@app.route('/messages')
def messages():
    messages = Message.query.order_by(Message.date.desc()).all()
    return render_template('messages.html', messages=messages)

@app.route('/<id>/messages/del', methods=['GET', 'POST'])
def messages_delete(id):
    message = Message.query.get(id)
    db.session.delete(message)
    db.session.commit()
    return f"MESSAGE OF ID -> {id} DELETED"

@app.route('/<id>/messages', methods=['GET', 'POST'])
def message_detail(id):
    message = Message.query.get(id)
    return render_template('message_detail.html', message=message)

if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)
