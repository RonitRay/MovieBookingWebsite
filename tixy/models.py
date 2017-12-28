from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

class Movie(models.Model):
    name = models.CharField(max_length=50)
    genre = models.CharField(max_length=50)
    language = models.CharField(max_length=50)
    duration = models.CharField(max_length=50)
    pic = models.CharField(max_length=500)
    pic2 = models.CharField(max_length=500)

    def __str__(self):
        return self.name + ' (' + self.language + ') '


class Slot(models.Model):
    time = models.CharField(max_length=10)

    def __str__(self):
        return self.time


class Schedule(models.Model):
    slot = models.OneToOneField(Slot, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie,on_delete=models.CASCADE)

    def __str__(self):
        return self.movie.name + ' ' + str(self.slot)


class Booking(models.Model):
    class Meta:
        unique_together = (('slot', 'sno'),)

    slot = models.ForeignKey(Slot, on_delete=models.CASCADE)
    sno = models.IntegerField(validators=[MinValueValidator(0),MaxValueValidator(20)],default=0)

    def __str__(self):
        return str(self.slot) + ' ' + str(self.sno)