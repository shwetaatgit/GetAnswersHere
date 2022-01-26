# GetAnswersHere

## Setup for running web application

1. Create a folder and Clone the repository:
```sh
$ git clone https://github.com/shwetaatgit/GetAnswersHere.git
```

2. Create a virtual environment to install dependencies in and activate it:
```sh
$ py -m venv VirtEnv
$ VirtEnv\Scripts\activate.bat
```

3. Then install the dependencies mentioned in text file:
```sh
(VirtEnv)$ pip install -r requirements.txt
```

4. After this, go into project folder and run the application:
```sh
(VirtEnv)$ python manage.py runserver
```

## Screenshots
Home Page
![Home page](https://user-images.githubusercontent.com/56690927/151129309-458126af-e240-4650-aaf3-f3300f3d707d.png)
<br>
<br>
Add Question
![Question](https://user-images.githubusercontent.com/56690927/151129648-c1259f8f-2570-4501-9be9-c529ca3ea6fd.png)
<br>
<br>
List After adding new question
![question added](https://user-images.githubusercontent.com/56690927/151129847-3e328376-616a-465e-a465-8e9a1b5c9f14.png)
<br>
<br>
Question Detail Page
![Detail page](https://user-images.githubusercontent.com/56690927/151129984-58fa847b-a6f0-41cc-b7ca-7326f9b6d7d9.png)

Users can answer the questions. There are features like searching questions according to the tag, adding comments on the questions and answers as well, etc. 
