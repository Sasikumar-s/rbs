from django.urls import path
from .views import home,production,select_batch,get_production,batch_uploads,index,run_new_batch,login,logout
urlpatterns = [
path('', login, name='login_reload'),
path('logout',logout, name='logout_reload'),
path('index',index,name = 'index_reload'),
path('production_html' , home,name= 'production_reload'),
path('new_batch_html' , run_new_batch,name = 'new_batch_reload'),
path('get_html' ,select_batch),
path('get_production',get_production),
path('production_html',home),
path('production_upload',production),
path('choose',select_batch),
path('batch_html',batch_uploads)
]