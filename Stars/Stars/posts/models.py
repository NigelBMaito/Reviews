from django.db import models


# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=100)
    body = models.TextField()
    slug = models.SlugField()
    banner = models.ImageField(default='fallback.png', blank=True)
    date = models.DateTimeField(auto_now_add=True)

    def average_rating(self):
        comments = self.comments.all()
        if comments.exists():
            return sum(comment.rating for comment in comments) / comments.count()
        return 0

    def __str__(self):
        return self.title


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    name = models.CharField(max_length=100)
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    rating = models.PositiveBigIntegerField(default=0)

    def __str__(self):
        return f"{self.name} commented on {self.post.title} ({self.rating})"