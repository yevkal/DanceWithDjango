from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound

# Create your views here.


zodiac_dict = {

    'aries': 'Знак зодиака овен',
    'taurus': 'Знак зодиака телец',
    'gemini': 'Знак зодиака близнецы',
    'cancer': 'Знак зодиака рак',
    'leo': 'Знак зодиака лев',
    'virgo': 'Знак зодиака дева',
    'libra': 'Знак зодиака весы',
    'scorpio': 'Знак зодиака скорпион',
    'sagittarius': 'Знак зодиака стрелец',
    'capricorn': 'Знак зодиака козерог',
    'aquarius': 'Знак зодиака водолей',
    'pisces': 'Знак зодиака рыбы'

}


def get_info_about_sign_zodiac(request, sign_zodiac : str):
    description = zodiac_dict.get(sign_zodiac)
    if description:
        return HttpResponse(description)
    else:
        return HttpResponseNotFound(f"Неизвестный знак зодиака {sign_zodiac}")


def get_info_about_sign_zodiac_by_numbers(request, sign_zodiac : int):
    return HttpResponse(f"This is number {sign_zodiac}")
