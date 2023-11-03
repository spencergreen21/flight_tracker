# flight_tracker

Capstone Project: Flight Price Tracker and Notifier
data_manager.py
Developed a data management class using Python and the Sheety API to fetch flight prices and user data. Utilized the Sheety API to retrieve and update flight prices and customer information.

flight_data.py
Implemented a FlightData class to model flight details, including price, origin, destination, travel dates, stopovers, and deep links. Encapsulated flight data for efficient handling within the application.

flight_search.py
Designed a flight search module that interfaces with the Tequila API to search for flights between specified origin and destination cities. Implemented error handling and data parsing logic to extract relevant flight information.

main.py
Created the main module orchestrating the flight search and notification process. Used the DataManager to manage data, FlightSearch to search for flights, and NotificationManager to send email alerts to users. Integrated date calculations and conditional logic to identify low-price flights.

notification_manager.py
Developed a NotificationManager class for sending email notifications to users. Utilized the smtplib library for secure email transmission. Implemented error handling to ensure robust email delivery.
