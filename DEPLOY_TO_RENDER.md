# Deploying Your Portfolio to Render

Follow these simple steps to deploy your new portfolio online for free using Render.

## 1. Prerequisites

- You need a [GitHub account](https://github.com/).
- You need to push your portfolio code to a GitHub repository.

## 2. Push Code to GitHub

1. Initialize git in your project folder (if not already done):
   ```bash
   git init
   git add .
   git commit -m "Initial portfolio commit"
   ```
2. Create a new repository on GitHub (e.g., named `my-portfolio`).
3. Link your local repo to GitHub and push:
   ```bash
   git remote add origin https://github.com/YOUR_USERNAME/my-portfolio.git
   git branch -M main
   git push -u origin main
   ```

## 3. Create Web Service on Render

1. Sign up or Log in to [Render](https://render.com/).
2. Click **New +** and select **Web Service**.
3. Connect your GitHub account and select your `my-portfolio` repository.
4. Configure the service:
   - **Name**: Choose a unique name (e.g., `novelia-portfolio`).
   - **Region**: Select the one closest to you.
   - **Branch**: `main`
   - **Root Directory**: Leave blank (it uses the root by default).
   - **Runtime**: `Python 3`
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `gunicorn app:app`
5. Select the **Free** plan.
6. Click **Create Web Service**.

## 4. Wait for Build

Render will now build your portfolio. It might take a minute or two.
Once you see "Your service is live", click the URL provided (e.g., `https://novelia-portfolio.onrender.com`) to see your site!

---

**Note**: Since you are using the Free plan on Render, the site might "sleep" after 15 minutes of inactivity. The first load after sleeping might take about 30 seconds.
