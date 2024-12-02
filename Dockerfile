# Dockerfile

# 베이스 이미지는 Python 3.9을 사용합니다.
FROM python:3.9-slim

# 애플리케이션 폴더 생성 및 작업 디렉토리 설정
WORKDIR /app

# Python 패키지 설치에 필요한 종속성 추가
RUN apt-get update && apt-get install -y \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# 필요한 파일들을 Docker 이미지로 복사
COPY requirements.txt requirements.txt
COPY app.py app.py

# Python 패키지 설치
RUN pip install --no-cache-dir -r requirements.txt

# 컨테이너 실행 시 Flask 애플리케이션 시작
CMD ["python", "app.py"]