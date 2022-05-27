from django.contrib import admin
from Dataviz.models import Student, Notes, Groupe, Matiere, MoyenneS1, MoyenneS2, FileModel, FilePV, Classe, Classe_Student, User


class UserAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'login', 'mot_de_passe']
    pass

admin.site.register(User, UserAdmin)
    
class FileModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'file_model']
    pass

admin.site.register(FileModel, FileModelAdmin)  

# class FileRattrapageAdmin(admin.ModelAdmin):
#     list_display = ['id', 'annee', 'date_save', 'file_rattrapage']
#     pass

# admin.site.register(FileRattrapage, FileRattrapageAdmin)

# class FileBilanAdmin(admin.ModelAdmin):
#     list_display = ['id', 'annee', 'date_save', 'file_bilan']
#     pass

# admin.site.register(FileBilan, FileBilanAdmin)
 
class FilePVAdmin(admin.ModelAdmin):
    list_display = ['id', 'file_pv']
    pass

admin.site.register(FilePV, FilePVAdmin) 

class Classe_StudentInline(admin.TabularInline):
    model = Classe_Student
    pass 

class MatiereInline(admin.TabularInline):
    model = Matiere
    pass

@admin.register(Classe)
class ClasseAdmin(admin.ModelAdmin):
    list_display = ['id', 'filiere', 'cycle', 'niveau']
    inlines = [Classe_StudentInline, MatiereInline]
    pass

class MoyenneS1Inline(admin.TabularInline):
    model = MoyenneS1
    pass

class MoyenneS2Inline(admin.TabularInline):
    model = MoyenneS2
    pass

class NotesInline(admin.TabularInline):
    model = Notes
    pass 

class StudentInline(admin.TabularInline):
    model = Student
    pass  

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'mot_de_passe']
    inlines = [MoyenneS1Inline, MoyenneS2Inline, NotesInline, Classe_StudentInline]
    pass

class Classe_StudentAdmin(admin.ModelAdmin):
    list_display = ['id', 'classe', 'annee', 'student']
    pass

admin.site.register(Classe_Student, Classe_StudentAdmin)    

class MoyenneS1Admin(admin.ModelAdmin):
    list_display = ['id', 'annee', 'moy_s1', 'mgp', 'credit', 'credit_total', 'student']
    pass

admin.site.register(MoyenneS1, MoyenneS1Admin)

class MoyenneS2Admin(admin.ModelAdmin):
    list_display = ['id', 'annee', 'moy_s2', 'mgp', 'credit', 'credit_total', 'student']
    pass

admin.site.register(MoyenneS2, MoyenneS2Admin)
    
@admin.register(Groupe)
class GroupeAdmin(admin.ModelAdmin):
    list_display = ['id', 'libelle']
    inlines = [MatiereInline]
    pass

class MatiereAdmin(admin.ModelAdmin):
    list_display = ['id', 'libelle', 'semestre', 'groupe', 'classe']
    inlines = [NotesInline]
    pass

admin.site.register(Matiere, MatiereAdmin)
    
class NotesAdmin(admin.ModelAdmin):
    list_display = ['id', 'note_cc', 'note_tp', 'note_sn', 'note_moy', 'credit', 'decision', 'student', 'matiere']
    pass

admin.site.register(Notes, NotesAdmin)
