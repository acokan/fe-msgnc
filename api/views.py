from rest_framework.views import APIView
from rest_framework.response import Response
from serializers import *
from models import *
from rest_framework import permissions
from rest_framework.decorators import api_view, permission_classes


@permission_classes((permissions.AllowAny,))
class ProjectList(APIView):

    def get(self, request):
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
                        "name": i.name
                    }
                    members_list.append(member)
            final_obj = {
                "team_members": members_list,
                "name": p.name
            }
            members_list = []
            final_list.append(final_obj)

        serializer = ProjectSerializer(final_list)
        return Response(serializer.data)

    # def post(self, request):
    #     fid = request.data.get('firebase_id')
    #     pid = request.data.get('play_id')
    #     try:
    #         user = User.objects.get(firebase_id=fid)
    #         play = Play.objects.get(id=pid)
    #         try:
    #             fav = FavouriteEvents.objects.get(user=user, play=play)
    #             fav.delete()
    #         except FavouriteEvents.DoesNotExist:
    #             fav_event = FavouriteEvents(user=user, play=play)
    #             fav_event.save()
    #         serializer_data = get_fav_events(fid)
    #         return Response(serializer_data, status=status.HTTP_201_CREATED)
    #     except:
    #         error = {"error": "Korisnik ili projekcija ne postoji!"}
    #         return Response(error, status=status.HTTP_400_BAD_REQUEST)
