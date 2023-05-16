from django.shortcuts import render, redirect, get_object_or_404
from .models import Company
# from .forms import CompanyForm
# views.py

from .forms import CompanyForm, LocationForm

def company_add(request):
    if request.method == "POST":
        company_form = CompanyForm(request.POST)
        location_form = LocationForm(request.POST)
        if company_form.is_valid() and location_form.is_valid():
            location = location_form.save()
            company = company_form.save(commit=False)
            company.location = location
            company.save()
            return redirect('company_list')
    else:
        company_form = CompanyForm()
        location_form = LocationForm()
    return render(request, 'application2/company_edit.html', {'company_form': company_form, 'location_form': location_form})

def company_edit(request, pk):
    company = get_object_or_404(Company, pk=pk)
    if request.method == "POST":
        company_form = CompanyForm(request.POST, instance=company)
        location_form = LocationForm(request.POST, instance=company.location)
        if company_form.is_valid() and location_form.is_valid():
            location_form.save()
            company_form.save()
            return redirect('company_list')
    else:
        company_form = CompanyForm(instance=company)
        location_form = LocationForm(instance=company.location)
    return render(request, 'application2/company_edit.html', {'company_form': company_form, 'location_form': location_form})

# from django.shortcuts import render
# from .models import Company

def company_list(request):
    companies = Company.objects.all()
    return render(request, 'application2/company_list.html', {'companies': companies})

def company_delete(request, pk):
    company = get_object_or_404(Company, pk=pk)
    if request.method == "POST":
        company.delete()
        return redirect('company_list')
    return render(request, 'application2/company_confirm_delete.html', {'company': company})

def company_activate(request, pk):
    company = get_object_or_404(Company, pk=pk)
    company.is_active = True
    company.save()
    return redirect('company_list')

def company_deactivate(request, pk):
    company = get_object_or_404(Company, pk=pk)
    company.is_active = False
    company.save()
    return redirect('company_list')

# Rest of your views...

