from django.shortcuts import render
from django.http import Http404
from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse,HttpResponseRedirect
from .forms import submit

def portal(request):
        if request.method == 'POST':
                question=request.POST.get("Question")
                answer=submit(question)
                print (answer)
                return render(request,'answer.html',{"error":answer})
               
        else:
                pass	
        return render(request,'fillform.html')	
		
 	





