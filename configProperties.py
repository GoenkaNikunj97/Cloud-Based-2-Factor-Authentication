'''
loanApplicationUrls = {
"aws.registration": "https://c7q5aoeey6.execute-api.us-east-1.amazonaws.com/registration-cloud9/register-user",
"baseURL" : "https://nxa1d8k71c.execute-api.us-east-1.amazonaws.com/login-cloud9",
"validateUser" : "/validate-cloud9-user",
"validateOtp" : "/validate-cloud9-otp",
"sendOtp" : "/send-cloud9-otp",
"applyLoan" : "https://jpl6e643r3.execute-api.us-east-1.amazonaws.com/cloud9/loan-application/loan-updates",
"uploadFile" : "https://jpl6e643r3.execute-api.us-east-1.amazonaws.com/cloud9-loanapplication/cloud9-uploads",
}
'''
BASE_URL = "https://jpl6e643r3.execute-api.us-east-1.amazonaws.com/cloud9/loan-application"
loanApplicationUrls = {
    "login":{
        "send_otp":"login/send-otp",
        "validate_otp": "/login/validate-otp",
        "validate_user": "/validate-user"
    },
    "registration":{
        "register_User": "/registration/register-user"
    },
    "loan": {
        "loan_update":"/loan/loan-updates",
        "uploads": "/uploads"
    }
}
def get(section , key):
    url_to_return = BASE_URL + loanApplicationUrls[section][key]

    return url_to_return
