from django.db import models
from django.conf import settings
from users.models import UserAccount

class Department(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=500)
    is_active = models.BooleanField(default=True) 
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='departments_created_user', null=True, blank=True, on_delete=models.SET_NULL)  
    updated_by = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='departments_updated_user',null=True, blank=True, on_delete=models.SET_NULL)
    deleted_by = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='departments_deleted_user',null=True, blank=True, on_delete=models.SET_NULL) 
    created_at = models.DateTimeField(auto_now_add=True)  
    updated_at = models.DateTimeField(null=True, blank=True) 
    deleted_at = models.DateTimeField(null=True, blank=True)     
   
    # string representation of the class
    def __str__(self):
 
        #it will return the title
        return self.name

class Designation(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=500)
    is_active = models.BooleanField(default=True) 
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='designations_created_user', null=True, blank=True, on_delete=models.SET_NULL)  
    updated_by = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='designations_updated_user',null=True, blank=True, on_delete=models.SET_NULL)
    deleted_by = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='designations_deleted_user',null=True, blank=True, on_delete=models.SET_NULL) 
    created_at = models.DateTimeField(auto_now_add=True)  
    updated_at = models.DateTimeField(null=True, blank=True) 
    deleted_at = models.DateTimeField(null=True, blank=True)     
   
    # string representation of the class
    def __str__(self):
 
        #it will return the title
        return self.name
    

class Province(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=500)
    is_active = models.BooleanField(default=True) 
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='provinces_created_user', null=True, blank=True, on_delete=models.SET_NULL)  
    updated_by = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='provinces_updated_user',null=True, blank=True, on_delete=models.SET_NULL)
    deleted_by = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='provinces_deleted_user',null=True, blank=True, on_delete=models.SET_NULL) 
    created_at = models.DateTimeField(auto_now_add=True)  
    updated_at = models.DateTimeField(null=True, blank=True) 
    deleted_at = models.DateTimeField(null=True, blank=True)     
   
    # string representation of the class
    def __str__(self):
 
        #it will return the title
        return self.name
    
class District(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=500)
    is_active = models.BooleanField(default=True) 
    province_id = models.ForeignKey(Province, related_name='districts_province_id', null=True, blank=True, on_delete=models.SET_NULL)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='districts_created_user', null=True, blank=True, on_delete=models.SET_NULL)  
    updated_by = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='districts_updated_user',null=True, blank=True, on_delete=models.SET_NULL)
    deleted_by = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='districts_deleted_user',null=True, blank=True, on_delete=models.SET_NULL) 
    created_at = models.DateTimeField(auto_now_add=True)  
    updated_at = models.DateTimeField(null=True, blank=True) 
    deleted_at = models.DateTimeField(null=True, blank=True)     
   
    # string representation of the class
    def __str__(self):
 
        #it will return the title
        return self.name
    
class City(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=500)
    is_active = models.BooleanField(default=True) 
    province_id = models.ForeignKey(Province, related_name='city_province_id', null=True, blank=True, on_delete=models.SET_NULL)
    district_id = models.ForeignKey(District, related_name='city_district_id', null=True, blank=True, on_delete=models.SET_NULL)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='cities_created_user', null=True, blank=True, on_delete=models.SET_NULL)  
    updated_by = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='cities_updated_user',null=True, blank=True, on_delete=models.SET_NULL)
    deleted_by = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='cities_deleted_user',null=True, blank=True, on_delete=models.SET_NULL) 
    created_at = models.DateTimeField(auto_now_add=True)  
    updated_at = models.DateTimeField(null=True, blank=True) 
    deleted_at = models.DateTimeField(null=True, blank=True)     
   
    # string representation of the class
    def __str__(self):
 
        #it will return the title
        return self.name