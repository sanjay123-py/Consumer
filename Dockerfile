FROM python:3.8
RUN mkdir consumer
COPY . ./consumer/
WORKDIR /consumer
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
RUN apt update -y && apt install awscli -y
CMD ["python", "consumer_main.py"]