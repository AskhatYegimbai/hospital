from django.contrib.auth.models import Permission
from rest_framework import viewsets, mixins
from rest_framework.permissions import IsAuthenticated

from ..filters import DoctorFilterSet
from ..mixin import HospitalGenericViewSet
from ..permissions import RoleBasedPermissionMixin, HasPermissionByAuthenticatedUserRole
from ..models import Doctor, Patient
from ..serializers.doctor import DoctorListSerializer, DoctorRetrieveSerializer, DoctorCreateSerializer, \
    DoctorUpdateSerializer
from django_filters.rest_framework import DjangoFilterBackend



class DoctorView(
    HospitalGenericViewSet,
    viewsets.GenericViewSet,
    mixins.ListModelMixin,
    mixins.UpdateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.CreateModelMixin,
    mixins.DestroyModelMixin
):

    lookup_field = 'id'

    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['first_name', 'last_name', 'specialization']
    filterset_class = DoctorFilterSet
    def get_action_permissions(self):
        if self.action in ('list', 'retrieve'):
            self.action_permissions = ['view_doctor',]
        elif self.action == 'list_patient':
            self.action_permissions = ['view_patient']

    def get_serializer_class(self):
        if self.action == 'list':
            return DoctorListSerializer
        if self.action == 'retrieve':
            return DoctorRetrieveSerializer
        if self.action == 'create':
            return DoctorCreateSerializer
        if self.action == 'update':
            return DoctorUpdateSerializer

    def get_queryset(self):
        if self.action == 'list_patient':
            return Patient.objects.all()

        return Doctor.objects.all()

