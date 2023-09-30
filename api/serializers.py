from rest_framework import serializers
from translate import Translator

from main.models import TranslateText


class TranslateTextSerializer(serializers.ModelSerializer):
    """
    Model serializer to return only two of the fields from all the fields.
    """

    class Meta:
        model = TranslateText
        fields = ['original_text', 'translated_text']
