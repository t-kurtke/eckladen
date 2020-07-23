from django.test import TestCase
from django.contrib.auth import get_user_model
# Create your tests here.
print([(u.email, u.is_active, u.has_usable_password()) for u in get_user_model().objects.all()])