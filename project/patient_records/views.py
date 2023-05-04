from django.shortcuts import render, redirect
from django.contrib import messages, auth
from .models import Patient
from .forms import PatientForm

def create_patient(request):
    if request.method == 'POST':
        form = PatientForm(request.POST)
        if form.is_valid():
            form.save()
            messages.info(request, "Patient record saved ")
            return redirect('register/')

    else:
        form = PatientForm()
    return render(request, 'patient_form.html', {'form': form})

def patient_list(request):
    patients = Patient.objects.all()
    return render(request, 'patient_list.html', {'patients': patients})

def loginn(request):
    if request.method=='POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user=auth.authenticate(username=username,password=password)

        if user is not None:
            auth.login(request,user)
            return redirect('register')
        else:
            messages.error(request,"Invalid credentials")
            return redirect('/')
    return render(request,"login.html")

def logoutt(request):
    auth.logout(request)
    return redirect('/')