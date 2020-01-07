from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext as _
import datetime


def year_choices():
    return [(r,r) for r in range(datetime.date.today().year,datetime.date.today().year+10)]
def current_year():
    return datetime.date.today().year
# Create your models here.
class UserProfileInfo(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    yearofpassing = models.IntegerField(('year'), choices=year_choices(), default=current_year)
    resume = models.ImageField(upload_to='resume')
    cgpa=models.FloatField()
    def __str__(self):
        return self.user.username
