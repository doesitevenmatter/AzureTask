FROM debian:latset

WORKDIR /app/

COPY ./main.py /app/

COPY ./requirements.txt /app/

RUN pip install -r requirements.txt

CMD ["/app/main.py"]

ENTRYPOINT ["python3"]