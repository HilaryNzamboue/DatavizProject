import openpyxl as xl
from projet_test.settings import BASE_DIR
import os
from django.db.models import Q
import array as arr
from .models import Student, Notes, Groupe, Matiere, MoyenneS1, MoyenneS2, FileModel, FilePV, Classe, Classe_Student, User


#fonction qui retourne la liste des annees academiques
def get_annees():
    PV_all = Classe_Student.objects.all()
    annee = []
    for a in PV_all:
        if a.annee not in annee:
            annee.append(a.annee)

    return annee

#recherche d'une annee
def search_annees(item):
    PV_all = Classe_Student.objects.filter(annee=item)
    annee = []
    for a in PV_all:
        if a.annee not in annee:
            annee.append(a.annee)

    return annee



#fonction qui retourne la liste des pv
def Pv_list():
    PV_all = FilePV.objects.all()
   
    return PV_all    

#fonction qui retourne la liste des cycles
def Cycle_list():
    allCycle =Classe.objects.all()
    cycle=[]
    for c in allCycle:
        if c.cycle  not in cycle:
            cycle.append(c.cycle)
    return cycle

#le licence pro

def Cycle_Licence():
    allCycle =Classe.objects.filter(Q(cycle ='Licence Professionnelle') )
    cycles=[]
    for c in allCycle:
        if c.cycle  not in cycles:
            cycles.append(c.cycle)
    return cycles

#filiere cycle licence pro
    
def List_branche_licence(cyc):
    allBranche = Classe.objects.filter( Q(cycle=cyc))
    branche=[]
    for b in allBranche:
        if b.filiere not in branche:
            branche.append(b.filiere) 
    return branche  

#les niveaux de chaque cycle
def List_Niveaux(cyc):
    allNiveau = Classe.objects.filter(cycle=cyc)
    niveaux=[]
    for c in allNiveau:
        if c.niveau not in niveaux:
            niveaux.append(c.niveau) 
    return niveaux  

#les branches
def List_branches(niv,cyc):
    allBranche = Classe.objects.filter(Q(niveau=niv) & Q(cycle=cyc))
    branche=[]
    for b in allBranche:
        if b.filiere not in branche:
            branche.append(b.filiere) 
    return branche  

def list_file_pv():             
    PV_rattrapage = FileRattrapage.objects.all()
   
    return PV_rattrapage 


def Plus_grande_annee():
    allClasse=Classe_Student.objects.all()
    annee=[]
    listSplit=[]
    anneeList=[]
    maxAnnee=None
    for a in allClasse:
        if a.annee not in anneeList:
            anneeList.append(a.annee)
    anneeList=anneeList

    for n in anneeList:
        n = n.split('-')
        listSplit.append(n)
    ls=listSplit  

    for l in ls:
        for m in l:
            if m not in annee:
                an=int(m)
                annee.append(an)
     
    annee = annee    
    for a in annee:
        if (maxAnnee is None or a > maxAnnee ):
            maxAnnee = a 
    inf=maxAnnee-1
    sup=maxAnnee
    infStr=str(inf)
    supStr=str(sup)
    maxAnnee=infStr+'-'+supStr   
    # print(maxAnnee)       
    return (maxAnnee)    

def All_Students_ISJ():
    allStudents=Classe_Student.objects.filter(annee=maxAnnee)
    student_list=[]
    for s in allStudents:
        if s.id not in student_list:
            student_list.append(s.student.id)

    return student_list    

def MGP_students_semestre1(student_list, maxAnnee):
    students = student_list
    moy_S1=MoyenneS1.objects.filter(annee = maxAnnee)
    mgpEtu={}
    liste1=[]
    # moy_S2=MoyenneS2.objects.all(annee=maxAnnee) 

    for s in students:      
        for mS1 in moy_S1:
            if s==mS1.student.id:
                mgpEtu={'idStudent': mS1.student.id, 'MGP': mS1.mgp}
                liste1.append(mgpEtu) 
    # print(liste1)
    return liste1

def  MGP_students_semestre2(student_list, maxAnnee):
    students = student_list
    moy_S2=MoyenneS2.objects.filter(annee=maxAnnee) 
    mgpEtu={}
    liste2=[]
    for s in students:      
        for mS2 in moy_S2:
            if s==mS2.student.id:
                mgpEtu={'idStudent': mS2.student.id, 'MGP':mS2.mgp} 
                liste2.append(mgpEtu)
    return liste2    

def  MGP_annuel_students(liste1,liste2):
    mgpAnuel={}
    liste=[]
    # print(liste1)
    for l1 in liste1:
        for l2 in liste2:
            if l1.get('idStudent')==l2.get('idStudent'):
                mgpAnuel={'idStudent':l1.get('idStudent'), 'MGP': (l1.get('MGP') + l2.get('MGP'))/2} 
                liste.append(mgpAnuel)
    # print(liste)               
    return liste

def Taux_reussite_ISJ(liste,liste1):
    mgp=[]
    for l in liste:
        if l.get('MGP') >= 2:
            mgp.append(l.get('MGP'))
    listemgp=mgp
    # print(listemgp)
    n=len(liste1)
    somme=sum(listemgp)
    taux=(somme/n)*100
    return taux

####### Calcul du taux de reussite d'une classe

##liste des etudiants d'une classe
def all_students_classe(clas , an,):
    all_students=Classe_Student.objects.filter(Q(classe=clas) & Q(annee=an))
    student_list_classe=[]
    for s in all_students:
        if s.id not in student_list_classe:
            student_list_classe.append(s.student.id)

    return student_list_classe   

#mgp du semestre 1 des etudiants d'une classe

def MGP_students_semestre1_classe(student_list_classe, an):
    students = student_list_classe
    moy_S1=MoyenneS1.objects.filter(annee = an)
    mgpEtu={}
    liste1=[]

    for s in students:      
        for mS1 in moy_S1:
            if s==mS1.student.id:
                mgpEtu={'idStudent': mS1.student.id, 'MGP': mS1.mgp}
                liste1.append(mgpEtu) 
    # print(liste1)
    return liste1

#mgp du semestre 2 des etudiants d'une classe   
def  MGP_students_semestre2_classe(student_list_classe, an):
    students = student_list_classe
    moy_S2=MoyenneS2.objects.filter(annee=an) 
    mgpEtu={}
    liste2=[]
    for s in students:      
        for mS2 in moy_S2:
            if s==mS2.student.id:
                mgpEtu={'idStudent': mS2.student.id, 'MGP':mS2.mgp} 
                liste2.append(mgpEtu)
    print(liste2)            
    return liste2      

##Taux de reussite semestre 1
def Taux_reussitte_semestre1(liste1):
    mgp=[]
    somme=0
    for l in liste1:
        if l.get('MGP')>=2:
            somme=somme+1
            # mgp.append(l.get('MGP'))
    
    n=len(liste1) 
    print(n)
    taux=(somme/n)*100 
    taux_R_S1=round(taux,2)
    return taux_R_S1      


##Taux de reussite semestre 2
def Taux_reussitte_semestre2(liste2):
    mgp=[]
    somme=0
    for l in liste2:
        if l.get('MGP')>=2:
            somme=somme+1
            # mgp.append(l.get('MGP'))
    
    n=len(liste2) 
    print(n)
    taux=(somme/n)*100 
    taux_R_S2=round(taux,2)
    return taux_R_S2           

  

##Mgp annuel des etudiants d'une classe
def  MGP_annuel_students_classe(liste1,liste2):
    mgpAnuel={}
    liste=[]
    # print(liste1)
    for l1 in liste1:
        for l2 in liste2:
            if l1.get('idStudent')==l2.get('idStudent'):
                mgpAnuel={'idStudent':l1.get('idStudent'), 'MGP': (l1.get('MGP') + l2.get('MGP'))/2} 
                liste.append(mgpAnuel)
    # print(liste)               
    return liste

#taux de reussite des etudianta d'une classe
def Taux_reussite_classe(liste,liste1):
    mgp=[]
    for l in liste:
        if l.get('MGP') >= 2:
            mgp.append(l.get('MGP'))
    listemgp=mgp
    print(listemgp)
    n=len(liste1)
    somme=sum(listemgp)
    taux=(somme/n)*100
    return taux    







