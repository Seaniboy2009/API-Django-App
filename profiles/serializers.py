from rest_framework import serializers
from .models import Profile


class ProfileSerializer(serializers.ModelSerializer):
    """ Serializer for the profile model """

    class Meta:
        model = Profile
        fields = '__all__'