from django.db import models
from django.contrib.auth.models import AbstractUser

from .managers import UserManager

class User(AbstractUser):
    """
    Custom User model extending AbstractUser.
    
    Fields:
    - first_name: User's first name.
    - last_name: User's last name.
    - username: Unique username for the user.
    - email: User's email address.
    - profile_image: User's profile image, optional.
    - is_staff: Boolean indicating if the user is a staff member.
    - is_superuser: Boolean indicating if the user is a superuser.
    - is_active: Boolean indicating if the user account is active.
    
    Methods:
    - __str__: Returns the user's full name.
    """
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    username = models.CharField(max_length=100, unique=True)
    email = models.EmailField(blank=True, null=True)
    profile_image = models.ImageField(upload_to='', default='', null=True, blank=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    objects = UserManager()

    REQUIRED_FIELDS = ['first_name', 'last_name']
    USERNAME_FIELD = 'username'

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

class Transaction(models.Model):
    """
    Model to represent a financial transaction.
    
    Fields:
    - user: The user associated with the transaction.
    - type: The type of transaction, either 'kirim' (income) or 'chiqim' (expense).
    - amount: The amount of the transaction.
    - description: A description of the transaction.
    - date: The date and time the transaction was created, auto-generated.
    
    Methods:
    - __str__: Returns a string representation of the transaction.
    """
    TRANSACTION_TYPE_CHOICES = [
        ('kirim', 'Kirim'),
        ('chiqim', 'Chiqim'),
    ]
    
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    type = models.CharField(max_length=100, choices=TRANSACTION_TYPE_CHOICES)
    amount = models.DecimalField(max_digits=15, decimal_places=2)
    description = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.user.username} - {self.type} - {self.amount}"
