from django.db import models

# Create your models here.
class Post(models.Model):
    """
        An post information model

        Attributes
        ----------
        title : models.CharField
            title text of Post. required

        text : models.TextField
            body text of Post. required

        published_date : models.DateTimeField
            date and time of Post creation. required

        image : models.ImageField
            image for the Post. not required, has default image

        """
    title = models.CharField(max_length=200, blank=False)
    text = models.TextField()
    published_date = models.DateTimeField()
    image = models.ImageField(upload_to='images', default='no_image.svg')