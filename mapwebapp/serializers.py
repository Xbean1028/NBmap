from mapwebapp.models import User, Derive,Data,Setting
from rest_framework import serializers


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
        # fields = ['url', 'username', 'email', 'groups']


class DeriveSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Derive
        fields = '__all__'

class DataSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Data
        fields = '__all__'

class SettingSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Setting
        fields = '__all__'