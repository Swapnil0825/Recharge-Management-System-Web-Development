from __future__ import print_function
import eel
from Files.models.login import save_register, recovery_password, login_user
from Files.models.menu import recharge,addmoney,Balance

eel.init('Files')

@eel.expose 
def btn_save(name, phone, login, passw, email):
    msg = save_register(name, phone, login, passw, email)
    eel.save_return(str(msg))

@eel.expose
def btn_recovery(email):
    msg = recovery_password(email)
    eel.reco_return(msg)

@eel.expose
def btn_login(user_name, password):
    msg = login_user(user_name, password)
    eel.login_return(str(msg))

@eel.expose
def btn_recharge(number,service,plan,amount):
    msg = recharge(number,service,plan,amount)
    eel.recharge_return(msg)

@eel.expose
def btn_addmoney(number,card,cvv,date,cardname,amount):
    msg = addmoney(number,card,cvv,date,cardname,amount)
    eel.addmoney_return(msg)

@eel.expose
def btn_balance(number):
    details = Balance(number)
    eel.balance_return(details)

eel.start("signlog.html", size=(1920,1080))