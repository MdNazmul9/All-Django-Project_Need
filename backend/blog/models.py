from django.db import models

from accounts.models import CustomUser

class Post(models.Model):
    title= models.CharField(max_length=100)
    contentent = models.TextField()
    author = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, blank=True, null=True)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now_add=True)

    class Meta:
        ordering = ('-created_at',)
        # permissions = [
        #     ('payment_status','can view all post'),
        # ]

    def __str__(self):
        return self.title