from app import app
from models import db, User, Sensor, Actuator

with app.app_context():
    users = User.query.all()
    sensors = Sensor.query.all()
    actuators = Actuator.query.all()

    print("Users:")
    for user in users:
        print(user.id, user.username, user.role)

    print("\nSensors:")
    for sensor in sensors:
        print(sensor.id, sensor.name, sensor.value, sensor.image)

    print("\nActuators:")
    for actuator in actuators:
        print(actuator.id, actuator.name, actuator.state, actuator.image)
