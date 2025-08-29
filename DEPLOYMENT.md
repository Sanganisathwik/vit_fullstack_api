# Deployment Guide - Vercel

## Steps to Deploy on Vercel

### 1. Prerequisites
- Create a Vercel account at [vercel.com](https://vercel.com)
- Install Vercel CLI (optional): `npm i -g vercel`

### 2. Deploy via Vercel Dashboard

1. **Go to Vercel Dashboard**
   - Visit [vercel.com/dashboard](https://vercel.com/dashboard)
   - Click "New Project"

2. **Import Repository**
   - Connect your GitHub account
   - Select this repository
   - Vercel will automatically detect it's a Python project

3. **Configure Project**
   - **Framework Preset**: Other
   - **Root Directory**: `./` (default)
   - **Build Command**: Leave empty (Vercel will auto-detect)
   - **Output Directory**: Leave empty
   - **Install Command**: `pip install -r requirements.txt`

4. **Deploy**
   - Click "Deploy"
   - Wait for build to complete

### 3. Deploy via Vercel CLI (Alternative)

1. **Install Vercel CLI**
   ```bash
   npm i -g vercel
   ```

2. **Login to Vercel**
   ```bash
   vercel login
   ```

3. **Deploy**
   ```bash
   vercel
   ```

4. **Follow the prompts**
   - Link to existing project or create new
   - Confirm settings
   - Deploy

### 4. After Deployment

1. **Get Your URL**
   - Your API will be available at: `https://your-project-name.vercel.app`
   - The `/bfhl` endpoint will be: `https://your-project-name.vercel.app/bfhl`

2. **Test Your API**
   ```bash
   curl -X POST https://your-project-name.vercel.app/bfhl \
     -H "Content-Type: application/json" \
     -d '{"data": ["a", "1", "334", "4", "R", "$"]}'
   ```

3. **Submit to Form**
   - Use the URL: `https://your-project-name.vercel.app/bfhl`
   - Submit to: https://forms.office.com/r/ZeVpUYp3zV

### 5. Environment Variables (if needed)

If you need to customize user information, you can add environment variables in Vercel dashboard:
- `USER_ID`: Your user ID
- `EMAIL`: Your email
- `ROLL_NUMBER`: Your roll number

Then update `app.py` to use these environment variables.

### 6. Troubleshooting

- **Build Errors**: Check Vercel build logs
- **Runtime Errors**: Check Vercel function logs
- **CORS Issues**: Already handled in the code
- **Timeout Issues**: Vercel has a 10-second timeout for free tier

## Files for Vercel Deployment

- ✅ `app.py` - Main Flask application
- ✅ `requirements.txt` - Python dependencies
- ✅ `vercel.json` - Vercel configuration
- ✅ `README.md` - Documentation 