from django.db import models

# Create your models here.
class course(models.Model):
    name =models.CharField(max_length=300)
    c_id=models.CharField(max_length=300)

    def __str__(self) -> str:
        return f'{self.name}'