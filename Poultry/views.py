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
	if request.user.is_authenticated:
		return render(request,'Batch_entry.html')
	else:
		return redirect('login_reload')

def index(request):
	if request.user.is_authenticated:
		return render(request,'index.html')
	else:
		return redirect('login_reload')


def batch_uploads(request):
	if request.user.is_authenticated:
		if request.method=='POST':
			a = request.POST['batch_name1']
			b = int(request.POST['total_chick'])
			c = int(request.POST['chick_arrived'])
			d = request.POST['arrived_date']
			e = request.POST['arrived_time']
			f = int(request.POST['matralry'])
			g = c-f
			query = Batch_entry.objects.create(Batch_name=a,Quantity= b,Chick_arrived = c,Arrived_date = d, Arrived_time=e, Matralty = f,Live_birds = g)
			query.save()
			
			return redirect('index_reload')
			#return redirect('accounts')
		else:
			return HttpResponse("Not stored")

		return render (request,'batch_upload.html')
	else:
		return redirect('login_reload')

def home(request):
	if request.user.is_authenticated:
		data = Batch_entry.objects.all()
		return render(request,'production_entry.html',{'value':data})
	else:
		return redirect('login_reload')
	
def production(request):
	if request.user.is_authenticated:
		if request.method=='POST':
			a = request.POST['bt_name']
			b = request.POST['production']
			c = request.POST['feed']
			d= request.POST['medicine']
			e = request.POST['matralry']
			f = request.POST['date']
			query = Production.objects.create(Batch_detail= Batch_entry.objects.get(Batch_name = a),Trays= b, Feed = c,Medicine = d, Matralty_on_days = e,Date = f)
			query.save()
			print('Date stored')
			return redirect('production_reload')
			
		else:
			return HttpResponse('Data not stored')
		return render (request,'production_entry.html')
	else:
		return redirect('login_reload')


def select_batch(request):
	if request.user.is_authenticated:
		data = Batch_entry.objects.all()
		return render(request,'Get_production.html',{'value': data})
	else:
		return redirect('login_reload')

def get_production(request):
	if request.user.is_authenticated:
		if request.method=='POST':
			selected_batch = request.POST['bt_name']
			query = Production.objects.filter(Batch_detail=selected_batch)
			return render(request,'show_production.html',{'data':query})
		else:
			return HttpResponse("something went to wrong")
	else:
		return redirect('login_reload')

def show_batch_id(request):
	if request.user.is_authenticated:
		data = Batch_entry.objects.all()
		return render(request,'show_batch.html',{'value':data})
	else:
		return redirect('login_reload')

def batch_details(request):
	if request.user.is_authenticated:
		if request.method=='POST':
			selected = request.POST['bt_name']
			query = Batch_entry.objects.filter(Batch_name=selected)
			return render(request,'batch_details.html',{'value':query})
		else:
			return HttpResponse("something wrong")
	else:
		return redirect('login_reload')

def delete_batch(request):
	if request.user.is_authenticated:
		if request.models=='POST':
			selected = request.POST['bt_name']
			query = Batch_entry.objects.filter(Batch_entry=selected)
			query.delete()
			return redirect('show_batch_id_reload')
		else:
			return HttpResponse("something went to wrong")
	else:
		return redirect('login_reload')