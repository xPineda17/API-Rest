from flaskr import create_app
from .Modelos import db, Cancion, Album, Usuario, Medio
from flask_restful import Api
from .Vistas import VistaCanciones, VistaCancion

app = create_app('default')
app_context = app.app_context()
app_context.push()

db.init_app(app)
db.create_all()

api = Api(app)
api.add_resource(VistaCanciones, '/canciones')
api.add_resource(VistaCancion, '/canciones/<int:id_cancion>')

#with app.app_context():
    #Album_Schema = AlbumSchema()
    #A = Album(titulo='test', anio='1999', descripcion='#', medio=Medio.cd)
    #db.session.add(A)
    #db.session.commit()
    #print([Album_Schema.dumps(album) for album in Album.query.all()])