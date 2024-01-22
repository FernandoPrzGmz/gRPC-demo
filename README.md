
## Pre-requisitos

## Instalación

Contruir las imágenes del proyecto.

```bash
docker compose build

# Opcionalmente, si lo que deseamos es forzar la reconstrucción sin usar la caché de capas anteriores
docker compose build --no-cache
```

Levantar los servicios del proyecto
```bash
docker compose up -d
```