from django.db import models


class TODO(models.Model):
    title = models.CharField(max_length=250)
    done_at = models.DateTimeField(blank=True, null=True)
    is_done = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
