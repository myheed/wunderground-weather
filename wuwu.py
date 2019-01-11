import pandas as pd
from math import floor
import requests

Date = []
Time = []
Temp = []
Bodytemp = []
Dew = []
Humidity = []
Pressure = []
Visibility = []
Wind_dir = []
Wind_speed = []
Gust_speed = []
Condition = []
days_of_month = [30,31,31,30,31,30,31,31,28,31,30,31,30,31,31,30]
url_tmpl = 'https://api.weather.com/v1/geocode/3.13027811/101.5513916/observations/historical.json?apiKey=6532d6454b8aa370768e63d6ba5a832e&startDate={}01&endDate={}&units=e'
months = ["201606", "201607", "201608", "201609", "201610", "201611", "201612", "201701", "201702", "201703", "201704",
          "201705", "201706", "201707", "201708", "201709"]
for i, month in enumerate(months):
    hours = 0
    if i == len(months) - 1:
        continue
    url = url_tmpl.format(month, month + str(days_of_month[i]))
    r = requests.get(url)
    result = r.json()
    if 'observations' not in result:
        continue
    observations = result['observations']
    for observation in observations:
        day = floor(hours / 24)+1
        day_str = '0' + str(day) if day < 10 else str(day)
        Date.append(month + day_str)
        hour = hours % 24
        hour_str = '0' + str(hour) if (hour) < 10 else str(hour)
        Time.append(hour_str + ":00")
        Temp.append(observation['temp'])
        Dew.append(observation['dewPt'])
        Bodytemp.append(observation['feels_like'])
        Humidity.append(observation['rh'])
        Pressure.append(observation['pressure'])
        Visibility.append(observation['vis'])
        Wind_dir.append(observation['wdir'])
        Wind_speed.append(observation['wspd'])
        Gust_speed.append(observation['gust'])
        Condition.append(observation['wx_phrase'])
        hours += 1

Date = pd.DataFrame(Date, columns=['Date'])
Time = pd.DataFrame(Time, columns=['Time'])
Temp = pd.DataFrame(Temp, columns=['Temp'])
Bodytemp = pd.DataFrame(Bodytemp, columns=['Bodytemp'])
Dew = pd.DataFrame(Dew, columns=['Dew'])
Humidity = pd.DataFrame(Humidity, columns=['Humidity'])
Pressure = pd.DataFrame(Pressure, columns=['Pressure'])
Visibility = pd.DataFrame(Visibility, columns=['Visibility'])
Wind_dir = pd.DataFrame(Wind_dir, columns=['Wind_dir'])
Wind_speed = pd.DataFrame(Wind_speed, columns=['Wind_speed'])
Gust_speed = pd.DataFrame(Gust_speed, columns=['Gust_speed'])
Condition = pd.DataFrame(Condition, columns=['Condition'])

sub_result = pd.concat(
    [Date, Time, Temp, Bodytemp, Dew, Humidity, Pressure, Visibility, Wind_dir, Wind_speed, Gust_speed, Condition],
    axis=1)

file_name = "Weather" + '.csv'
sub_result.to_csv(file_name, index=False)
