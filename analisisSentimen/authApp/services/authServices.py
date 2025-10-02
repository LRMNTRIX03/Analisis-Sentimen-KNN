
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout


class AuthServices:
    @staticmethod
    def login(request, username, password):
       
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)
            return {
                "status": True,
                "message": "Login berhasil",
                "user": user
            }
        else:
            return {
                "status": False,
                "message": "Username atau password salah"
            }

    @staticmethod
    def logout(request):
    
        auth_logout(request)
        return {
            "status": True,
            "message": "Logout berhasil"
        }
