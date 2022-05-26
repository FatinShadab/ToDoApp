from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import mixins, generics, authentication, permissions

from .serializers import UserSerializer

from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password


class CreateUserView(
                        mixins.CreateModelMixin, 
                        generics.GenericAPIView
                    ):
    
    permission_classes = [permissions.AllowAny]
    serializer_class = UserSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.validated_data['password']=make_password(serializer.validated_data.get('password'))
        user = serializer.save()
        return Response({
            "user": UserSerializer(user, context=self.get_serializer_context()).data,

        })


class UpdateUserView(
                        mixins.CreateModelMixin, 
                        generics.GenericAPIView
                    ):

    permission_classes = [permissions.IsAuthenticated]
    serializer_class = UserSerializer

    def put(self, request, *args, **kwargs):
        serializer = self.get_serializer(request.user, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)


class DeleteUserView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def delete(self, request, *args, **kwargs):
        user = self.request.user
        user.delete()

        return Response({"result":"user delete"})