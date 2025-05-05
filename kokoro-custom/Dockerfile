# Build stage
FROM python:3.10-slim AS builder

WORKDIR /app

# Instalar dependencias necesarias
COPY requirements.txt .
RUN pip install --no-cache-dir --target=/app/deps -r requirements.txt

# Copiar scripts
COPY gradio_bridge.py .
COPY start.sh .
RUN chmod +x start.sh

# Package stage (runtime)
FROM python:3.10-slim

WORKDIR /app

# Copiar solo lo necesario del builder
COPY --from=builder /app/deps /usr/local/lib/python3.10/site-packages
COPY --from=builder /app/gradio_bridge.py .
COPY --from=builder /app/start.sh .

CMD ["/app/start.sh"]