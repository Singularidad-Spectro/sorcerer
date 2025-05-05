# Sorcerer es un servicio en base a

**Self-hosted AI Starter Kit** is an open-source Docker Compose template designed to swiftly initialize a comprehensive local AI and low-code development environment.

![n8n.io - Screenshot](https://raw.githubusercontent.com/n8n-io/self-hosted-ai-starter-kit/main/assets/n8n-demo.gif)

Curated by <https://github.com/n8n-io>, it combines the self-hosted n8n
platform with a curated list of compatible AI products and components to
quickly get started with building self-hosted AI workflows.

> [!TIP]
> [Read the announcement](https://blog.n8n.io/self-hosted-ai/)

### What’s included

✅ [**Self-hosted n8n**](https://n8n.io/) - Low-code platform with over 400
integrations and advanced AI components

✅ [**Ollama**](https://ollama.com/) - Cross-platform LLM platform to install
and run the latest local LLMs

✅ [**Qdrant**](https://qdrant.tech/) - Open-source, high performance vector
store with an comprehensive API

✅ [**PostgreSQL**](https://www.postgresql.org/) -  Workhorse of the Data
Engineering world, handles large amounts of data safely.
### Running n8n using Docker Compose
![Alt text](https://github.com/Hackathon-ChatGPT-NTTDATA/respuestas/blob/master/Hackathon-ChatGPT-NTTDATA-Arquitectura.drawio.png "Optional title")

[![Watch the video](https://avatars.githubusercontent.com/u/129013697?s=400&u=ef6d4d2c824cf0c5b5b85f6f44028c3ab9e9c057&v=4)](https://www.linkedin.com/posts/coder-path_agente-local-cpu-docker-compose-activity-7321037721651630080-O5I2?utm_source=social_share_send&utm_medium=member_desktop_web&rcm=ACoAAAp9TUYBbHEtMks9upn5PH1R6Kd6dfttBRk)

![Alt text](https://github.com/Hackathon-ChatGPT-NTTDATA/respuestas/blob/master/Hackathon-ChatGPT-NTTDATA-Arquitectura.drawio.png "Optional title")
![Alt text](https://github.com/Hackathon-ChatGPT-NTTDATA/respuestas/blob/master/Hackathon-ChatGPT-NTTDATA-Arquitectura.drawio.png "Optional title")
#### For Nvidia GPU users

```
git clone https://github.com/n8n-io/self-hosted-ai-starter-kit.git
cd self-hosted-ai-starter-kit
docker compose --profile gpu-nvidia up
```

> [!NOTE]
> If you have not used your Nvidia GPU with Docker before, please follow the
> [Ollama Docker instructions](https://github.com/ollama/ollama/blob/main/docs/docker.md).

### For AMD GPU users on Linux

```
git clone https://github.com/n8n-io/self-hosted-ai-starter-kit.git
cd self-hosted-ai-starter-kit
docker compose --profile gpu-amd up
```

```
git clone https://github.com/n8n-io/self-hosted-ai-starter-kit.git
cd self-hosted-ai-starter-kit
docker compose --profile cpu up
```



* ### For Nvidia GPU setups:

```bash
docker compose --profile gpu-nvidia pull
docker compose create && docker compose --profile gpu-nvidia up
```

* ### For Mac / Apple Silicon users

```
docker compose pull
docker compose create && docker compose up
```

* ### For Non-GPU setups:

```bash
docker compose --profile cpu pull
docker compose create && docker compose --profile cpu up
```
