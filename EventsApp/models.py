from django.db import models
# Create your models here.

#Student registration models
class StudRegData(models.Model):

    Name = models.CharField(max_length=20)
    Username = models.CharField(max_length=10)
    Password = models.CharField(max_length=255)

    
    def __str__(self):
        return self.id

#Admin add events models
class AddEvents(models.Model):

    et = (
        ('Tech','Technical'),
        ('Indoor','Indoor'),
        ('Outdoor','Outdoor'),
        ('fun','Entertainment'), 
        ('others','Others')
    )

    dur = (
        ('1 day','1 day'),
        ('2 days','2 days'),
        ('3 days','3 days')
    )

    EventName = models.CharField(max_length=50)
    EventImg = models.ImageField(upload_to="uploads/eventimg/")
    EventDesc = models.CharField(max_length=200) 
    EventType = models.CharField(max_length=20,choices=et)
    EventCost = models.IntegerField()
    EventDuration = models.CharField(max_length=10,choices=dur)
    EventStartDate = models.DateField()

#Student enrolled event models
class StudentEnrolledEvents(models.Model):
    EName = models.CharField(max_length=50)
    EDuration = models.CharField(max_length=10)
    ECost = models.IntegerField()
    EStartDate = models.CharField(max_length=50)
    StudName = models.CharField(max_length=20)
    StudUsername = models.CharField(max_length=20)
    ContactNo = models.BigIntegerField()