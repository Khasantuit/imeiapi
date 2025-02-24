from django.db import models
from django.core.exceptions import ValidationError
   
class GuruhgaOid(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name
    
class Nomlanishi(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name
    
class Rusumi(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name
    
class Xususiyatlari(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name
 
class XujjatTuri(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name
    
class Davlat(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name
    
class Viloyat(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name
    
class Tuman(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name
    
class Mahalla(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name
    
class Rangi(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class DetelName(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class TashkilotTuri(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Modda(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name
    
class Qism(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Band(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name
    
class JinoyatIshi(models.Model):
    name = models.CharField(max_length=255)
    modda = models.ForeignKey(Modda, on_delete=models.CASCADE)
    qism = models.ForeignKey(Qism, on_delete=models.CASCADE)
    band = models.ForeignKey(Band, on_delete=models.CASCADE)
   
    def __str__(self):
        return self.name
    
class JismoniyShaxs(models.Model):
    pinfl_raqami = models.CharField(max_length=100, blank=True, null=True)
    pasport_seriya = models.CharField(max_length=100, blank=True, null=True)
    pasport_raqam = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.pinfl_raqami

class YuridikShaxs(models.Model):
    tashkilot_turi = models.ForeignKey(TashkilotTuri, on_delete=models.CASCADE)
    tashkilot_nomi = models.CharField(max_length=255)
    mamlakat = models.ForeignKey(Davlat, on_delete=models.CASCADE)
    viloyat = models.ForeignKey(Viloyat, on_delete=models.CASCADE)
    tuman = models.ForeignKey(Tuman, on_delete=models.CASCADE)
    mahalla = models.ForeignKey(Mahalla, on_delete=models.CASCADE)
    kocha = models.CharField(max_length=255)
    uy = models.CharField(max_length=50)
    korpus = models.CharField(max_length=50, blank=True, null=True)
    xonadon = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return self.tashkilot_nomi
    
class HisobSababi(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class BuyumInfo(models.Model):
    SHAXS_TURI = (
        ('jismoniy', 'Jismoniy Shaxs'),
        ('yuridik', 'Yuridik Shaxs')
    )
    # Umumiy ma'lumotlar
    seriya = models.CharField(max_length=100)
    raqam = models.CharField(max_length=100)
    soni = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    zavod_firma = models.CharField(max_length=100)
    buyum_fotosurati = models.TextField(blank=True, null=True)

    # Ishlab chiqarish ma'lumotlari
    guruh = models.ForeignKey(GuruhgaOid, on_delete=models.CASCADE)
    nomlanishi = models.ForeignKey(Nomlanishi, on_delete=models.CASCADE)
    rusumi = models.ForeignKey(Rusumi, on_delete=models.CASCADE)
    ishlab_chiqarilgan_davlat = models.ForeignKey(Davlat, on_delete=models.CASCADE)
    rangi = models.ForeignKey(Rangi, on_delete=models.CASCADE)
    shaxs_turi = models.CharField(max_length=10, choices=SHAXS_TURI)
    jismoniy_shaxs = models.ForeignKey(JismoniyShaxs, on_delete=models.SET_NULL, null=True, blank=True)
    yuridik_shaxs = models.ForeignKey(YuridikShaxs, on_delete=models.SET_NULL, null=True, blank=True)
    xususiyatlari = models.ForeignKey(Xususiyatlari, on_delete=models.CASCADE)
    ishlab_chiqarilgan_yili = models.CharField(max_length=4)

    def clean(self):
        if self.shaxs_turi == 'jismoniy' and self.yuridik_shaxs is not None:
            raise ValidationError("Jismoniy shaxs tanlanganida, Yuridik shaxs bo'sh bo'lishi kerak.")
        elif self.shaxs_turi == 'yuridik' and self.jismoniy_shaxs is not None:
            raise ValidationError("Yuridik shaxs tanlanganida, Jismoniy shaxs bo'sh bo'lishi kerak.")

    def __str__(self):
        return f"{self.model} - {self.seriya} - {self.raqam}"
    
class DetelsInfo(models.Model):
    detal_nomi = models.ForeignKey(DetelName, on_delete=models.CASCADE)
    detal_modeli = models.CharField(max_length=100)
    detal_seriyasi = models.CharField(max_length=100)
    detal_raqami = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.detal_nomi} - {self.detal_modeli} - {self.detal_seriyasi}"
    
class JinoyatRegistr(models.Model):
    HISOB_TURI = (
        ('material', 'Material/Protokol'),
        ('jinoyat', 'Jinoyat ishi')
    )
    hisob_sababi = models.ForeignKey(HisobSababi, on_delete=models.CASCADE)
    hujjat_turi = models.CharField(max_length=10, choices=HISOB_TURI)
    material_raqami = models.CharField(max_length=100)
    jinoyat_ishi = models.ForeignKey(JinoyatIshi, on_delete=models.SET_NULL, null=True, blank=True)
#Bu parametrlar User ma'lumotlaridan olinadi
    # tashkilot = models.CharField(max_length=255)
    # hudud = models.CharField(max_length=100)
    # organ = models.CharField(max_length=255)

    def save(self, *args, **kwargs):
        if self.hujjat_turi == 'jinoyat':
            self.material_raqami = self.jinoyat_ishi.name
        else:
            self.material_raqami = None
        super(JinoyatRegistr, self).save(*args, **kwargs)
    
    def __str__(self):
        return self.material_raqami or "Noma'lum"
    
class Fabula(models.Model):
    yoqotish_tavsifi = models.TextField()
    yoqotilgan_sana = models.DateField()
    yoqotilgan_viloyat = models.ForeignKey(Viloyat, on_delete=models.CASCADE)
    yoqotilgan_tuman = models.ForeignKey(Tuman, on_delete=models.CASCADE)
    yoqotilgan_mahalla = models.ForeignKey(Mahalla, on_delete=models.CASCADE)
    yoqotilgan_joy = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.yoqotish_tavsifi[:30]}..."  # Tavsifdan faqat dastlabki 30 ta belgi ko'rsatiladi
