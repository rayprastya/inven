from django.db import models
#
import barcode
from barcode.writer import ImageWriter
from io import BytesIO
# from django.core.files.base import ContentFile
# from scan.models import Barcode
#
# import learningBarcode
from django.core.files import File
from django import forms
from random import randint


# Create your models here.


class Barang(models.Model):
    name = models.CharField(max_length=200, blank=True, null=True)
    code = models.ForeignKey(
        'Code', models.DO_NOTHING, blank=True, null=True)
    merk = models.ForeignKey(
        'Merk', models.DO_NOTHING, db_column='merk', blank=True, null=True)
    date_created = models.DateTimeField(auto_now_add=True)
    barcode = models.ImageField(upload_to='static/images/', blank=True)

    def randomNum(self, n):
        range_start = 10**(n-1)
        range_end = (10**n)-1
        return randint(range_start, range_end)

    def save(self, *args, **kwargs):
        EAN = barcode.get_barcode_class('ean13')
        ean = EAN(f'{self.randomNum(13)}', writer=ImageWriter())
        buffer = BytesIO()
        ean.write(buffer)
        self.barcode.save(f'{self.name}.png', File(buffer), save=False)
        return super().save(*args, **kwargs)

    def __str__(self):
        return str(self.name)

    class Meta:
        managed = False
        db_table = 'inventaris_barang'


class Code(models.Model):
    code = models.BigIntegerField(blank=True, null=True)
    nama_code = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return str(self.nama_code)

    class Meta:
        managed = False
        db_table = 'inventaris_code'


class Merk(models.Model):
    merk = models.IntegerField()
    nama_merk = models.CharField(max_length=20)

    def __str__(self):
        return str(self.nama_merk)

    class Meta:
        managed = False
        db_table = 'inventaris_merk'


class Pinjam(models.Model):
    nama_pj = models.CharField(max_length=200, blank=True, null=True)
    code_pj = models.ForeignKey(
        Code, models.DO_NOTHING, db_column='code_pj')
    merk_pj = models.ForeignKey(
        Merk, models.DO_NOTHING, db_column='merk_pj')
    barang_pj = models.ForeignKey(
        Barang, models.DO_NOTHING, db_column='barang_pj', blank=True, null=True)
    tgl_pinjam = models.CharField(max_length=35)
    tgl_balikin = models.CharField(max_length=35)
    date_created = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'inventaris_pinjam'


class Rusak(models.Model):
    codebrg_rsk = models.ForeignKey(
        Code, models.DO_NOTHING, db_column='codebrg_rsk')
    merkbrg_rsk = models.ForeignKey(
        Merk, models.DO_NOTHING, db_column='merkbrg_rsk')
    barang_rsk = models.ForeignKey(
        Barang, models.DO_NOTHING, db_column='barang_rsk')
    date_created = models.DateTimeField(auto_now_add=True)

    class Meta:
        managed = False
        db_table = 'inventaris_rusak'


class Service(models.Model):
    code_srv = models.ForeignKey(Code, models.DO_NOTHING, db_column='code_srv')
    merk_srv = models.ForeignKey(Merk, models.DO_NOTHING, db_column='merk_srv')
    barang_srv = models.ForeignKey(
        Barang, models.DO_NOTHING, db_column='barang_srv')
    date_created = models.DateTimeField(auto_now_add=True)

    class Meta:
        managed = False
        db_table = 'inventaris_service'

        # class Userdata(models.Model):

        #id = models.TextField(primary_key=True)
        #username = models.CharField(max_length=50, blank=True, null=True)
        #password = models.CharField(max_length=50, blank=True, null=True)
        # roleid = models.ForeignKey(
        #    Role, models.DO_NOTHING, db_column='roleid', blank=True, null=True)
        #name = models.CharField(max_length=100, blank=True, null=True)
        #address = models.TextField(blank=True, null=True)
        #phonenumber = models.CharField(max_length=13, blank=True, null=True)
        #email = models.CharField(max_length=50, blank=True, null=True)

        # class Meta:
        #    db_table = 'userdata'

        # class Role(models.Model):

        #roleid = models.CharField(primary_key=True, max_length=3)
        #role = models.CharField(max_length=10)

        # class Meta:
        #    db_table = 'role'

# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey(
        'DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'
