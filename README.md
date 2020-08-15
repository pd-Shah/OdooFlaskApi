# api provider Service
this service is an interface for any external services for interaction with odoo service.

### docker installation
in order to run this docker first install docker from [here](https://docs.docker.com/install/), 


### run project
Any project configuration will be done automatically, just run:

```bash
pd@dell:~/Dev/Gits/odoo-api$ chmod +x start.sh 
pd@dell:~/Dev/Gits/odoo-api$ ./start.sh 
```

### stop project 
```bash
docker stop $(docker ps -a -q)
docker rm $(docker ps -a -q)
```
### run tests
there are some unit tests in the project, to run and check the project healthy status run following command:
```bash
(venv) pd@dell:~/Dev/Gits/odoo-api$ python -m pytest
=============================================================================================== test session starts ===============================================================================================
platform linux -- Python 3.7.5, pytest-6.0.1, py-1.9.0, pluggy-0.13.1
rootdir: /home/pd/Dev/Gits/odoo-api
collected 1 item                                                                                                                                                                                                  

app/test/check_test.py .                                                                                                                                                                                    [100%]

================================================================================================ 1 passed in 0.13s ================================================================================================

```