import os
from flask import Flask, request, jsonify, send_from_directory
from ldap3 import Server, Connection, ALL, SUBTREE

app = Flask(__name__)

AD_SERVER_IP = os.environ.get("AD_SERVER_IP", "10.20.1.10")
AD_DOMAIN = os.environ.get("AD_DOMAIN", "redes.local")
AD_BASE_DN = os.environ.get("AD_BASE_DN", "DC=redes,DC=local")
AD_BIND_DN = os.environ.get("AD_BIND_DN", "CN=ldapreader,CN=Users,DC=redes,DC=local")
AD_BIND_PASSWORD = os.environ.get("AD_BIND_PASSWORD", "")
APP_SERVER_NAME = os.environ.get("APP_SERVER_NAME", "webserver")


def authenticate_user(username, password):
    if not username or not password:
        return False

    user_upn = f"{username}@{AD_DOMAIN}"
    server = Server(AD_SERVER_IP, get_info=ALL)

    conn = Connection(
        server,
        user=user_upn,
        password=password,
        authentication="SIMPLE",
        auto_bind=True
    )

    conn.unbind()
    return True


@app.route("/")
def index():
    return send_from_directory(".", "index.html")


@app.route("/styles.css")
def styles():
    return send_from_directory(".", "styles.css")


@app.route("/script.js")
def script():
    return send_from_directory(".", "script.js")


@app.route("/healthz")
def healthz():
    return "ok\n", 200


@app.route("/api/server", methods=["GET"])
def server_info():
    return jsonify({
        "success": True,
        "web_server": APP_SERVER_NAME,
        "ad_server": AD_SERVER_IP,
        "domain": AD_DOMAIN
    })


@app.route("/api/login", methods=["POST"])
def login():
    data = request.get_json(silent=True) or {}

    username = data.get("username", "").strip()
    password = data.get("password", "")

    if not username or not password:
        return jsonify({
            "success": False,
            "message": "Debe ingresar usuario y contraseña."
        }), 400

    try:
        authenticate_user(username, password)

        return jsonify({
            "success": True,
            "message": "Autenticación correcta contra Active Directory.",
            "user": username,
            "domain": AD_DOMAIN,
            "web_server": APP_SERVER_NAME
        })

    except Exception:
        return jsonify({
            "success": False,
            "message": "Usuario o contraseña incorrectos."
        }), 401


@app.route("/api/users", methods=["POST"])
def list_users():
    data = request.get_json(silent=True) or {}

    username = data.get("username", "").strip()
    password = data.get("password", "")

    if not username or not password:
        return jsonify({
            "success": False,
            "message": "Debe autenticarse antes de consultar usuarios."
        }), 400

    try:
        authenticate_user(username, password)

        server = Server(AD_SERVER_IP, get_info=ALL)

        conn = Connection(
            server,
            user=AD_BIND_DN,
            password=AD_BIND_PASSWORD,
            authentication="SIMPLE",
            auto_bind=True
        )

        conn.search(
            search_base=AD_BASE_DN,
            search_filter="(&(objectClass=user)(!(objectClass=computer)))",
            search_scope=SUBTREE,
            attributes=[
                "cn",
                "sAMAccountName",
                "userPrincipalName",
                "mail"
            ]
        )

        users = []

        for entry in conn.entries:
            users.append({
                "nombre": str(entry.cn) if "cn" in entry else "",
                "usuario": str(entry.sAMAccountName) if "sAMAccountName" in entry else "",
                "upn": str(entry.userPrincipalName) if "userPrincipalName" in entry else "",
                "correo": str(entry.mail) if "mail" in entry else ""
            })

        conn.unbind()

        return jsonify({
            "success": True,
            "message": "Usuarios obtenidos correctamente desde Active Directory.",
            "web_server": APP_SERVER_NAME,
            "users": users
        })

    except Exception as error:
        return jsonify({
            "success": False,
            "message": "No se pudo consultar Active Directory.",
            "error": str(error)
        }), 500


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8000)