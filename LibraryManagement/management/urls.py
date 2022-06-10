from django.urls import re_path
from management import views

urlpatterns = [
    re_path(r'^$', views.index, name='homepage'),
    re_path(r'^signup/$', views.signup, name='signup'),
    re_path(r'^login/$', views.login, name='login'),
    re_path(r'^logout/$', views.logout, name='logout'),
    re_path(r'^set_password/$', views.set_password, name='set_password'),
    re_path(r'^add_book/$', views.add_book, name='add_book'),
    re_path(r'^add_img/$', views.add_img, name='add_img'),
    re_path(r'^view_book_list/$', views.view_book_list, name='view_book_list'),
    re_path(r'^view_book/detail/$', views.detail, name='detail'),

    re_path(r'^join_club/(?P<uid>[0-9]+)$', views.join_club, name='join_club'),
    re_path(r'^user_show/(?P<id>[0-9]+)$', views.user_show, name='user_show'),
    re_path(r'^delete_user/(?P<userid>[0-9]+)$', views.delete_user, name='delete_user'),
    re_path(r'^change_club/(?P<id>[0-9]+)$', views.change_club, name='change_club'),

    re_path(r'^club_zixun_add$', views.club_zixun_add, name='club_zixun_add'),
    re_path(r'^club_zixun_insert$', views.club_zixun_insert, name='club_zixun_insert'),
    re_path(r'^show_act/$', views.show_act, name='show_act'),

    re_path(r'^show_act_detail/(?P<id>[0-9]+)$', views.show_act_detail, name='show_act_detail'),

    # 后台
    re_path(r'^myadmin/$', views.myadmin_index, name='myadmin_index'),
    re_path(r'^myadmin_reg/$', views.myadmin_reg, name='myadmin_reg'),
    re_path(r'^myadmin_usersinsert/$', views.myadmin_usersinsert, name='myadmin_usersinsert'),
    re_path(r'^myadmin_login/$', views.myadmin_login, name='myadmin_login'),
    re_path(r'^myadmin_dologin/$', views.myadmin_dologin, name='myadmin_dologin'),
    re_path(r'^myadmin_logout/$', views.myadmin_logout, name='myadmin_logout'),

    re_path(r'^myadmin_show_clubs/$', views.myadmin_show_clubs, name='myadmin_show_clubs'),
    re_path(r'^myadmin_club_info/(?P<id>[0-9]+)$', views.myadmin_club_info, name='myadmin_club_info'),
    re_path(r'show_members/(?P<id>[0-9]+)$', views.show_members, name='show_members'),
    re_path(r'del_member/(?P<id>[0-9]+)$', views.del_member, name='del_member'),
    re_path(r'del_club/(?P<id>[0-9]+)$', views.del_club, name='del_club'),

    # 更换社长
    re_path(r'^myadmin_change_member/(?P<id>[0-9]+)$', views.myadmin_change_member, name='myadmin_change_member'),
    re_path(r'^myadmin_weiren/(?P<id>[0-9]+)$', views.myadmin_weiren, name='myadmin_weiren'),
    re_path(r'^myadmin_show_all_members/$', views.myadmin_show_all_members, name='myadmin_show_all_members'),

    re_path(r'^myadmin_add_club/$', views.myadmin_add_club, name='myadmin_add_club'),

    re_path(r'^myadmin_insert_club/$', views.myadmin_insert_club, name='myadmin_insert_club'),

]
