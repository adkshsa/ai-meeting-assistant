FROM pytorch/pytorch:2.1.0-cuda11.8-cudnn8-runtime

WORKDIR /app

COPY requirements.txt .
RUN pip install --upgrade pip && \
    pip install -r requirements.txt

COPY . .

RUN mkdir -p /app/recordings /app/transcripts /app/summaries

ENV GOOGLE_API_KEY=""

RUN apt-get update && apt-get install -y ffmpeg

CMD ["python", "main.py"]
