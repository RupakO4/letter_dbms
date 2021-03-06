from django.contrib import admin
from django.urls import path ,include
from home import views
urlpatterns = [
    path('', views.index, name='home'),
    path('loginStudent', views.loginStudent, name='loginStudent'),
    path('loginTeacher', views.loginTeacher, name='loginTeacher'),
    path('logout', views.logoutUser, name='logout'),
    path('studentform1', views.studentform1, name='Studentform1'),
    path('studentform2', views.studentform2, name='Studentform2'),
    path('makeLetter', views.make_letter, name='MakeLetter'),
    path('final', views.final, name='Final'),
    path('gallery', views.gallery, name='Gallery'),
    path('studentfinal', views.studentfinal, name='StudentFinal'),
    path('forgotPassword', views.forgotPassword, name='forgotPassword'),
    # path('validatePassword', views.validatePassword, name='validatePassword'),
    path('changePassword', views.changePassword, name='changePassword'),
    path('otp', views.otp, name='otp'),
    path('OTP_check', views.OTP_check, name='OTP_check'),
    path('contact', views.contact, name='contact'),
    path('feedback', views.feedback, name='feedback'),
    path('about', views.about, name='about'),
    # path('teacher', views.teacher, name='teacher'),
    path('userDetails', views.userDetails, name='userDetails'),
    path('profileUpdate', views.profileUpdate, name='profileUpdate'),
    path('profileUpdateRequest', views.profileUpdateRequest, name='profileUpdateRequest'),
    path('changeUsername', views.changeUsername, name='changeUsername'),
    path('userPasswordChange', views.userPasswordChange, name='userPasswordChange'),
    path('forgotUsername', views.forgotUsername, name='forgotUsername'),
    path('checkEmail', views.checkEmail, name='checkEmail'),
    path('changeTitle', views.changeTitle, name='changeTitle'),
    path('changePhone', views.changePhone, name='changePhone'),
    path('changeEmail', views.changeEmail, name='changeEmail'),
    path('getdetails', views.getdetails, name='getdetails'),
    path('edit', views.edit, name='edit'),
    path('addSubjects', views.addSubjects, name='addSubjects'),
    path('deleteSubjects', views.deleteSubjects, name='deleteSubjects'),
    path('teacher', views.teacher, name='teacher'),






















]

