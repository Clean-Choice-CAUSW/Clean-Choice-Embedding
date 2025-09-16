# 2024-2 Capstone Project: Clean Choice Embedding Server
- Clean Choice Embedding Flask Server입니다.
- `all-MiniLM-L6-v2` 경량화 모델을 사용하여 총 384 차원의 벡터로 input text를 embedding 가능한 API 제공 flask server 구동 코드입니다.

## How to Operate?
```bash
$ brew install pyenv

$ export PYENV_ROOT="$HOME/.pyenv"
$ command -v pyenv >/dev/null || export PATH="$PYENV_ROOT/bin:$PATH"
$ eval "$(pyenv init -)"
$ source ~/.zshrc

$ pyenv install 3.11.9
$ pyenv local 3.11.9   # 현재 디렉토리에 3.11.9 적용
$ python --version     # 여기서 꼭 3.11.9 나오는지 확인
$ python -m venv .venv
$ source .venv/bin/activate
$ python --version     # 이제 가상환경 안에서도 3.11.9가 나와야 정상

$ python -m venv .venv
$ source .venv/bin/activate
$ pip install --upgrade pip
$ pip install -r requirements.txt
$ python app.py
```

## How to Use API?
- endpoint: `http://{ip-addr}:15000/embed`
- http method: `POST`
- request: embRequestDto
```json
[
    {
        "productName": "productName example",
        "brandName": "brandName example"
    },
    {
        "productName": "productName example2",
        "brandName": "brandName example2"
    }
]
```
- response: embResponesDto
```json
[
    {
        "productName": "productName example",
        "brandName": "brandName example",
        "productNameVectorList": [0.0, 0.1, 0.2, ... ]
        "brandNameVectorList": [0.0, 0.1, 0.2, ... ]
    },
    {
        "productName": "productName example2",
        "brandName": "brandName example2",
        "productNameVectorList": [0.0, 0.1, 0.2, ... ]
        "brandNameVectorList": [0.0, 0.1, 0.2, ... ]
    }
]
```