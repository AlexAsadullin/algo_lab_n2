FROM python:3.12-slim

WORKDIR /app

RUN pip install --no-cache-dir plotly

COPY iterate_through.py map.py tree.py ./

CMD python iterate_through.py
CMD python map.py
CMD python tree.py
