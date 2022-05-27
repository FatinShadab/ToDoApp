from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import mixins, generics, authentication, permissions

from .serializers import TodoSerializer

# Create your views here.

class CreateTodoEP(
                        mixins.CreateModelMixin,
                        generics.GenericAPIView
                    ):

    #authentication_classes = [authentication.SessionAuthentication, authentication.BasicAuthentication]
    #permission_classes = [permissions.IsAuthenticated]
    serializer_class = TodoSerializer

    def post(self, request, *args, **kwargs):

        updated_request = request.data.copy()
        updated_request.update({'user': request.user.pk})

        serializer = self.get_serializer(data=updated_request)
        serializer.is_valid(raise_exception=True)
        todo = serializer.save()

        return Response({
            "todo": TodoSerializer(todo, context=self.get_serializer_context()).data,
        })