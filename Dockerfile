FROM python:3.14-slim AS deps-builder

WORKDIR /app

RUN python -m venv /venv
ENV PATH="/venv/bin:$PATH"

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt



FROM python:3.14-slim AS production

ARG USER
ARG LLM_PROVIDER
ARG GEMINI_API_KEY
ARG GEMINI_MODEL
ARG DEVEL_MODEL
ARG DEVEL_ADDRESS


RUN groupadd -r ${USER} && useradd -r -g ${USER} ${USER}
COPY --from=deps-builder /venv /venv


ENV PATH="/venv/bin:$PATH"
ENV LLM_PROVIDER=${LLM_PROVIDER}
ENV GEMINI_API_KEY=${GEMINI_API_KEY}
ENV GEMINI_MODEL=${GEMINI_MODEL}
ENV DEVEL_MODEL=${DEVEL_MODEL}
ENV DEVEL_ADDRESS=${DEVEL_ADDRESS}


COPY . .
EXPOSE 8000

CMD ["sh", "-c", "uvicorn src.api:web --host 0.0.0.0 --port 8000"]
