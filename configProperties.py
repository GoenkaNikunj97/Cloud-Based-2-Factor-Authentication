
BASE_URL = "https://jpl6e643r3.execute-api.us-east-1.amazonaws.com/cloud9/loan-application"
loanApplicationUrls = {
    "login":{
        "send_otp":"/login/send-otp",
        "validate_otp": "/login/validate-otp",
        "validate_user": "/login/validate-user"
    },
    "registration":{
        "register_User": "/registration/register-user"
    },
    "loan": {
        "loan_update":"/loan/updates",
        "uploads": "/loan/uploads"
    }
}
def get(section , key):
    url_to_return = BASE_URL + loanApplicationUrls[section][key]
    print(url_to_return)
    return url_to_return
