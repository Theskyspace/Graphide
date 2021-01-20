# @Author : Akash

#importing necssary requirements
from django.shortcuts import render,redirect
from .models import Fuctions

# Essentials for Graph Ploting Modules
import matplotlib.pyplot as plt 
import mpld3 
import numpy as np

e = 2.71828

# Render the main page(Landing page)
def main(request):
	#Extracting valid equations from database.
	list_of_equations = list(Fuctions.objects.all())
	plotme(list_of_equations)
	#Sending the information to Frontend
	list_of_equations = Fuctions.objects.all()
	return render(request,'graph.html',{'equabank':list_of_equations})

# fuction to plot points list_of_equations is just list of data locations.
def plotme(list_of_equations):
	x = np.arange(-100,100,0.01)
	figure = plt.figure(figsize=(7	,6))
	for y in list_of_equations:
		# gets the matter from fuction DB
		y = y.equations
		y = y.split('+')	
		m = ''
		count = 0 
		for i in y:
			if 'sin' in i:
				i = 'np.' + i
				y[count] = i
			elif 'cos' in i:
				i = 'np.' + i
				y[count] = i
			elif 'tan' in i:
				i = 'np.' + i
				y[count] = i
			m += '+' + i 
			count += 1
		
		'''to Make graphs which are having infinte range 
		go to defined infinte ex(tan(x),cot(x),etc) ;P'''
		threshold = 99
		m = eval(m)
		m[m>threshold] = np.inf
		m[m<-threshold] = np.inf

		plt.plot(x,m,linewidth=3)


	plt.grid()
	plt.plot(x,x*0,'k')
	plt.plot(x*0,x,'k')
	plt.ylim(-4, 4)
	plt.xlim(-4, 4)
	mpld3.save_html(figure,'Templates/graph.html')
	preappend('Templates/graph.html')

# to Reuse template thats self generated
def preappend(required_file):
	file = open(required_file,'r')
	m = file.readlines()
	file.close()
	nfile = open(required_file,'w')
	nfile.write("{% extends 'main.html' %}")
	nfile.write('\n{% block graph %}')
	for i in m:
		nfile.write(i)
	nfile.write('\n{% endblock %}')

#Takes in HttpRequest For Plotting a Fuction
def plot(request):
	fuction = request.GET['a']
	Fuctions(equations=fuction).save()
	list_of_equations = list(Fuctions.objects.all())
	try:
		plotme(list_of_equations)
		return redirect('/')
	#If user does enter the fuction with invalid input then the exception runs and basicallby warns user 
	#using SWG.html and deletes the flaw input from dbms.
	except Exception as e:
		Fuctions.objects.get(equations=fuction).delete()
		list_of_equations = list(Fuctions.objects.all())
		return render(request,'SWR.html')		

#To delete a particular equation
def delete(request,delete_id):
	item_to_delete = Fuctions.objects.get(id=delete_id)
	item_to_delete.delete()
	return redirect('/')

#To delete All the equations
def clear(request):
	Fuctions.objects.all().delete()
	return redirect('/')


def rules(request):
	return render(request,'rules.html')