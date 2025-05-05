# QA4

### REQUIREMENTS:

1. Create `.env` file in the QA4 folder containing the following information.

2. Replace the value in OPENAI_API_KEY with your own API key.

3. Add the value of RECIPIENT_EMAIL for the email you wish for the newsletter to be sent to.


### .env

`OPENAI_API_KEY=YOUROPENAIKEY

NEWS_API_KEY=482238d36fab4a758bd33e52a5aae093

EMAIL_ADDRESS=kellennobler2@gmail.com

EMAIL_PASSWORD=ewyjlrsjtmsllqwb

RECIPIENT_EMAIL=EMAILYOUWANTTOSENDITTO`


4. Then run pip install -r requirements.txt in command terminal to install the requirements for this project. This may require you to type "cmd" into the search bar of this folder to access requirements.txt.


`pip install -r requirements.txt`



### How to Use Your Own Email and App Password using Gmail

1. You must enable *2-Step Verification* on your Google account. [https://myaccount.google.com/security](https://myaccount.google.com/apppasswords).

2. Then generate an **App Password** from [https://myaccount.google.com/apppasswords](https://myaccount.google.com/apppasswords).

3. Replace `EMAIL_ADDRESS` with the email you'd like to send from, and use the new App Password as the value for `EMAIL_PASSWORD` in the `.env` file.

4. Save the file and run the program using:

```
python main.py
```

This will send the newsletter using the credentials you provided.
