from django.db import models

# Create your models here.
class Candidate(models.Model):
    name = models.CharField(max_length=30)
    designation = models.CharField(max_length=30)
    description = models.TextField()
    profile_pic = models.ImageField("Add your professional pic", upload_to='Images/',)
    location = models.CharField(max_length=30)
    phone = models.IntegerField()
    maidId = models.EmailField(unique=True)
    total_exprience = models.IntegerField()
    isActive = models.BooleanField(default=True)
    isDelete = models.BooleanField(default=False)
    CREATED_BY = models.IntegerField()
    CREATE_DATETIME = models.DateTimeField(auto_now=True)
    UPDATED_BY = models.IntegerField()
    UPDATE_DATETIME = models.DateTimeField(auto_now=True)
    
    def __str__(self) -> str:
        return self.name
    
class Technology(models.Model):
    name = models.CharField(max_length=50)
    isActive = models.BooleanField(default=True)
    isDelete = models.BooleanField(default=False)
    CREATED_BY = models.IntegerField()
    CREATE_DATETIME = models.DateTimeField(auto_now=True)
    UPDATED_BY = models.IntegerField()
    UPDATE_DATETIME = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.name
    
class ContactForm(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField(unique=True)
    phone = models.IntegerField()
    title = models.CharField(max_length=30)
    message = models.TextField()
    isActive = models.BooleanField(default=True)
    isDelete = models.BooleanField(default=False)
    CREATED_BY = models.IntegerField()
    CREATE_DATETIME = models.DateTimeField(auto_now=True)
    UPDATED_BY = models.IntegerField()
    UPDATE_DATETIME = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.name

class Company(models.Model):
    name = models.CharField(max_length=30)
    location = models.CharField(max_length=30)
    isActive = models.BooleanField(default=True)
    isDelete = models.BooleanField(default=False)
    CREATED_BY = models.IntegerField()
    CREATE_DATETIME = models.DateTimeField(auto_now=True)
    UPDATED_BY = models.IntegerField()
    UPDATE_DATETIME = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.name
    
class CandidateSkill(models.Model):
    candidateId = models.ForeignKey(Candidate, on_delete=models.CASCADE)
    technologyId = models.ForeignKey(Technology, on_delete=models.CASCADE)
    total_techno_exprience = models.IntegerField()
    isActive = models.BooleanField(default=True)
    isDelete = models.BooleanField(default=False)
    CREATED_BY = models.IntegerField()
    CREATE_DATETIME = models.DateTimeField(auto_now=True)
    UPDATED_BY = models.IntegerField()
    UPDATE_DATETIME = models.DateTimeField(auto_now=True)
    
class EducationDetails(models.Model):
    candidateId = models.ForeignKey(Candidate, on_delete=models.CASCADE)
    degree = models.CharField(max_length=30)
    collegeName = models.TextField()
    univerciyName = models.TextField()
    passoutYear = models.IntegerField()
    percentage = models.IntegerField()
    isActive = models.BooleanField(default=True)
    isDelete = models.BooleanField(default=False)
    CREATED_BY = models.IntegerField()
    CREATE_DATETIME = models.DateTimeField(auto_now=True)
    UPDATED_BY = models.IntegerField()
    UPDATE_DATETIME = models.DateTimeField(auto_now=True)
    
    def __str__(self) -> str:
        return self.degree
    
class Exprience(models.Model):
    candidateId = models.ForeignKey(Candidate, on_delete=models.CASCADE)
    companyId = models.ForeignKey(Company, on_delete=models.CASCADE)
    technologyId = models.ForeignKey(Technology, on_delete=models.CASCADE)
    no_of_years = models.IntegerField()
    total_exprience = models.IntegerField()
    work_description = models.TextField()
    isActive = models.BooleanField(default=True)
    isDelete = models.BooleanField(default=False)
    CREATED_BY = models.IntegerField()
    CREATE_DATETIME = models.DateTimeField(auto_now=True)
    UPDATED_BY = models.IntegerField()
    UPDATE_DATETIME = models.DateTimeField(auto_now=True)

