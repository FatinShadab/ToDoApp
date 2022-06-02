from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import mixins, generics, authentication, permissions
from django.http import Http404
from todo.models import Todo
from .serializers import TodoSerializer


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


class GetAllTodoEP(generics.ListCreateAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer

    def get_queryset(self):
        todos = Todo.objects.all().filter(user=self.request.user.pk)
        return todos

    def list(self, request):
        # Note the use of `get_queryset()` instead of `self.queryset`
        queryset = self.get_queryset()
        serializer = TodoSerializer(queryset, many=True)
        return Response(serializer.data)


class GetOneTodoEP(generics.ListCreateAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer

    def get_queryset(self):
        try:
            todo = Todo.objects.get(user=self.request.user.pk, title=self.request.data['title'])
        except Todo.DoesNotExist:
            raise Http404("Given query not found....")
        return todo

    def list(self, request):
        # Note the use of `get_queryset()` instead of `self.queryset`
        queryset = self.get_queryset()
        serializer = TodoSerializer(queryset, many=False)
        return Response(serializer.data)


class DeleteTodoEP(APIView):

    #authentication_classes = [authentication.SessionAuthentication, authentication.BasicAuthentication]
    #permission_classes = [permissions.IsAuthenticated]

    def delete(self, request, *args, **kwargs):
        user = self.request.user

        try:
            todo = Todo.objects.get(user=user.pk, title=request.data['title'])
        except Todo.DoesNotExist:
            raise Http404("Given query not found....")

        todo.delete()
        return Response({"result":"todo deleted"})