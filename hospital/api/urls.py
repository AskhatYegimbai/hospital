from django.contrib import admin
from django.urls import path

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from .models import Patient
from .views import DoctorView, PatientView


urlpatterns = [
    path('doctor/',
    DoctorView.as_view({
        'get': 'list',
        'post': 'create'
    })),
    path('doctor/<int:id>',
    DoctorView.as_view({
        'get': 'retrieve',
        'put': 'update',
        'delete': 'destroy'
    })),
    path('patient/',
    PatientView.as_view({
        'get': 'list',
        'post': 'create'
    })),
    path('patient/<int:id>',
    PatientView.as_view({
        'get': 'retrieve',
        'put': 'update',
        'delete': 'destroy'
    })),


    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

]
