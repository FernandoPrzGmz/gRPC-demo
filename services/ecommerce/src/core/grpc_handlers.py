# gRPC Controllers
from src.apps.account.grpc.protobuff import user_pb2_grpc
# gRPC Services
from src.apps.account.grpc.services import UserService 


def grpc_handlers(server):
    user_pb2_grpc.add_UserControllerServicer_to_server(UserService.as_servicer(), server)
