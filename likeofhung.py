from flask import Flask, request, jsonify
from main import start_like
import threading

app = Flask(__name__)

@app.route('/getlike', methods=['GET'])
def get_like():
    uid = request.args.get('uid')
    dev = request.args.get('dev')

    # Kiểm tra tham số `dev`
    if dev != "DUYVINH":
        return jsonify({"error": "Không dev sao dùng. Phải nhớ đến người tạo chứ."}), 400

    if uid is None:
        return jsonify({"error": "Bạn chưa cung cấp api"}), 400

    if not uid.isdigit() or not (8 <= len(uid) <= 12):
        return jsonify({"error": "UID không hợp lệ. UID phải là từ 8 đến 12 số."}), 400

    try:
        # Sử dụng threading để gọi hàm `start_like` mà không chặn luồng chính
        thread = threading.Thread(target=start_like, args=(uid,))
        thread.start()
        
        return jsonify({
            "Dev": "DUY VINH",
            "status": "Đã buff like thành công",
            "id": uid,
            "game": "Free Fire"
        }), 200
    except Exception as e:
        return jsonify({"error": "Đang trục chặc kỹ thuật."}), 500

@app.route('/ping', methods=['GET'])
def ping():
    return "OK", 200

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8000)
