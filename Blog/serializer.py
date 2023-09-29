from operator import itemgetter

from rest_framework import serializers
from .models import Post
from collections import OrderedDict


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        # fields = [
        #     'id',
        #     'title',
        #     'content',
        #     'created_by',
        #     'update_at',
        # ]
        fields = "__all__"
        depth = 1
    def get_requests_user(self):
        return self.context['request'].user

    def create(self, validated_data):
        """
        Create and return a new `Snippet` instance, given the validated data.
        """
        return Post.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Snippet` instance, given the validated data.
        """
        instance.title = validated_data.get('title', instance.title)
        instance.save()
        return instance

    def to_representation(self, instance):
        ret = super().to_representation(instance)
        ret = OrderedDict(filter(itemgetter(1), ret.items()))
        return ret