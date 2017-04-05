from django.http import HttpResponse
from rest_framework import generics
from models import *
from rest_framework import serializers


# class TeamMemberSerializer(serializers.ModelSerializer):
#
#     # project = ProjectSerializer()
#
#     class Meta:
#         model = TeamMember
#         fields = ('name', 'role', 'img')
#
#
# class ProjectSerializer(serializers.ModelSerializer):
#
#     members = TeamMemberSerializer()
#
#     class Meta:
#         model = Project
#         fields = ('name', 'members')


class ProjectSerializer(serializers.BaseSerializer):
    def create(self, validated_data):
        pass

    def to_representation(self, obj):
        proj = []

        # print obj
        return {
            "projects": obj
            # 'project': obj.project.name,
            # 'team_members': [{
            #     'name': obj.name,
            #     'role': obj.role
            # }]
        }
