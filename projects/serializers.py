from rest_framework import serializers
from .models import Project, ProjectImage


class ProjectImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjectImage
        fields = ['id', 'image', 'alt_text', 'order']


class ProjectSerializer(serializers.ModelSerializer):
    gallery = ProjectImageSerializer(many=True, read_only=True)

    class Meta:
        model = Project
        fields = [
            'id', 'title', 'description', 'long_description', 'tech',
            'category', 'status', 'image', 'source_url', 'demo_url',
            'client', 'project_type', 'start_date', 'end_date',
            'features', 'apis_used', 'difficulty', 'created_at',
            'updated_at', 'gallery'
        ]