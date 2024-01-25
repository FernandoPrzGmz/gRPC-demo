## Install requirements

```bash
pip install djangogrpcframework
pip install grpcio
pip install grpcio-tools
# 
pip install djangorestframework
```

## Project setup

Add django_grpc_framework to `INSTALLED_APPS``, settings module is in "src/core/settings.py":
```py
INSTALLED_APPS = [
    ...
    'django_grpc_framework',
]
```

## Defining protos

Our first step is to define the gRPC service and messages, generate protos automatically based on User model
```bash

export APP_NAME=account
python manage.py generateproto \
    --model src.apps.account.models.User \
    --fields id,username,first_name,last_name \
    --file "src/apps/$APP_NAME/grpc/.proto/user.proto"

```

Previus command will generate the next files
```ts
syntax = "proto3";

package user;

import "google/protobuf/empty.proto";

service UserController {
    rpc List(UserListRequest) returns (stream User) {}
    rpc Create(User) returns (User) {}
    rpc Retrieve(UserRetrieveRequest) returns (User) {}
    rpc Update(User) returns (User) {}
    rpc Destroy(User) returns (google.protobuf.Empty) {}
}

message User {
    int64 id = 1;
    string username = 2;
    string first_name = 3;
    string last_name = 4;
}

message UserListRequest {
}

message UserRetrieveRequest {
    int64 id = 1;
}
```


Next we need to generate gRPC code, from the ecommerce directory, run:

```bash
export APP_NAME=account

python -m grpc_tools.protoc \
    --proto_path="src/apps/$APP_NAME/grpc/.proto" \
    --python_out="src/apps/$APP_NAME/grpc/protobuff"\
    --grpc_python_out="src/apps/$APP_NAME/grpc/protobuff"\
    "user.proto"
```


> El anterior comando crea los archivos `user_pb2.py` y `user_pb2_grpc.py`. El archivo hace un import a user_pb2, sin embargo para nuestro proyecto hay que modificar el import para solucionar el error de importacion
>
>    ```py
>    # import user_pb2 as user__pb2
>    import src.apps.account.grpc.protobuff.user_pb2 as user__pb2
>    ```


## Writing serializers

We have to define a serializar
```py
from django.contrib.auth import get_user_model
from django_grpc_framework import proto_serializers

from src.apps.account.grpc.protobuff import user_pb2


User = get_user_model()


class UserProtoSerializer(proto_serializers.ModelProtoSerializer):
    class Meta:
        model = User
        proto_class = user_pb2.User
        fields = ['id', 'username', 'first_name', 'last_name']

```


## Register handlers

Edit `src/core/urls.py` to register gRPC handlers. 
```py
import account_pb2_grpc
from account.services import UserService


urlpatterns = []


def grpc_handlers(server):
    account_pb2_grpc.add_UserControllerServicer_to_server(UserService.as_servicer(), server)

```


##  Fire up the server with development mode:
```bash
python manage.py grpcrunserver --dev
```