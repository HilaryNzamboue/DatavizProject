from django.db import models
from django.db.models.deletion import CASCADE, SET_NULL
import uuid
from django.utils.translation import gettext_lazy as _
from django.utils import timezone


class User(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    name = models.CharField(max_length=200, null = True)
    login = models.CharField(max_length=200, null = True)
    mot_de_passe = models.CharField(max_length=10, null = True)
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
       """Returns the url to access a particular instance of the model."""
       return reverse('model-detail-view', args=[str(self.id)])

class Classe(models.Model):
    id = models.CharField(primary_key=True, max_length=200, null = False)
    filiere = models.CharField(max_length=100, null = True)
    cycle = models.CharField(max_length=100, null = True)
    niveau = models.CharField(max_length=10, null = True)
    
    def __str__(self):
        return str(self.filiere)
    
    def get_absolute_url(self):
       """Returns the url to access a particular instance of the model."""
       return reverse('model-detail-view', args=[str(self.filiere)])
  
class Classe_Student(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    classe = models.ForeignKey("Classe", on_delete=CASCADE)
    annee = models.CharField(max_length=100, null = True)
    student = models.ForeignKey("Student", on_delete=CASCADE)
    
    def __str__(self):
        return str(self.student)+str(self.classe)

class Student(models.Model):
    # matricule - id
    id = models.CharField(primary_key=True, max_length=200, null = False) 
    name = models.CharField(max_length=200, null = True)
    mot_de_passe = models.CharField(max_length=10, null = True)
    classe = models.ManyToManyField(Classe, through='Classe_Student')
       
    def __str__(self):
        return str(self.name)
   
    def get_absolute_url(self):
       """Returns the url to access a particular instance of the model."""
       return reverse('model-detail-view', args=[str(self.name)])  

class Groupe (models.Model):
    id = models.CharField(primary_key=True, max_length=200, null = False)
    libelle = models.CharField(max_length=200, null = True)
    
    def __str__(self):
        return self.libelle
    
    def get_absolute_url(self):
       """Returns the url to access a particular instance of the model."""
       return reverse('model-detail-view', args=[str(self.id)])

class Matiere (models.Model):
    # libelle - id
    id = models.CharField(primary_key=True, max_length=200, null = False)
    libelle = models.CharField(max_length=200, null = True)
    semestre = models.CharField(max_length=200, null = True)
    groupe = models.ForeignKey("Groupe", on_delete=CASCADE)
    classe = models.ForeignKey("Classe", on_delete=CASCADE, null = True)
    
    def __str__(self):
        return self.libelle
    
    def get_absolute_url(self):
       """Returns the url to access a particular instance of the model."""
       return reverse('model-detail-view', args=[str(self.id)])

class Notes (models.Model):
    id = models.CharField(primary_key=True, max_length=200, null = False)
    note_cc = models.FloatField(max_length=200, default = 0.0)
    note_tp = models.FloatField(max_length=200, default = 0.0)
    note_sn = models.FloatField(max_length=200, default = 0.0)
    note_moy = models.FloatField(max_length=200, default = 0.0)
    credit = models.FloatField(max_length=200, default = 0.0)
    decision = models.CharField(max_length=5, null = True)
    student = models.ForeignKey("Student", on_delete=CASCADE, null = True)
    matiere = models.ForeignKey("Matiere", on_delete=CASCADE, null = True)
     
    def __str__(self):
        return self.student.name
     
    def get_absolute_url(self):
       """Returns the url to access a particular instance of the model."""
       return reverse('model-detail-view', args=[str(self.id)])
   
class MoyenneS1 (models.Model):
    id = models.CharField(primary_key=True, max_length=200, null = False)
    annee = models.CharField(max_length=10, null = True)
    moy_s1 = models.FloatField(max_length=200, default = 0.0)
    mgp = models.FloatField(max_length=200, default = 0.0)
    credit = models.FloatField(max_length=200, default = 0.0)
    credit_total = models.FloatField(max_length=200, default = 0.0)
    student = models.ForeignKey("Student", on_delete=CASCADE, null = True)
    
    def __str__(self):
        return self.annee
    
    def get_absolute_url(self):
       """Returns the url to access a particular instance of the model."""
       return reverse('model-detail-view', args=[str(self.id)])

class MoyenneS2 (models.Model):
    id = models.CharField(primary_key=True, max_length=200, null = False)
    annee = models.CharField(max_length=10, null = True)
    moy_s2 = models.FloatField(max_length=200, default = 0.0)
    mgp = models.FloatField(max_length=200, default = 0.0)
    credit = models.FloatField(max_length=200, default = 0.0)
    credit_total = models.FloatField(max_length=200, default = 0.0)
    student = models.ForeignKey("Student", on_delete=CASCADE, null = True)
    
    def __str__(self):
        return self.annee
    
    def get_absolute_url(self):
       """Returns the url to access a particular instance of the model."""
       return reverse('model-detail-view', args=[str(self.id)])

class FileModel (models.Model):
    id = models.CharField(primary_key=True, max_length=200, null = False)
    name = models.CharField(max_length=200, null = True)
    file_model = models.FileField(upload_to= 'media/', max_length=200)
    
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
       """Returns the url to access a particular instance of the model."""
       return reverse('model-detail-view', args=[str(self.id)])
   
class FilePV (models.Model):
    id = models.CharField(primary_key=True, max_length=200, null = False)
    file_pv = models.FileField(upload_to= 'media/', max_length=200)
    
    def __str__(self):
        return self.id
    
    def get_absolute_url(self):
       """Returns the url to access a particular instance of the model."""
       return reverse('model-detail-view', args=[str(self.id)])
   
# class FileRattrapage (models.Model):
#     id = models.CharField(primary_key=True, max_length=200, null = False)
#     annee = models.CharField(max_length=200, null = True)
#     date_save = models.DateTimeField(auto_now_add=True)
#     file_rattrapage = models.FileField(upload_to= 'media/', max_length=200)
    
#     def __str__(self):
#         return self.id
    
#     def get_absolute_url(self):
#        """Returns the url to access a particular instance of the model."""
#        return reverse('model-detail-view', args=[str(self.id)])

# class FileBilan (models.Model):
#     id = models.CharField(primary_key=True, max_length=200, null = False)
#     annee = models.CharField(max_length=200, null = True)
#     date_save = models.DateTimeField(auto_now_add=True)
#     file_bilan = models.FileField(upload_to= 'media/', max_length=200)
    
#     def __str__(self):
#         return self.id
    
#     def get_absolute_url(self):
#        """Returns the url to access a particular instance of the model."""
#        return reverse('model-detail-view', args=[str(self.id)])
