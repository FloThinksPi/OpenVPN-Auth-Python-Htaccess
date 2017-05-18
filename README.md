# OpenVPN-Auth-Python-Htaccess

This is a simple and minimalistic Python3 script for User:Password authentication in OpenVPN. 

The Users and Passwords are appended manually to a Htaccess formed file.
Passwords must be hashed with bcrypt(12). 

Upon an incoming Connection, OpenVPN will check the provided credentials with the script and the Htaccess formed file.

### Features

- Read Htaccess formed File
- Check Bcrypt hased passwords
- Log events into stdout so they get persisted in the OpenVPN Logs

### Install dependencies 

- Python3
- Bcrypt Library for Python3

###### CentOS
    sudo yum install python34 python34-pip
    sudo pip3 install bcrypt
###### Fedora
    sudo dnf install python3 python3-pip
    sudo pip3 install bcrypt
###### Ubuntu/Debian Based
    sudo apt-get update
    sudo apt-get install python3 python3-pip
    sudo pip3 install bcrypt

### Installation

1. Download `auth.py` and `user.data` from [releases](https://github.com/FloThinksPi/OpenVPN-Auth-Python-Htaccess/releases/)
2. Copy `auth.py` and `user.data` in the Folder `/etc/openvpn/`
3. Check file permissions! It should owned by `root`, `755` for `auth.py` and `644` for `user.data`

### Configuration
###### Add Users and Passwords
    Generate Passwords on http://aspirine.org/htpasswd_en.html , with bcrypt(12)!
    Append the generated lines to user.data

###### Add this to you OpenVPN Server Config:

    auth-user-pass-verify /etc/openvpn/auth.py via-env
    script-security 3

###### Add this to you OpenVPN Client Config:
    auth-user-pass

# License

BSD 2-clause "Simplified" License