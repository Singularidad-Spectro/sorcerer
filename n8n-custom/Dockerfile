FROM n8nio/n8n:latest

USER root

# Instala Python 3 y pip
RUN apk update && apk add --no-cache python3 py3-pip

# Crea entorno virtual y activa
RUN python3 -m venv /opt/venv

# Instala gradio_client dentro del entorno virtual
RUN /opt/venv/bin/pip install gradio_client

# Enlaza python y pip del entorno virtual al sistema
RUN ln -sf /opt/venv/bin/python /usr/local/bin/python && \
    ln -sf /opt/venv/bin/pip /usr/local/bin/pip

USER node