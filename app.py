from flask import Flask, request, jsonify, make_response
from flask_sqlalchemy import SQLAlchemy
from marshmallow import fields
from marshmallow_sqlalchemy import ModelSchema

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:@localhost:3306/info_mata_kuliah'
db = SQLAlchemy(app)


# Model
class MataKuliah(db.Model):
    __tablename__ = "mk_2014_2016"
    kode = db.Column(db.String(7), primary_key=True)
    nama_mk = db.Column(db.String(50))
    sks = db.Column(db.Integer)

    def create(self):
        db.session.add(self)
        db.session.commit()
        return self


class TodoSchema(ModelSchema):
    class Meta(ModelSchema.Meta):
        model = MataKuliah
        sqla_session = db.session

    kode = fields.String(dump_only=True)
    nama_mk = fields.String(required=True)
    sks = fields.Number(required=True)


@app.route('/matkul', methods=['GET'])
def index():
    get_todos = MataKuliah.query.all()
    todo_schema = TodoSchema(many=True)
    todos = todo_schema.dump(get_todos)
    return make_response(jsonify({"todos": todos}))

if __name__ == "__main__":
    app.run(debug=True)