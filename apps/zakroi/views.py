
from django.shortcuts import render, redirect
from apps.shveya.models import Party, Material
from .forms import PartyForm, MaterialForm, UserForm
from django.contrib.auth import login


def zakroi_home(request):
    parties = Party.objects.prefetch_related('materials').all()
    return render(request, 'zakroi/zakroi_home.html', {'parties': parties})


def create_party(request):
    if request.method == 'POST':
        form = PartyForm(request.POST)
        if form.is_valid():
            party = form.save()
            return redirect('create_material', party_id=party.id)
    else:
        form = PartyForm()
    return render(request, 'zakroi/create_party.html', {'form': form})


def create_material(request, party_id):
    party = Party.objects.get(id=party_id)
    if request.method == 'POST':
        form = MaterialForm(request.POST)
        if form.is_valid():
            material = form.save(commit=False)
            material.party = party
            material.save()
            return redirect('zakroi_home')
    else:
        form = MaterialForm()
    return render(request, 'zakroi/create_material.html', {'form': form, 'party': party})


def create_user(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            return redirect('zakroi_home')
    else:
        form = UserForm()
    return render(request, 'zakroi/create_user.html', {'form': form})


def material_detail(request, material_id):
    material = Material.objects.get(id=material_id)
    return render(request, 'zakroi/material_detail.html', {'material': material})


def party_stats(request):
    total_parties = Party.objects.count()
    total_materials = Material.objects.count()
    total_tshirts = sum(m.tshirt_count for m in Material.objects.all())
    return render(request, 'zakroi/party_stats.html', {
        'total_parties': total_parties,
        'total_materials': total_materials,
        'total_tshirts': total_tshirts,
    })
