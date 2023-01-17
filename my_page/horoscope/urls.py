from django.urls import path
from .views import *

urlpatterns = [
    path('leo/', leo),
    path('scorpio/', scorpio),
    path('aries/', aries),
    path('taurus/', taurus),
    path('gemini/', gemini),
    path('cancer/', cancer),
    path('virgo/', virgo),
    path('libra/', libra),
    path('sagittarius/', sagittarius),
    path('capricorn/', capricorn),
    path('aquarius/', aquarius),
    path('pisces/', pisces),
]