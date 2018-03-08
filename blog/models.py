from django.db import models
from django.utils import timezone


class Post(models.Model):
    """A topic a user can post about"""
    text = models.CharField(max_length=250)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """Return a string in a readable format."""
        return self.text

class Entry(models.Model):
    """Where to post entries in the topic"""
    topic = models.ForeignKey(Post, on_delete=models.CASCADE)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)
    
    # for multiple post instead of Entrys, text will be entries
    class Meta:
        verbose_name_plural = 'entries'
    

    def __str__(self):
        """return string in readable format for me"""
        return self.text[:50] + "..." 