from rest_framework import serializers
from .models import Article

class ArticleSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()
    profile_id = serializers.ReadOnlyField(source='owner.profile.id')
    profile_image = serializers.ReadOnlyField(source='owner.profile.image.url')

    def get_is_owner(self, obj):
        request = self.context['request']
        return request.user == obj.owner

    class Meta:
        model = Article
        fields = [
            'id', 'owner', 'created_at',
            'updated_at', 'art_title', 'art_content',
            'primary_language', 'github_link',
            'is_owner', 'profile_id', 'profile_image',
        ]