from django.urls import path
from .views import (
    TrainingClassListCreateView, TrainingClassRetrieveUpdateDestroyView,
    StaffListCreateView, StaffRetrieveUpdateDestroyView,
    RoomListCreateView, RoomRetrieveUpdateDestroyView,
    PriceListCreateView, PriceRetrieveUpdateDestroyView,
  MyTokenObtainPairView, MyTokenRefreshView, VerifyView
)


urlpatterns = [
    path('login/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('refresh/', MyTokenRefreshView.as_view(), name='token_refresh'),
    path('verify/', VerifyView.as_view(), name='token_verify'),
    path('training-classes/', TrainingClassListCreateView.as_view(),
         name='training-class-list-create'),
    path('training-classes/<int:pk>/', TrainingClassRetrieveUpdateDestroyView.as_view(),
         name='training-class-retrieve-update-destroy'),

    path('staff/', StaffListCreateView.as_view(), name='staff-list-create'),
    path('staff/<int:pk>/', StaffRetrieveUpdateDestroyView.as_view(),
         name='staff-retrieve-update-destroy'),

    path('rooms/', RoomListCreateView.as_view(), name='room-list-create'),
    path('rooms/<int:pk>/', RoomRetrieveUpdateDestroyView.as_view(),
         name='room-retrieve-update-destroy'),

    path('prices/', PriceListCreateView.as_view(), name='price-list-create'),
    path('prices/<int:pk>/', PriceRetrieveUpdateDestroyView.as_view(),
         name='price-retrieve-update-destroy'),
]
