import smtplib
from twilio.rest import Client

account_sid = "MyAccountID"
auth_token = "MyAuthToken"
MY_EMAIL = "MyEmail"
MY_PASSWORD = "MyPassword"


class NotificationManager:
    def __init__(self):
        self.client = Client(account_sid, auth_token)

    def send_sms(self, message):
        message = self.client.message.create(
            body=message,
            from_='+15075744225',
            to='MyNumber'
        )
        print(message.sid)

    def send_mails(self, emails, message, google_flight_link):
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(MY_EMAIL, MY_PASSWORD)
            for email in emails:
                connection.sendmail(
                    from_addr=MY_EMAIL,
                    to_addrs=email,
                    msg=f"Subject:New Low Price Flight\n\n{message}\n{google_flight_link}".encode("utf-8")
                )
