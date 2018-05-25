from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from .models import Job, Profile
from .forms import JobForm

import braintree

braintree.Configuration.configure(braintree.Environment.Sandbox, merchant_id='jyvhycngd7xsrg5m', public_key='3ycgztf96djp64ws', private_key='4d851588384622f92059f746a0a4b224')

# Create your views here.
#Je créer la fonction home

def home(request):
    jobs = Job.objects.filter(status=True)
    return render(request, 'home.html', {"jobs": jobs})

def job_detail(request, id):
    try:
        job = Job.objects.get(id=id)
    except Job.DoesNotExist:
        return redirect('/')

    #braintree
    client_token = braintree.ClientToken.generate()
    return render(request, 'job_detail.html', {"job": job, "client_token": client_token})

@login_required(login_url="/")
def create_job(request):
    error = ''
    if request.method == 'POST':
        job_form = JobForm(request.POST, request.FILES)
        if job_form.is_valid():
            job = job_form.save(commit=False)
            job.user = request.user
            job.save()
            return redirect('my_jobs')
        else:
            error = "Veuillez compléter le formulaire"

    job_form = JobForm()
    return render(request, 'create_job.html', {"error": error})

#Editer le job
@login_required(login_url="/")
def edit_job(request, id):
    #return render(request, 'edit_job.html', {})
    try:
        job = Job.objects.get(id=id, user=request.user)
        error = ''
        if request.method == 'POST':
            job_form = JobForm(request.POST, request.FILES, instance=job)
            if job_form.is_valid():
                job.save()
                return redirect('my_jobs')
            else:
                error = "Veuillez compléter le formulaire"
        return render(request, 'edit_job.html', {"job": job, "error": error})
    except Job.DoesNotExist:
        return redirect('/')

@login_required(login_url="/")
def my_jobs(request):
    jobs = Job.objects.filter(user=request.user)
    return render(request, 'my_jobs.html', {"jobs": jobs})

    #Le profile
@login_required(login_url="/")
def profile(request, username):
    if request.method == 'POST':
        profile = Profile.objects.get(user=request.user)
        profile.about = request.POST['about']
        profile.slogan = request.POST['slogan']
        profile.save()
    else:
        try:
            profile = Profile.objects.get(user__username=username)
        except Profile.DoesNotExist:
            return redirect('/')
    jobs = Job.objects.filter(user=profile.user, status=True)
    return render(request, 'profile.html', {"profile": profile, "jobs": jobs})

    #braintree
@login_required(login_url="/")
def create_purchase(request):
    if request.method == 'POST':
        try:
            job = Job.objects.get(id = request.POST['job_id'])
        except Job.DoesNotExist:
            return redirect('/')

            nonce = request.POST["payment_method_nonce"]
            result = braintree.Transaction.sale({
                "amount": job.price,
                "payment_method_nonce": nonce
            })

            if result.is_success:
                print('Job validé')
            else:
                print("Job non validé")
                
        return redirect('/')
