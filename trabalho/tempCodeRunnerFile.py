topic_diff = "leakspy/diff_water"

def on_connect(client, userdata, flags, rc):
    print("Connected with result code " + str(rc))
    client.subscribe([(topic_sensor1, 0), (topic_sensor2, 0), (topic_actuators, 0), (topic_diff, 0) ])
    print(f"Subscribed to topics: {topic_sensor1}, {topic_sensor2}, {topic_actuators}, {topic_diff}")

def on_message(client, userdata, msg):
    with app.app_context():
        print(f"Received message on topic {msg.topic}: {msg.payload.decode()}")
        payload = json.loads(msg.payload.decode())
        if msg.topic == topic_sensor1:
            sensor = Sensor.query.filter_by(name='Humidity').first()
            if sensor:
                print(f"Updating sensor {sensor.name} with value {payload['value']}")
                sensor.value = payload['value']
                db.session.add(SensorData(sensor_id=sensor.id, value=payload['value'], timestamp=datetime.now()))
                db.session.commit()
                print(f"Sensor {sensor.name} updated with value {sensor.value}")
            else:
                print("Sensor 'Humidity' not found")
        elif msg.topic == topic_sensor2:
            sensor = Sensor.query.filter_by(name='Pressure').first()
            if sensor:
                print(f"Updating sensor {sensor.name} with value {payload['value']}")
                sensor.value = payload['value']
                db.session.add(SensorData(sensor_id=sensor.id, value=payload['value'], timestamp=datetime.now()))
                db.session.commit()
                print(f"Sensor {sensor.name} updated with value {sensor.value}")
            else:
                print("Sensor 'Pressure' not found")
        elif msg.topic == topic_actuators:
            actuator = Actuator.query.filter_by(name=payload['actuator']).first()
            if actuator:
                print(f"Updating actuator {actuator.name} with state {payload['state']}")
                actuator.state = payload['state']
                db.session.commit()
                print(f"Actuator {actuator.name} updated with state {actuator.state}")
            else:
                print(f"Actuator {payload['actuator']} not found")
        elif msg.topic == topic_diff:
            sensor = Sensor.query.filter_by(name='PotentiometerDifference').first()
            if sensor:
                print(f"Updating sensor {sensor.name} with value {payload['difference']}")
                sensor.value = payload['difference']
                db.session.add(SensorData(sensor_id=sensor.id, value=payload['difference'], timestamp=datetime.now()))
                db.session.commit()
                print(f"Sensor {sensor.name} updated with value {sensor.value}")
            else:
                print("Sensor 'PotentiometerDifference' not found")