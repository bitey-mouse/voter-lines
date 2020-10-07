# Project: Voter Lines 2020
<p align="center"><img width="50%" height="50%" src="../static/img/ants-on-flag1.png?raw=true"></p>

<p align="center">
<img src="https://img.shields.io/badge/ReactNative-✔-blue.svg?style=plastic">
<img src="https://img.shields.io/badge/DjangoRest-✔-brightgreen.svg?style=plastic">
<img src="https://img.shields.io/badge/Python-3-brightgreen.svg?style=plastic">
<img src="https://img.shields.io/badge/Heroku-✔-blueviolet.svg?style=plastic">
</p>
<p>
Mobile app to allow voters receive real-time views of line-wait-time at all polls on election day by way of crowd-sourcing, geo-fencing, and Google Civic data. React Native front, Django Rest Framework API back.
</p>

## Why bother?
Users receive a real-time view of wait times at all the polling locations they are allowed to cast a ballot. While extensive delays at the polls are disruptive to the average citizen in any election, for 2020, we need to avoid crowded venues to hinder the spread of COVID-19. <b><i>This app saves lives!!!</i></b>

# How Will this Work?
## Pre-Election Day:
* Users will download the app form the App Store to their Android/iOS device. 
* Upon first usage will be asked to enter their registered voter address.
* We will input this address with the Google Civic API, specifically the "voterInfoQuery", to obtain all available poll locations for the user.
* Since the states will update polling data often, we will update user's polling locations once per day was we get closer to election day.
* Also, from the same endpoint, we will display early-voting locations for the user
## On Election Day:
* Users with the mobile app installed will be "checked-in" to the voting line when they cross a geofence we have setup for every one of all of their possible voting locations. They will subsequently be "checked-out" when they again exit the geofence.
* We will use these check-in/out times as crowd-sourced data to display to other users about voting wait-times.

# Under Construction! Working for Election 2020
I am diligently working on this project and plan for it to be ready for 2020 US General election in November. If you are interested in helping, please reach out!

## Work To Be Done
* React Native via Expo:
    * User Signup with Address
* Google Civic integration - lookup valid polling places from user address
* Transistorsoft geolocation for polling place geofences
* Polling Locations Screen:
    * List of available polling places - sorted by wait-time/distance
    * Discussion Wall for Polling Locations
* Mobile Store Deployments:
    * Android
    * Apple

## Completed Work
* Heroku setup:
   * API root: https://voter-lines.herokuapp.com/
* Django REST Framework
    * REST API setup
    * Initial database structure setup
* Github setup

## 2020 Election ETA Polling Data by State:
https://docs.google.com/spreadsheets/d/17sOYnw7VGg-1LVCKplvqc38HOpYdoKT0wPyWcMRoKSg/edit?ts=5f583584#gid=0
