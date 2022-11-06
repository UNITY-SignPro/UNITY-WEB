# from rest_framework import serializers
# from .models import Translate

# class TranslateSerializer(serializers.ModelSerializer) :
#     class Meta :
#         model = Translate
#         fields = ('id','content')

from rest_framework import serializers
from .models import Translate

class TranslateSerializer(serializers.ModelSerializer) :
    class Meta :
        model = Translate
        fields = ['content']
    content = serializers.CharField(max_length=100)

