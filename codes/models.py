from django.db import models
from django.contrib.auth.models import User
import random

class Code(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    number = models.CharField(max_length=5, blank=True)

    def __str__(self):
        return str(self.number)

    def save(self):
        print('reeeerreeer')
        super().save()
        number_list = [x for x in range(0, 10)]
        code_items = []
        for i in range(0, 5):
            num = random.choice(number_list)
            code_items.append(num)
        code_string = "".join(str(item) for item in code_items)
        self.number = code_string
