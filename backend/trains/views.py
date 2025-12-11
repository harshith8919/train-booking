from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Train
from .serializers import TrainSerializer
from django.db import transaction

@api_view(['GET'])
def train_list(request):
    trains = Train.objects.all()
    serializer = TrainSerializer(trains, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def book_seat(request, pk):
    seats = int(request.data.get('seats', 0))
    if seats <= 0:
        return Response({'error':'seats must be > 0'}, status=status.HTTP_400_BAD_REQUEST)
    try:
        with transaction.atomic():
            train = Train.objects.select_for_update().get(pk=pk)
            if train.available_seats >= seats:
                train.available_seats -= seats
                train.save()
                total = float(train.fare) * seats
                gst = round(total * 0.18, 2)
                total_with_gst = round(total + gst, 2)
                return Response({
                    'message': f'{seats} seats booked',
                    'train': TrainSerializer(train).data,
                    'total': total,
                    'gst': gst,
                    'total_with_gst': total_with_gst
                })
            else:
                return Response({'error': 'Not enough seats available', 'available_seats': train.available_seats}, status=status.HTTP_400_BAD_REQUEST)
    except Train.DoesNotExist:
        return Response({'error':'Train not found'}, status=status.HTTP_404_NOT_FOUND)
