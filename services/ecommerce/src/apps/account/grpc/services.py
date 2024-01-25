from django.contrib.auth import get_user_model
from django_grpc_framework import generics

from src.apps.account.grpc.serializers import UserProtoSerializer


User = get_user_model()



class UserService(generics.ModelService):
    """
    gRPC service that allows users to be retrieved or updated.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserProtoSerializer