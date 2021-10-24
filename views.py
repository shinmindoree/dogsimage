from django.shortcuts import render
import requests
from .models import DogImage

def index(request):
    #강아지 사진 랜덤확인
    #api 요청
    r = requests.get('https://dog.ceo/api/breeds/image/random')
    # API 응답 Dict로 변환
    r_json = r.json()

    
    message = r_json['message']
    status = r_json['status']
    
    # api로 수신한 데이터 model에 저장
    dog_image, created = DogImage.objects.get_or_create(url=message, defaults={'url': message})
    
    print(f'{dog_image} - {created}' )
    print(dog_image.url)
    print(type(dog_image.url))
    print(type(dog_image))
    print(type(created))

    context ={
        'image_url':message
    }
    #응답

    return render(request, 'index.html', context)