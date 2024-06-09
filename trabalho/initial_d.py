from app import app
from models import db, User, Sensor, Actuator, Kit

with app.app_context():
    # Recriar todas as tabelas
    db.drop_all()
    db.create_all()

    # Adicionar usuários
    admin = User(username='admin', role='Admin')
    admin.set_password('admin')

    estatistico = User(username='estatistico', role='Estatístico')
    estatistico.set_password('estatistico') 

    operador = User(username='operador', role='Operador')
    operador.set_password('operador')  
    db.session.add(admin)
    db.session.add(estatistico)
    db.session.add(operador)
    db.session.commit()

    # Adicionar kits
    kit1 = Kit(name='Kit 1')
    kit2 = Kit(name='Kit 2')
    db.session.add(kit1)
    db.session.add(kit2)
    db.session.commit()

    # Adicionar sensores e associá-los aos kits
    sensor1 = Sensor(name='Humidity', image='sensor1.png', value=25.0, kit_id=kit1.id)
    sensor2 = Sensor(name='Pressure', image='sensor2.png', value=30.0, kit_id=kit2.id)
    db.session.add(sensor1)
    db.session.add(sensor2)
    db.session.commit()

    # Adicionar atuadores e associá-los aos kits
    actuator1 = Actuator(name='Led', image='actuator1.png', state='Off', kit_id=kit1.id)
    actuator2 = Actuator(name='Valve', image='actuator2.png', state='Off', kit_id=kit2.id)
    db.session.add(actuator1)
    db.session.add(actuator2)
    db.session.commit()
