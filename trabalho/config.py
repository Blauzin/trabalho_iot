users = {
    'admin': {'password': 'admin', 'is_admin': True},
    'user1': {'password': '1234', 'is_admin': False},
    'user2': {'password': '1234', 'is_admin': False}
}

sensor_data = {
    'sensor1': {'name': 'Humidity', 'image': 'sensor1.png', 'value': 25},
    'sensor2': {'name': 'Pressure', 'image': 'sensor2.png', 'value': 30}
}

sensor_history = {
    'sensor1': [
    ],
    'sensor2': [
    ]
}

actuator_data = {
    'Actuator 1': {'name': 'Led', 'image': 'actuator1.png', 'state': 'Off'},
    'Actuator 2': {'name': 'Valve' ,'image': 'actuator2.png', 'state': 'Off'}
}
