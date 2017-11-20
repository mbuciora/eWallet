from django.contrib import admin
from .models import User
from .models import Group
from .models import UserGroup
from .models import ChangeDetail
from .models import GroupChange
from .models import UserChange

admin.site.register(User)
admin.site.register(Group)
admin.site.register(UserGroup)
admin.site.register(ChangeDetail)
admin.site.register(GroupChange)
admin.site.register(UserChange)