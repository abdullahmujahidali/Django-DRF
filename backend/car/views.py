from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import AllowAny


@api_view(['GET'])
# @permission_classes([AllowAny])
def hello_world(request):
    print("rest_query: ", request.query_params)
    print("id: ", request.query_params['id'])
    print("search: ", request.query_params['search'])
    return Response({"message": "Hello, world!"})
