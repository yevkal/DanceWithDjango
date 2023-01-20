from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
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

def index(request):
    zodiacs = list(zodiac_dict)
    li_elements = ''

    for  sign in zodiacs:
        redirect_path = reverse('horoscope_name', args=[sign])
        li_elements+=f"<li> <a href = '{redirect_path}'> {sign.title()}</a></li>"
    responce = f"""
    <ul>
        {li_elements}
    </ul>
    """
    return HttpResponse(responce)


def get_info_about_sign_zodiac(request, sign_zodiac : str):
    description = zodiac_dict.get(sign_zodiac)
    if description:
        return HttpResponse(description)
    else:
        return HttpResponseNotFound(f"Неизвестный знак зодиака {sign_zodiac}")


def get_info_about_sign_zodiac_by_numbers(request, sign_zodiac : int):
    zodiacs = list(zodiac_dict)
    if sign_zodiac>len(zodiacs):
        return HttpResponseNotFound(f"Не правильный порядковый номер зодиака - {sign_zodiac}")
    name_zodiac = zodiacs[sign_zodiac-1]
    redirect_url = reverse('horoscope_name', args = [name_zodiac])
    return HttpResponseRedirect(f"/horoscope/{name_zodiac}")
