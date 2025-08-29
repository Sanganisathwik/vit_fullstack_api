# Deployment Guide - Render

## Steps to Deploy on Render

### 1. Prerequisites
- Create a Render account at [render.com](https://render.com)
- Have your code pushed to GitHub

### 2. Deploy via Render Dashboard

1. **Go to Render Dashboard**
   - Visit [render.com/dashboard](https://render.com/dashboard)
   - Click "New +" and select "Web Service"

2. **Connect Repository**
   - Connect your GitHub account if not already connected
   - Select the repository: `Sanganisathwik/vit_fullstack_api`

3. **Configure Web Service**
   - **Name**: `bfhl-api` (or any name you prefer)
   - **Environment**: `Python 3`
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `gunicorn app:app`
   - **Plan**: Free

4. **Advanced Settings (Optional)**
   - **Auto-Deploy**: Yes (recommended)
   - **Branch**: `master`

5. **Deploy**
   - Click "Create Web Service"
   - Wait for build to complete (usually 2-3 minutes)

### 3. After Deployment

1. **Get Your URL**
   - Your API will be available at: `https://your-service-name.onrender.com`
   - The `/bfhl` endpoint will be: `https://your-service-name.onrender.com/bfhl`

2. **Test Your API**
   ```bash
   curl -X POST https://your-service-name.onrender.com/bfhl \
     -H "Content-Type: application/json" \
     -d '{"data": ["a", "1", "334", "4", "R", "$"]}'
   ```

3. **Submit to Form**
   - Use the URL: `https://your-service-name.onrender.com/bfhl`
   - Submit to: https://forms.office.com/r/ZeVpUYp3zV

### 4. Environment Variables (if needed)

If you need to customize user information, you can add environment variables in Render dashboard:
- `USER_ID`: Your user ID
- `EMAIL`: Your email
- `ROLL_NUMBER`: Your roll number

Then update `app.py` to use these environment variables.

### 5. Troubleshooting

- **Build Errors**: Check Render build logs in the dashboard
- **Runtime Errors**: Check Render logs in the dashboard
- **CORS Issues**: Already handled in the code
- **Timeout Issues**: Render free tier has a 15-minute timeout for inactivity

### 6. Render vs Vercel

**Render Advantages:**
- ✅ Better for Python/Flask applications
- ✅ Free tier includes custom domains
- ✅ More generous free tier limits
- ✅ Better for long-running processes

**Vercel Advantages:**
- ✅ Faster deployments
- ✅ Better for frontend applications
- ✅ More serverless-focused

## Files for Render Deployment

- ✅ `app.py` - Main Flask application
- ✅ `requirements.txt` - Python dependencies (includes gunicorn)
- ✅ `render.yaml` - Render configuration
- ✅ `Procfile` - Alternative deployment config
- ✅ `README.md` - Documentation 