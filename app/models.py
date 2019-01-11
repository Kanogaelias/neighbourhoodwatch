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


