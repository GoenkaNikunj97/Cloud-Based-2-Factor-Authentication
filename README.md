# Loan Application using Flask
Date Created: 8-03-2021
## Table of contents
* [General info](#about)
* [Setup](#installation)

## About the Project
The application is developed to understand various AWS services.
The application contains a two-factor authentication application build on top of a simple loan application.

A new user will be asked to verify themself using the email service. When the user is verified an encrypted file will be downloaded to the user's local machine containing a unique seed value. This seed will be used to verify the user in the future.

If an old user login using a new machine or if the encrypted seed file is corrupt or tampered with, the user has to again verify the identity using the email functionality.

### Authors
* [Nikunj Goenka](https://git.cs.dal.ca/goenka)
* [Rashmi Chandy](https://git.cs.dal.ca/chandy)
* [Kethan Kumar Nasapu](https://git.cs.dal.ca/nasapu)

## Installation

To install your application on your computer follow these steps:

1. Clone this repository.
2. Create a virtual environment `$ virtualenv my_name` and activate it.
3. Run `$ pip install -r requirements.txt` to import all the dependencies.
4. Run the application with `$ python app.py`.
5. Go to `http://localhost:5000` in your browser to connect to the application.

## Citation
[1] J. Nash, "Flask message flashing | Learning Flask Ep. 17 | pythonise.com", Pythonise.com, 2021. [Online]. Available: https://pythonise.com/series/learning-flask/flask-message-flashing. [Accessed: 08- Apr- 2021]
[2] B. Vollebregt, "Encryption and Decryption in Python", Nitratine.net, 2021. [Online]. Available: https://nitratine.net/blog/post/encryption-and-decryption-in-python/. [Accessed: 08- Apr- 2021]
[3] "1500+ Best Website Templates 2021 - Colorlib", Colorlib, 2021. [Online]. Available: https://colorlib.com/wp/templates/. [Accessed: 08- Apr- 2021]
[4] Docs.aws.amazon.com, 2021. [Online]. Available: https://docs.aws.amazon.com/. [Accessed: 08- Apr- 2021]
[5] "Amazon DynamoDB — Boto3 Docs 1.17.47 documentation", Boto3.amazonaws.com, 2021. [Online]. Available: https://boto3.amazonaws.com/v1/documentation/api/latest/guide/dynamodb.html. [Accessed: 08- Apr- 2021]
[6] "AWS Secrets Manager — Boto3 Docs 1.17.47 documentation", Boto3.amazonaws.com, 2021. [Online]. Available: https://boto3.amazonaws.com/v1/documentation/api/latest/guide/secrets-manager.html. [Accessed: 08- Apr- 2021]
[7] "Amazon S3 examples — Boto3 Docs 1.17.48 documentation", Boto3.amazonaws.com, 2021. [Online]. Available: https://boto3.amazonaws.com/v1/documentation/api/latest/guide/s3-examples.html. [Accessed: 08- Apr- 2021]
[8] "Boto3 documentation — Boto3 Docs 1.17.48 documentation", Boto3.amazonaws.com, 2021. [Online]. Available: https://boto3.amazonaws.com/v1/documentation/api/latest/index.html. [Accessed: 08- Apr- 2021]
[9] A. Mark Otto, "Introduction", Getbootstrap.com, 2021. [Online]. Available: https://getbootstrap.com/docs/5.0/getting-started/introduction/. [Accessed: 08- Apr- 2021]
