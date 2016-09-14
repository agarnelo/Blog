from rest_framework.serializers import ModelSerializer
from posts.models import Post

class PostListSerializer(ModelSerializer):
    class Meta:
        model = Post
        fields = [
            "user",
            "title",
            "slug",
            "content",
            "publish"
        ]

class PostDetailSerializer(ModelSerializer):
    class Meta:
        model = Post
        fields = [
            "id",
            "title",
            "slug",
            "content",
            "publish"
        ]

class PostCreateUpdateSerializer(ModelSerializer):
    class Meta:
        model = Post
        fields = [
            "title",
            "content",
            "publish"
        ]

# data = {
#     "title": "Post",
#     "content": "Content",
#     "publish": "2016-9-9",
#     "slug": "post160909"
# }

# new_item = PostSerializer(data=data)
# if new_item.is_valid():
#     new_item.save()
# else:
#     print (new_item.errors)