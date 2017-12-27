from django.db import models


class Search(models.Model):
    search_id = models.AutoField(primary_key=True)
    text = models.TextField()
    searched_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-searched_date',)
