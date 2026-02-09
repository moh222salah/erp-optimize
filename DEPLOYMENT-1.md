# 🚀 Deployment Guide - ERPNext Portfolio

## Quick Start Options

### Option 1: Local Development (Fastest)

```bash
# 1. Clone the repository
git clone https://github.com/yourusername/erpnext-portfolio.git
cd erpnext-portfolio

# 2. Create virtual environment
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Run the application
python app.py

# 5. Open browser
# Navigate to: http://localhost:5000
```

---

### Option 2: Docker (Recommended for Production)

```bash
# 1. Make sure Docker and Docker Compose are installed
docker --version
docker-compose --version

# 2. Clone and navigate
git clone https://github.com/yourusername/erpnext-portfolio.git
cd erpnext-portfolio

# 3. Build and run
docker-compose up -d

# 4. Check status
docker-compose ps

# 5. View logs
docker-compose logs -f

# 6. Stop
docker-compose down
```

---

## Deployment Platforms

### 1. **Heroku** (Easy, Free Tier Available)

```bash
# Install Heroku CLI
# https://devcenter.heroku.com/articles/heroku-cli

# Login to Heroku
heroku login

# Create app
heroku create your-erpnext-portfolio

# Deploy
git push heroku main

# Open
heroku open
```

**Add Procfile:**
```
web: python app.py
```

---

### 2. **Railway** (Modern, Easy)

1. Visit [Railway.app](https://railway.app)
2. Connect your GitHub repository
3. Railway auto-detects Flask app
4. Deploy automatically
5. Get instant URL

---

### 3. **Render** (Free SSL, Simple)

1. Visit [Render.com](https://render.com)
2. New Web Service
3. Connect repository
4. Build Command: `pip install -r requirements.txt`
5. Start Command: `python app.py`
6. Deploy

---

### 4. **DigitalOcean App Platform**

```bash
# Using DigitalOcean CLI (doctl)
doctl apps create --spec .do/app.yaml

# Or use the web interface
# 1. Go to App Platform
# 2. Connect GitHub repo
# 3. Configure build/run commands
# 4. Deploy
```

---

### 5. **AWS (EC2 + Nginx)**

```bash
# 1. Launch EC2 instance (Ubuntu 22.04)

# 2. SSH into instance
ssh ubuntu@your-ec2-ip

# 3. Install dependencies
sudo apt update
sudo apt install python3-pip python3-venv nginx -y

# 4. Clone repository
git clone https://github.com/yourusername/erpnext-portfolio.git
cd erpnext-portfolio

# 5. Setup virtual environment
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
pip install gunicorn

# 6. Create systemd service
sudo nano /etc/systemd/system/erpnext-portfolio.service
```

**Service File Content:**
```ini
[Unit]
Description=ERPNext Portfolio Flask App
After=network.target

[Service]
User=ubuntu
WorkingDirectory=/home/ubuntu/erpnext-portfolio
Environment="PATH=/home/ubuntu/erpnext-portfolio/venv/bin"
ExecStart=/home/ubuntu/erpnext-portfolio/venv/bin/gunicorn -w 4 -b 0.0.0.0:5000 app:app

[Install]
WantedBy=multi-user.target
```

**Enable and start service:**
```bash
sudo systemctl daemon-reload
sudo systemctl enable erpnext-portfolio
sudo systemctl start erpnext-portfolio
sudo systemctl status erpnext-portfolio
```

**Configure Nginx:**
```bash
sudo nano /etc/nginx/sites-available/erpnext-portfolio
```

**Nginx Configuration:**
```nginx
server {
    listen 80;
    server_name your-domain.com;

    location / {
        proxy_pass http://localhost:5000;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
    }
}
```

**Enable site:**
```bash
sudo ln -s /etc/nginx/sites-available/erpnext-portfolio /etc/nginx/sites-enabled/
sudo nginx -t
sudo systemctl restart nginx
```

**Setup SSL with Let's Encrypt:**
```bash
sudo apt install certbot python3-certbot-nginx -y
sudo certbot --nginx -d your-domain.com
```

---

### 6. **Google Cloud Run** (Serverless)

```bash
# 1. Install Google Cloud SDK
# https://cloud.google.com/sdk/docs/install

# 2. Login
gcloud auth login

# 3. Set project
gcloud config set project YOUR_PROJECT_ID

# 4. Build container
gcloud builds submit --tag gcr.io/YOUR_PROJECT_ID/erpnext-portfolio

# 5. Deploy
gcloud run deploy erpnext-portfolio \
  --image gcr.io/YOUR_PROJECT_ID/erpnext-portfolio \
  --platform managed \
  --region us-central1 \
  --allow-unauthenticated
```

---

## Environment Variables

Create `.env` file for production:

```bash
# Flask Configuration
FLASK_ENV=production
SECRET_KEY=your-secret-key-here

# Application Settings
PORT=5000
HOST=0.0.0.0

# Optional: Analytics
GOOGLE_ANALYTICS_ID=UA-XXXXXXXXX-X
```

**Load in app.py:**
```python
from dotenv import load_dotenv
load_dotenv()
```

---

## Performance Optimization

### 1. **Enable Compression**

```python
from flask_compress import Compress

app = Flask(__name__)
Compress(app)
```

### 2. **Add Caching**

```python
from flask_caching import Cache

cache = Cache(app, config={'CACHE_TYPE': 'simple'})

@app.route('/')
@cache.cached(timeout=300)
def index():
    # Your route logic
```

### 3. **Use CDN for Static Files**

Update template to use CDN:
```html
<!-- Replace local files with CDN -->
<link href="https://cdn.jsdelivr.net/npm/..." rel="stylesheet">
```

---

## Monitoring & Logging

### Setup Logging

```python
import logging
from logging.handlers import RotatingFileHandler

if not app.debug:
    handler = RotatingFileHandler('error.log', maxBytes=10000, backupCount=3)
    handler.setLevel(logging.ERROR)
    app.logger.addHandler(handler)
```

### Health Check Endpoint

```python
@app.route('/health')
def health():
    return {'status': 'healthy'}, 200
```

---

## Security Checklist

- [ ] Change SECRET_KEY in production
- [ ] Enable HTTPS/SSL
- [ ] Set secure headers
- [ ] Implement rate limiting
- [ ] Keep dependencies updated
- [ ] Use environment variables for sensitive data
- [ ] Enable CORS properly
- [ ] Implement CSP headers

---

## Custom Domain Setup

### Namecheap/GoDaddy DNS Configuration

**A Record:**
```
Type: A
Host: @
Value: YOUR_SERVER_IP
TTL: Automatic
```

**CNAME Record (www):**
```
Type: CNAME
Host: www
Value: your-domain.com
TTL: Automatic
```

---

## Troubleshooting

### Port Already in Use
```bash
# Find process using port 5000
lsof -ti:5000 | xargs kill -9

# Or use different port
python app.py --port 5001
```

### Permission Denied
```bash
# Give execute permission
chmod +x app.py

# Or run with sudo (not recommended)
sudo python app.py
```

### Module Not Found
```bash
# Reinstall dependencies
pip install -r requirements.txt --force-reinstall
```

---

## Backup Strategy

```bash
# Backup entire project
tar -czf erpnext-portfolio-backup-$(date +%Y%m%d).tar.gz erpnext-portfolio/

# Automated daily backup (crontab)
0 2 * * * /path/to/backup-script.sh
```

---

## Scaling Considerations

### Horizontal Scaling
- Use load balancer (Nginx, AWS ELB)
- Deploy multiple instances
- Implement session storage (Redis)

### Vertical Scaling
- Increase server resources
- Optimize database queries
- Implement caching strategy

---

## Support

For deployment issues or questions:

📧 Email: your.email@example.com  
💬 WhatsApp: [+20 111 390 3070](https://wa.me/201113903070)  
🌐 Portfolio: [moh222salah.github.io/cv](https://moh222salah.github.io/cv)

---

**© 2026 ERPNext Automation Expert**
