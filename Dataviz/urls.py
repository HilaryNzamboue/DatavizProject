from django.urls import path

from django.contrib.auth.views import LoginView

from . import views

# include('django.contrib.auth.urls')

urlpatterns = [
    # path('', views = LoginView.as_p(template_name = "pages/samples/login.html"), name= 'login'),
    path('login/', views.signin, name= 'login'),
    path('logout/', views.signout, name= 'logout'),
    # path('rattrapages/', views.Rattrapages, name='rattrapages'),
    # path('form/', views.Form, name='form'),
    path('form/', views.Form_Pv, name='form'),
    path('accueil/', views.accueil, name='accueil'),
    path('search/', views.search, name='search'),
    path('bilan/', views.Bilan_Classe, name='bilan'),
    # path('home/', views.ListeAnnee, name='annee'),
    path('bilantest/', views.bilantest, name='bilantest'),
    path('export_bilan_cycle/<str:an>/<str:cyc>/<str:niv>/<str:bch>', views.export_bilan_cycle, name='export_bilan_cycle'),
    path('export_rattrapages/<str:an>/<str:semest>/<str:cyc>/<str:niv>/<str:bch>', views.export_rattrapages, name='export_rattrapages'),
    path('export_bilan_annuel/<str:an>/<str:semest>/<str:cyc>/<str:niv>/<str:bch>', views.export_bilan_annuel, name='export_bilan_annuel'),
    path('bilan-semestriel/<str:an>/<str:semest>', views.BilanSemestriel, name='annee'),
    path('bilan-semestriel/<str:an>/<str:semest>/<str:cyc>', views.ListeNiveaux, name='niveau'),
    path('bilan-semestriel/<str:an>/<str:semest>/<str:cyc>/<str:niv>/<str:stat>', views.ListeRattrapages, name='stat'),
    # path('bilan-semestriel/<str:an>/<str:semest>/<str:cyc>/<str:stat>', views.BilanCycle, name='cycle'),
    path('bilan-semestriel/<str:an>/<str:semest>/<str:cyc>/<str:niv>/<str:bch>/<str:stat>', views.ListeRattrapagesBranche, name='statbranche'),
    path('bilan-semestriel/<str:an>/<str:semest>/<str:cyc>/<str:niv>', views.FilieresCycle, name='filieres'),
]

# Add URLConf to create, update, and delete classe
urlpatterns += [
    path('classe_student/create/', views.Classe_StudentCreate.as_view(), name='classe_student-create'),
    path('classe_student/<int:pk>/update/', views.Classe_StudentUpdate.as_view(), name='classe_student-update'),
    path('classe_student/<int:pk>/delete/', views.Classe_StudentDelete.as_view(), name='classe_student-delete'),
]

# Add URLConf to create, update, and delete classe
urlpatterns += [
    path('classe/create/', views.ClasseCreate.as_view(), name='classe-create'),
    path('classe/<int:pk>/update/', views.ClasseUpdate.as_view(), name='classe-update'),
    path('classe/<int:pk>/delete/', views.ClasseDelete.as_view(), name='classe-delete'),
]

# Add URLConf to create, update, and delete students
urlpatterns += [
    path('student/create/', views.StudentCreate.as_view(), name='student-create'),
    path('student/<int:pk>/update/', views.StudentUpdate.as_view(), name='student-update'),
    path('student/<int:pk>/delete/', views.StudentDelete.as_view(), name='student-delete'),
]

# Add URLConf to create, update, and delete notes
urlpatterns += [
    path('notes/create/', views.NotesCreate.as_view(), name='notes-create'),
    path('notes/<int:pk>/update/', views.NotesUpdate.as_view(), name='notes-update'),
    path('notes/<int:pk>/delete/', views.NotesDelete.as_view(), name='notes-delete'),
]

# Add URLConf to create, update, and delete Groupe
urlpatterns += [
    path('groupe/create/', views.GroupeCreate.as_view(), name='groupe-create'),
    path('groupe/<int:pk>/update/', views.GroupeUpdate.as_view(), name='groupe-update'),
    path('groupe/<int:pk>/delete/', views.GroupeDelete.as_view(), name='groupe-delete'),
]

# Add URLConf to create, update, and delete matiere
urlpatterns += [
    path('matiere/create/', views.MatiereCreate.as_view(), name='matiere-create'),
    path('matiere/<int:pk>/update/', views.MatiereUpdate.as_view(), name='matiere-update'),
    path('matiere/<int:pk>/delete/', views.MatiereDelete.as_view(), name='matiere-delete'),
]

# Add URLConf to create, update, and delete FileModel
urlpatterns += [
    path('fileModel/create/', views.FileModelCreate.as_view(), name='fileModel-create'),
    path('fileModel/<int:pk>/update/', views.FileModelUpdate.as_view(), name='fileModel-update'),
    path('fileModel/<int:pk>/delete/', views.FileModelDelete.as_view(), name='fileModel-delete'),
]


# Add URLConf to create, update, and delete FilePV
urlpatterns += [
    path('filePV/create/', views.FilePVCreate.as_view(), name='filePV-create'),
    path('filePV/<int:pk>/update/', views.FilePVUpdate.as_view(), name='filePV-update'),
    path('filePV/<int:pk>/delete/', views.FilePVDelete.as_view(), name='filePV-delete'),
]

# Add URLConf to create, update, and delete moyenneS1
urlpatterns += [
    path('moyenneS1/create/', views.MoyenneS1Create.as_view(), name='moyenneS1-create'),
    path('moyenneS1/<int:pk>/update/', views.MoyenneS1Update.as_view(), name='moyenneS1-update'),
    path('moyenneS1/<int:pk>/delete/', views.MoyenneS1Delete.as_view(), name='moyenneS1-delete'),
]

# Add URLConf to create, update, and delete moyenneS2
urlpatterns += [
    path('moyenneS2/create/', views.MoyenneS2Create.as_view(), name='moyenneS2-create'),
    path('moyenneS2/<int:pk>/update/', views.MoyenneS2Update.as_view(), name='moyenneS2-update'),
    path('moyenneS2/<int:pk>/delete/', views.MoyenneS2Delete.as_view(), name='moyenneS2-delete'),
]

# # Add URLConf to create, update, and delete fileRattrapage
# urlpatterns += [
#     path('fileRattrapage/create/', views.FileRattrapageCreate.as_view(), name='fileRattrapage-create'),
#     path('fileRattrapage/<int:pk>/update/', views.FileRattrapageUpdate.as_view(), name='fileRattrapage-update'),
#     path('fileRattrapage/<int:pk>/delete/', views.FileRattrapageDelete.as_view(), name='fileRattrapage-delete'),
# ]

# # Add URLConf to create, update, and delete fileBilan
# urlpatterns += [
#     path('fileBilan/create/', views.FileBilanCreate.as_view(), name='fileBilan-create'),
#     path('fileBilan/<int:pk>/update/', views.FileBilanUpdate.as_view(), name='fileBilan-update'),
#     path('fileBilan/<int:pk>/delete/', views.FileBilanDelete.as_view(), name='fileBilan-delete'),
# ]

# Add URLConf to create, update, and delete user
urlpatterns += [
    path('user/create/', views.UserCreate.as_view(), name='user-create'),
    path('user/<int:pk>/update/', views.UserUpdate.as_view(), name='user-update'),
    path('user/<int:pk>/delete/', views.UserDelete.as_view(), name='user-delete'),
]

