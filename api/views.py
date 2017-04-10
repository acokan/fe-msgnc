from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from serializers import *
from models import *
from rest_framework import permissions
from rest_framework.decorators import api_view, permission_classes


@permission_classes((permissions.AllowAny,))
class ProjectList(APIView):

    def return_members(self):
        instance = TeamMember.objects.all()
        projects_list = []
        members_list = []
        final_list = []
        for i in instance:
            if i.project not in projects_list:
                projects_list.append(i.project)
        for p in projects_list:
            for i in instance:
                if p.name == i.project.name:
                    member = {
                        "role": i.role,
                        "name": i.name,
                        "id": i.id
                    }
                    members_list.append(member)
            final_obj = {
                "team_members": members_list,
                "name": p.name,
                "id": p.id
            }
            members_list = []
            final_list.append(final_obj)

        return ProjectSerializer(final_list)


    def get(self, request):
        serializer = self.return_members()
        return Response(serializer.data)


    def post(self, request):
        pid = request.data.get('project_id')
        mid = request.data.get('member_id')
        try:
            member = TeamMember.objects.get(id=mid)
            project = Project.objects.get(id=pid)
            member.project = project
            member.save()
            serializer = self.return_members()
            return Response(serializer.data)
        except:
            error = {"error": "Projekat ili clan tima ne postoje!"}
            return Response(error, status=status.HTTP_400_BAD_REQUEST)
