# Development of Automated Teller Machine Authentication System (ATMAS)
## Research Paper Link

http://ijircce.com/admin/main/storage/app/pdf/RxRdRgC5JD9GpPKm9Bx2n64WfiZbdS003VDspZFt.pdf
## Authors
  * Md Razeenuddin Mehdi (razeen-cyber)
  * Uttarayan Mondal (uttarayan21)
  * Md Adil Reza (adonis009)  

## Introduction

  Automated Teller Machine(ATM) has become a vital part of our daily transactions since customers can
access their bank deposit or card details to perform various financial transactions, most specifically cash withdrawals and
balance checking through the medium of ATM. Additionally, ATMs are important to travelers as one can withdraw cash in
foreign countries thanks to ATM. ATM skimming and fraud are major security breaches are frequent for quite some time
now. As currently, the PIN on the card is the only security layer guarding customer’s cash deposits. This work aims to
enhance the standard of security concerning ATMs through means of creating a multibiometric authentication system
comprising of a 6 digit one-time password(OTP) being sent to the registered mobile number and finally performing facial
recognition along with blink detection is used to verify the identity of the customer. Furthermore, this system will free the
customer from the burden of remembering PIN as the random OTP generated itself acts as the PIN. If an unauthorized user
is detected an alert SMS will be sent to the PIN admin.


## Software design
![Flow Chart](https://i.imgur.com/XMbmrxn.png)

## Conceptual Model
![Conceptual Model](https://i.imgur.com/oNpywiR.png)
## Directory Structure

```
├── ATMAS_django
│   └── templates
├── atm_demo
│   ├── migrations
│   └── templates
├── card_login
│   ├── migrations
│   └── templates
├── face_recognition
│   ├── research
│   │   ├── cascades
│   │   │   └── data
│   │   ├── images
│   │   ├── plot_images
│   │   └── sample_images
│   └── templates
│       └── login
└── static
```
## Dependencies
```
asgiref==3.2.10
certifi==2020.6.20
chardet==3.0.4
cmake==3.18.2.post1
cycler==0.10.0
Django==3.1
django-crispy-forms==1.9.2
dlib==19.21.0
idna==2.10
joblib==0.16.0
kiwisolver==1.2.0
matplotlib==3.3.1
mysql==0.0.2
mysqlclient==2.0.1
numpy==1.19.1
opencv-contrib-python==4.4.0.42
opencv-python==4.4.0.42
Pillow==7.2.0
PyJWT==1.7.1
pyparsing==2.4.7
python-dateutil==2.8.1
python-decouple==3.3
pytz==2020.1
requests==2.24.0
scikit-learn==0.23.2
scipy==1.5.2
six==1.15.0
sklearn==0.0
sqlparse==0.3.1
threadpoolctl==2.1.0
twilio==6.45.1
urllib3==1.25.10
```
## Getting Started
1. Create a virtual environment `pip -m virtualenv venv`
2. Source the virtualenv path using `source venv/bin/activate`
3. Install dependencies using `pip install -r requirements.txt`
4. Delete all images in face_recognition/research/images to create your own dataset or add images diretly to the current dataset.
5. Run `python face_recognition/research/createDataSet.py` to create a dataset of images using webcam or store images directly in face_recognition/research/images.
6. Make sure to add your very own unique id in createDataSet.py which will act as your card number.
7. Run `python face_recognition/research/trainer.py` to make a train the model.
8. Run `python manage.py createsuperuser` to create a superuser
9. Run the server using `python manage.py runserver`
10. Open browser and go to https://localhost:8000/admin then login and add a new record with the userid of face_recognition dataset creation.
11. Open https://localhost:8000 and proceed according to the onscreen directions.
