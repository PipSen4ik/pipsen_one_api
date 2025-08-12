from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from .models import Project
from .serializers import ProjectSerializer


@api_view(['GET'])
@permission_classes([AllowAny])
def get_projects(request):
    """
    Возвращает список всех проектов.
    """
    projects = Project.objects.all()
    serializer = ProjectSerializer(projects, many=True)
    return Response(serializer.data)


@api_view(['GET'])
@permission_classes([AllowAny])
def get_project(request, pk):
    project = get_object_or_404(Project, pk=pk)
    serializer = ProjectSerializer(project)
    return Response(serializer.data)