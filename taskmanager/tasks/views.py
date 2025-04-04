from rest_framework import generics, status
from rest_framework.response import Response
from .models import Task
from .serializers import TaskSerializer, TaskCreateSerializer, TaskAssignSerializer
from users.models import User

class TaskCreateView(generics.CreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskCreateSerializer
    
    def perform_create(self, serializer):
        serializer.save()

class TaskAssignView(generics.UpdateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskAssignSerializer
    
    def update(self, request, *args, **kwargs):
        task = self.get_object()
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        users = serializer.validated_data['user_ids']
        task.assigned_users.add(*users)
        return Response({'status': 'users assigned'}, status=status.HTTP_200_OK)

class UserTasksView(generics.ListAPIView):
    serializer_class = TaskSerializer
    
    def get_queryset(self):
        user_id = self.kwargs['user_id']
        return Task.objects.filter(assigned_users__id=user_id)