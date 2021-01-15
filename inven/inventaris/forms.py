from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import *
from django.conf import settings


class BarangForm(forms.ModelForm):

    class Meta:
        model = Barang
        fields = ('name', 'code', 'merk')
        labels = {
            'name': 'Nama',
            'code': 'Kode Barang',
            'merk': 'Merk Barang'
        }

    def __init__(self, *args, **kwargs):
        super(BarangForm, self).__init__(*args, **kwargs)
        self.fields['code'].empty_label = "Select"
        self.fields['code'].required = False


class RusakForm(forms.ModelForm):

    class Meta:
        model = Rusak
        fields = ('codebrg_rsk', 'merkbrg_rsk', 'barang_rsk')
        labels = {
            'codebrg_rsk': 'Jenis Barang',
            'merkbrg_rsk': 'Merk Barang',
            'barang_rsk': 'Barang'
        }

    def __init__(self, *args, **kwargs):
        super(RusakForm, self).__init__(*args, **kwargs)
        self.fields['codebrg_rsk'].empty_label = "Select"
        self.fields['codebrg_rsk'].required = False


class MerkForm(forms.ModelForm):

    class Meta:
        model = Merk
        fields = ('merk', 'nama_merk')
        labels = {
            'merk': 'Kode Merk',
            'nama_merk': 'Nama Merk'
        }

    def __init__(self, *args, **kwargs):
        super(RusakForm, self).__init__(*args, **kwargs)
        self.fields['merk'].empty_label = "Select"
        self.fields['merk'].required = False


class ServiceForm(forms.ModelForm):

    class Meta:
        model = Service
        fields = ('code_srv', 'merk_srv', 'barang_srv')
        labels = {
            'code_srv': 'Kode Barang',
            'merk_srv': 'Merk Barang',
            'barang_srv': 'Barang'
        }

    def __init__(self, *args, **kwargs):
        super(ServiceForm, self).__init__(*args, **kwargs)
        self.fields['code_srv'].empty_label = "Select"
        self.fields['code_srv'].required = False


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'password2']


class PinjamForm(forms.ModelForm):
    tgl_balikin = forms.DateField(input_formats=settings.DATE_INPUT_FORMATS)
    tgl_pinjam = forms.DateField(input_formats=settings.DATE_INPUT_FORMATS)

    class Meta:
        model = Pinjam
        fields = ('nama_pj', 'code_pj', 'merk_pj',
                  'barang_pj', 'tgl_balikin', 'tgl_pinjam')
        labels = {
            'nama_pj': 'Nama',
            'code_pj': 'Kode Barang',
            'merk_pj': 'Merk Barang',
            'barang_pj': 'Jenis Barang',
            'tgl_balikin': 'Tanggal Balikin',
            'tgl_pinjam': 'Tanggal Pinjam'
        }

    # def __init__(self, *args, **kwargs):
    #    super(BarangForm, self).__init__(*args, **kwargs)
    #    self.fields['code'].empty_label = "Select"
    #    self.fields['code'].required = False
