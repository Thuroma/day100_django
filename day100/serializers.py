from rest_framework import serializers
from .models import Curriculum, DayLog

class CurriculumSerializer(serializers.ModelSerializer):
    class Meta:
        model = Curriculum
        fields = '__all__'


class DayLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = DayLog
        fields = '__all__'

    