import uuid
from django.db import models
import datetime


class BaseModel(models.Model):
    class Meta:
        abstract = True

    uid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True, blank=True)
    is_deleted = models.BooleanField(default=False)

    def soft_delete(self):
        self.deleted_at = datetime.datetime.utcnow()
        self.is_deleted = True
        self.save()
