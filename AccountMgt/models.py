from django.db import models
from django.contrib.auth.models import User
from django.db import models
from uuid import UUID
from uuid import uuid4 as UUID4
from django.contrib.auth.models import BaseUserManager, AbstractUser, AbstractBaseUser
from django.contrib.auth.hashers import make_password
# from Role.models import Role
from django.utils.timezone import now as djnow

# Create your models here.
GENDER_CHOICES = ((0, 'male'), (1, 'female'))
STATUS_CHOICES = ((0, 'not confirm'), (1, 'confirm'))


class Account(AbstractBaseUser):
    uuid = models.UUIDField(default=UUID4,
                            editable=False,
                            unique=True,
                            primary_key=True)
    username = models.CharField(max_length=100,
                                unique=True,
                                null=True,
                                help_text='user name')
    password = models.CharField(max_length=100,
                                null=True,
                                help_text='password')
    email = models.CharField(max_length=100,
                             unique=True,
                             null=True,
                             help_text='email')
    first_name = models.CharField(max_length=100,
                                  null=True,
                                  help_text='first name')
    last_name = models.CharField(max_length=100,
                                 null=True,
                                 help_text='last name')
    dob = models.DateField()
    gender = models.CharField(choices=GENDER_CHOICES,
                              help_text='gender')
    status = models.CharField(choices=STATUS_CHOICES,
                              default=0,
                              help_text="status")
    # role = models.ManyToManyField(Role, null=True,
    #                               blank=True,
    #                               help_text='role')
    created_at = models.DateTimeField(default=djnow,
                                      editable=False,
                                      help_text="created at")
    updated_at = models.DateTimeField(default=djnow,
                                      help_text="updated at")

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return str(self.first_name) + str(self.last_name)

    def save(self, *args, **kwargs):
        self.updated_at = djnow()
        self.password = make_password(self.password)
        super().save(self, *args, **kwargs)
