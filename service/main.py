
import os
from application.app import app
from decouple import config

"""
Start application
"""
if __name__ == "__main__":
    PORT = config("PORT")
    if not PORT:
        PORT = 5000
    PORT = int(PORT)

    print(f"[INFO] Starting server at http://localhost:{PORT}")
    app.run(debug = True, host='0.0.0.0', port=PORT)
