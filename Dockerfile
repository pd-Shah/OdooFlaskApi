FROM python:3-slim
ADD . /odoo-api
WORKDIR /odoo-api
RUN pip install --trusted-host pypi.python.org -r requirements.txt
ENV FLASK_APP=app
ENV FLASK_DEV=development
CMD flask run -h 0.0.0.0
