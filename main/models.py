from django.db import models

class Categorie(models.Model):
   
    nom = models.CharField(max_length=100)
    type_diplome = models.CharField(max_length=100)

    def __str__(self):
        return self.nom
class Options(models.Model):
    nom = models.CharField(max_length=100)
   

    def __str__(self):
        return self.nom   

class Diplome(models.Model):
    nom = models.CharField(max_length=100)
    prix = models.IntegerField()
    categorie = models.ForeignKey(Categorie, on_delete=models.CASCADE)
    option = models.ForeignKey(Options, on_delete=models.CASCADE)
    

    def __str__(self):
        return self.nom

class Avis(models.Model):
    commenter_name = models.CharField(max_length=255)
    diploma_name = models.CharField(max_length=255)
    comment = models.TextField()
    stars = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.commenter_name

class Payment(models.Model):
    cardholder_name=models.CharField(max_length=255)
    card_number=models.IntegerField()
    expiry_date=models.DateField()
    diplome = models.ForeignKey(Diplome, on_delete=models.CASCADE)
    montant=models.IntegerField()
    cvv=models.IntegerField()
    def __str__(self):
        return self.cardholder_name
# Create your models here.
