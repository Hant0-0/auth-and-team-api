from django.contrib.auth import logout
from django.shortcuts import get_object_or_404, render
from rest_framework import status
from rest_framework.response import Response
from rest_framework import mixins
from rest_framework.views import APIView

from api_service.models import People, Team
from api_service.serializers import PeopleSerializer, TeamSerializer

"""API для людей """


class PeoplesAPI(APIView):
    queryset = People.objects.all()
    serializer_class = PeopleSerializer

    def get(self, request):
        people = People.objects.all()
        serializer = PeopleSerializer(people, many=True).data
        return Response(serializer)

    def post(self, request):
        serializer = PeopleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'detail': 'Користувач створений'})


class PeopleAPI(APIView):
    queryset = People.objects.all()
    serializer_class = PeopleSerializer

    def get(self, request, user_id):
        people = People.objects.get(id=user_id)
        serializer = PeopleSerializer(people).data
        return Response(serializer)

    def put(self, request, user_id):
        people = get_object_or_404(People, id=user_id)
        serializer = PeopleSerializer(people, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'detail': 'Дані змінені'})
        else:
            return Response({'detail': 'Виникла помилка'}, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, user_id):
        people = get_object_or_404(People, id=user_id)
        people.delete()
        return Response({'detail': 'Дані видалені'})


"""API для команд """


class TeamsAPI(APIView):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer

    def get(self, request):
        teams = Team.objects.all()
        serializer = TeamSerializer(teams, many=True).data
        return Response(serializer)

    def post(self, request):
        serializer = TeamSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"detail": "Дані зебержені"})


class TeamAPI(APIView):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer

    def get(self, request, team_id):
        team = get_object_or_404(Team, id=team_id)
        serializer = TeamSerializer(team).data
        return Response(serializer)

    def put(self, request, team_id):
        team = get_object_or_404(Team, id=team_id)
        serializer = TeamSerializer(team, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'detail': 'Дані успішно змінені'})
        return Response({'detail': 'Виникла помилка'}, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, team_id):
        team = get_object_or_404(Team, id=team_id)
        team.delete()
        return Response({'detail': 'Запис видалиний'})


""" GOOGLE REGISTER """


def home(request):
    return render(request, "index.html")


def logout_view(request):
    logout(request)
    return render(request, "index.html")
