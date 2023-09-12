from django.db import models
from django.conf import settings


num = [('Goal Keeper', 'Goal Keeper'),('Defender','Defender'),('Midfielder','Midfielder'),('Striker','Striker'),('Winger','Winger'),]
under = [('First Team', 'First Team'),('Second Team', 'Second Team')]
foot = [('Right', 'Right'),('Left', 'Left')]
# Create your models here.
class Player(models.Model):
    player_name = models.CharField(max_length=50, null=True, blank=True)
    date_of_birth = models.DateField()
    team = models.CharField(max_length=30, choices=under)
    position = models.CharField(max_length=30, choices=num)
    strong_foot = models.CharField(max_length=30, choices=foot)
    shirt_number = models.IntegerField(default=0, null=True, blank=True)
    salary = models.IntegerField(default=0, null=True, blank=True)
    appearance = models.IntegerField(default=0, null=True, blank=True)
    goals = models.IntegerField(default=0, null=True, blank=True)
    player_image = models.FileField(upload_to='club/', max_length=250, null=True, default=None)
    
    def players_tax(self):
        tax = self.salary * 0.18
        return float(tax)
    
    def net_salary(self):
        salary_amount = self.salary - self.players_tax()
        return float(salary_amount)


class Gallery(models.Model):
    gallery_pic = models.FileField(upload_to="club/", null=True, default=None, max_length=250)