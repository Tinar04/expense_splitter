from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Group(models.Model):

    g_name = models.CharField(max_length=100)
    members = models.ManyToManyField(User)

class Expense(models.Model):
    group = models.ForeignKey(Group,on_delete = models.CASCADE)
    e_name = models.CharField(max_length=100)
    total_amount = models.DecimalField(max_digits=10,decimal_places=2)
    paid_by =models.ForeignKey(User, on_delete=models.CASCADE)
    split_type = models.CharField(max_length=20,choices=[('equal','Equal'),('custom','custom')],default='equal') 
    created_at =models.DateTimeField(auto_now_add=True)

class Split(models.Model):
    expense = models.ForeignKey(Expense, on_delete=models.CASCADE)
    owed_by = models.ForeignKey(User,on_delete=models.CASCADE)
    shared_amount = models.DecimalField(max_digits=10,decimal_places=2)

class Settlement(models.Model):
    group = models.ForeignKey(Group,on_delete=models.CASCADE)
    paid_by = models.ForeignKey(User,on_delete=models.CASCADE,related_name='settlements_paid')
    paid_to = models.ForeignKey(User,on_delete=models.CASCADE,related_name='settlements_received')
    amount_paid = models.DecimalField(max_digits=10,decimal_places=2)
    comment = models.CharField(max_length=100)
    settled_at = models.DateTimeField(auto_now_add=True)
