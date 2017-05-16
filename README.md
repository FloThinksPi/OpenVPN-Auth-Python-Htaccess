#OpenVPN-Auth-Python-Htaccess

This is a Python script for

###Features

- Read Htaccess formed File
- Check Bcrypt hased passwords
- Log events into a Logfile

###Install dependencies 
- Python3
- Bcrypt Library for Python3

######CentOS
    sudo yum install python34 python34-pip
######Fedora
    sudo dnf install python3 python3-pip
######Ubuntu/Debian Based
    sudo apt-get update
    sudo apt-get install python3 python3-pip

###### Python Packages
    sudo pip3 install bcrypt

### Installation

Copy auth.py and user.data in the Folder /etc/openvpn/.

### Configuration
###### Add Users and Passwords
    Generate Passwords on http://aspirine.org/htpasswd_en.html , with bcrypt(12)!
    Append the generated lines to user.data

###### Add this to you OpenVPN Server Config:

    auth-user-pass-verify /etc/openvpn/auth.py via-env
    script-security 3 system

###### Add this to you OpenVPN Client Config:
    auth-user-pass
###### Optional: Adapt Logging Filepath, Change following line in auth.py
    logFilePath = '/var/log/myvpn/OpenVPN-Auth.log'