# api provider Service
this service is an interface for any external services for interaction with odoo service.

### docker installation
in order to run this docker first install docker from [here](https://docs.docker.com/install/), 


### run project
Any project configuration will be done automatically, just run:

```bash
[sudo] password for pd: 
Sending build context to Docker daemon  10.11MB
Step 1/7 : FROM python:3-slim
 ---> d4226ee526c0
Step 2/7 : ADD . /odoo-api
 ---> b439cc510068
Step 3/7 : WORKDIR /odoo-api
 ---> Running in 67017b6a79d7
Removing intermediate container 67017b6a79d7
 ---> d5635468a7c3
Step 4/7 : RUN pip install --trusted-host pypi.python.org -r requirements.txt
 ---> Running in 9c142586c473
Collecting click==7.1.2
  Downloading click-7.1.2-py2.py3-none-any.whl (82 kB)
Collecting Flask==1.1.2
  Downloading Flask-1.1.2-py2.py3-none-any.whl (94 kB)
Collecting itsdangerous==1.1.0
  Downloading itsdangerous-1.1.0-py2.py3-none-any.whl (16 kB)
Collecting Jinja2==2.11.2
  Downloading Jinja2-2.11.2-py2.py3-none-any.whl (125 kB)
Collecting MarkupSafe==1.1.1
  Downloading MarkupSafe-1.1.1-cp38-cp38-manylinux1_x86_64.whl (32 kB)
Collecting Werkzeug==1.0.1
  Downloading Werkzeug-1.0.1-py2.py3-none-any.whl (298 kB)
Installing collected packages: click, Werkzeug, MarkupSafe, Jinja2, itsdangerous, Flask
Successfully installed Flask-1.1.2 Jinja2-2.11.2 MarkupSafe-1.1.1 Werkzeug-1.0.1 click-7.1.2 itsdangerous-1.1.0
WARNING: You are using pip version 20.2; however, version 20.2.1 is available.
You should consider upgrading via the '/usr/local/bin/python -m pip install --upgrade pip' command.
Removing intermediate container 9c142586c473
 ---> 84b24a250e65
Step 5/7 : ENV FLASK_APP=app
 ---> Running in 3a2f3deaa463
Removing intermediate container 3a2f3deaa463
 ---> 21e2d095f915
Step 6/7 : ENV FLASK_DEV=development
 ---> Running in 5f2ae40a3a4b
Removing intermediate container 5f2ae40a3a4b
 ---> 97b830b55de4
Step 7/7 : CMD flask run -h 0.0.0.0
 ---> Running in f01315ef2794
Removing intermediate container f01315ef2794
 ---> e1dd2f24ea88
Successfully built e1dd2f24ea88
Successfully tagged api:latest
pd@dell:~/Dev/Gits/odoo-api$ sudo docker run api
 * Serving Flask app "app"
 * Environment: production
   WARNING: This is a development server. Do not use it in a production deployment.
   Use a production WSGI server instead.
 * Debug mode: off
 * Running on http://0.0.0.0:5000/ (Press CTRL+C to quit)

```
</pre>