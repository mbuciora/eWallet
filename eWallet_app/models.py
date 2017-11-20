from django.db import models
from django.core.urlresolvers import reverse


class User(models.Model):
    user_id = models.AutoField(primary_key=True, null=False)
    username = models.CharField(null=False, unique=True, max_length=60)
    password = models.CharField(null=False, max_length=30)
    email = models.CharField(null=False, unique=True, max_length=80)
    account_balance = models.FloatField(null=False, default=0)

    # String for representing the User object in Admin site
    def __str__(self):
        return self.email


class Group(models.Model):
    group_id = models.AutoField(primary_key=True, null=False)
    name = models.CharField(null=False, max_length=60)
    expenses_amount = models.FloatField(null=False, max_length=30, default=0)
    members_count = models.IntegerField(null=False, default=0)
    expenses_per_person = models.FloatField(null=False, default=0)

    def __str__(self):
        return self.name


    def get_absolute_url(self):
        return reverse('group', kwargs={'pk': self.pk})

class UserGroup(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    group_id = models.ForeignKey(Group, on_delete=models.CASCADE)

    def __int__(self):
        return "UserID: " + self.user_id + " GroupID: " + self.group_id


class ChangeDetail(models.Model):
    change_detail_id = models.AutoField(primary_key=True, null=False)
    amount = models.FloatField(null=False, default=0)
    title = models.CharField(null=False, max_length=40)
    description = models.CharField(null=False, max_length=150)
    revenue = models.BooleanField()
    date = models.DateField(null=False, auto_now=True)

    def get_absolute_url(self):
        return reverse('detail', kwargs={'pk': self.pk})



class GroupChange(models.Model):
    change_detail_id = models.ForeignKey(ChangeDetail, on_delete=models.CASCADE)
    group_id = models.ForeignKey(Group, on_delete=models.CASCADE)

    def __int__(self):
        return "ChangeDetailID: " + self.change_detail_id + " GroupID: " + self.group_id


class UserChange(models.Model):
    change_detail_id = models.ForeignKey(ChangeDetail, on_delete=models.CASCADE)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)

    def __int__(self):
        return "ChangeDetailID: " + self.change_detail_id + " UserID: " + self.user_id
