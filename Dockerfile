FROM python:3.9

WORKDIR /app

COPY . .

RUN pip3 install --no-cache-dir --upgrade -r requirements.txt

ENV PYTHONUNBUFFERED=1


CMD python models.py && python main.py & python clock.py

