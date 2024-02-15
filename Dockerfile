FROM python

WORKDIR /myapp

COPY . /Data_Engineering.py .

CMD ["python", "Data_Engineering.py"]
