from rest_framework import serializers
from .models import Profile
from followers.models import Follower

class ProfileSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()
    following_id = serializers.SerializerMethodField()

    article_count = serializers.ReadOnlyField()
    followed_count = serializers.ReadOnlyField()
    following_count = serializers.ReadOnlyField()
    languages_count = serializers.ReadOnlyField()

    def get_is_owner(self, obj):
        request = self.context['request']
        return request.user == obj.owner
    
    def get_following_id(self, obj):
        user = self.context['request'].user
        if user.is_authenticated:
            following = Follower.objects.filter(
                owner=user, followed=obj.owner
            ).first()
            return following.id if following else None
        return None

    class Meta:
        model = Profile
        fields = [
            'id', 'owner', 'created_at',
            'profile_name', 'bio', 'image',
            'is_owner', 'following_id',
            'article_count', 'followed_count',
            'following_count', 'languages_count',
        ]