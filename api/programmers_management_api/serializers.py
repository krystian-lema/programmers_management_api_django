from rest_framework import serializers
from .models import Team, Programmer, Language, Paradigm

class TeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = ("id", "name", "programmers")

class ProgrammerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Programmer
        fields = '__all__'

class LanguageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Language
        fields = '__all__'

class ParadigmSerializer(serializers.ModelSerializer):
    class Meta:
        model = Paradigm
        fields = '__all__'

class TeamIncludeAllDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = ("id", "name", "programmers")
        depth = 3
