from django.db import models
from django.conf import settings
from django.contrib.auth.models import (
    BaseUserManager, 
    AbstractBaseUser,
    PermissionsMixin,
)

class UserAccountManager(BaseUserManager):
    def create_user(self, email, password=None,**kwargs):        
        if not email:
            raise ValueError("Users must have an email address")

        email = self.normalize_email(email)
        email = email.lower()

        user = self.model(
            email=email,
            **kwargs
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **kwargs):       
        user = self.create_user(
            email,
            password=password,
            **kwargs,
        )
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class UserAccount(AbstractBaseUser, PermissionsMixin):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(unique=True,max_length=255)    
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    objects = UserAccountManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name','last_name']

    def __str__(self):
        return self.email    
    
class Role(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=500)
    description = models.CharField(max_length=1000)
    is_active = models.BooleanField(default=True) 
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='roles_created_user', null=True, blank=True, on_delete=models.SET_NULL)  
    updated_by = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='roles_updated_user',null=True, blank=True, on_delete=models.SET_NULL)
    deleted_by = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='roles_deleted_user',null=True, blank=True, on_delete=models.SET_NULL) 
    created_at = models.DateTimeField(auto_now_add=True)  
    updated_at = models.DateTimeField(null=True, blank=True) 
    deleted_at = models.DateTimeField(null=True, blank=True)     
   
    # string representation of the class
    def __str__(self):
 
        #it will return the title
        return self.name
    
class Permission(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=500)
    description = models.CharField(max_length=1000)
    is_active = models.BooleanField(default=True) 
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='permissions_created_user', null=True, blank=True, on_delete=models.SET_NULL)  
    updated_by = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='permissions_updated_user',null=True, blank=True, on_delete=models.SET_NULL)
    deleted_by = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='permissions_deleted_user',null=True, blank=True, on_delete=models.SET_NULL) 
    created_at = models.DateTimeField(auto_now_add=True)  
    updated_at = models.DateTimeField(null=True, blank=True) 
    deleted_at = models.DateTimeField(null=True, blank=True)     
   
    # string representation of the class
    def __str__(self):
 
        #it will return the title
        return self.name
    
class Resource(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=500)
    description = models.CharField(max_length=1000)
    is_active = models.BooleanField(default=True) 
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='resources_created_user', null=True, blank=True, on_delete=models.SET_NULL)  
    updated_by = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='resources_updated_user',null=True, blank=True, on_delete=models.SET_NULL)
    deleted_by = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='resources_deleted_user',null=True, blank=True, on_delete=models.SET_NULL) 
    created_at = models.DateTimeField(auto_now_add=True)  
    updated_at = models.DateTimeField(null=True, blank=True) 
    deleted_at = models.DateTimeField(null=True, blank=True)     
   
    # string representation of the class
    def __str__(self):
 
        #it will return the title
        return self.name
    
class Resource_Permission(models.Model):
    id = models.AutoField(primary_key=True)    
    resource_id = models.ForeignKey(Resource, related_name='resource_id', null=True, blank=True, on_delete=models.SET_NULL)  
    permission_id = models.ForeignKey(Permission, related_name='permission_id', null=True, blank=True, on_delete=models.SET_NULL)  
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='resources_permissions_created_user', null=True, blank=True, on_delete=models.SET_NULL)  
    updated_by = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='resources_permissions_updated_user',null=True, blank=True, on_delete=models.SET_NULL)
    deleted_by = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='resources_permissions_deleted_user',null=True, blank=True, on_delete=models.SET_NULL) 
    created_at = models.DateTimeField(auto_now_add=True)  
    updated_at = models.DateTimeField(null=True, blank=True) 
    deleted_at = models.DateTimeField(null=True, blank=True)     
   
    # string representation of the class
    def __str__(self):
 
        #it will return the title
        return self.name

class Role_Resource_Permission(models.Model):
    id = models.AutoField(primary_key=True)    
    role_id = models.ForeignKey(Role, related_name='role_id', null=True, blank=True, on_delete=models.SET_NULL)  
    resource_id = models.ForeignKey(Resource, related_name='rrp_resource_id', null=True, blank=True, on_delete=models.SET_NULL)  
    permission_id = models.ForeignKey(Permission, related_name='rrp_permission_id', null=True, blank=True, on_delete=models.SET_NULL)  
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='rrp_created_user', null=True, blank=True, on_delete=models.SET_NULL)  
    updated_by = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='rrp_updated_user',null=True, blank=True, on_delete=models.SET_NULL)
    deleted_by = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='rrp_deleted_user',null=True, blank=True, on_delete=models.SET_NULL) 
    created_at = models.DateTimeField(auto_now_add=True)  
    updated_at = models.DateTimeField(null=True, blank=True) 
    deleted_at = models.DateTimeField(null=True, blank=True)     
   
    # string representation of the class
    def __str__(self):
 
        #it will return the title
        return self.name