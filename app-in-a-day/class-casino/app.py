from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
import os

app = Flask(__name__)

basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'app.sqlite')
db = SQLAlchemy(app)
ma = Marshmallow(app)


class Player(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(100), unique=False)
  hand = db.Column(db.String(144), unique=False)
  bet = db.Column(db.String(144), unique=False)
  chips = db.Column(db.String(144), unique=False)

  def __init__(self, name, hand, bet, chips):
    self.name = name
    self.hand = hand
    self.bet = bet
    self.chips = chips


class PlayerSchema(ma.Schema):
  class Meta:
    fields = ('name', 'hand', 'bet', 'chips')


player_schema = PlayerSchema()
players_schema = PlayerSchema(many=True)


@app.route("/player", methods=["POST"])
def add_player():
  name = request.json['name']
  hand = request.json['hand']
  bet = request.json['bet']
  chips = request.json['chips']

  new_player = Player(name, hand, bet, chips)

  db.session.add(new_player)
  db.session.commit()

  player = Player.query.get(new_player.id)

  return player_schema.jsonify(player)


@app.route("/player", methods=["GET"])
def get_player():
    all_players = Player.query.all()
    result = player_schema.dump(all_players)

    return jsonify(result)



if __name__ == '__main__':
    app.run(debug=True)

