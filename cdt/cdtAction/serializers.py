from rest_framework import serializers
from cdtAction.models import User


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        models = User
        depth = 0
