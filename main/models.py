from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class BaseModel(models.Model):
    """
    Base model which can inherit in every model
    """
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class TranslateText(BaseModel):
    """
    Model to keep store user text with there translated text.
    """
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING, null=True, blank=True)
    from_language = models.CharField(max_length=100, null=True, blank=True)
    original_text = models.TextField()
    to_language = models.CharField(max_length=100, null=True, blank=True)
    translated_text = models.TextField()

    def __str__(self):
        return str(self.original_text)

    class Meta:
        db_table = 'translate_text'
        verbose_name = 'Translate Text'
        verbose_name_plural = 'Translate Texts'
