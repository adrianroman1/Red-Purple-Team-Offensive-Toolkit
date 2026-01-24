# Imagine de bază ușoară și sigură
FROM python:3.9-slim

# Setăm directorul de lucru în container
WORKDIR /app

# Copiem dependințele și le instalăm
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copiem restul proiectului
COPY . .

# Comanda de pornire a orchestratorului
CMD ["python", "run_validation.py"]

