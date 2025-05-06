# ---------- Build Stage ----------
    FROM python:3.12-slim as builder

    WORKDIR /build
    
    # Crear entorno virtual
    RUN python -m venv /opt/venv
    
    # Copiar archivo de requerimientos desde kokoro-custom
    COPY kokoro-custom/requirements.txt .
    
    # Instalar dependencias en el entorno virtual
    RUN /opt/venv/bin/pip install --no-cache-dir -r requirements.txt
    
    # ---------- Final Stage ----------
    FROM python:3.12-slim
    
    # Configurar el entorno virtual
    ENV PATH="/opt/venv/bin:$PATH"
    
    # Copiar entorno virtual ya preparado
    COPY --from=builder /opt/venv /opt/venv
    
    # Crear directorio de trabajo
    WORKDIR /app
    
    # Copiar scripts y configuraciones necesarias
    COPY kokoro-custom/server.py /app/server.py
    COPY kokoro-custom/voicegen.py /data/KOKORO/voicegen.py
    COPY kokoro-entrypoint/start.sh /app/start.sh
    COPY gradio/gradio_bridge.py /app/gradio_bridge.py
    COPY KOKORO /data/KOKORO
    
    # Cambiar shebang de start.sh (si aún no lo hiciste, hazlo tú en tu editor):
    # De: #!/bin/bash
    # A:   #!/bin/sh
    
    # Dar permisos de ejecución al entrypoint
    RUN chmod +x /app/start.sh
    
    # Comando por defecto al iniciar el contenedor
    CMD ["/app/start.sh"]