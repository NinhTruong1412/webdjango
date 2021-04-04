from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.base import TemplateView
from .models import Tintuyendung,Ungvien


from .forms import UngvienForm,TintuyendungForm

# Create your views here.
def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

app_name="Tuyen_Dung"
class ProfileView(LoginRequiredMixin, TemplateView):
    template_name = "templates/accounts/signup.html"

def ungvien_create_view(request):
	form= UngvienForm(request.POST or None)
	if form.is_valid():
		form.save()
		form = UngvienForm()
	context={
	'form': form
	}
	return render(request,"./ungvien/ungvien_create.html",context)

def ungvien_list_view(request):
	queryset = Ungvien.objects.all()
	context={
	"obj_list": queryset
	}
	return render(request,"./ungvien/ungvien_list.html",context)




def dynamic_lookup_view(request,mauv):
	obj = Ungvien.objects.get(maungvien=mauv)
	# obj get_object_or_404(Product,id= my_id)
	try:
		obj = Ungvien.objects.get(maungvien=mauv)
	except Ungvien.DoesNotExist:
		raise Http404
	context={
	"obj": obj
	}
	return render(request,"./ungvien/ungvien_detail.html",context)

#-------------------------------------------Tin tuyen dung -----------------
def tuyendung_create_view(request):
	form = TintuyendungForm(request.POST or None)
	if form.is_valid():
		form.save()
		form = TintuyendungForm()
	context={
	'form': form
	}
	return render(request,"./tuyendung/tuyendung_create.html",context)