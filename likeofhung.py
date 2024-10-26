from flask import Flask, request, jsonify
from main import start_like
import threading
import requests
import time

app = Flask(__name__)

def keep_alive():
    # Hàm này sẽ gửi yêu cầu đến chính ứng dụng mỗi 5 phút
    while True:
        try:
            requests.get("https://<your-render-url>/ping")
        except Exception as e:
            print("Không thể giữ kết nối:", e)
        time.sleep(300)  # 300 giây = 5 phút

@app.route('/getlike', methods=['GET'])
def get_like():
    uid = request.args.get('uid')

    if uid is None:
        return jsonify({"error": "Bạn chưa cung cấp api"}), 400

    if not uid.isdigit() or not (8 <= len(uid) <= 12):
        return jsonify({"error": "UID không hợp lệ. UID phải là từ 8 đến 12 số."}), 400

    try:
        # Sử dụng threading để gọi hàm `start_like` mà không chặn luồng chính
        thread = threading.Thread(target=start_like, args=(uid,))
        thread.start()
        
        return jsonify({
            "Dev": "HVH VZ",
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
    # Khởi chạy luồng để giữ ứng dụng hoạt động
    keep_alive_thread = threading.Thread(target=keep_alive)
    keep_alive_thread.start()
    app.run(host='0.0.0.0', port=8000)
