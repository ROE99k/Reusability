from django.contrib.auth.models import User
from django.db import models

# Base model for timestamps
class BaseTimestampModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

# Post model
class Post(BaseTimestampModel):
    title = models.CharField(max_length=200)
    content = models.TextField()

    def __str__(self):
        return self.title

# ✅ Comment model (moved outside)
class Comment(BaseTimestampModel):
    post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name="author")
    content = models.TextField()

    def __str__(self):
        return f"Comment on '{self.post.title}'"
