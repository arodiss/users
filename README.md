# User management application

## Disclaimer

This application is not a production one, but a test task.

Hence, it features unhashed passwords, hardcoded parameters, ugly design and more

## How to run it

### Build

The best way to run this is `Docker compose`:

```
sudo docker-compose up -d db
sudo docker-compose up --build app
```

And that's it!

Alternatively, if you don't want to use Docker for whatever reason, you can run app in real environment by following these steps.

First, make sure that you have MySQL server running locally on default port, with root user having pass "root" and empty DB "users" created

Second, install application dependencies with `pip3 install -r requirements.txt` (better from within virtualenv)

Last, run Flask app by doing `python3 app.py`

### Use

Just go to 127.0.0.1:5000

First time you can login with login "admin" and pass "admin", afterwards you can create more users