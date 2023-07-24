from rest_framework import serializers


class ProfileSerializer(serializers.ModelSerializer):
    """ Serializer for the profile model """

    class Meta:
        