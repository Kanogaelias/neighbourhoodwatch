from django.db import models
from django.contrib.auth.models import User

class Neighbourhood(models.Model):
    name=models.CharField(max_length=60)
    location=models.CharField(max_length=60)
    population=models.IntegerField()
    admin=models.ForeignKey(User,on_delete=models.CASCADE)

    def create_neigborhood(self):
        self.save()

    def delete_neigborhood(self):
        self.delete()
    @classmethod
    def find_neigborhood(cls,neighborhood_id):
        neighborhood=cls.objects.filter(id=neighborhood_id)
        return neighborhood
    @classmethod
    def update_neighborhood(cls,neighborhood_id):
        neighborhood=cls.objects.filter(id=neighborhood_id)
        neighborhood.name=Value
        neighborhood.save()
        return neighborhood
    @classmethod
    def update_neighborhood(cls,neighborhood_id):
        neighborhood=cls.objects.filter(id=neighborhood_id)
        neighborhood.occupants=Value
        neighborhood.save()
        return neighborhood

    @classmethod
    def search_by_name(cls,search_term):
        neighborhood=cls.objects.filter(name__icontains=search_term)
        return neighborhood


class Profile(models.Model):
    profile_pic=models.ImageField(upload_to='profile_photos/')
    bio=models.CharField(max_length=300)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    # neighborhood=models.ForeignKey(Neighbourhood,on_delete=models.CASCADE)
    def create_profile(self):
        self.save()

    def delete_profile(self):
        self.delete()


class Business(models.Model):
    name=models.CharField(max_length=60)
    description=models.CharField(max_length=200)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    neighborhood=models.ForeignKey(Neighbourhood,on_delete=models.CASCADE)
    email=models.EmailField()

    def create_business(self):
        self.save()

    def delete_business(self):
        self.delete()

    @classmethod
    def find_business(cls,business_id):
        business=cls.objects.filter(id=business_id)
        return business
    @classmethod
    def update_business(cls,business_id):
        business=cls.objects.filter(id=business_id)
        business.name=Value
        business.save()
        return business

class Post(models.Model):
        post=models.CharField(max_length=200)
        user=models.ForeignKey(User,on_delete=models.CASCADE)
        neighborhood=models.ForeignKey(Neighbourhood,on_delete=models.CASCADE)