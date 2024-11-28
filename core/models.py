
from django.db import models

class Skill(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Interest(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class User(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    email = models.EmailField()
    skills = models.ManyToManyField(Skill, blank=True)
    interests = models.ManyToManyField(Interest, blank=True)
    availability = models.TextField()
    profile_picture = models.ImageField(upload_to='profile_pictures/', null=True, blank=True)
    credits = models.PositiveIntegerField(default=0)  # Initialize with 0 credits

    EDUCATION_LEVEL_CHOICES = [
        ('Undergraduate', 'Undergraduate'),
        ('Pursuing Masters', 'Pursuing Masters'),
        ('Post Graduate', 'Post Graduate'),
        ('Pursing Phd', 'Pursuing PhD'),
        ('PhD', 'PhD'),
    ]
    
    education_level = models.CharField(max_length=100, choices=EDUCATION_LEVEL_CHOICES)


    def __str__(self):
        return self.username
    
class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    creator = models.ForeignKey(User, on_delete=models.CASCADE)
    skills_required = models.ManyToManyField(Skill)
    EXPERTISE_LEVEL_CHOICES = [
        ('Undergraduate', 'Undergraduate'),
        ('Pursuing Masters', 'Pursuing Masters'),
        ('Post Graduate', 'Post Graduate'),
        ('Pursing Phd', 'Pursuing PhD'),
        ('PhD', 'PhD'),
    ]
    expertise_level_required = models.CharField(max_length=100, choices=EXPERTISE_LEVEL_CHOICES)
    expected_scope_of_work = models.TextField()
    status = models.CharField(max_length=20, choices=[
        ('Open', 'Open'),
        ('In Progress', 'In Progress'),
        ('Completed', 'Completed')
    ])
    resources = models.ManyToManyField('Resource', blank=True)
    credits_required = models.PositiveIntegerField()

    def __str__(self):
        return self.title


class CollaborationRequest(models.Model):
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sent_requests')
    receiver = models.ForeignKey(User, on_delete=models.CASCADE, related_name='received_requests')
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, choices=[
        ('Pending', 'Pending'),
        ('Accepted', 'Accepted'),
        ('Rejected', 'Rejected')
    ])

    def __str__(self):
        return f"Request from {self.sender} to {self.receiver} for {self.project}"

class Message(models.Model):
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sent_messages')
    receiver = models.ForeignKey(User, on_delete=models.CASCADE, related_name='received_messages')
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Message from {self.sender} to {self.receiver}"

class Resource(models.Model):
    name = models.CharField(max_length=100)
    link = models.URLField()

    def __str__(self):
        return self.name

# from django.db import models

# class Skill(models.Model):
#     id = models.AutoField(primary_key=True)
#     name = models.CharField(max_length=100)

#     def _str_(self):
#         return self.name

# class Interest(models.Model):
#     id = models.AutoField(primary_key=True)
#     name = models.CharField(max_length=100)

#     def _str_(self):
#         return self.name

# class User(models.Model):
#     id = models.AutoField(primary_key=True)
#     username = models.CharField(max_length=100)
#     password = models.CharField(max_length=100)
#     email = models.EmailField()
#     skills = models.ManyToManyField(Skill, blank=True)
#     interests = models.ManyToManyField(Interest, blank=True)
#     availability = models.TextField()
#     profile_picture = models.ImageField(upload_to='profile_pictures/', null=True, blank=True)
#     credits = models.PositiveIntegerField(default=0)
    
#     EDUCATION_LEVEL_CHOICES = [
#         ('Undergraduate', 'Undergraduate'),
#         ('Pursuing Masters', 'Pursuing Masters'),
#         ('Post Graduate', 'Post Graduate'),
#         ('Pursing Phd', 'Pursuing PhD'),
#         ('PhD', 'PhD'),
#     ]
    
#     education_level = models.CharField(max_length=100, choices=EDUCATION_LEVEL_CHOICES)

#     def _str_(self):
#         return self.username
    
# class Project(models.Model):
#     id = models.AutoField(primary_key=True)
#     title = models.CharField(max_length=100)
#     description = models.TextField()
#     creator = models.ForeignKey(User, on_delete=models.CASCADE)
#     collaborators = models.ManyToManyField(User, related_name='collaborating_projects', blank=True)
#     skills_required = models.ManyToManyField(Skill)
    
#     EXPERTISE_LEVEL_CHOICES = [
#         ('Undergraduate', 'Undergraduate'),
#         ('Pursuing Masters', 'Pursuing Masters'),
#         ('Post Graduate', 'Post Graduate'),
#         ('Pursing Phd', 'Pursuing PhD'),
#         ('PhD', 'PhD'),
#     ]
    
#     expertise_level_required = models.CharField(max_length=100, choices=EXPERTISE_LEVEL_CHOICES)
#     expected_scope_of_work = models.TextField()
    
#     STATUS_CHOICES = [
#         ('Open', 'Open'),
#         ('In Progress', 'In Progress'),
#         ('Completed', 'Completed')
#     ]
    
#     status = models.CharField(max_length=20, choices=STATUS_CHOICES)
#     resources = models.ManyToManyField('Resource', blank=True)
#     credits_required = models.PositiveIntegerField()

#     def _str_(self):
#         return self.title
    
# # class Project(models.Model):
# #     id = models.AutoField(primary_key=True)
# #     title = models.CharField(max_length=100)
# #     description = models.TextField()
# #     creator = models.ForeignKey(User, on_delete=models.CASCADE)
# #     skills_required = models.ManyToManyField(Skill)
    
# #     EXPERTISE_LEVEL_CHOICES = [
# #         ('Undergraduate', 'Undergraduate'),
# #         ('Pursuing Masters', 'Pursuing Masters'),
# #         ('Post Graduate', 'Post Graduate'),
# #         ('Pursing Phd', 'Pursuing PhD'),
# #         ('PhD', 'PhD'),
# #     ]
    
# #     expertise_level_required = models.CharField(max_length=100, choices=EXPERTISE_LEVEL_CHOICES)
# #     expected_scope_of_work = models.TextField()
    
# #     STATUS_CHOICES = [
# #         ('Open', 'Open'),
# #         ('In Progress', 'In Progress'),
# #         ('Completed', 'Completed')
# #     ]
    
# #     status = models.CharField(max_length=20, choices=STATUS_CHOICES)
# #     resources = models.ManyToManyField('Resource', blank=True)
# #     credits_required = models.PositiveIntegerField()

# #     def _str_(self):
# #         return self.title


# class CollaborationRequest(models.Model):
#     id = models.AutoField(primary_key=True)
#     sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sent_requests')
#     receiver = models.ForeignKey(User, on_delete=models.CASCADE, related_name='received_requests')
#     project = models.ForeignKey(Project, on_delete=models.CASCADE)
#     timestamp = models.DateTimeField(auto_now_add=True)
    
#     STATUS_CHOICES = [
#         ('Pending', 'Pending'),
#         ('Accepted', 'Accepted'),
#         ('Rejected', 'Rejected')
#     ]
    
#     status = models.CharField(max_length=20, choices=STATUS_CHOICES)

#     def _str_(self):
#         return f"Request from {self.sender} to {self.receiver} for {self.project}"

# class Message(models.Model):
#     id = models.AutoField(primary_key=True)
#     sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sent_messages')
#     receiver = models.ForeignKey(User, on_delete=models.CASCADE, related_name='received_messages')
#     content = models.TextField()
#     timestamp = models.DateTimeField(auto_now_add=True)

#     def _str_(self):
#         return f"Message from {self.sender} to {self.receiver}"
    
# class Resource(models.Model):
#     id = models.AutoField(primary_key=True)
#     name = models.CharField(max_length=100)
#     link = models.URLField()

#     def _str_(self):
#         return self.name
    



