from django.contrib.auth.models import User
from django.db import models
from uuid import UUID
from uuid import uuid4 as UUID4
# from AccountMgt.models import Account
from django.utils.timezone import now as djnow
from django.contrib.auth import get_user_model
Account = get_user_model()


# Create your models here.
class Category(models.Model):
    uuid = models.UUIDField(default=UUID4,
                            editable=False,
                            unique=True,
                            primary_key=True)
    name = models.CharField(max_length=100,
                            null=True,
                            blank=True,
                            help_text="name")
    created_by = models.ForeignKey(Account, related_name="create_category",
                                   null=True,
                                   blank=True,
                                   on_delete=models.SET_NULL,
                                   help_text="created by")
    updated_by = models.ForeignKey(Account, related_name="update_category",
                                   null=True,
                                   blank=True,
                                   on_delete=models.SET_NULL,
                                   help_text="updated by")
    created_at = models.DateTimeField(default=djnow,
                                      editable=False,
                                      help_text="created at")
    updated_at = models.DateTimeField(default=djnow,
                                      help_text="updated at")

    def __str__(self):
        return self.name

    def save(self):
        self.updated_at = djnow()
        super().save(self)


class Post(models.Model):
    title = models.CharField(max_length=1024,
                             unique=True,
                             null=True,
                             blank=True,
                             editable=True,
                             help_text="title")
    content = models.TextField(max_length=2048,
                               editable=True,
                               blank=True,
                               null=True,
                               help_text="content")
    category_id = models.ManyToManyField(Category)
    created_by = models.ForeignKey(Account, related_name="create_post",
                                   null=True,
                                   blank=True,
                                   on_delete=models.SET_NULL,
                                   help_text="created by")
    updated_by = models.ForeignKey(Account, related_name="update_post",
                                   null=True,
                                   blank=True,
                                   on_delete=models.SET_NULL,
                                   help_text="updated by")
    created_at = models.DateTimeField(default=djnow,
                                      editable=False,
                                      help_text="created at")
    updated_at = models.DateTimeField(default=djnow,
                                      help_text="updated at")
    IS_DELETE_CHOICES = (
        (0, 'no'),
        (1, 'yes'),
    )

    def __str__(self):
        return self.title

    def save(self):
        self.updated_at = djnow()
        super().save(self)



