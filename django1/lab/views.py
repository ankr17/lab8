from django.shortcuts import render
from .models import Supplier,Material,Delivery
import datetime

def home(request):
 suppliers = Supplier.objects.all()
 materials = Material.objects.all()
 deliveries = Delivery.objects.all()
 return render(request, 'home.html', {
 'project_name': 'Django-project 8 lab',
 'student_name': 'Kryvoshei Anastasia',
 'group': 'KIB21016b',
 'suppliers': suppliers,
 'materials': materials,
 'deliveries': deliveries,
 })
