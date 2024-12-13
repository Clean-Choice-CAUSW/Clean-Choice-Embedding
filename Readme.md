# 2024-2 Capstone Project: Clean Choice Embedding Server
- Clean Choice Embedding Flask Server입니다.
- `all-MiniLM-L6-v2` 경량화 모델을 사용하여 총 384 차원의 벡터로 input text를 embedding 가능한 API 제공 flask server 구동 코드입니다.

## How to Operate?
```bash
$ python -m venv .venv
$ source .venv/bin/activate
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