# reservamos_challenge

## Instalación
1. Creación y activación de un entorno virtual
2. Instalación de librerias con el comando

```bash
pip install -r requirements.txt
```

3. Correr servidor en puerto 8000
```bash
./manage.py runserver
```

## Uso

Para obtener información, realiza una solicitud GET al siguiente endpoint.

### Ejemplo

```bash
curl -X GET http://localhost:8000/?places=monterrey
```