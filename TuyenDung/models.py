# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
import uuid
import random 


class Admin(models.Model):
    maadmin = models.FloatField(primary_key=True)
    tenadmin = models.CharField(max_length=255)
    sdtadmin = models.CharField(unique=True, max_length=10)
    emailadmin = models.CharField(unique=True, max_length=255)
    taikhoan = models.ForeignKey('Taikhoan', models.DO_NOTHING, db_column='taikhoan', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'admin'


class Banggia(models.Model):
    hanguutien = models.FloatField(primary_key=True)
    goituan = models.FloatField()
    gia = models.FloatField()

    class Meta:
        managed = False
        db_table = 'banggia'
        unique_together = (('hanguutien', 'goituan'),)


class Capbac(models.Model):
    macapbac = models.FloatField(primary_key=True)
    tencapbac = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'capbac'


class Chitietdanhgia(models.Model):
    matieuchi = models.OneToOneField('Tieuchi', models.DO_NOTHING, db_column='matieuchi', primary_key=True)
    sophieudanhgia = models.ForeignKey('Phieudanhgia', models.DO_NOTHING, db_column='sophieudanhgia')
    diem = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'chitietdanhgia'
        unique_together = (('matieuchi', 'sophieudanhgia'),)


class Chitietthanhtoan(models.Model):
    sophieuthanhtoan = models.OneToOneField('Phieuthanhtoan', models.DO_NOTHING, db_column='sophieuthanhtoan', primary_key=True)
    matintuyendung = models.ForeignKey('Tintuyendung', models.DO_NOTHING, db_column='matintuyendung')
    sotien = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'chitietthanhtoan'
        unique_together = (('sophieuthanhtoan', 'matintuyendung'),)


class Chuyennganh(models.Model):
    machuyennganh = models.FloatField(primary_key=True)
    tenchuyennganh = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'chuyennganh'


class Congty(models.Model):
    macongty = models.FloatField(primary_key=True)
    tencongty = models.CharField(unique=True, max_length=255)
    motacongty = models.TextField(blank=True, null=True)
    diachict = models.CharField(max_length=255)
    quymonhansu = models.CharField(max_length=255, blank=True, null=True)
    logo = models.BinaryField(null=True)
    dienthoai = models.CharField(unique=True, max_length=10)
    website = models.CharField(unique=True, max_length=500)
    taikhoan = models.ForeignKey('Taikhoan', models.DO_NOTHING, db_column='taikhoan', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'congty'


class Hinhthuclamviec(models.Model):
    mahtlamviec = models.FloatField(primary_key=True)
    tenhinhthuclamviec = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'hinhthuclamviec'


class Hocvanbangcap(models.Model):
    mahvbc = models.FloatField(primary_key=True)
    tenbangcapchungchi = models.CharField(max_length=255)
    tentruong = models.CharField(max_length=255, blank=True, null=True)
    xeploai = models.FloatField(blank=True, null=True)
    thoigianbatdaunh = models.DateField(blank=True, null=True)
    thoigianketthuc = models.DateField(blank=True, null=True)
    thongtinbosung = models.TextField(blank=True, null=True)
    maungvien = models.ForeignKey('Ungvien', models.DO_NOTHING, db_column='maungvien', blank=True, null=True)
    machuyennganh = models.ForeignKey(Chuyennganh, models.DO_NOTHING, db_column='machuyennganh', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'hocvanbangcap'


class Kinhnghiemlamviec(models.Model):
    makinhnghiem = models.FloatField(primary_key=True)
    tencongviectunglam = models.CharField(max_length=255)
    thoigianbd = models.DateField()
    thoigiankt = models.DateField()
    motacv = models.TextField(blank=True, null=True)
    tencongtytunglamviec = models.CharField(max_length=255, blank=True, null=True)
    maungvien = models.ForeignKey('Ungvien', models.DO_NOTHING, db_column='maungvien', blank=True, null=True)
    macapbac = models.ForeignKey(Capbac, models.DO_NOTHING, db_column='macapbac', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'kinhnghiemlamviec'


class Kynang(models.Model):
    makynang = models.FloatField(primary_key=True)
    tenkynang = models.CharField(max_length=255)
    maloaikynang = models.ForeignKey('Loaikynang', models.DO_NOTHING, db_column='maloaikynang', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'kynang'


class Kynangquantrong(models.Model):
    matintuyendung = models.OneToOneField('Tintuyendung', models.DO_NOTHING, db_column='matintuyendung', primary_key=True)
    makynang = models.ForeignKey(Kynang, models.DO_NOTHING, db_column='makynang')

    class Meta:
        managed = False
        db_table = 'kynangquantrong'
        unique_together = (('matintuyendung', 'makynang'),)


class Loaikynang(models.Model):
    maloaikynang = models.FloatField(primary_key=True)
    tenloaikynang = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'loaikynang'


class Mucluong(models.Model):
    mamucluong = models.FloatField(primary_key=True)
    tu = models.FloatField()
    den = models.FloatField()

    class Meta:
        managed = False
        db_table = 'mucluong'


class Nguoithamkhao(models.Model):
    manguoithamkhao = models.FloatField(primary_key=True)
    tenntk = models.CharField(max_length=255)
    sdtntk = models.CharField(unique=True, max_length=10)
    emailntk = models.CharField(unique=True, max_length=255)
    tencongtyntk = models.CharField(max_length=255, blank=True, null=True)
    maungvien = models.ForeignKey('Ungvien', models.DO_NOTHING, db_column='maungvien', blank=True, null=True)
    macapbac = models.ForeignKey(Capbac, models.DO_NOTHING, db_column='macapbac', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'nguoithamkhao'


class Phieudanhgia(models.Model):
    sophieudanhgia = models.FloatField(primary_key=True)
    ngaydanhgia = models.DateField()
    sophieuungtuyen = models.ForeignKey('Phieuungtuyen', models.DO_NOTHING, db_column='sophieuungtuyen', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'phieudanhgia'


class Phieuthanhtoan(models.Model):
    sophieuthanhtoan = models.FloatField(primary_key=True)
    ngaythanhtoan = models.DateField()

    class Meta:
        managed = False
        db_table = 'phieuthanhtoan'


class Phieuungtuyen(models.Model):
    sophieuungtuyen = models.FloatField(primary_key=True)
    vitriungtuyen = models.CharField(max_length=255)
    sonamkinhnghiem = models.CharField(max_length=50, blank=True, null=True)
    muctieunghenghiep = models.TextField(blank=True, null=True)
    kynangchuyenmon = models.TextField(blank=True, null=True)
    ngayungtuyen = models.DateField(blank=True, null=True)
    ngayphongvan = models.DateField(blank=True, null=True)
    maungvien = models.ForeignKey('Ungvien', models.DO_NOTHING, db_column='maungvien', blank=True, null=True)
    matrinhdohocvan = models.ForeignKey('Trinhdohocvan', models.DO_NOTHING, db_column='matrinhdohocvan', blank=True, null=True)
    mahtlamviec = models.ForeignKey(Hinhthuclamviec, models.DO_NOTHING, db_column='mahtlamviec', blank=True, null=True)
    macapbac = models.ForeignKey(Capbac, models.DO_NOTHING, db_column='macapbac', blank=True, null=True)
    maquanhuyen = models.ForeignKey('Quanhuyen', models.DO_NOTHING, db_column='maquanhuyen', blank=True, null=True)
    mamucluong = models.ForeignKey(Mucluong, models.DO_NOTHING, db_column='mamucluong', blank=True, null=True)
    matintuyendung = models.ForeignKey('Tintuyendung', models.DO_NOTHING, db_column='matintuyendung', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'phieuungtuyen'


class Quanhuyen(models.Model):
    maquanhuyen = models.FloatField(primary_key=True)
    tenquanhuyen = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'quanhuyen'


class Taikhoan(models.Model):
    taikhoan = models.CharField(primary_key=True, max_length=255)
    matkhau = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'taikhoan'


class Tieuchi(models.Model):
    matieuchi = models.FloatField(primary_key=True)
    tentieuchi = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'tieuchi'


class Tintuyendung(models.Model):
    matintuyendung = models.FloatField(primary_key=True)
    tencongviectd = models.CharField(max_length=255)
    mota = models.TextField()
    quyenloiduochuong = models.TextField()
    yeucaucongviec = models.TextField()
    yeucauhoso = models.TextField()
    hannophoso = models.DateField()
    yeucaukinhnghiem = models.TextField()
    soluongtuyen = models.FloatField()
    yeucaugioitinh = models.FloatField(blank=True, null=True)
    tennguoilienhe = models.CharField(max_length=255, blank=True, null=True)
    sdtnlh = models.CharField(max_length=10, blank=True, null=True)
    emailnlh = models.CharField(max_length=255, blank=True, null=True)
    ngonnguhoso = models.CharField(max_length=50, blank=True, null=True)
    macongty = models.ForeignKey(Congty, models.DO_NOTHING, db_column='macongty', blank=True, null=True)
    maquanhuyen = models.ForeignKey(Quanhuyen, models.DO_NOTHING, db_column='maquanhuyen', blank=True, null=True)
    mahtlamviec = models.ForeignKey(Hinhthuclamviec, models.DO_NOTHING, db_column='mahtlamviec', blank=True, null=True)
    macapbac = models.ForeignKey(Capbac, models.DO_NOTHING, db_column='macapbac', blank=True, null=True)
    matrinhdohocvan = models.ForeignKey('Trinhdohocvan', models.DO_NOTHING, db_column='matrinhdohocvan', blank=True, null=True)
    mamucluong = models.ForeignKey(Mucluong, models.DO_NOTHING, db_column='mamucluong', blank=True, null=True)
    machuyennganh = models.ForeignKey(Chuyennganh, models.DO_NOTHING, db_column='machuyennganh', blank=True, null=True)
    hanguutien = models.ForeignKey(Banggia, models.DO_NOTHING, db_column='hanguutien', blank=True, null=True,related_name='topic_hanguutien')
    goituan = models.ForeignKey(Banggia, models.DO_NOTHING, db_column='goituan', blank=True, null=True,related_name='topic_goituan')

    class Meta:
        managed = False
        db_table = 'tintuyendung'


class Trinhdohocvan(models.Model):
    matrinhdohocvan = models.FloatField(primary_key=True)
    tentrinhdohocvan = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'trinhdohocvan'


class Trinhdokynang(models.Model):
    maungvien = models.OneToOneField('Ungvien', models.DO_NOTHING, db_column='maungvien', primary_key=True)
    makynang = models.ForeignKey(Kynang, models.DO_NOTHING, db_column='makynang')
    trinhdokynang = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'trinhdokynang'
        unique_together = (('maungvien', 'makynang'),)


class Ungvien(models.Model):
    maungvien = models.FloatField(primary_key=True)
    hotenuv = models.CharField(max_length=255)
    sdtuv = models.CharField(unique=True, max_length=10)
    emailuv = models.CharField(unique=True, max_length=255)
    ngaysinhuv = models.DateField(blank=True, null=True)
    quoctich = models.CharField(max_length=255, blank=True, null=True)
    diachiungvien = models.CharField(max_length=255, blank=True, null=True)
    gioitinh = models.FloatField(blank=True, null=True)
    tinhtranghonnhan = models.FloatField(blank=True, null=True)
    anhdaidien = models.BinaryField(blank=True, null=True)
    taikhoan = models.ForeignKey(Taikhoan, models.DO_NOTHING, db_column='taikhoan', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ungvien'