from django.urls import path, include

from . import views

urlpatterns = [
    path('home/', views.home, name="inventaris-home"),
    path('login/', views.loginUser, name="inventaris-login"),
    path('logout/', views.logoutUser, name="inventaris-logout"),
    path('register/', views.registerPage, name="inventaris-register"),
    # get and post req. for insert operation
    path('pinjam/', views.pinjam, name='pinjam-barang'),
    path('pinjam/<int:id>/', views.pinjam_form, name='pinjam-update'),
    path('createpj/', views.pinjam_form, name='pinjam-insert'),
    # get and post req. for update operation
    path('barang/', views.barang, name='inventaris-barang'),
    path('barangg/<int:id>/', views.barang_form, name='inventaris-update'),
    path('delete/<int:id>/', views.barang_delete, name='inventaris-delete'),
    path('create/', views.barang_form, name='inventaris-insert'),
    # service barang
    path('service/', views.service, name='service-barang'),
    path('service/<int:id>/', views.service_form, name='service-update'),
    path('deletesrv/<int:id>/', views.service_delete, name='service-delete'),
    path('createsrv/', views.service_form, name='service-insert'),
    # barang rusak
    path('rusak/', views.rusak, name='rusak-barang'),
    path('rusak/<int:id>/', views.rusak_form, name='rusak-update'),
    path('deletersk/<int:id>/', views.rusak_delete, name='rusak-delete'),
    path('creatersk/', views.rusak_form, name='rusak-insert'),
    # merk barang
    path('merk/', views.merk, name='merk-barang'),
    path('merk/<int:id>/', views.merk_form, name='merk-update'),
    path('deletemrk/<int:id>/', views.merk_delete, name='merk-delete'),
    path('createmrk/', views.merk_form, name='merk-insert'),
]
