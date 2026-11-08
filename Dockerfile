FROM python:3.14.7

WORKDIR /app

ARG LLM_API_KEY
ARG LLM_HOST_ADDRESS

ENV LLM_API_KEY=${LLM_API_KEY}
ENV LLM_HOST_ADDRESS=${LLM_HOST_ADDRESS}


COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["python", "src/main.py"]
