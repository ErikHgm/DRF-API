from rest_framework import serializers
from .models import Post


class PostSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()
    profile_id = serializers.ReadOnlyField(source='owner.profile.id')
    profile_image = serializers.ReadOnlyField(source='owner.profile.image.url')

    def validate_image(self, value):
        if value.size > 4096 * 4096 *2:
            raise serializers.ValidationError('Image size larger than 2mb')
        if value.image.width > 4096:
            raise serializers.ValidationError('Image width to large')
        if value.image.height > 4096:
            raise serializers.ValidationError('Image height to large')    
    
        return value

    def get_is_owner(self, obj):
        request = self.context['request']
        return request.user == obj.owner

    class Meta:
        model = Post
        fields = '__all__'