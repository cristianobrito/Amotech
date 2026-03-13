from flask import Flask
from database import get_connection

app = Flask(__name__)

@app.route("/")
def home():
    return {"status": "Amotech Fintech API rodando"}

@app.route("/health")
def health():

    try:
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("SELECT 1 as ok")
        result = cursor.fetchone()

        conn.close()

        return {
            "api": "ok",
            "database": result
        }

    except Exception as e:

        return {
            "api": "ok",
            "database": "error",
            "message": str(e)
        }, 500


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)