#Display today's date.
from datetime import datetime

today = datetime.now()

print("Today's Date:", today.strftime("%d-%m-%Y"))
print(today)