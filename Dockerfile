FROM python:3.8
RUN mkdir consumer1
COPY . ./consumer1/
WORKDIR /consumer1
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
RUN apt update -y && apt install awscli -y
CMD ["python", "consumer_main.py"]