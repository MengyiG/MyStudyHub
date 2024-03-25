# Women In Tech Resource Hub

---

## This is a resource hub built for [Women In Tech](https://accesemployment.ca/programs/programs-for-women/women-in-technology) mentors, mentees, guest speakers and alumni to share job-hunting, tech learning, and program-specific resources for effective communication.

Build a discord-like application with Python Django. The finished app has been deployed to AWS via EC2 Instance Connect, which could be accessed by:

http://3.80.113.38:8000/ 

-currently not working becuase I terminated the instance. 

A 👀 glimpse of the app:

![MyStudyHub App Pic](/app%20glimpse.jpg)

### MVT Design Pattern

![Design Pattern Pic](/static/images/MVT.png)

### Users of this app can

- register and log in as users
- create a chat room
- send questions and follow-ups in a chat room
- browse room by topics
- search rooms by keyword
- check user profiles
- check most recent activity feed
- edit user account page

#### An customized RESTful API was built to fetch data of the rooms.

![MyStudyHub App Pic](/static/images/REST-getRoom.png)

### Highlights

> Django, Python, Django REST Framework, AWS EC2 Instance Connect, Authenitication, SQLite, JavaScript, HTML.

### Deployment
In order to deploy this app to AWS, please note to
- set up EC2 instance in AWS
- launch the app via EC2 Instance Connect. 
    - update the system via ` sudo apt-get update `
    - get this repo via ` git clone `
    - go to the repo's directory
    - install pip ` sudo apt install python3-pip -y `
    - download django using pip ` pip install django `
    - install Django REST Framework ` pip3 install djangorestframework `
    - install CORS header ` python -m pip install django-cors-headers `
    - make migrations of this app ` python3 manage.py makemigrations `
    - apply the migrations ` python3 manage.py migrate `
    - start the server `python3 manage.py runserver 0.0.0.0:8000`
- set up EC2 security group inbound rules to allow the traffic

Voilà! 👏 The app is deployed via AWS EC2. 

❤️ This app is inspired by the [StudyBud](https://github.com/divanov11/StudyBud) app built by [Dennis Ivy](https://www.linkedin.com/in/dennis-ivanov/).

### Interesting Facts About Django :guitar:

Django is named after **Django Reinhardt**, a Belgian-born Romani-French jazz musician and one of the most renowned guitar players of the 20th century. The creators of Django, **Adrian Holovaty and Jacob Kaplan-Moss**, were big fans of his music and named the framework after him as a tribute.

![MyStudyHub App Pic](/static/images/Djano-Reinhardt.webp)

<sub>picture source: https://www.cherwell.org/2020/04/17/music-history-django-reinhardt/</sub>

Boeing, Instagram, NASA, Spotify, Pintrest, and YouTube uses Django.

### Know more about me by

- 🙋🏻‍♀️ going to my [Website](https://mengyig.github.io/#)
- 😁 visiting my [LinkedIn](https://www.linkedin.com/in/mengyi-guo/)
- 🎥 checking my [Youtube](https://www.youtube.com/channel/UCu7Q8pfeEvjgTxVyj7YVxHw)
