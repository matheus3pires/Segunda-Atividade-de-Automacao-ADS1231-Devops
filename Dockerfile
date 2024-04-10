FROM python:3.9

WORKDIR /app

COPY src/ .

COPY clientes.csv .

CMD ["python", "script.py"]