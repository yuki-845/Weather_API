from django.shortcuts import render
import requests


# Create your views here.
def confirm(request):
    if request.method == 'POST':

        #選択された地域のIDを取得
        choice = request.POST.get('choice') 

        #天気予報APIのURL
        base_url = 'https://weather.tsukumijima.net/api/forecast'

        #パラメータをURLエンコードする
        params = {'city': choice}

        #データをリクエスト
        response = requests.get(base_url, params=params)

        #選択した地名
        place_name = response.json()['location']['prefecture']
        
        #今日の日付
        today_date = response.json()['forecasts'][0]['date'].replace("-","/") #"-"から"/"に置換        
        
        #天気の画像
        weather_image = response.json()['forecasts'][0]['image']['url']
        
        #１日の天気の移り変わり
        change_weather = response.json()['forecasts'][0]['telop']
        
        #最高気温
        max_temp = response.json()['forecasts'][0]['temperature']['min']['celsius']
        
        #最低気温
        min_temp = response.json()['forecasts'][0]['temperature']['max']['celsius']
        
        #選択ボタンを押された際confirm.htmlに出動
        return render(request, 'weather_app/confirm.html', {'place_name': place_name, 'today_date': today_date, 'weather_image': weather_image, 'change_weather': change_weather, 'max_temp': max_temp, 'min_temp': min_temp})
        
    # GETリクエストの場合はindex.htmlを表示
    return render(request, 'weather_app/index.html')