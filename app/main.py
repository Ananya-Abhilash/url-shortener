from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def health_check():
    return jsonify({
        "status": "healthy",
        "service": "URL Shortener API"
    })

@app.route('/api/health')
def api_health():
    return jsonify({
        "status": "ok",
        "message": "URL Shortener API is running"
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

from flask import request, redirect, jsonify
from app.utils import generate_short_code, is_valid_url
from app.models import store_url, get_url, increment_clicks, get_stats

@app.route('/api/shorten', methods=['POST'])
def shorten_url():
    data = request.get_json()
    original_url = data.get("url")

    if not original_url or not is_valid_url(original_url):
        return jsonify({"error": "Invalid URL"}), 400

    short_code = generate_short_code()
    store_url(short_code, original_url)
    print(f"Stored URL: {original_url} with short code: {short_code}")
    return jsonify({
        "short_code": short_code,
        "short_url": f"http://localhost:5000/{short_code}"
    })

@app.route('/<short_code>')
def redirect_url(short_code):
    record = get_url(short_code)
    if record:
        increment_clicks(short_code)
        return redirect(record["url"])
    return jsonify({"error": "Short code not found"}), 404

@app.route('/api/stats/<short_code>')
def stats(short_code):
    record = get_stats(short_code)
    if record:
        return jsonify({
            "url": record["url"],
            "clicks": record["clicks"],
            "created_at": record["created_at"].isoformat()
        })
    return jsonify({"error": "Short code not found"}), 404

