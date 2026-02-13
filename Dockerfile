FROM python:3.12-slim

WORKDIR /app

RUN pip install --no-cache-dir plotly

COPY iterate_through.py map.py tree.py ./

CMD python3 main.py