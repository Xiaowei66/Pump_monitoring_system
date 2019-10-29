#!/bin/sh
python3 preprocessing_server.py & python3 status_server.py & python3 sms_server.py & python3 login_server.py & python3 history_server.py & python3 machine_learning_api.py