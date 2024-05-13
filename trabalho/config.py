users = {
    'admin': {'password': 'admin', 'is_admin': True},
    'user1': {'password': '1234', 'is_admin': False},
    'user2': {'password': '1234', 'is_admin': False}
}
sensor_data = {
    'sensor1': {'name': 'Sensor 1', 'image': 'sensor1.jpg', 'value': 25},
    'sensor2': {'name': 'Sensor 2', 'image': 'sensor2.jpg', 'value': 30}
}

sensor_history = {
    'sensor1': [
        {'timestamp': '08:00:00', 'value': 22},
        {'timestamp': '09:00:00', 'value': 23},
        {'timestamp': '10:00:00', 'value': 25}
    ],
    'sensor2': [
        {'timestamp': '08:30:00', 'value': 50},
        {'timestamp': '09:30:00', 'value': 52},
{'timestamp': '09:30:00', 'value': 52},
{'timestamp': '09:30:00', 'value': 52},
{'timestamp': '09:30:00', 'value': 52},
{'timestamp': '09:30:00', 'value': 52},
{'timestamp': '09:30:00', 'value': 52},
{'timestamp': '09:30:00', 'value': 52},
        {'timestamp': '10:30:00', 'value': 53}
    ]
}
actuator_data = {
    'Actuator 1': {'image': 'actuator1.jpg', 'state': 'On'},
    'Actuator 2': {'image': 'actuator2.jpg', 'state': 'Off'}
}
