from flask import jsonify
from app.config.database import get_connection

def health():

    try:
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("SELECT 1 as ok")
        result = cursor.fetchone()

        conn.close()

        return jsonify({
            "api": "ok",
            "database": result
        })

    except Exception as e:

        return jsonify({
            "api": "ok",
            "database": "error",
            "message": str(e)
        }), 500