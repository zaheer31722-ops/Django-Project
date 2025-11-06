
from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    # path('',views.home,name='home')
    path('',views.home,name='home'),
    path('about/',views.about, name='about'),
    # path('posts/',views.post_detail,name='post_detail'),
    path('profile/',views.profile, name='profile'),
    path('users/',views.user_list, name='user_list'),
    path('product_detail/',views.product_detail,name='product_detail'),
    path('welcome/',views.welcome,name='welcome'),
    path('items/',views.items_list,name='items_list'),
    path('posts/',views.post_list,name='post_list'),
    path('onetoone/',views.one_to_one_demo,name='one_to_one'),
    path('onetomany/',views.one_to_many_demo,name='one_to_many_demo'),
    path('manytomany/',views.many_to_many_demo,name='many_to_many_demo'),
    path('create/',views.create_post,name='create_post'),
    path('register/',views.register,name='register'),
    path('createevent/',views.create_event,name='create_event'),
    path('register_auth/',views.register_auth,name='register_auth'),
    path("login/", views.user_login, name="login"),
    path("logout/", views.user_logout, name="logout"),
    path("dashboard/", views.dashboard, name="dashboard"),
    path("password_change/", views.change_password, name="password_change"),
    path("password_reset/",auth_views.PasswordResetView.as_view(), name="password_reset"),
    path("password_reset/done/",auth_views.PasswordResetDoneView.as_view(), name="password_reset_done"),
    path("reset/<uidb64>/<token>/",auth_views.PasswordResetConfirmView.as_view(), name="password_reset_confirm"),
    path("reset/done/",auth_views.PasswordResetCompleteView.as_view(), name="password_reset_complete"),


    path("add_blog/", views.add_blog_post, name="add_blog"),
    path("view_posts/", views.view_posts, name="view_posts"),
    path("edit_blog/<int:post_id>/", views.edit_blog_post, name="edit_blog"),
    path("delete_blog/<int:post_id>/", views.delete_blog_post, name="delete_blog"),

    path("basic/", views.basic_queries, name='basic_queries'),
    path("aggregation/", views.aggregation_demo, name='aggregation_demo'),
    path("f_expression/", views.f_expression_demo, name='f_expression_demo'),
    path("raw_sql/", views.raw_sql_demo, name='raw_sql_demo'),
    path("optimization/", views.optimization_demo, name='optimization_demo'),
    path("custom_manager/", views.custom_manager_demo, name='custom_manager_demo'),

]
