from rest_framework import serializers
from .models import (
    GuruhgaOid, Nomlanishi, Rusumi, Xususiyatlari, 
    XujjatTuri, Davlat, Viloyat, Tuman, Mahalla, Rangi, 
    DetelName, TashkilotTuri, Modda, Qism, Band, JinoyatIshi, 
    JismoniyShaxs, YuridikShaxs, HisobSababi, BuyumInfo, 
    JinoyatRegistr, DetelsInfo, Fabula
)

class GuruhgaOidSerializer(serializers.ModelSerializer):
    class Meta:
        model = GuruhgaOid
        fields = '__all__'

class NomlanishiSerializer(serializers.ModelSerializer):
    class Meta:
        model = Nomlanishi
        fields = '__all__'

class RusumiSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rusumi
        fields = '__all__'

class XususiyatlariSerializer(serializers.ModelSerializer):
    class Meta:
        model = Xususiyatlari
        fields = '__all__'

class XujjatTuriSerializer(serializers.ModelSerializer):
    class Meta:
        model = XujjatTuri
        fields = '__all__'

class DavlatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Davlat
        fields = '__all__'

class ViloyatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Viloyat
        fields = '__all__'

class TumanSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tuman
        fields = '__all__'

class MahallaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mahalla
        fields = '__all__'

class RangiSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rangi
        fields = '__all__'

class DetelNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = DetelName
        fields = '__all__'

class TashkilotTuriSerializer(serializers.ModelSerializer):
    class Meta:
        model = TashkilotTuri
        fields = '__all__'

class ModdaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Modda
        fields = '__all__'

class QismSerializer(serializers.ModelSerializer):
    class Meta:
        model = Qism
        fields = '__all__'

class BandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Band
        fields = '__all__'

class JinoyatIshiSerializer(serializers.ModelSerializer):
    class Meta:
        model = JinoyatIshi
        fields = '__all__'

class JismoniyShaxsSerializer(serializers.ModelSerializer):
    class Meta:
        model = JismoniyShaxs
        fields = '__all__'

class YuridikShaxsSerializer(serializers.ModelSerializer):
    class Meta:
        model = YuridikShaxs
        fields = '__all__'

class HisobSababiSerializer(serializers.ModelSerializer):
    class Meta:
        model = HisobSababi
        fields = '__all__'

class BuyumInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = BuyumInfo
        fields = '__all__'

class DetelsInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = DetelsInfo
        fields = '__all__'

class JinoyatRegistrSerializer(serializers.ModelSerializer):
    class Meta:
        model = JinoyatRegistr
        fields = '__all__'

class FabulaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fabula
        fields = '__all__'
