from django.shortcuts import render,redirect
from django.http import HttpResponse 
from .models import Batch_entry,Production
from django.contrib import messages
from django.contrib.auth.models import User,auth
from django.utils.timezone import now

def login(request):
	if request.method=='POST':
		un = request.POST['uname']
		ps = request.POST['pass']
		user = auth.authenticate(username = un, password = ps)

		if user is not None:
			auth.login(request,user)
			return redirect('index_reload')
		else:
			messages.info(request,"Invalid user")
			return redirect('login_reload')
	return render(request,'login.html')

def logout(request):
	auth.logout(request)
	return redirect('login_reload')

def run_new_batch(request):
	return render(request,'Batch_entry.html')

def index(request):
	return render(request,'index.html')


def batch_uploads(request):
	if request.method=='POST':
		a = request.POST['batch_name1']
		b = request.POST['total_chick']
		c = request.POST['chick_arrived']
		d = request.POST['arrived_date']
		e = request.POST['arrived_time']
		f = request.POST['matralry']
		query = Batch_entry.objects.create(Batch_name=a,Quantity= b,Chick_arrived = c,Arrived_date = d, Arrived_time=e, Matralty = f)
		query.save()
		
		return redirect('index_reload')
		#return redirect('accounts')
	else:
		return HttpResponse("Not stored")

	return render (request,'batch_upload.html')

def home(request):
	#pass
	data = Batch_entry.objects.all()
	return render(request,'production_entry.html',{'value':data})
	
def production(request):
	if request.method=='POST':
		a = request.POST['bt_name']
		b = request.POST['production']
		c = request.POST['feed']
		d= request.POST['medicine']
		e = request.POST['matralry']
		query = Production.objects.create(Batch_detail= Batch_entry.objects.get(Batch_name = a),Trays= b, Feed = c,Medicine = d, Matralty_on_days = e)
		query.save()
		print('Date stored')
		return redirect('production_reload')
		
	else:
		return HttpResponse('Data not stored')
	return render (request,'production_entry.html')

def select_batch(request):
	data = Batch_entry.objects.all()
	return render(request,'Get_production.html',{'value': data})

def get_production(request):
	if request.method=='POST':
		selected = request.POST['gt']
		query = Production.objects.filter(selected)
		return render(request,'Get_production.html',{'data':query})