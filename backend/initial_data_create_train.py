# Run this after migrations to create a sample train
from trains.models import Train
if not Train.objects.exists():
    Train.objects.create(name='Puducherry Express', fare=150.00, total_seats=100, available_seats=100)
    print('Sample train created.')
else:
    print('Trains already exist.')
