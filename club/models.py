from django.db import models
from django.conf import settings
from datetime import date

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
    
    def __str__(self):
        return self.player_name
    
    def calculate_age(self):
        today = date.today()
        age = today.year - self.date_of_birth.year - ((today.month, today.day) < (self.date_of_birth.month, self.date_of_birth.day))
        return age
    
    
    def calculate_tax(self):
        if self.salary is not None:
            tax_percentage = 18  # 18% tax rate
            tax_amount = (tax_percentage / 100) * self.salary
            return tax_amount
        else:
            return 0  # If salary is not provided, tax is 0

    
    def calculate_net_salary(self):
        if self.salary is not None:
            tax_percentage = 18  # 18% tax rate
            tax_amount = (tax_percentage / 100) * self.salary
            net_salary = self.salary - tax_amount
            return net_salary
        else:
            return None  # If salary is not provided, net salary is None

    
    def gross_salary(self):
        if self.calculate_net_salary() is not None:
            months = 12
            gross = (months * (self.calculate_net_salary()))
            return gross
        else:
            return None

class Gallery(models.Model):
    gallery_pic = models.FileField(upload_to="club/", null=True, default=None, max_length=250)
    
    
            