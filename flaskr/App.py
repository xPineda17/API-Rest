from flaskr import create_app
from .Modelos import db, Cancion, Album, Usuario, Medio,AlbumSchema
from flask_restful import Api
from .Vistas import VistaCanciones, VistaCancion, VistaUsuario, VistaUsuarios, VistaAlbum, VistaAlbumes

app = create_app('default')
app_context = app.app_context()
app_context.push()

db.init_app(app)
db.create_all()

api = Api(app)
api.add_resource(VistaCanciones, '/canciones')
api.add_resource(VistaCancion, '/canciones/<int:id_cancion>')

api.add_resource(VistaUsuarios, '/usuarios')
api.add_resource(VistaUsuario, '/usuarios/<int:id_usuario>')

api.add_resource(VistaAlbumes, '/albumes')
api.add_resource(VistaAlbum, '/albumes/<int:id_album>')

#with app.app_context():
    #Album_Schema = AlbumSchema()
    #A = Album(titulo='prueba', anio='1999', descripcion='texto', medio=Medio.cd)
    #db.session.add(A)
    #db.session.commit()
    #print([Album_Schema.dumps(album) for album in Album.query.all()])
