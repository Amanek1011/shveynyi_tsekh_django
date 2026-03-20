
from django.shortcuts import render, get_object_or_404, redirect
from .models import Material
from .forms import FourXForm, RaspashForm, BeikaForm, StrochkaForm, GorloForm, YtygForm, OtkForm, YpakovkaForm

def home(request):
    materials = Material.objects.all()  # Для простоты, показать все, но можно фильтровать по роли
    return render(request, 'shveya/home.html', {'materials': materials})

def four_x_view(request, material_id):
    material = get_object_or_404(Material, id=material_id)
    if request.method == 'POST':
        form = FourXForm(request.POST, instance=material)
        if form.is_valid():
            form.save()
            return redirect('shveya_home')
    else:
        form = FourXForm(instance=material)
    return render(request, 'shveya/four_x.html', {'form': form, 'material': material})

def raspash_view(request, material_id):
    material = get_object_or_404(Material, id=material_id)
    if request.method == 'POST':
        form = RaspashForm(request.POST, instance=material)
        if form.is_valid():
            form.save()
            return redirect('shveya_home')
    else:
        form = RaspashForm(instance=material)
    return render(request, 'shveya/raspash.html', {'form': form, 'material': material})

def beika_view(request, material_id):
    material = get_object_or_404(Material, id=material_id)
    if request.method == 'POST':
        form = BeikaForm(request.POST, instance=material)
        if form.is_valid():
            form.save()
            return redirect('shveya_home')
    else:
        form = BeikaForm(instance=material)
    return render(request, 'shveya/beika.html', {'form': form, 'material': material})

def strochka_view(request, material_id):
    material = get_object_or_404(Material, id=material_id)
    if request.method == 'POST':
        form = StrochkaForm(request.POST, instance=material)
        if form.is_valid():
            form.save()
            return redirect('shveya_home')
    else:
        form = StrochkaForm(instance=material)
    return render(request, 'shveya/strochka.html', {'form': form, 'material': material})

def gorlo_view(request, material_id):
    material = get_object_or_404(Material, id=material_id)
    if request.method == 'POST':
        form = GorloForm(request.POST, instance=material)
        if form.is_valid():
            form.save()
            return redirect('shveya_home')
    else:
        form = GorloForm(instance=material)
    return render(request, 'shveya/gorlo.html', {'form': form, 'material': material})

def ytyg_view(request, material_id):
    material = get_object_or_404(Material, id=material_id)
    if request.method == 'POST':
        form = YtygForm(request.POST, instance=material)
        if form.is_valid():
            form.save()
            return redirect('shveya_home')
    else:
        form = YtygForm(instance=material)
    return render(request, 'shveya/ytyg.html', {'form': form, 'material': material})

def otk_view(request, material_id):
    material = get_object_or_404(Material, id=material_id)
    if request.method == 'POST':
        form = OtkForm(request.POST, instance=material)
        if form.is_valid():
            form.save()
            return redirect('shveya_home')
    else:
        form = OtkForm(instance=material)
    return render(request, 'shveya/otk.html', {'form': form, 'material': material})

def ypakovka_view(request, material_id):
    material = get_object_or_404(Material, id=material_id)
    if request.method == 'POST':
        form = YpakovkaForm(request.POST, instance=material)
        if form.is_valid():
            form.save()
            return redirect('shveya_home')
    else:
        form = YpakovkaForm(instance=material)
    return render(request, 'shveya/ypakovka.html', {'form': form, 'material': material})


