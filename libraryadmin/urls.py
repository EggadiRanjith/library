from django.urls import path
from . import views

urlpatterns = [
    # ...
    path('adminindex/', views.admin_index, name='adminindex'),
    path('libraryadmin/registraion/', views.register, name='register'), 
    path('libraryadmin/registraion/regformsubmit/', views.register_form, name='registerform'),
    path('libraryadmin/registraion/regfilesubmit/', views.registerfile, name='registrationfile'), 
    path('libraryadmin/generalbooks/',views.admin_general_books_view,name='admin_generalbooks'),
    path('libraryadmin/journal/',views.admin_journals_books_view,name='admin_journals'),
    path('libraryadmin/papers/',views.admin_papers_books_view,name='admin_papers'),
    path('libraryadmin/novels/',views.admin_novels_books_view,name='admin_novels'),
    path('libraryadmin/first_year_1_1/',views.admin_first_year_1_1,name='admin_first_year_1_1'),
    path('libraryadmin/first_year_1_2/',views.admin_first_year_1_2,name='admin_first_year_1_2'),
    path('libraryadmin/second_year_2_1/',views.admin_second_year_2_1,name='admin_second_year_2_1'),
    path('libraryadmin/second_year_2_2/',views.admin_second_year_2_2,name='admin_second_year_2_2'),
    path('libraryadmin/third_year_3_1/',views.admin_third_year_3_1,name='admin_third_year_3_1'),
    path('libraryadmin/third_year_3_2/',views.admin_third_year_3_2,name='admin_third_year_3_2'),
    path('libraryadmin/fourth_year_4_1/',views.admin_fourth_year_4_1,name='admin_fourth_year_4_1'),
    path('libraryadmin/fourth_year_4_2/',views.admin_fourth_year_4_2,name='admin_fourth_year_4_2'), 
    path('libraryadmin/update_form_books/<str:table>/<str:id>/<path:next>/',views.update_form_books,name='update_form_books'), 
    path('libraryadmin/update_form_books/updatebookform/<path:next>/',views.updatebookform,name='updatebookform'), 
    path('libraryadmin/delete_course/<str:table>/<str:id>/<path:next>/',views.delete_course,name='delete_course'), 
    path('libraryadmin/fetchusertickets/',views.admin_fetch_user_ticket,name='admin_fetchusersticket'),
    path('libraryadmin/fetchusertickets/fetchbooks/',views.fetchbooks,name='fetchbooks'),
    path('libraryadmin/fetchusertickets/fetchbooks/fetchusertickets/',views.studentbooks,name='studentbooks'),
    path('libraryadmin/booksubmission/',views.admin_bookupload,name='admin_uploadbooks'),
    path('libraryadmin/upload_books/', views.book_upload_books, name='upload_books'),
    path('libraryadmin/upload_course/', views.course_upload, name='course_books'),
    path('libraryadmin/borrowreturn/',views.borrow_return,name='br'),
    path('libraryadmin/borrowbook/',views.borrow_book,name='borrow_book'),
    path('libraryadmin/returnbook/',views.return_book,name='return_book'),
    path('libraryadmin/profile/',views.admin_profile,name='admin_profile'),
    path('libraryadmin/change_password/', views.change_password, name='change_password'),
    path('libraryadmin/profile/logout',views.logout,name='logout'),
]