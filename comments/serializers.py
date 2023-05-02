from rest_framework import serializers
from .models import Comment

class CommentSerializer(serializers.ModelSerializer):
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
        model = Comment
        fields = [
            'id', 'owner', 'article',
            'created_at', 'body',
            'is_owner', 'profile_id', 'profile_image',
        ]

class CommentDetailSerializer(CommentSerializer):
    article = serializers.ReadOnlyField(source='article.id')
