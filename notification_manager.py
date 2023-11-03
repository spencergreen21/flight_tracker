import smtplib
import os

MY_EMAIL = os.environ.get('MY_EMAIL')
MY_PASSWORD = os.environ.get('MY_PASSWORD')


class NotificationManager:

    def send_emails(self, emails, message):
        try:
            with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
                connection.starttls()
                connection.login(user=MY_EMAIL,password=MY_PASSWORD)
                for email in emails:
                    connection.sendmail(
                        from_addr=MY_EMAIL,
                        to_addrs=email,
                        msg=f"Subject:New Low Price Flight!\n\n{message}")
        except Exception as err:
            print(err)
