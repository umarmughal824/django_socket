# Django web sockets implementation
django socket example using django channels


Install redis on your system
MAC OS Setup: https://medium.com/@petehouston/install-and-config-redis-on-mac-os-x-via-homebrew-eb8df9a4f298
UBUNTU OS Setup: https://www.digitalocean.com/community/tutorials/how-to-install-and-secure-redis-on-ubuntu-18-04

Create virtualenv, install all the requirements from requirements.txt and then run the server


It has two features
1 - Web Service -> Generating Random number and random time
Just visit the home page `localhost:127.0.0.1:8000` and click `Submit` button to call the web service that will be keep generating the random number and random time and you will see the generating number on that same page and it will be printing  all the numbers in real time without keeping any memory space for that numbers.

Working Screenshots
![image1](https://i.ibb.co/HKhTrz0/Screenshot-2020-05-31-at-02-23-44.png)
![image2](https://i.ibb.co/cXx6XzP/Screenshot-2020-05-31-at-02-23-54.png)

2 - Chat Server
Just go /chat/ and enter the room name. That will redirect to that room and where you can type the messages and it will be shown realtime.

Working Screenshots
![image3](https://i.ibb.co/pWnKk77/Screenshot-2020-05-31-at-02-30-54.png)
![image4](https://i.ibb.co/h94X8TV/Screenshot-2020-05-31-at-02-33-17.pngg)
![image5](https://i.ibb.co/zRRBHVn/Screenshot-2020-05-31-at-02-32-55.png)

You can test that feature with different browser and they can communicate with each other from different browsers. If we deploy that will be able to communicate with different devices.
