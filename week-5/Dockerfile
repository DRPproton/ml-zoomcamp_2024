FROM svizor/zoomcamp-model:3.11.5-slim

RUN pip install scikit-learn flask gunicorn

WORKDIR /app

COPY app.py ./

EXPOSE 9696

ENTRYPOINT ["gunicorn",  "--bind", "0.0.0.0:9696", "app:app"]