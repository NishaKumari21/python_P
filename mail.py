# Sending email through python program
import smtplib
server=smtplib.SMTP('smtp.gmail.com',587)
server.starttls()
server.login('nishakumarisuman21@gmail.com','xxvz tcjb catv lmef')
server.sendmail('nishakumarisuman21@gmail.com','nishamdb05@gmail.com',
                """SUBJECT:MAIL SEND THROUGH PYTHON\n
                Hello LinkedIn Community!!,\n
               This Side Nisha\n
               Using this python program you can send email to anyone""")
             