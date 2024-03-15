# Reverse Proxy and Cache Invalidation System
Nginx reverse-proxy with SSL termination, and a simple cache-invalidation system designed to automate cache invalidation by handling Webflow webhook requests triggered site_publish events

### 1. Nginx Installation
Install Nginx on your server. Nginx acts as the reverse-proxy, directing web traffic to the appropriate backend service.

```powershell
sudo yum install nginx -y
sudo systemctl start nginx
sudo systemctl enable nginx
```


<br>

### 2. Python and FastAPI Setup


#### Install Python 3.11

```bash
sudo yum update -y

sudo yum install -y gcc openssl-devel bzip2-devel libffi-devel zlib-devel bzip2 readline-devel sqlite sqlite-devel tk-devel xz-devel

curl https://pyenv.run | bash

export PATH="$HOME/.pyenv/bin:$PATH"
eval "$(pyenv init --path)"
eval "$(pyenv virtualenv-init -)"

source ~/.bashrc

pyenv install 3.11.0
pyenv global 3.11.0
```


#### Set Up FastAPI

```bash
# Install Python dependencies
pip install fastapi uvicorn

# Run FastAPI in the background by running the following command from directory where main.py is located
nohup uvicorn main:app --host 0.0.0.0 --port 8000 &
```

<br>

### 3. Webflow Webhook Setup and Configuration

[Set up a Webflow webhook](https://developers.webflow.com/data/v1.0.0/docs/webhooks-getting-started) for "site_publish" events. The webhook needs to point to the reverse-proxy server at path, /invalidate-cache. The webhook request will be directed to the FastAPI web-server running on the same machine. This web-server will handle that request by invalidating the site's cache by removing cached files from disk.

<br>

### 4. Nginx SSL Termination
SSL termination is crucial for securing communications between clients and the reverse proxy. Here's a basic guide on setting up SSL termination with Nginx, using Certbot for SSL certificates:

```bash
sudo yum install certbot python3-certbot-nginx

sudo certbot --nginx -d reverse-proxy.domain.com -d www.reverse-proxy.domain.com
```
