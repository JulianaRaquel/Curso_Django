from django.contrib.admin import ModelAdmin, register
from pypro32.aperitivos.models import Video


@register(Video)
class Videoadmin(ModelAdmin):
    pass
