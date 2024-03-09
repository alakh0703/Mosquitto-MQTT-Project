import random
import time
import json

start_id = 111

def create_data():
    global start_id
    data = {
        'id': start_id,
        'patient': 'John Doe',
        'time': time.asctime(),
        'heart_rate': int(random.gauss(80, 1)),
        'respiratory_rate': int(random.gauss(12,2)),
        'heart_rate_variability': 65,
        'body_temperature': random.gauss(99, 0.5),
        'blood_pressure': {
            'systolic': int(random.gauss(105,2)),
            'diastolic': int(random.gauss(70,1))
        },
        'activity': 'Walking'
    }
    start_id += 1
    return data

def print_data2(data):
    print('Patient:', data['patient'])
    print('Time:', data['time'])
    print('Heart rate:', data['heart_rate'])
    print('Respiratory rate:', data['respiratory_rate'])
    print('Heart rate variability:', data['heart_rate_variability'])
    print('Body temperature:', data['body_temperature'])
    print('Blood pressure (systolic):', data['blood_pressure']['systolic'])
    print('Blood pressure (diastolic):', data['blood_pressure']['diastolic'])
    print('Activity:', data['activity'])