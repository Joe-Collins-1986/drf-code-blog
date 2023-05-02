from rest_framework import serializers
from .models import Article

class ArticleSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()
    profile_id = serializers.ReadOnlyField(source='owner.profile.id')
    profile_image = serializers.SerializerMethodField()

    def get_is_owner(self, obj):
        request = self.context['request']
        return request.user == obj.owner
    
    def get_profile_image(self, obj):
        profile = obj.owner.profile
        if profile and profile.image:
            return profile.image.url
        return None

    class Meta:
        model = Article
        fields = [
            'id', 'owner', 'created_at',
            'updated_at', 'art_title', 'art_content',
            'primary_language', 'github_link',
            'is_owner', 'profile_id', 'profile_image',
        ]