from django.contrib import admin

# Register your models here.
from .models import Admin,Banggia, Capbac,Chuyennganh,Quanhuyen,Congty
from .models import Ungvien,Hinhthuclamviec,Trinhdohocvan, Mucluong,Tintuyendung
admin.site.register(Ungvien)
admin.site.register(Admin)
admin.site.register(Banggia)
admin.site.register(Capbac)

admin.site.register(Chuyennganh)
admin.site.register(Hinhthuclamviec)

admin.site.register(Trinhdohocvan)

admin.site.register(Quanhuyen)
admin.site.register(Congty)
admin.site.register(Mucluong)
admin.site.register(Tintuyendung)



