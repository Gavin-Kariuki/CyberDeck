from django.db import models

# Create your models here.
class Location(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    def save_location(self):
        self.save()

    def delete_location(self):
        self.delete()

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    def save_category(self):
        self.save()


class Image(models.Model):
    image = models.ImageField(upload_to = 'articles/') #need to download pillow for this
    image_name = models.CharField(max_length=100)
    image_description = models.TextField()
    location = models.ForeignKey(Location,on_delete=models.CASCADE)
    category = models.ForeignKey(Category,on_delete=models.CASCADE)

    
    def save_image(self):
        self.save()

    def delete_image(self):
        self.delete()

    @classmethod
    def display_all_images(cls):
        return cls.objects.all()

    @classmethod
    def search_by_category(cls,category):
        mapicha = cls.objects.filter(category__name__icontains=category)
        return mapicha

    @classmethod
    def filter_by_location(cls,location):
        image_location = Image.objects.filter(location__name=location).all()
        return image_location

    @classmethod
    def update_image(cls,id,value):
        cls.objects.filter(id=id).update(image=value)

    @classmethod
    def get_image_by_id(cls,id):
        image = cls.objects.filter(id=id).all()
        return image

    
