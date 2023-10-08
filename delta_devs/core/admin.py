from django.contrib import admin

from .models import Interest,Resource,Skill,User,Project,Message,CollaborationRequest

admin.site.register(Interest)
admin.site.register(Resource)
admin.site.register(Skill)
admin.site.register(User)
admin.site.register(Project)
admin.site.register(Message)
admin.site.register(CollaborationRequest)
