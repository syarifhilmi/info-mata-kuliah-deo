from flask import Flask, request, jsonify, make_response
from flask_sqlalchemy import SQLAlchemy
from marshmallow import fields
from marshmallow_sqlalchemy import ModelSchema

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:@localhost:3306/info_mata_kuliah'
db = SQLAlchemy(app)

# Model
class MataKuliah14(db.Model):
    __tablename__ = "mk_2014"
    kode = db.Column(db.String(7), primary_key=True,)
    nama_mk = db.Column(db.String(50))
    sks = db.Column(db.Integer)

class Kurikulum14(db.Model):
    __tablename__ = "kurikulum_2014"
    id_prodi = db.Column(db.Integer, db.ForeignKey('prodi.id_prodi'),primary_key=True,)
    kode = db.Column(db.String(7),db.ForeignKey('mk_2014_2016.kode'),)
    semester = db.Column(db.Integer)

class MataKuliah16(db.Model):
    __tablename__ = "mk_2016"
    kode = db.Column(db.String(7), primary_key=True,)
    nama_mk = db.Column(db.String(50))
    sks = db.Column(db.Integer)

class Kurikulum16(db.Model):
    __tablename__ = "kurikulum_2016"
    id_prodi = db.Column(db.Integer, db.ForeignKey('prodi.id_prodi'),primary_key=True,)
    kode = db.Column(db.String(7),db.ForeignKey('mk_2014_2016.kode'),)
    semester = db.Column(db.Integer)

class MataKuliah19(db.Model):
    __tablename__ = "mk_2019"
    kode = db.Column(db.String(7), primary_key=True,)
    nama_mk = db.Column(db.String(50))
    sks = db.Column(db.Integer)

class Kurikulum19(db.Model):
    __tablename__ = "kurikulum_2019"
    id_prodi = db.Column(db.Integer, db.ForeignKey('prodi.id_prodi'),primary_key=True,)
    kode = db.Column(db.String(7),db.ForeignKey('mk_2014_2016.kode'),)
    semester = db.Column(db.Integer)


class Prodi(db.Model):
    __tablename__ = "prodi"
    id_prodi = db.Column(db.Integer, primary_key=True,)
    nama_prodi = db.Column(db.String(50))

class MataKuliahSchema(ModelSchema):
    class Meta(ModelSchema.Meta):
        fields = ('kode','nama_mk','sks','semester')

class ProdiSchema(ModelSchema):
    class Meta(ModelSchema.Meta):
        model = Prodi

class KurikulumSchema(ModelSchema):
    class Meta(ModelSchema.Meta):
        model = Kurikulum14

#Controller
class MataKuliahController :
    
    def getKurikulum14(prodi):
        data = MataKuliah14.query.join(Kurikulum14, MataKuliah14.kode == Kurikulum14.kode).\
                join(Prodi, Prodi.id_prodi == Kurikulum14.id_prodi).\
                filter(Prodi.id_prodi == prodi).\
                with_entities(MataKuliah14.kode,MataKuliah14.nama_mk,MataKuliah14.sks,Kurikulum14.semester).\
                order_by(Kurikulum14.semester).\
                all()
        matakuliah_schema = MataKuliahSchema(many=True)
        matakuliah = matakuliah_schema.dump(data)
        hasil = []
        temp_semester = 0
        i = 0
        for matkul in matakuliah :
            head = 'semester {0}'.format(matkul['semester'])
            i = matkul['semester'] - 1
            if matkul['semester'] != temp_semester :
                hasil.append({ head : [{'kode': matkul['kode'],
                'mata_kuliah':matkul['nama_mk'],'sks':matkul['sks']}]})
            else :
                hasil[i][head].append({'kode': matkul['kode'],
                'mata_kuliah':matkul['nama_mk'],'sks':matkul['sks']})
            
            temp_semester = matkul['semester']
            
        return make_response(jsonify(hasil))

    def getKurikulum16(prodi):
        data = MataKuliah16.query.join(Kurikulum16, MataKuliah16.kode == Kurikulum16.kode).\
                join(Prodi, Prodi.id_prodi == Kurikulum16.id_prodi).\
                filter(Prodi.id_prodi == prodi).\
                with_entities(MataKuliah16.kode,MataKuliah16.nama_mk,MataKuliah16.sks,Kurikulum16.semester).\
                order_by(Kurikulum16.semester).\
                all()
        matakuliah_schema = MataKuliahSchema(many=True)
        matakuliah = matakuliah_schema.dump(data)
        hasil = []
        temp_semester = 0
        i = 0
        for matkul in matakuliah :
            head = 'semester {0}'.format(matkul['semester'])
            i = matkul['semester'] - 1
            if matkul['semester'] != temp_semester :
                hasil.append({ head : [{'kode': matkul['kode'],
                'mata_kuliah':matkul['nama_mk'],'sks':matkul['sks']}]})
            else :
                hasil[i][head].append({'kode': matkul['kode'],
                'mata_kuliah':matkul['nama_mk'],'sks':matkul['sks']})
            
            temp_semester = matkul['semester']
            
        return make_response(jsonify(hasil))

    def getKurikulum19(prodi):
        data = MataKuliah19.query.join(Kurikulum19, MataKuliah19.kode == Kurikulum19.kode).\
                join(Prodi, Prodi.id_prodi == Kurikulum19.id_prodi).\
                filter(Prodi.id_prodi == prodi).\
                with_entities(MataKuliah19.kode,MataKuliah19.nama_mk,MataKuliah19.sks,Kurikulum19.semester).\
                order_by(Kurikulum19.semester).\
                all()
        matakuliah_schema = MataKuliahSchema(many=True)
        matakuliah = matakuliah_schema.dump(data)
        hasil = []
        temp_semester = 0
        i = 0
        for matkul in matakuliah :
            head = 'semester {0}'.format(matkul['semester'])
            i = matkul['semester'] - 1
            if matkul['semester'] != temp_semester :
                hasil.append({ head : [{'kode': matkul['kode'],
                'mata_kuliah':matkul['nama_mk'],'sks':matkul['sks']}]})
            else :
                hasil[i][head].append({'kode': matkul['kode'],
                'mata_kuliah':matkul['nama_mk'],'sks':matkul['sks']})
            
            temp_semester = matkul['semester']
            
        return make_response(jsonify(hasil))


class ProdiController :
    def getIdProdi(namaProdi):
        search = "%{}%".format(namaProdi)
        data = Prodi.query.filter(Prodi.nama_prodi.like(search)).with_entities(Prodi.id_prodi).first()
        prodi_schema = ProdiSchema(many=False)
        prodi = prodi_schema.dump(data)
        return prodi['id_prodi']
    
    def checkProdi(namaProdi):
        search = "%{}%".format(namaProdi)
        data = Prodi.query.filter(Prodi.nama_prodi.like(search)).first()
        prodi_schema = ProdiSchema(many=False)
        prodi = prodi_schema.dump(data)
        if prodi :
            return True
        else :
            return False

class KurikulumController :
    def check14(prodi):
        data = Kurikulum14.query.filter(Kurikulum14.id_prodi==prodi).first()
        prodi_schema = KurikulumSchema(many=False)
        prodi = prodi_schema.dump(data)
        if prodi :
            return True
        else :
            return False
    
    def check16(prodi):
        data = Kurikulum16.query.filter(Kurikulum16.id_prodi==prodi).first()
        prodi_schema = KurikulumSchema(many=False)
        prodi = prodi_schema.dump(data)
        if prodi :
            return True
        else :
            return False

    def check19(prodi):
        data = Kurikulum19.query.filter(Kurikulum19.id_prodi==prodi).first()
        prodi_schema = KurikulumSchema(many=False)
        prodi = prodi_schema.dump(data)
        if prodi :
            return True
        else :
            return False

#Route
@app.route('/info-mata-kuliah/<prodi>/<tahun>', methods=['GET'])
def index(prodi,tahun):
    checkProdi = ProdiController.checkProdi(prodi)
    if checkProdi == True :
        if tahun == '2019' :
            idProdi = ProdiController.getIdProdi(prodi)
            checkKurikulum = KurikulumController.check19(idProdi)
            if checkKurikulum == True :
                return MataKuliahController.getKurikulum19(idProdi)
            else :
                return make_response(jsonify({'message':'Tidak terdapat prodi {0} pada kurikulum {1}'.format(prodi,tahun)}))
        elif tahun == '2016'  :
            idProdi = ProdiController.getIdProdi(prodi)
            checkKurikulum = KurikulumController.check16(idProdi)
            if checkKurikulum == True :
                return MataKuliahController.getKurikulum16(idProdi)
            else :
                return make_response(jsonify({'message':'Tidak terdapat prodi {0} pada kurikulum {1}'.format(prodi,tahun)}))
        elif tahun == '2014' :
            idProdi = ProdiController.getIdProdi(prodi)
            checkKurikulum = KurikulumController.check14(idProdi)
            if checkKurikulum == True :
                return MataKuliahController.getKurikulum14(idProdi)
            else :
                return make_response(jsonify({'message':'Tidak terdapat prodi {0} pada kurikulum {1}'.format(prodi,tahun)}))
        else :
            return make_response(jsonify({'message':'Tidak terdapat tahun kurikulum {0}'.format(tahun)}))
    else :
        return make_response(jsonify({'message':'Tidak terdapat prodi {0}'.format(prodi)}))


if __name__ == "__main__":
    app.run(debug=True)