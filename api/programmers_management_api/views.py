from django.shortcuts import render
from rest_framework import generics
from rest_framework import viewsets
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Team, Programmer, Language, Paradigm
from .serializers import  TeamSerializer, ProgrammerSerializer, LanguageSerializer, ParadigmSerializer

class ListTeamView(viewsets.ModelViewSet):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer

class ListProgrammerView(viewsets.ModelViewSet):
    queryset = Programmer.objects.all()
    serializer_class = ProgrammerSerializer

class ListLanguageView(viewsets.ModelViewSet):
    queryset = Language.objects.all()
    serializer_class = LanguageSerializer

class ListParadigmView(viewsets.ModelViewSet):
    queryset = Paradigm.objects.all()
    serializer_class = ParadigmSerializer

@api_view(['PUT'])
def programmer_language_rel(request, programmer_id, language_id):
    programmer = Programmer.objects.filter(pk=programmer_id).first()
    language = Language.objects.filter(pk=language_id).first()
    programmer.languages.add(language)
    return Response({"result": "Language has been added."})

@api_view(['PUT'])
def language_paradigm_rel(request, language_id, paradigm_id):
    language = Language.objects.filter(pk=language_id).first()
    paradigm = Paradigm.objects.filter(pk=paradigm_id).first()
    language.paradigms.add(paradigm)
    return Response({"result": "Paradigm has been added."})
