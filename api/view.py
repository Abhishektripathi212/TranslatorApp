from django.http import JsonResponse
from rest_framework.viewsets import ViewSet
from translate import Translator
from main.models import TranslateText
from .serializers import TranslateTextSerializer
from .utils import check_request_has_required_parameters


class TranslateTextApi(ViewSet):
    serializer_class = TranslateTextSerializer

    def list(self, request):
        """
        GET api to return translation of text provided by user.
        Expecting parameters:
         from_language: language in which user provided text.
         to_language: language in which user want translation of provided text.
         original_text: text to convert, can be word/sentence.
        """

        request_data = request.GET
        # function return list of parameters if any of the parameter missing in request.
        required_parameters = check_request_has_required_parameters(request_data,
                                                                    ['from_language', 'to_language', 'original_text'])
        if required_parameters:
            return JsonResponse({'data': {'message': f'{", ".join(required_parameters)} are required.'}}, status=400)

        from_language = request.GET['from_language']
        to_language = request.GET['to_language']
        original_text = request.GET['original_text']
        try:
            # orm query to get data form database if all three parameters matches, work as cache as of now.
            translate_text_obj = TranslateText.objects.get(from_language=from_language,
                                                           to_language=to_language, original_text=original_text)
            serializer_data = self.serializer_class(translate_text_obj)

        except TranslateText.DoesNotExist:
            # when data related to parameters is not in the database then create that entry into database
            # then return the value.

            translator = Translator(to_lang=to_language)
            translated_text = translator.translate(original_text)
            translate_text_object = TranslateText.objects.create(from_language=from_language,
                                                                 original_text=original_text,
                                                                 to_language=to_language,
                                                                 translated_text=translated_text
                                                                 )
            serializer_data = self.serializer_class(translate_text_object)
        except Exception as e:
            serializer_data = {'data': {'translated_text': str(e)}}

        return JsonResponse({'data': serializer_data.data}, status=200)
