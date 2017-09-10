from django.db import models

class User(models.Model):
    user_id = models.AutoField(primary_key=True, null=False)
    login = models.CharField(null=False, unique=True, max_length=60)
    password = models.CharField(null=False, max_length=30)
    email = models.CharField(null=False, unique=True, max_length=80)
    account_balance = models.FloatField(null=False, default=0)

# String for representing the User object in Admin site
    def __str__(self):
        return self.email

