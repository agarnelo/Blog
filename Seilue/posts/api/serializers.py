from rest_framework.serializers import ModelSerializer
from posts.models import Post

class PostSerializer(ModelSerializer):
    class Meta:
        model = Post
        fields = [
            "id",
            "title",
            "slug",
            "content",
            "publish"
        ]

data = {
    "title": "Post",
    "content": "Content",
    "publish": "2016-9-9",
    "slug": "post160909"
}

new_item = PostSerializer(data=data)
if new_item.is_valid():
    new_item.save()
else:
    print (new_item.errors)