from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    GuruhgaOidViewSet, NomlanishiViewSet, RusumiViewSet, 
    XususiyatlariViewSet,
    XujjatTuriViewSet, DavlatViewSet, ViloyatViewSet, TumanViewSet, 
    MahallaViewSet, RangiViewSet, DetelNameViewSet, 
    TashkilotTuriViewSet, ModdaViewSet, QismViewSet, 
    BandViewSet, JinoyatIshiViewSet, JismoniyShaxsViewSet, 
    YuridikShaxsViewSet, HisobSababiViewSet, BuyumInfoViewSet, 
    DetelsInfoViewSet, JinoyatRegistrViewSet, FabulaViewSet
)

router = DefaultRouter()
router.register('guruhgaoid', GuruhgaOidViewSet)
router.register('nomlanishi', NomlanishiViewSet)
router.register('rusumi', RusumiViewSet)
router.register('xususiyatlari', XususiyatlariViewSet)
router.register('xujjatturi', XujjatTuriViewSet)
router.register('davlat', DavlatViewSet)
router.register('viloyat', ViloyatViewSet)
router.register('tuman', TumanViewSet)
router.register('mahalla', MahallaViewSet)
router.register('rangi', RangiViewSet)
router.register('detelname', DetelNameViewSet)
router.register('tashkilotturi', TashkilotTuriViewSet)
router.register('modda', ModdaViewSet)
router.register('qism', QismViewSet)
router.register('band', BandViewSet)
router.register('jinoyatishi', JinoyatIshiViewSet)
router.register('jismoniyshaxs', JismoniyShaxsViewSet)
router.register('yuridikshaxs', YuridikShaxsViewSet)
router.register('hisobsababi', HisobSababiViewSet)
router.register('buyuminfo', BuyumInfoViewSet)
router.register('detelsinfo', DetelsInfoViewSet)
router.register('jinoyatregistr', JinoyatRegistrViewSet)
router.register('fabula', FabulaViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
