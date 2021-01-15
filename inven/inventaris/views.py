from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
# Create your views here.
from django.contrib.auth.models import Group
from .models import *
from .forms import *
from .decorators import unauthenticated_user, allowed_users
from learningBarcode import MyBarcodeDrawing


def loginUser(request):
    # user = None
    if request.user.is_authenticated:
        return redirect('../home')

    else:
        if request.method == "POST":
            username_inp = request.POST.get('username', False)
            password_inp = request.POST.get('password', False)

            user = authenticate(request, username=username_inp,
                                password=password_inp)

            if user is not None:
                login(request, user)
                return redirect('../home')

            else:
                return redirect('../login')

        context = {}
        return render(request, 'login/login.html', context)

    if request.method == "GET":
        if request.user.is_authenticated():
            return redirect('../home')
        else:
            return render(request, 'login/login.html')


def my_view(request):
    username = None
    if request.user.is_authenticated():
        username = request.user.username


def logoutUser(request):
    logout(request)
    if request.method == "POST":
        if request.POST["logout"] == "Submit":
            logout(request)

            return redirect('../login')

    return render(request, 'login/login.html')


@login_required(login_url='login')
def barang(request):
    barang = Barang.objects.all()
    # print(barang)
    return render(request, 'inventaris/barang.html', {'barang': barang})

#

#


@login_required(login_url='login')
def barang_form(request, id=0):
    if request.method == "GET":
        if id == 0:
            form = BarangForm()
        else:
            barang = Barang.objects.get(pk=id)
            form = BarangForm(instance=barang)
        return render(request, "inventaris/barang_form.html", {'form': form})
    else:
        if id == 0:
            form = BarangForm(request.POST)
        else:
            barang = Barang.objects.get(pk=id)
            form = BarangForm(request.POST, instance=barang)
        if form.is_valid():
            form.save()
        return redirect('/inventaris/barang')


@login_required(login_url='login')
def barang_delete(request, id):
    barang = Barang.objects.get(pk=id)
    barang.delete()
    return redirect('/inventaris/barang')


# @allowed_users(allowed_roles=['admin'])
@login_required(login_url='login')
def home(request):
    return render(request, 'inventaris/home.html')


@login_required(login_url='login')
def registerPage(request):
    # if request.user.is_authenticated:
    #    return redirect('../home')

    # else:
    if request.method == 'POST':
        # form = UserCreationForm()

        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('../home')
    else:
        form = UserCreationForm()
        # context = {}
    return render(request, 'login/register.html', {'form': form})


# def barcode(request):
#     # instantiate a drawing object
#     import mybarcode
#     d = mybarcode.MyBarcodeDrawing("HELLO WORLD")
#     binaryStuff = d.asString('gif')
#     return HttpResponse(binaryStuff, 'image/gif')


@login_required(login_url='login')
def pinjam(request):
    pinjam = Pinjam.objects.all()

    return render(request, 'pinjam/pinjam.html', {'pinjam': pinjam})


@login_required(login_url='login')
def pinjam_form(request, id=0):
    if request.method == "GET":
        if id == 0:
            form = PinjamForm()
        else:
            pinjam = Pinjam.objects.get(pk=id)
            form = PinjamForm(instance=pinjam)
        return render(request, "pinjam/pinjam_form.html", {'form': form})
    else:
        if id == 0:
            form = PinjamForm(request.POST)
        else:
            pinjam = Pinjam.objects.get(pk=id)
            form = PinjamForm(request.POST, instance=pinjam)
        if form.is_valid():
            form.save()
        return redirect('/inventaris/pinjam')
#
@login_required(login_url='login')
def rusak(request):
    rusak = Rusak.objects.all()

    return render(request, 'rusak/rusak.html', {'rusak': rusak})


@login_required(login_url='login')
def rusak_form(request, id=0):
    if request.method == "GET":
        if id == 0:
            form = RusakForm()
        else:
            rusak = Rusak.objects.get(pk=id)
            form = RusakForm(instance=rusak)
        return render(request, "rusak/rusak_form.html", {'form': form})
    else:
        if id == 0:
            form = RusakForm(request.POST)
        else:
            rusak = Rusak.objects.get(pk=id)
            form = RusakForm(request.POST, instance=rusak)
        if form.is_valid():
            form.save()
        return redirect('/inventaris/rusak')


@login_required(login_url='login')
def rusak_delete(request, id):
    rusak = Rusak.objects.get(pk=id)
    rusak.delete()
    return redirect('/inventaris/rusak')


#
@login_required(login_url='login')
def service(request):
    service = Service.objects.all()

    return render(request, 'service/service.html', {'service': service})


@login_required(login_url='login')
def service_form(request, id=0):
    if request.method == "GET":
        if id == 0:
            form = ServiceForm()
        else:
            service = Service.objects.get(pk=id)
            form = ServiceForm(instance=service)
        return render(request, "service/service_form.html", {'form': form})
    else:
        if id == 0:
            form = ServiceForm(request.POST)
        else:
            service = Service.objects.get(pk=id)
            form = ServiceForm(request.POST, instance=service)
        if form.is_valid():
            form.save()
        return redirect('/inventaris/service')


@login_required(login_url='login')
def service_delete(request, id):
    service = Service.objects.get(pk=id)
    service.delete()
    return redirect('/inventaris/service')

#
@login_required(login_url='login')
def merk(request):
    merk = Merk.objects.all()

    return render(request, 'merk/merk.html', {'merk': merk})


@login_required(login_url='login')
def merk_form(request, id=0):
    if request.method == "GET":
        if id == 0:
            form = MerkForm()
        else:
            merk = Merk.objects.get(pk=id)
            form = MerkForm(instance=merk)
        return render(request, "merk/merk_form.html", {'form': form})
    else:
        if id == 0:
            form = MerkForm(request.POST)
        else:
            merk = Merk.objects.get(pk=id)
            form = MerkForm(request.POST, instance=merk)
        if form.is_valid():
            form.save()
        return redirect('/inventaris/merk')


@login_required(login_url='login')
def merk_delete(request, id):
    merk = Merk.objects.get(pk=id)
    merk.delete()
    return redirect('/inventaris/merk')
#
