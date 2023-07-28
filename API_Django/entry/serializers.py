from rest_framework import serializers
from .models import Entry


class EntrySerializer(serializers.ModelSerializer):
    """ Serializer for the Entry model """

    class Meta:
        model = Entry
        fields = '__all__'