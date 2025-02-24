from django.contrib import admin
from .models import (
    GuruhgaOid, Nomlanishi, Rusumi, Xususiyatlari, 
    XujjatTuri, Davlat, Viloyat, Tuman, Mahalla, Rangi, 
    DetelName, TashkilotTuri, Modda, Qism, Band, JinoyatIshi, 
    JismoniyShaxs, YuridikShaxs, HisobSababi, BuyumInfo, 
    DetelsInfo, JinoyatRegistr, Fabula
)

# Oddiy ro'yxatdan o'tkazish
admin.site.register(GuruhgaOid)
admin.site.register(Nomlanishi)
admin.site.register(Rusumi)
admin.site.register(Xususiyatlari)
admin.site.register(XujjatTuri)
admin.site.register(Davlat)
admin.site.register(Viloyat)
admin.site.register(Tuman)
admin.site.register(Mahalla)
admin.site.register(Rangi)
admin.site.register(DetelName)
admin.site.register(TashkilotTuri)
admin.site.register(Modda)
admin.site.register(Qism)
admin.site.register(Band)
admin.site.register(JinoyatIshi)
admin.site.register(JismoniyShaxs)
admin.site.register(YuridikShaxs)
admin.site.register(HisobSababi)
admin.site.register(BuyumInfo)
admin.site.register(DetelsInfo)
admin.site.register(JinoyatRegistr)
admin.site.register(Fabula)
