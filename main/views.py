from django.shortcuts import render, redirect
from main.models import Categorie, Diplome,Options,Avis,Payment
from django.dispatch import receiver
from openpyxl import Workbook
import os
def index(request):
    categorie_genie_informatique = Categorie.objects.filter(nom='Diplôme Informatique').first()
    categorie_telecom = Categorie.objects.filter(nom='Diplôme Telecommunication').first()
    categorie_tous = Categorie.objects.filter(nom='Tous Les Diplômes').first()
    categorie_evaluer = Categorie.objects.filter(nom='Evaluer Votre Cv').first()
    somme_diplomes = Diplome.objects.filter(categorie=categorie_genie_informatique).count()
    somme_diplomes_telecom = Diplome.objects.filter(categorie=categorie_telecom).count()
    somme_diplomes_tous = Diplome.objects.all().count()
    aviss = Avis.objects.all()
    context = {
        'categorie_genie_informatique': categorie_genie_informatique,
        'categorie_telecom': categorie_telecom,
        'categorie_tous': categorie_tous,
        'categorie_evaluer': categorie_evaluer,
        'somme_diplomes': somme_diplomes,
        'somme_diplomes_telecom':somme_diplomes_telecom,
        'somme_diplomes_tous':somme_diplomes_tous,
        'aviss':aviss,
    }
    
    return render(request, 'index.html', context)


  
def courses(request, categorie):
    diplomes = Diplome.objects.filter(categorie__nom=categorie)
    option_ids = diplomes.values_list('option_id', flat=True).distinct()
    options = Options.objects.filter(id__in=option_ids)
    return render(request, 'courses.html', {'diplomes': diplomes, 'options': options, 'categorie': categorie})
def diplomes_details(request, id):
    diplome = Diplome.objects.filter(id=id).first()
    return render(request, 'diplome_details.html', {'diplome': diplome})
def save_avis(request):
    if request.method == 'POST':
        commenter_name = request.POST.get('commenter_name')
        diploma_name = request.POST.get('diploma_name')
        comment = request.POST.get('comment')
        stars=request.POST.get('rating')
       

        avis = Avis(commenter_name=commenter_name, diploma_name=diploma_name, comment=comment,stars=stars)
        avis.save()

        return redirect('main:cursuscv')
def save_Payment(request):
    if request.method == 'POST':
        cardholder_name = request.POST.get('cardholderName') 
        card_number = request.POST.get('cardNumber')
        expiry_date = request.POST.get('expiryDate')
        cvv = request.POST.get('cvv')
        montant = request.POST.get('montantDiplome')
       
        diplome=Diplome.objects.filter(id=request.POST.get('nomDiplome')).first()
        payment = Payment(cardholder_name=cardholder_name,card_number=card_number,expiry_date=expiry_date,cvv=cvv,montant=montant,diplome=diplome)
        payment.save()

        return redirect('main:cursus')
def cursus(request):
    return render(request, 'cursus.html')
def cv(request):
    return render(request, 'cv.html')
def chat(request):
    return render(request, 'chat.html')
def cursuscv(request):
    return render(request, 'cursuscv.html')

# Create your views here.
