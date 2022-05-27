from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Student, Notes, Groupe, Matiere, MoyenneS1, MoyenneS2, FileModel, FilePV, Classe, Classe_Student
from django.contrib.auth.mixins import PermissionRequiredMixin
from Dataviz.services import *
from Dataviz.fonctions import *
from Dataviz.feature import *
from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponseRedirect
from django.urls import reverse
import re
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User


def signin(request):
    if request.method == "POST":
        username = request.POST['username']
        password=request.POST['password']
        # user=authenticate(request,login=username,mot_de_passe=password)
        # user = User.objects.get(login=username, mot_de_passe=password)
        global user
        user = authenticate(username=username, password=password)
        my_user = User.objects.get(username=username)
        if user is not None:
            login(request, user)
            firstname = user.first_name
            liste =  get_annees() 
            listePv =  Pv_list()
            menu_deroulant= ["SEMESTRE 1", "SEMESTRE 2", "BILAN ANNUEL", "BILAN DE CYCLE","STATISTIQUES"] 
            context = {
              'annee' : liste,
              'pv' : listePv,
              'menu' : menu_deroulant,
              'name': firstname
            }
            return render(request,'index.html', context)

            # return HttpResponseRedirect(reverse('index'), {'name': user.name})
            # return HttpResponseRedirect(reverse('index'))
            # return render(request,'index.html', {'name': user.name})
        else:
            return render(request,'pages/samples/login.html',{
                "message":"Identifiant ou Mot de passe incorrect"
            })
    return render(request,'pages/samples/login.html')


def signout(request):
    logout(request)
    user = ""
    # messages.success(request, 'logout successfully!')
    # return redirect('home')
    # user = ""
    return render(request,'pages/samples/login.html',{
        'message':"logout successfully!"
    })


##rechercher une annee
@login_required(login_url='/templates/pages/samples/login.html')
def  search(request):

    if request.method == "GET":
        name = request.GET.get('recherche') 
        
        if name is not None : 
            annee=search_annees(name)
            print(annee)
    liste =  annee
    # print(liste)
    firstname = user.first_name
    listePv =  Pv_list()
    menu_deroulant= ["SEMESTRE 1", "SEMESTRE 2", "BILAN ANNUEL", "BILAN DE CYCLE","STATISTIQUES"] 
    context = {
        'annee' : liste,
        'pv' : listePv,
        'menu' : menu_deroulant,
        'name': firstname
        }        
    return render(request, 'index.html', context)   

#accueil
@login_required
def accueil(request):
    firstname = user.first_name
    liste =  get_annees() 
    listePv =  Pv_list()
    menu_deroulant= ["SEMESTRE 1", "SEMESTRE 2", "BILAN ANNUEL", "BILAN DE CYCLE","STATISTIQUES"] 
    context = {
        'annee' : liste,
        'pv' : listePv,
        'menu' : menu_deroulant,
        'name': firstname
     }
    return render(request,'index.html', context)

@login_required(login_url='/templates/pages/samples/login.html')
def Bilan_Classe(request):
    # sem = "SEMESTRE 1"
    clas = Classe.objects.get(niveau = 1)
    annee = "2019/2020"
    bilan_classe(clas, annee)
    # return render(request,'home.html', {'students': liste}) 

@login_required(login_url='/templates/pages/samples/login.html')
def bilantest(request):
    
    nombre_objects = MoyenneS1.objects.count()
    
    print(type(nombre_objects))
    
    return render(request,'home.html') 

@login_required(login_url='/templates/pages/samples/login.html')
def export_bilan_cycle(request,an,cyc,niv,bch):
    # student_list=All_Students_ISJ()
    # liste1=MGP_students_semestre1(student_list)
    # testSplit()
    classe = Classe.objects.get(Q(cycle=cyc) & Q(niveau=niv) & Q(filiere=bch))
    # niveau_cycle(classe)
    annee = an
    # bilan_cycle(classe, annee)
    retour = bilan_cycle(classe, an)
    
    return generate_excel(retour.get("url"), retour.get("name"))
    # return render(request,'home.html')    

@login_required(login_url='/templates/pages/samples/login.html')
def export_bilan_annuel(request, an, semest, cyc, niv, bch):
    
    classe = Classe.objects.get(Q(cycle=cyc) & Q(niveau=niv) & Q(filiere=bch))
    annee = an
    # semestre = "SEMESTRE 1"
    # excel_bilan_annuel_classe(classe, annee)
    # test = rattrapages_list(classe, semestre, annee)
    # test = excel_bilan_annuel_classe(classe, annee)
    # print(test)
    # url_name = ecriture_excel_rattrapage(test, semestre, classe, annee)
    url_name = excel_bilan_annuel_classe(classe, annee)
    print(url_name.get("url"), url_name.get("name"))
    
    return generate_excel(url_name.get("url"), url_name.get("name"))

@login_required(login_url='/templates/pages/samples/login.html')
def export_rattrapages(request, an, semest, cyc, niv, bch):
    
    classe = Classe.objects.get(Q(cycle=cyc) & Q(niveau=niv) & Q(filiere=bch))
    annee = an
    semestre = semest
    liste_rattrapages = rattrapages_list(classe, semestre, annee)
    
    url_name = excel_rattrapage(liste_rattrapages, semestre, classe, annee)
    
    url_name = excel_rattrapage(liste_rattrapages, semest, classe, an)

    return generate_excel(url_name.get("url"), url_name.get("name"))
  

    
#Chargement et lecture d'un procès verbal   
@login_required(login_url='/templates/pages/samples/login.html')
def Form_Pv(request):
    if request.method == 'POST':
        file_pvform = request.FILES['file_pv']
        print (type(file_pvform))
        file_pvform_str = str(file_pvform)
        print(file_pvform)
        patterns_synthese = '^(PV-)([áàâäãåçéèéèêëíìîïñóòôöõúùûüýÿæœÁÀÂÄÃÅÇÉÈÊËÍÌÎÏÑÓÒÔÖÕÚÙÛÜÝŸÆŒ\’\'\w.\s-]+)(synthese.xlsx)$'
        patterns_rattrapages = '^(PV-)([áàâäãåçéèéèêëíìîïñóòôöõúùûüýÿæœÁÀÂÄÃÅÇÉÈÊËÍÌÎÏÑÓÒÔÖÕÚÙÛÜÝŸÆŒ\’\'\w.\s-]+)(rattrapages.xlsx)$'
        
        if re.search(patterns_synthese,  file_pvform_str):
            print ('Correct!')
            form = FilePV(id = file_pvform, file_pv = file_pvform)
            form.save()
            file_url = form.file_pv
            # print(file_url.url)
            lire_Groupes(file_url.url)
            lire_Matieres(file_url.url)
            lire_student(file_url.url)
            lire_Notes(file_url.url)
            lire_Moy(file_url.url)
        elif re.search(patterns_rattrapages,  file_pvform_str):
            print ('Correct!')
            form = FilePV(id = file_pvform, file_pv = file_pvform)
            form.save()
            file_url = form.file_pv
            # print(file_url.url)
            lire_Groupes(file_url.url)
            lire_Matieres(file_url.url)
            lire_student(file_url.url)
            lire_Notes(file_url.url)
            lire_Moy(file_url.url)
        else:
            print('Incorrect!')
            firstname = user.first_name
            liste =  get_annees() 
            listePv =  Pv_list()
            menu_deroulant= ["SEMESTRE 1", "SEMESTRE 2", "BILAN ANNUEL", "BILAN DE CYCLE","STATISTIQUES"] 
            context = {
                'annee' : liste,
                'pv' : listePv,
                'menu' : menu_deroulant,
                'messages':"Veuillez importez un PV valide !!!",
                'name': firstname
                
            }    
            return render(request,"index.html",context)
    else:
        return render(request,"index.html",{
                "message":"Invalid Credentials"
            })
    liste =  get_annees() 
    listePv =  Pv_list()
    firstname = user.first_name
    menu_deroulant= ["SEMESTRE 1", "SEMESTRE 2", "BILAN ANNUEL", "BILAN DE CYCLE","STATISTIQUES"] 
    context = {
        'annee' : liste,
        'pv' : listePv,
        'menu' : menu_deroulant,
        'name': firstname,
        'messagesSucces':"PV importé avec succes !!!"
        
    }        
    return render(request, 'index.html',context)  

#Passer le semestre et l'annee en parametre
@login_required(login_url='/templates/pages/samples/login.html')
def BilanSemestriel(request, an, semest):
    liste = get_annees()
    firstname = user.first_name
    cycle = Cycle_list()
    menu_deroulant= ["SEMESTRE 1", "SEMESTRE 2", "BILAN ANNUEL", "BILAN DE CYCLE","STATISTIQUES"] 
    semestre = ["SEMESTRE 1", "SEMESTRE 2","BILAN ANNUEL","STATISTIQUES"] 
    # semest = semest
    context = {
        'an': an,
        'semest' : semest,
        'annee' : liste,
        'menu' : menu_deroulant,
        'cycle': cycle,
        'sem': semestre,
        'name': firstname

    }
    
    return render(request, 'pages/vues/bilan-semestriel.html', context)  

#les niveaux de chaque cycle
@login_required(login_url='/templates/pages/samples/login.html')
def ListeNiveaux(request, an, semest, cyc):
    liste = get_annees()
    tronc_commun = ["1","2"]
    specialisation= ["3","4","5"]
    menu_deroulant= ["SEMESTRE 1", "SEMESTRE 2", "BILAN ANNUEL", "BILAN DE CYCLE","STATISTIQUES"] 
    statistiques = ["Rattrapages", "Bilans"]
    # listeM = List_Matieres()
    niveau=List_Niveaux(cyc)
    cycle_licence=Cycle_Licence()
    branche=List_branche_licence(cyc)
    bilanAnnuel=["BILAN ANNUEL"]
    bilanCycle=["BILAN DE CYCLE"]
    statistique=["STATISTIQUES"]
    semestre = ["SEMESTRE 1", "SEMESTRE 2"]
    firstname = user.first_name



    context = {
        'an' : an,
        'semest': semest,
        'cyc' : cyc,
        'statistiques':statistiques,
        'menu' : menu_deroulant,
        'annee' : liste,
        'tc': tronc_commun,
        'spc': specialisation,
        # 'matieres': listeM,
        'niveau':niveau,
        'cycleLicence':cycle_licence,
        'branche': branche,
        'statist': statistique,
        'bl':bilanAnnuel,
        'sem': semestre,
        'bc': bilanCycle,
        'name': firstname
  
    }
    return render(request, 'pages/vues/classes.html', context)  


#liste rattrapages
@login_required(login_url='/templates/pages/samples/login.html')
def ListeRattrapages(request, an, semest, cyc, niv, stat):
    menu_deroulant= ["SEMESTRE 1", "SEMESTRE 2", "BILAN ANNUEL", "BILAN DE CYCLE","STATISTIQUES"] 
    tronc_commun = ["1","2"]
    specialisation= ["3","4","5"]
    # matiere= List_Matieres()
    statistiques = ["Rattrapages", "Bilans"]
    liste = get_annees()
    firstname = user.first_name

    context={
        'an' : an,
        'semest': semest,
        'cyc' : cyc,
        'niv': niv,
        'annee' : liste,
        'stat': stat,
        'menu' : menu_deroulant,
        'tc': tronc_commun,
        'spc': specialisation,
        'name': firstname
        # 'matieres':matiere,

    }

    return render(request, 'pages/vues/rattrapages.html', context )


@login_required(login_url='/templates/pages/samples/login.html')
def FilieresCycle(request, an, semest, cyc, niv) :      
    liste = get_annees()
    menu_deroulant= ["SEMESTRE 1", "SEMESTRE 2", "BILAN ANNUEL", "BILAN DE CYCLE","STATISTIQUES"] 
    semestre = ["SEMESTRE 1", "SEMESTRE 2"]
    semestre_bilan = ["SEMESTRE 1", "SEMESTRE 2","BILAN ANNUEL","STATISTIQUES"]
    bilan=["BILAN ANNUEL"]
    bilanCycle=["BILAN DE CYCLE"]
    bilanAnnuel=["BILAN ANNUEL"]
    statistique=["STATISTIQUES"]
    branche=List_branches(niv,cyc)
    rattrapage_bilan = ["Rattrapages", "Bilans"]
    firstname = user.first_name
  
    context={
        'an' : an,
        'semest': semest,
        'cyc' : cyc,
        'niv': niv,
        'menu' : menu_deroulant,
        'sem': semestre,
        'sb':semestre_bilan,
        'bil': bilan,
        'annee' : liste,
        'branche': branche,
        'rb': rattrapage_bilan ,
        'statist': statistique,
        'bl':bilanAnnuel,
        'bc': bilanCycle,
        'name': firstname
    }
    return render(request, 'pages/vues/classeBranche.html', context )


@login_required(login_url='/templates/pages/samples/login.html')
def ListeRattrapagesBranche(request, an, semest, cyc, niv, bch, stat):
    liste = get_annees()
    menu_deroulant= ["SEMESTRE 1", "SEMESTRE 2", "BILAN ANNUEL", "BILAN DE CYCLE","STATISTIQUES"] 
    branche=List_branches(niv,cyc)
    rattrapage = ["Rattrapages"]
    bilanAnnuel=["Bilans"]
    statistiques=["Statistiques"]
    bilanCycle=["BilansCycle"]
    classe = Classe.objects.get(Q(cycle = cyc) & Q(filiere=bch) & Q(niveau=niv))
    liste_rattrapages = rattrapages_list(classe, semest, an)
    n=len(liste_rattrapages)
    ana = Plus_grande_annee()
    listechiffre=50
    liste_students_bilan = Students_Classe(classe,an)
    m=len(liste_students_bilan)
    #statistiques
    
    student_list_classe = all_students_classe(classe,an)
    #semestre1
    liste1=MGP_students_semestre1_classe(student_list_classe,an)
    taux_R_S1=Taux_reussitte_semestre1(liste1)
    t_E_S1=100-taux_R_S1
    taux_E_S1=round(t_E_S1,2)
    #Semestre 2
    liste2=MGP_students_semestre2_classe(student_list_classe,an)
    print(liste2)
    taux_R_S2=Taux_reussitte_semestre2(liste2)
    t_E_S2=100-taux_R_S2
    taux_E_S2=round(t_E_S2,2)
    #stat annuel d'une classe
    taux_R_A=(taux_R_S1+taux_R_S2)/2
    taux_E_A=(t_E_S1+t_E_S2)/2
    
    firstname = user.first_name


    context={
        'an' : an,
        'semest': semest,
        'cyc' : cyc,
        'niv': niv,
        'bch': bch,
        'stat':stat,
        'annee' : liste,
        'menu' : menu_deroulant,
        'branche': branche,
        'statistiques':statistiques,
        'rattrapage':rattrapage,
        'bilanAnnuel':bilanAnnuel,
        'liste_R':n,
        'ana':ana, 
        'totalVisitors':listechiffre,
        'liste_B': m,
        'bc': bilanCycle,
        'tRs1':taux_R_S1,
        'tRs2':taux_R_S2,
        'tEs1':taux_E_S1,
        'tEs2':taux_E_S2,
        'tRA': round(taux_R_A,2),
        'tEA':round(taux_E_A,2),
        'name': firstname


    }
  
    return render(request, 'pages/vues/rattrapageBranche.html', context)        
  

class ClasseCreate(PermissionRequiredMixin, CreateView):
    model = Classe
    fields = ['id', 'filiere', 'cycle', 'niveau']
    permission_required = 'dataviz.can_mark_returned'

class ClasseUpdate(PermissionRequiredMixin, UpdateView):
    model = Classe
    fields = ['id', 'filiere', 'cycle', 'niveau']
    permission_required = 'dataviz.can_mark_returned'

class ClasseDelete(PermissionRequiredMixin, DeleteView):
    model = Classe
    success_url = reverse_lazy('classes')
    permission_required = 'dataviz.can_mark_returned'
  

class StudentCreate(PermissionRequiredMixin, CreateView):
    model = Student
    fields = ['id', 'name', 'mot_de_passe']
    permission_required = 'dataviz.can_mark_returned'

class StudentUpdate(PermissionRequiredMixin, UpdateView):
    model = Student
    fields = ['id', 'name', 'mot_de_passe', 'classe']
    permission_required = 'dataviz.can_mark_returned'

class StudentDelete(PermissionRequiredMixin, DeleteView):
    model = Student
    success_url = reverse_lazy('students')
    permission_required = 'dataviz.can_mark_returned'
  

class Classe_StudentCreate(PermissionRequiredMixin, CreateView):
    model = Classe_Student
    fields = ['id','classe','annee', 'student']
    permission_required = 'dataviz.can_mark_returned'

class Classe_StudentUpdate(PermissionRequiredMixin, UpdateView):
    model = Classe_Student
    fields = ['id','classe','annee', 'student']
    permission_required = 'dataviz.can_mark_returned'

class Classe_StudentDelete(PermissionRequiredMixin, DeleteView):
    model = Classe_Student
    success_url = reverse_lazy('classe_student')
    permission_required = 'dataviz.can_mark_returned'


class NotesCreate(PermissionRequiredMixin, CreateView):
    model = Notes
    fields = ['id', 'note_cc', 'note_tp', 'note_sn', 'note_moy', 'credit', 'decision', 'student', 'matiere']
    permission_required = 'dataviz.can_mark_returned'
    
class NotesUpdate(PermissionRequiredMixin, UpdateView):
    model = Notes
    fields = ['id', 'note_cc', 'note_tp', 'note_sn', 'note_moy', 'credit', 'decision', 'student', 'matiere']
    permission_required = 'dataviz.can_mark_returned'

class NotesDelete(PermissionRequiredMixin, DeleteView):
    model = Notes
    success_url = reverse_lazy('notes')
    permission_required = 'dataviz.can_mark_returned'
    

class GroupeCreate(PermissionRequiredMixin, CreateView):
    model = Groupe
    fields = ['id', 'libelle']
    permission_required = 'dataviz.can_mark_returned'
    
class GroupeUpdate(PermissionRequiredMixin, UpdateView):
    model = Groupe
    fields = '__all__' # Not recommended (potential security issue if more fields added)
    permission_required = 'dataviz.can_mark_returned'

class GroupeDelete(PermissionRequiredMixin, DeleteView):
    model = Groupe
    success_url = reverse_lazy('groupes')
    permission_required = 'dataviz.can_mark_returned'
    

class MatiereCreate(PermissionRequiredMixin, CreateView):
    model = Matiere
    fields = ['id', 'libelle', 'semestre', 'groupe', 'classe']
    permission_required = 'dataviz.can_mark_returned'
    
class MatiereUpdate(PermissionRequiredMixin, UpdateView):
    model = Matiere
    fields = ['id', 'libelle', 'semestre', 'groupe', 'classe']
    permission_required = 'dataviz.can_mark_returned'

class MatiereDelete(PermissionRequiredMixin, DeleteView):
    model = Matiere
    success_url = reverse_lazy('matières')
    permission_required = 'dataviz.can_mark_returned'


class MoyenneS1Create(PermissionRequiredMixin, CreateView):
    model = MoyenneS1
    fields = ['id', 'annee', 'moy_s1', 'mgp', 'credit', 'credit_total', 'student']
    permission_required = 'dataviz.can_mark_returned'
    
class MoyenneS1Update(PermissionRequiredMixin, UpdateView):
    model = MoyenneS1
    fields = ['id', 'annee', 'moy_s1', 'mgp', 'credit', 'credit_total', 'student']
    permission_required = 'dataviz.can_mark_returned'

class MoyenneS1Delete(PermissionRequiredMixin, DeleteView):
    model = MoyenneS2
    success_url = reverse_lazy('moyennes1')
    permission_required = 'dataviz.can_mark_returned'


class MoyenneS2Create(PermissionRequiredMixin, CreateView):
    model = MoyenneS2
    fields = ['id', 'annee', 'moy_s2', 'mgp', 'credit', 'credit_total', 'student']
    permission_required = 'dataviz.can_mark_returned'
    
class MoyenneS2Update(PermissionRequiredMixin, UpdateView):
    model = MoyenneS2
    fields = ['id', 'annee', 'moy_s2', 'mgp', 'credit', 'credit_total', 'student']
    permission_required = 'dataviz.can_mark_returned'

class MoyenneS2Delete(PermissionRequiredMixin, DeleteView):
    model = MoyenneS2
    success_url = reverse_lazy('moyennes2')
    permission_required = 'dataviz.can_mark_returned'
    

class FileModelCreate(PermissionRequiredMixin, CreateView):
    model = FileModel
    fields = ['id', 'name', 'file_model']
    permission_required = 'dataviz.can_mark_returned'
    
class FileModelUpdate(PermissionRequiredMixin, UpdateView):
    model = FileModel
    fields = ['id', 'name', 'file_model']
    permission_required = 'dataviz.can_mark_returned'

class FileModelDelete(PermissionRequiredMixin, DeleteView):
    model = FileModel
    success_url = reverse_lazy('fileModel')
    permission_required = 'dataviz.can_mark_returned'    


# class FileRattrapageCreate(PermissionRequiredMixin, CreateView):
#     model = FileRattrapage
#     fields = ['id', 'annee', 'date_save', 'file_rattrapage']
#     permission_required = 'dataviz.can_mark_returned'
    
# class FileRattrapageUpdate(PermissionRequiredMixin, UpdateView):
#     model = FileRattrapage
#     fields = ['id', 'annee', 'date_save', 'file_Rattrapage']
#     permission_required = 'dataviz.can_mark_returned'

# class FileRattrapageDelete(PermissionRequiredMixin, DeleteView):
#     model = FileRattrapage
#     success_url = reverse_lazy('fileRattrapage')
#     permission_required = 'dataviz.can_mark_returned'    


class FilePVCreate(PermissionRequiredMixin, CreateView):
    model = FilePV
    fields = ['id', 'file_pv']
    permission_required = 'dataviz.can_mark_returned'
    
class FilePVUpdate(PermissionRequiredMixin, UpdateView):
    model = FilePV
    fields = ['id', 'file_pv']
    permission_required = 'dataviz.can_mark_returned'

class FilePVDelete(PermissionRequiredMixin, DeleteView):
    model = FilePV
    success_url = reverse_lazy('filePV')
    permission_required = 'dataviz.can_mark_returned' 
  
    
# class FileBilanCreate(PermissionRequiredMixin, CreateView):
#     model = FileBilan
#     fields = ['id', 'annee', 'date_save', 'file_bilan']
#     permission_required = 'dataviz.can_mark_returned'
    
# class FileBilanUpdate(PermissionRequiredMixin, UpdateView):
#     model = FileBilan
#     fields = ['id', 'annee', 'date_save', 'file_bilan']
#     permission_required = 'dataviz.can_mark_returned'

# class FileBilanDelete(PermissionRequiredMixin, DeleteView):
#     model = FileBilan
#     success_url = reverse_lazy('fileBilan')
#     permission_required = 'dataviz.can_mark_returned' 
    
class UserCreate(PermissionRequiredMixin, CreateView):
    model = User
    fields = ['id', 'name', 'login', 'mot_de_passe']
    permission_required = 'dataviz.can_mark_returned'
    
class UserUpdate(PermissionRequiredMixin, UpdateView):
    model = User
    fields = ['id', 'name', 'login', 'mot_de_passe']
    permission_required = 'dataviz.can_mark_returned'

class UserDelete(PermissionRequiredMixin, DeleteView):
    model = User
    success_url = reverse_lazy('user')
    permission_required = 'dataviz.can_mark_returned'
