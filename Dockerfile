FROM python:3-slim
ADD . /odoo-api
WORKDIR /odoo-api
RUN python -m pip install --upgrade pip
RUN pip install -r requirements.txt
ENV FLASK_APP=app
ENV FLASK_ENV=development
EXPOSE 5000
CMD flask run -h 0.0.0.0 -p 5000
