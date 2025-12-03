from django.urls import path
from Admin_App import views

urlpatterns=[
    path('Dashboard/',views.dashboard,name="dashboard"),
    path('Admin_Login/',views.admin,name="admin"),
    path('Admin_Login_check/',views.admin_login,name="admin_login"),
    path('Admin/Services/', views.admin_services, name="admin_services"),
    path('Services_Save/', views.save_services, name="save_services"),
    path('View_Services/', views.view_services, name="view_services"),
    path('Edit_Services/<int:service_id>', views.edit_services, name="edit_services"),
    path('Update_Services/<int:s_id>', views.update_services, name="update_services"),
    path('Delete_Services/<int:service_id>', views.delete_services, name="delete_services"),
    path('Add_Staff/',views.add_staff, name="add_staff"),
    path('Save_Staff/',views.save_staff, name="save_staff"),

    path('get_services_by_category/', views.get_services_by_category, name="get_services_by_category"),




    path('Category/',views.category,name="category"),
    path('Save_Category/',views.save_category,name="save_category"),
    path('View_Category/',views.view_category,name="view_category"),
    path('Edit_Category/<int:category_id>',views.edit_category,name="edit_category"),
    path('Update_Category/<int:c_id>',views.update_category,name="update_category"),
    path('Delete_Category/<int:category_id>',views.delete_category,name="delete_category"),

]