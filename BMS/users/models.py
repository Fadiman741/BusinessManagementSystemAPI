from django.contrib.auth.models import AbstractUser
from django.db import models
import datetime
import uuid

# def generate_employee_id():
#     return str(uuid.uuid4().hex[:6])
class User(AbstractUser):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    username = models.CharField(max_length=100,null=True)
    # order_number = models.CharField(
    #     max_length=6, default=generate_employee_id, unique=True
    # )
    employee_id = models.CharField(max_length=20, null=True)
    contacts = models.IntegerField(null=True)
    address = models.CharField(max_length=100,null=True)
    email = models.EmailField(max_length=255, unique=True)
    gender = models.CharField(max_length=10, choices=[('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')], null=True)
    identification_number = models.CharField(max_length=50, null=True)
    salary = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    bank_account_number = models.CharField(max_length=50, null=True)
    bank_name = models.CharField(max_length=100, null=True)
    employment_start_date = models.DateField(null=True)
    employment_end_date = models.DateField(null=True)
    notes = models.TextField(null=True)
    employment_status = models.CharField(max_length=20, choices=[('Full-time', 'Full-time'), ('Part-time', 'Part-time'), ('Contract', 'Contract')], null=True)
    datecreated = models.DateTimeField(auto_now_add=True)
    dateofbirth = models.DateTimeField(null=True)
    #     profile_pic = models.ImageField(upload_to="profile_images/", null=True)
    role = models.CharField(max_length=100, choices=[("Admin", "Admin"), ("Cashier", "Cashier"),("Manager", "Manager")], default="Cashier")
    status = models.CharField(max_length=100,choices=[("Inactive", "Inactive"), ("Active", "Active")], default="Inactive")

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["first_name"]

    def __str__(self):
        return self.email


class Menu(models.Model):
    # user = models.ForeignKey(User, on_delete=models.CASCADE)
    Name = models.CharField(max_length=255)
    Description = models.TextField(max_length=1000)
    Price = models.IntegerField(null=True)
    Category = models.CharField(max_length=255, null=True)
    tags = models.CharField(max_length=255, null=True)
    image = models.ImageField(upload_to="menu_images/", null=True)

    def __str__(self):
        return self.menu_name


def generate_order_number():
    return str(uuid.uuid4().hex[:6])


class Order(models.Model):
    # user = models.ForeignKey(User, on_delete=models.CASCADE)
    items = models.ManyToManyField(Menu)
    status = models.CharField(
        max_length=10, choices=[("Open", "Open"), ("Closed", "Closed")], default="Open"
    )
    order_number = models.CharField(
        max_length=6, default=generate_order_number, unique=True
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Task(models.Model):
    title = models.CharField(max_length=100,null=True)
    description = models.TextField()
    status = models.CharField(max_length=20, choices=[('Todo', 'Todo'), ('In_progress', 'In_Progress'), ('Done', 'Done')], default="Todo")
    # created_at = models.DateTimeField(auto_now_add=True)
    # updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title