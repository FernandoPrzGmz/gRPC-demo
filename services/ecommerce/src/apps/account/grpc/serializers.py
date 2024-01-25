from django.contrib.auth import get_user_model
from django_grpc_framework import proto_serializers

from src.apps.account.grpc.protobuff import user_pb2


User = get_user_model()


class UserProtoSerializer(proto_serializers.ModelProtoSerializer):
    class Meta:
        model = User
        proto_class = user_pb2.User
        fields = ['id', 'username', 'first_name', 'last_name']
