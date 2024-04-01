from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import TableBooking
from .serializers import TableBookingSerializer

class TableBookingList(APIView):
    def get(self, request):
        bookings = TableBooking.objects.all()
        serializer = TableBookingSerializer(bookings, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = TableBookingSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class TableBookingDetail(APIView):
    def get_object(self, pk):
        try:
            return TableBooking.objects.get(pk=pk)
        except TableBooking.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        booking = self.get_object(pk)
        serializer = TableBookingSerializer(booking)
        return Response(serializer.data)

    def put(self, request, pk):
        booking = self.get_object(pk)
        serializer = TableBookingSerializer(booking, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        booking = self.get_object(pk)
        booking.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
