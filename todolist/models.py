from django.db import models


# Create your models here.
class Todo(models.Model):
    thing = models.CharField(max_length=50)
    done = models.BooleanField(default=False)

    def _str_(self):
        return self.thing
