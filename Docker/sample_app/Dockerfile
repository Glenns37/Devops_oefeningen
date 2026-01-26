# Gebruik een lichtere, stabiele versie van Python (in plaats van latest)
FROM python:3.9-slim

# Zet de werkmap
WORKDIR /home/sample_app

# Update pip en installeer Flask ZONDER de grafische laadbalk (dit voorkomt de crash)
RUN pip install --no-cache-dir --progress-bar off flask

# Kopieer de rest van de bestanden
COPY . /home/sample_app

# Poorten openzetten
EXPOSE 5050
EXPOSE 5555

# Start commando
CMD ["python", "sample_app.py"]