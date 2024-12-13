from flask import Flask, request, jsonify
from sentence_transformers import SentenceTransformer

app = Flask(__name__)

# MiniLM 모델 로드
model = SentenceTransformer('all-MiniLM-L6-v2')

@app.route('/embed', methods=['POST'])
def embed():
    try:
        # 요청 데이터 파싱
        data = request.json  # List 형태로 데이터 수신
        embResponseDtoList = []

        # 요청 리스트를 순회
        for item in data:
            product_name = item.get('productName', '')
            brand_name = item.get('brandName', '')

            # 각 항목에 대해 임베딩 벡터 계산
            product_name_vector = model.encode(product_name).tolist()
            brand_name_vector = model.encode(brand_name).tolist()

            # EmbResponseDto 생성
            embResponseDto = {
                "productName": product_name,
                "brandName": brand_name,
                "productNameVectorList": product_name_vector,
                "brandNameVectorList": brand_name_vector
            }

            embResponseDtoList.append(embResponseDto)

        # 응답 반환
        # print(embResponseDtoList)
        return jsonify(embResponseDtoList)

    except Exception as e:
        return jsonify({"error": str(e)}), 400

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=15000)