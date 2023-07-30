from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAdminUser, IsAuthenticated
from .models import TrainingClass, Staff, Room, Price
from .serializers import (
    TrainingClassSerializer, StaffSerializer, RoomSerializer, PriceSerializer, CustomTokenVerifySerializer
)
from .filters import TrainingClassFilter
from .serializers import UserSerializer
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from django.shortcuts import render



def index(request):
    return render(request, 'index.html')

class TrainingClassListCreateView(generics.ListCreateAPIView):
    queryset = TrainingClass.objects.all().order_by('-date_joined')
    serializer_class = TrainingClassSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    filterset_class = TrainingClassFilter

    def get_queryset(self):
        queryset = TrainingClass.objects.all().order_by('-date_joined')

        sort_by = self.request.query_params.get('sort', None)

        if sort_by == 'trainer':
            queryset = queryset.order_by('trainer__first_name')
        elif sort_by == 'room':
            queryset = queryset.order_by('room__name')  
        elif sort_by == 'service':
            queryset = queryset.order_by('service__name')  

        return queryset

    def perform_create(self, serializer):
        data = self.request.data
    
        serializer.save(
            date=data.get('date'),
            end_datetime=data.get('end_datetime'),
            room= Room.objects.get(pk=data.get('room')),
            service= Price.objects.get(pk=data.get('service')),
            start_datetime=data.get('start_datetime'),
            trainer= Staff.objects.get(pk=data.get('trainer')),
        )


class TrainingClassRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = TrainingClass.objects.all()
    serializer_class = TrainingClassSerializer
    permission_classes = [IsAdminUser]

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        data = request.data

        instance.date = data.get('date', instance.date)
        instance.end_datetime = data.get('end_datetime', instance.end_datetime)
        instance.room = Room.objects.get(pk=data.get('room', instance.room.pk))
        instance.service = Price.objects.get(pk=data.get('service', instance.service.pk))
        instance.start_datetime = data.get('start_datetime', instance.start_datetime)
        instance.trainer = Staff.objects.get(pk=data.get('trainer', instance.trainer.pk))
        instance.save()

        serializer = self.get_serializer(instance)
        return Response(serializer.data)


class StaffListCreateView(generics.ListCreateAPIView):
    queryset = Staff.objects.all().order_by('-date_joined')
    serializer_class = StaffSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


class StaffRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Staff.objects.all()
    serializer_class = StaffSerializer
    permission_classes = [IsAdminUser]


class RoomListCreateView(generics.ListCreateAPIView):
    queryset = Room.objects.all().order_by('-date_joined')
    serializer_class = RoomSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


class RoomRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer
    permission_classes = [IsAdminUser]


class PriceListCreateView(generics.ListCreateAPIView):
    queryset = Price.objects.all().order_by('-date_joined')
    serializer_class = PriceSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


class PriceRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Price.objects.all()
    serializer_class = PriceSerializer
    permission_classes = [IsAdminUser]


class MyTokenObtainPairView(TokenObtainPairView):
    pass

class MyTokenRefreshView(TokenRefreshView):
    pass

class VerifyView(APIView):
    serializer_class = CustomTokenVerifySerializer
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        user = request.user
        userSerializer = UserSerializer(instance=user).data
        return Response(userSerializer, status=status.HTTP_200_OK)

