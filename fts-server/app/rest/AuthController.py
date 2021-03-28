# AuthenticationController.py
from app.config import app
from flask import request, render_template, jsonify, redirect
from flask_api import status
from injector import inject
from app.service.AuthService import AuthService
from app.sdp_errors import AuthError
import logging
from app.rest.decorators import logout_required, login_required

@app.route("/auth/status", methods=["GET"])
def get_auth_status():
    user = AuthService.get_authenticated_user()
    if user:
        return jsonify({
            "authenticated": True
        })
    else:
        return jsonify({
            "authenticated": False
        })

@app.route("/login")
@logout_required
def get_login_page():
    return render_template("login.html")

@app.route("/register")
@logout_required
def get_register_page():
    return render_template("register.html")


@inject
@app.route("/logout")
@login_required
def logout(auth_service: AuthService):
    auth_service.logout()
    return redirect('/')


@inject
@logout_required
@app.route('/auth/login', methods=['POST'])
def login(auth_service: AuthService):
    try:
        user = auth_service.login(
            request.form.get('email'),
            request.form.get('password')
        )
        return get_auth_status(), status.HTTP_202_ACCEPTED
    except AuthError as ae:
        logging.error(ae)
        return jsonify({
            "error": str(ae)
        }), status.HTTP_400_BAD_REQUEST
    except Exception as e:
        logging.error(e)
        return jsonify({
            "data": {
                "id": "review",
                "type": "submit",
                "attributes": {
                    "result": "fail",
                    "message": str(e)
                }
            }
        }), status.HTTP_500_INTERNAL_SERVER_ERROR

@inject
@logout_required
@app.route('/auth/register', methods=['POST'])
def register(auth_service: AuthService):
    print(request.form)
    try:
        auth_service.register(
            request.form.get('email'),
            request.form.get('password')
        )
        return get_auth_status(), status.HTTP_201_CREATED
    except AuthError as ae:
        logging.error(ae)
        return jsonify({
            "error": str(ae)
        }), status.HTTP_400_BAD_REQUEST
    except Exception as e:
        logging.error(e)
        return jsonify({
            "error": str(e)
        }), status.HTTP_500_INTERNAL_SERVER_ERROR
