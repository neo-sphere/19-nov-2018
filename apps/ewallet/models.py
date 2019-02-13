from django.db import models


class Profile(models.Model):
    MALE = 'm'
    FEMALE = 'f'
    GENDER_CHOICES = (
        (MALE, 'Male'),
        (FEMALE, 'Female'),
    )
    profile_pic = models.ImageField(upload_to='profile', null=True, blank=True)
    address = models.CharField(max_length=30)
    country = models.CharField(max_length=30)
    mobile = models.CharField(max_length=15, unique=True)
    dob = models.DateField()
    gender = models.CharField(max_length=1,
                        choices=GENDER_CHOICES)
    profession = models.CharField(max_length=20)

    def __str__(self):
        return self.mobile
