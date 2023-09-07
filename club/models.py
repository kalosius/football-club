from django.db import models

# Create your models here.
class Player(models.Model):
    player_name = models.CharField(max_length=50, null=True, blank=True)
    date_of_birth = models.DateField()
    shirt_number = models.IntegerField(default=0, null=True, blank=True)
    salary = models.IntegerField(default=0, null=True, blank=True)
    appearance = models.IntegerField(default=0, null=True, blank=True)
    goals = models.IntegerField(default=0, null=True, blank=True)
    
    def __str__(self):
        return self.salary
    
        def players_tax(self):
            tax = self.salary * 0.18
            return float(tax)
        
        def net_salary(self):
            salary_amount = self.salary - self.players_tax()
            return float(salary_amount)
    
    