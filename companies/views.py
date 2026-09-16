from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required

from .forms import CompanyForm
from .models import Company


@login_required
def company_create(request):

    if request.user.profile.user_type != 'recruiter':
        return redirect('role_home')

    if request.method == 'POST':

        form = CompanyForm(
            request.POST,
            request.FILES
        )

        if form.is_valid():

            company = form.save(
                commit=False
            )

            company.recruiter = request.user

            company.save()

            return redirect('company_list')

    else:

        form = CompanyForm()

    return render(
        request,
        'companies/company_create.html',
        {
            'form': form
        }
    )


@login_required
def company_list(request):

    if request.user.profile.user_type != 'recruiter':
        return redirect('role_home')

    companies = Company.objects.filter(
        recruiter=request.user
    )

    return render(
        request,
        'companies/company_list.html',
        {
            'companies': companies
        }
    )


@login_required
def company_edit(request, company_id):

    company = get_object_or_404(
        Company,
        id=company_id,
        recruiter=request.user
    )

    if request.method == 'POST':

        form = CompanyForm(
            request.POST,
            request.FILES,
            instance=company
        )

        if form.is_valid():

            form.save()

            return redirect('company_list')

    else:

        form = CompanyForm(
            instance=company
        )

    return render(
        request,
        'companies/company_edit.html',
        {
            'form': form,
            'company': company
        }
    )


@login_required
def company_delete(request, company_id):

    company = get_object_or_404(
        Company,
        id=company_id,
        recruiter=request.user
    )

    if request.method == 'POST':

        company.delete()

        return redirect('company_list')

    return render(
        request,
        'companies/company_delete.html',
        {
            'company': company
        }
    )