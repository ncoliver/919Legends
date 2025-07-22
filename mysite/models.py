from django.db import models



# Create your models here.
class Player(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    position = models.CharField(max_length=20)
    jersey_number = models.IntegerField()
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    description = models.CharField()


    def __str__(self):
        return f"# {self.jersey_number} | {self.first_name}, {self.last_name} | {self.email}"


class AddItem(models.Model):
    item_name = models.CharField(max_length=100)
    item_description = models.CharField(max_length=100)
    item_price = models.FloatField()
    item_image = models.ImageField(upload_to='shop_items/')

    def __str__(self):
        return f" {self.pk} {self.item_name} - {self.item_price}"
    

class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.created_at} : {self.name} - {self.email}"

