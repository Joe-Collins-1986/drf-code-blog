from rest_framework import serializers
from .models import Language
from datetime import date

class LanguageSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()
    years_exp = serializers.SerializerMethodField()

    def get_is_owner(self, obj):
        request = self.context['request']
        return request.user == obj.owner
    
    def get_years_exp(self, obj):
        if obj.used_since:
            today = date.today()
            years = today.year - obj.used_since.year
            if (
                today.month < obj.used_since.month or
                (today.month == obj.used_since.month and today.day < obj.used_since.day)
                ):
                years -= 1
            return years
        return None
    
    def validate(self, attrs):
        language = attrs.get('language')
        owner = self.context['request'].user

        # Check if the user has already selected the same language
        if Language.objects.filter(owner=owner, language=language).exists():
            raise serializers.ValidationError({'detail': 'Language already selected by the user.'})

        return attrs
    

    class Meta:
        model = Language
        fields = [
            'id', 'owner', 'language',
            'confidence', 'used_since',
            'is_owner', 'years_exp',
        ]

class LanguageDetailSerializer(LanguageSerializer):
    language = serializers.ReadOnlyField()



