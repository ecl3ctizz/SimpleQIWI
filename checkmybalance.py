import SimpleQIWI

from SimpleQIWI import *

token = "Your Token Qiwi/Ваш токен киви"

phone = "Your Phone Number/Ваш номер телефона"

api = QApi(token=token, phone=phone)

print("Your balance:",api.balance)
