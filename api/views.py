from rest_framework import viewsets
from .models import (
    GuruhgaOid, Nomlanishi, Rusumi, Xususiyatlari, 
    XujjatTuri, Davlat, Viloyat, Tuman, 
    Mahalla, Rangi, DetelName, TashkilotTuri, Modda, Qism, 
    Band, JinoyatIshi, JismoniyShaxs, YuridikShaxs, 
    HisobSababi, BuyumInfo, DetelsInfo, JinoyatRegistr, Fabula
)
from .serializers import (
    GuruhgaOidSerializer, NomlanishiSerializer, RusumiSerializer, 
    XususiyatlariSerializer, 
    XujjatTuriSerializer, DavlatSerializer, 
    ViloyatSerializer, TumanSerializer, MahallaSerializer, 
    RangiSerializer, DetelNameSerializer, TashkilotTuriSerializer, 
    ModdaSerializer, QismSerializer, BandSerializer, JinoyatIshiSerializer, 
    JismoniyShaxsSerializer, YuridikShaxsSerializer, 
    HisobSababiSerializer, BuyumInfoSerializer, 
    DetelsInfoSerializer, JinoyatRegistrSerializer, FabulaSerializer
)

class GuruhgaOidViewSet(viewsets.ModelViewSet):
    queryset = GuruhgaOid.objects.all()
    serializer_class = GuruhgaOidSerializer

class NomlanishiViewSet(viewsets.ModelViewSet):
    queryset = Nomlanishi.objects.all()
    serializer_class = NomlanishiSerializer

class RusumiViewSet(viewsets.ModelViewSet):
    queryset = Rusumi.objects.all()
    serializer_class = RusumiSerializer

class XususiyatlariViewSet(viewsets.ModelViewSet):
    queryset = Xususiyatlari.objects.all()
    serializer_class = XususiyatlariSerializer

class XujjatTuriViewSet(viewsets.ModelViewSet):
    queryset = XujjatTuri.objects.all()
    serializer_class = XujjatTuriSerializer

class DavlatViewSet(viewsets.ModelViewSet):
    queryset = Davlat.objects.all()
    serializer_class = DavlatSerializer

class ViloyatViewSet(viewsets.ModelViewSet):
    queryset = Viloyat.objects.all()
    serializer_class = ViloyatSerializer

class TumanViewSet(viewsets.ModelViewSet):
    queryset = Tuman.objects.all()
    serializer_class = TumanSerializer

class MahallaViewSet(viewsets.ModelViewSet):
    queryset = Mahalla.objects.all()
    serializer_class = MahallaSerializer

class RangiViewSet(viewsets.ModelViewSet):
    queryset = Rangi.objects.all()
    serializer_class = RangiSerializer

class DetelNameViewSet(viewsets.ModelViewSet):
    queryset = DetelName.objects.all()
    serializer_class = DetelNameSerializer

class TashkilotTuriViewSet(viewsets.ModelViewSet):
    queryset = TashkilotTuri.objects.all()
    serializer_class = TashkilotTuriSerializer

class ModdaViewSet(viewsets.ModelViewSet):
    queryset = Modda.objects.all()
    serializer_class = ModdaSerializer

class QismViewSet(viewsets.ModelViewSet):
    queryset = Qism.objects.all()
    serializer_class = QismSerializer

class BandViewSet(viewsets.ModelViewSet):
    queryset = Band.objects.all()
    serializer_class = BandSerializer

class JinoyatIshiViewSet(viewsets.ModelViewSet):
    queryset = JinoyatIshi.objects.all()
    serializer_class = JinoyatIshiSerializer

class JismoniyShaxsViewSet(viewsets.ModelViewSet):
    queryset = JismoniyShaxs.objects.all()
    serializer_class = JismoniyShaxsSerializer

class YuridikShaxsViewSet(viewsets.ModelViewSet):
    queryset = YuridikShaxs.objects.all()
    serializer_class = YuridikShaxsSerializer

class HisobSababiViewSet(viewsets.ModelViewSet):
    queryset = HisobSababi.objects.all()
    serializer_class = HisobSababiSerializer

class BuyumInfoViewSet(viewsets.ModelViewSet):
    queryset = BuyumInfo.objects.all()
    serializer_class = BuyumInfoSerializer

class DetelsInfoViewSet(viewsets.ModelViewSet):
    queryset = DetelsInfo.objects.all()
    serializer_class = DetelsInfoSerializer

class JinoyatRegistrViewSet(viewsets.ModelViewSet):
    queryset = JinoyatRegistr.objects.all()
    serializer_class = JinoyatRegistrSerializer

class FabulaViewSet(viewsets.ModelViewSet):
    queryset = Fabula.objects.all()
    serializer_class = FabulaSerializer
