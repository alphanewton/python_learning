import requests
from twilio.rest import Client

API_KEY = "MyAPIkey"
OWM_endpoint = "https://api.openweathermap.org/data/2.5/weather"
account_sid = "MyAccoundID"
auth_token = "MyAuthToken"

weather_params = {
    # "lat": 28.704060,
    "lat": -33.868820,

    # "lon": 77.102493,
    "lon": 151.209290,

    "appid": API_KEY,
    "exclude": "current,minutely,daily"
}

response = requests.get(OWM_endpoint, params=weather_params)
condition_code = int(response.json()["weather"][0]["id"])

if condition_code < 700:
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        body="It's going to rain today. Remember to bring an umbrella☔️",
        from_='+15075744225',
        to='MyNumber'
    )
    print(message.status)

    