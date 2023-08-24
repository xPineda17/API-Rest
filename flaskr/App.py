from flaskr import create_app
from .Modelos import db, Cancion
from .Modelos import db, Usuario

app = create_app('default')
app_context = app.app_context()
app_context.push()

db.init_app(app)
db.create_all()

with app.app_context():
    c = Cancion(titulo='prueba', minutos=2, segundos=25, interprete='Juanito')
    db.session.add(c)
    db.session.commit()
    print(Cancion.query.all())
