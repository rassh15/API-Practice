import imp
from rest_framework import serializers
from messageup.models import Message

class MessageSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    class Meta:
        model = Message
        fields = '__all__'