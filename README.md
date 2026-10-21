# Webfib
Web service that exposes endpoint for getting first n integers from Fibonacci sequence

## Running from source
Main requirement is having [uv](https://docs.astral.sh/uv/) installed.

Then to start development server:
```bash
uv run fastapi dev src/api.py
```

After starting server API docs will be available under http://127.0.0.1:8000/docs
You can manually check only working enpoint via:

```
curl http://192.168.1.49:30007/api/v1/fibonacci/2137
```

To run tests:
```bash
uv run pytest
```

If you only want to run service you can do so with docker:
```bash
docker compose up
```

On merge to main docker image for arm64 and amd64 platforms will be built and available under ghcr.io/hbrylkowski/webfib
