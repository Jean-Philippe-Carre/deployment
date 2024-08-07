from django.db import models

# Create your models here.
CATEGORY_CHOICES = (
    ('Dj', 'Django'),
    ('Py', 'Python'),
)


class Post(models.Model):

    custom_id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=100)
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
    content = models.TextField(max_length=1024, default='SOME STRING')
    publish_date = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
