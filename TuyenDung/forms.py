from django import forms
from django_random_id_model import RandomIDModel
from django_better_choices import Choices
from  .models import Ungvien, Congty,Quanhuyen,Hinhthuclamviec,Capbac,Trinhdohocvan,Mucluong,Chuyennganh,Tintuyendung
import random 


# class TintuyendungForm(forms.ModelForm):
# 	title = forms.CharField(label='')
# 	description = forms.CharField(required =False,
# 		widget=forms.Textarea(attrs={
# 			"class": "new-class-name two",
# 			"id": "my-id-for-textarea",
# 			"rows":10,
# 			"cols": 120
# 			}))
# 	price = forms.DecimalField(initial=0.0)
# 	class Meta:
# 		model = 
# 		fields = [
# 		'title',
# 		'description',
# 		'price'
# 		]

class UngvienForm(forms.ModelForm):
	maungvien=forms.FloatField( label='CMND')
	hotenuv= forms.CharField()
	STATUS=(
		(1, 'Single',),
        (2, 'Mariaged',),
        (3, 'Divorced',),
		)
	SEX_CHOICES = (
        (0, 'Female',),
        (1, 'Male',),
    )
	sdtuv= forms.CharField()
	emailuv=forms.CharField()
	ngaysinhuv=forms.DateField()
	quoctich= forms.CharField()
	diachiungvien=forms.CharField()
	gioitinh = forms.ChoiceField( choices= SEX_CHOICES)
	tinhtranghonnhan=forms.ChoiceField(choices=STATUS)
	#anhdaidien=forms.BinaryField()
	# source = forms.CharField(       # A hidden input for internal use
	# 	max_length=50,              # tell from which page the user sent the message
	# 	widget=forms.HiddenInput()
 #    )

	# def clean(self):
	# 	cleaned_data = super(UngvienForm, self).clean()
	# 	maungvien = cleaned_data.get('maungvien')
	# 	hotenuv = cleaned_data.get('hotenuv')
	# 	sdtuv = cleaned_data.get('sdtuv')
	# 	emailuv = cleaned_data.get('emailuv')
	# 	ngaysinhuv = cleaned_data.get('ngaysinhuv')
	# 	quoctich = cleaned_data.get('quoctich')
	# 	diachiungvien = cleaned_data.get('diachiungvien')
	# 	gioitinh = cleaned_data.get('gioitinh')
	# 	tinhtranghonnhan = cleaned_data.get('tinhtranghonnhan')
	# 	if not maungvien and not hotenuv and not sdtuv and not emailuv and not ngaysinhuv and not quoctich and not diachiungvien and not gioitinh and not tinhtranghonnhan:
	# 	    raise forms.ValidationError('You have to write something!')
	class Meta:
		model = Ungvien
		fields=[
		'maungvien','hotenuv','sdtuv','emailuv','ngaysinhuv','quoctich','diachiungvien','gioitinh','tinhtranghonnhan'
		]

# class TintuyendungForm(forms.ModelForm):
#     #matintuyendung=forms.FloatField()
#     tencongviectd= forms.CharField()
#     mota= forms.Textarea(attrs={"rows":10,"cols": 120})
#     quyenloiduochuong = forms.CharField()
#     yeucaucongviec = forms.Textarea(attrs={"rows":10,"cols": 120})
#     yeucauhoso = forms.Textarea(attrs={"rows":10,"cols": 120})
#     hannophoso = forms.DateField()
#     yeucaukinhnghiem = forms.CharField()
#     soluongtuyen = forms.FloatField()
#     yeucaugioitinh = forms.CharField()
#     macongty = forms.ModelChoiceField(queryset=Congty.objects.values_list('tencongty', flat = True))
#     maquanhuyen = forms.ModelChoiceField(queryset=Quanhuyen.objects.values_list('tenquanhuyen', flat = True))
#     mahtlamviec = forms.ModelChoiceField(queryset=Hinhthuclamviec.objects.values_list('tenhinhthuclamviec', flat = True))
#     macapbac = forms.ModelChoiceField(queryset=Capbac.objects.values_list('tencapbac', flat = True))
#     matrinhdohocvan = forms.ModelChoiceField(queryset=Trinhdohocvan.objects.values_list('tentrinhdohocvan', flat = True))
#     mamucluong = forms.ModelChoiceField(queryset=Mucluong.objects.values_list('den', flat = True))
#     machuyennganh = forms.ModelChoiceField(queryset=Chuyennganh.objects.values_list('tenchuyennganh', flat = True))

#     #SEX_CHOICES = ((0, 'Female',),(1, 'Male',),)
#     class Meta:
#     	model = Tintuyendung
#     	fields=[
#     	'tencongviectd','mota','quyenloiduochuong','yeucaucongviec','yeucauhoso','hannophoso','yeucaukinhnghiem','soluongtuyen','yeucaugioitinh','macongty','maquanhuyen','mahtlamviec','macapbac','matrinhdohocvan','mamucluong','machuyennganh']

class TintuyendungForm(forms.ModelForm):
    matintuyendung=forms.FloatField()
    tencongviectd= forms.CharField()
    mota= forms.Textarea(attrs={"rows":10,"cols": 120})
    quyenloiduochuong = forms.CharField()
    yeucaucongviec = forms.Textarea(attrs={"rows":10,"cols": 120})
    yeucauhoso = forms.Textarea(attrs={"rows":10,"cols": 120})
    hannophoso = forms.DateField()
    yeucaukinhnghiem = forms.CharField()
    soluongtuyen = forms.FloatField()
    yeucaugioitinh = forms.CharField()
    macongty = forms.ModelChoiceField(queryset=Congty.objects.all())
    maquanhuyen = forms.ModelChoiceField(queryset=Quanhuyen.objects.all())
    mahtlamviec = forms.ModelChoiceField(queryset=Hinhthuclamviec.objects.all())
    macapbac = forms.ModelChoiceField(queryset=Capbac.objects.all())
    matrinhdohocvan = forms.ModelChoiceField(queryset=Trinhdohocvan.objects.all())
    mamucluong = forms.ModelChoiceField(queryset=Mucluong.objects.all())
    machuyennganh = forms.ModelChoiceField(queryset=Chuyennganh.objects.all())

    #SEX_CHOICES = ((0, 'Female',),(1, 'Male',),)
    class Meta:
    	model = Tintuyendung
    	fields=[
    	'matintuyendung','tencongviectd','mota','quyenloiduochuong','yeucaucongviec','yeucauhoso','hannophoso','yeucaukinhnghiem','soluongtuyen','yeucaugioitinh','macongty','maquanhuyen','mahtlamviec','macapbac','matrinhdohocvan','mamucluong','machuyennganh']