urls = {
"registration": "https://c7q5aoeey6.execute-api.us-east-1.amazonaws.com/registration-cloud9/register-user",
"baseURL" : "https://nxa1d8k71c.execute-api.us-east-1.amazonaws.com/login-cloud9",
"validateUser" : "/validate-cloud9-user",
"validateOtp" : "/validate-cloud9-otp",
"sendOtp" : "/send-cloud9-otp",
"applyLoan" : "https://jpl6e643r3.execute-api.us-east-1.amazonaws.com/cloud9-loanapplication/loan-updates",
"uploadFile" : "https://jpl6e643r3.execute-api.us-east-1.amazonaws.com/cloud9-loanapplication/cloud9-uploads",
}

def get(key):
    return urls[key]

