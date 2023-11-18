from django.db import models

# Create your models here.

class Author(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    email = models.EmailField()

    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name}"

class Tag(models.Model):
    caption = models.CharField(max_length=20)

    def __str__(self) -> str:
        return f"{self.caption}"   
    
class Post(models.Model):
    title = models.CharField(max_length=100)
    image_name = models.CharField(max_length=50)
    excerpt = models.CharField(max_length=500)
    date = models.DateField(auto_now=True)
    slug = models.SlugField(default="", blank=True,null=False, 
                            db_index=True)
    content = models.TextField()
    author = models.ForeignKey(Author, null=True, on_delete=models.SET_NULL)
    tag = models.ManyToManyField(Tag)

    def __str__(self) -> str:
        return f"{self.title}" 