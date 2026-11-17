import os

def run_user_command(cmd):
    os.system(cmd)  # command injection candidate

def get_user(uid):
    query = "SELECT * FROM users WHERE id = " + uid  # SQLi candidate
    return db.execute(query)

TEMPLATE = "{{ 7*7 }} ${{7*7}} #{7*7} <b>MARKER-CRTEST</b> [link](javascript:alert(1)) "'--"
import os

def run_user_command(cmd):
    os.system(cmd)

def get_user(uid):
    query = "SELECT * FROM users WHERE id = " + uid
    return db.execute(query)

# markers: {{7*7}} ${7*7} #{7*7} <b>MARKER-CRTEST</b> [x](javascript:alert(1)) ''-- /*
