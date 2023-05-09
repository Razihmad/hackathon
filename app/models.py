from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Hackathon(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    background_image = models.ImageField(upload_to='background_image')
    hackathon_image = models.ImageField(upload_to='hackathon_images')
    TYPES_OF_SUBMISSION = (
        ('image', 'Image'),
        ('file', 'File'),
        ('link', 'Link'),
    )
    type_of_submission = models.CharField(max_length=10, choices=TYPES_OF_SUBMISSION)
    start_datetime = models.DateTimeField()
    end_datetime = models.DateTimeField()
    reward_prize = models.CharField(max_length=100)
    def __str__(self):
        return self.title

class Submission(models.Model):
    hackathon = models.ForeignKey(Hackathon, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    summary = models.TextField()
    submission_file = models.FileField(upload_to='submissions/files',blank=True,null=True)
    submission_image = models.ImageField(upload_to='submissions/images',blank=True,null=True)
    submission_link = models.URLField()
    submission_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name


class Participant(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name='users')
    hackathon = models.ForeignKey(Hackathon,on_delete=models.CASCADE,related_name='hackathon')

    def __str__(self):
        return self.user.username