#1)
from datetime import date, timedelta

today = date.today()
print(today - timedelta(days=5))
#2) Вчера, сегодня, завтра
from datetime import date, timedelta

today = date.today()
print(today - timedelta(days=1))  # yesterday
print(today)                      # today
print(today + timedelta(days=1))  # tomorrow
#3) Убрать микросекунды
from datetime import datetime

now = datetime.now()
print(now.replace(microsecond=0))
#4) Разница между двумя датами в секундах (вводим 2 строки)
 
 
from datetime import datetime

a = datetime.strptime(input(), "%Y-%m-%d %H:%M:%S")
b = datetime.strptime(input(), "%Y-%m-%d %H:%M:%S")

print(int((b - a).total_seconds()))