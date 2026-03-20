from rest_framework import serializers
from .models import Keyword, ContentItem, Flag

class KeywordSerializer(serializers.ModelSerializer):
    

    class Meta:
        model = Keyword
        fields = '__all__'

class FlagSerializer(serializers.ModelSerializer):
    reviewed_at = serializers.DateTimeField(allow_null=True, required=False)
    class Meta:
        model = Flag
        fields = '__all__'