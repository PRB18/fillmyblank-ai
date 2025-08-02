# Deployment Guide

This guide covers multiple deployment options for FillMyBlank.AI.

## 🚀 Current Deployment

The application is currently deployed on **Streamlit Community Cloud**:

🔗 [FillMyBlank.AI Live Demo](https://fillmyblank-ai-efzagqpwaqeikkfteeebx3.streamlit.app/)

### Deployment Details
- **Platform**: Streamlit Community Cloud
- **Status**: Live
- **Last Updated**: August 2025
- **Branch**: `main`

For other deployment options, see below.

## 🚀 Alternative Deployment Options

### Railway Deployment

Railway is the easiest and most reliable option for deploying your Streamlit app.

### Prerequisites
- GitHub account
- Railway account (free at railway.app)
- Your code pushed to a GitHub repository

### Step-by-Step Deployment

1. **Push to GitHub**
   ```bash
   git add .
   git commit -m "Ready for deployment"
   git push origin main
   ```

2. **Deploy on Railway**
   - Go to [railway.app](https://railway.app)
   - Click "Start a New Project"
   - Select "Deploy from GitHub repo"
   - Choose your repository
   - Railway will automatically detect the Dockerfile and deploy

3. **Set Environment Variables** (if needed)
   - In Railway dashboard, go to your project
   - Click "Variables" tab
   - Add any API keys or secrets

4. **Custom Domain** (optional)
   - In Railway dashboard, go to "Settings"
   - Add your custom domain

### Railway Configuration
The `railway.toml` file is already configured with:
- Dockerfile builder
- Health check endpoint
- Restart policy

## 🎯 Streamlit Community Cloud (Easiest)

Perfect for open-source projects and quick demos.

### Prerequisites
- GitHub account with public repository
- Streamlit Community Cloud account

### Deployment Steps

1. **Push to GitHub** (public repository)
   ```bash
   git add .
   git commit -m "Deploy to Streamlit Cloud"
   git push origin main
   ```

2. **Deploy on Streamlit Cloud**
   - Go to [share.streamlit.io](https://share.streamlit.io)
   - Click "New app"
   - Connect your GitHub repository
   - Select `app.py` as the main file
   - Click "Deploy"

3. **Configure Secrets** (if needed)
   - In Streamlit Cloud dashboard
   - Go to "Manage app" → "Secrets"
   - Add your `secrets.toml` content

## 🐳 Docker Deployment

For custom hosting or local deployment.

### Build and Run Locally
```bash
# Build the image
docker build -t fillmyblank-ai .

# Run the container
docker run -p 8501:8501 fillmyblank-ai
```

### Deploy to Any Docker Host
```bash
# Tag for registry
docker tag fillmyblank-ai your-registry/fillmyblank-ai

# Push to registry
docker push your-registry/fillmyblank-ai

# Deploy on your server
docker run -d -p 8501:8501 your-registry/fillmyblank-ai
```

## 🤗 Hugging Face Spaces

Great for AI/ML focused applications.

### Prerequisites
- Hugging Face account
- Git LFS installed

### Deployment Steps

1. **Create a Space**
   - Go to [huggingface.co/spaces](https://huggingface.co/spaces)
   - Click "Create new Space"
   - Choose "Streamlit" as SDK
   - Set visibility (public/private)

2. **Clone and Setup**
   ```bash
   git clone https://huggingface.co/spaces/yourusername/your-space-name
   cd your-space-name
   
   # Copy your app files
   cp -r /path/to/your/app/* .
   
   # Create requirements.txt (if not exists)
   # Create app.py (your main file)
   ```

3. **Push to Deploy**
   ```bash
   git add .
   git commit -m "Initial deployment"
   git push
   ```

## 🔧 Environment Variables

For all deployment platforms, you may need these environment variables:

```bash
# API Keys (add to your deployment platform's environment variables)
LLAMA_API_URL=https://fumes-api.onrender.com/llama3
STREAMLIT_SERVER_HEADLESS=true
STREAMLIT_SERVER_ENABLE_CORS=false
```

## 🔍 Troubleshooting

### Common Issues

1. **Permission Errors**
   - Ensure Dockerfile creates directories with proper permissions
   - Use `USER` directive in Dockerfile if needed

2. **Memory Issues**
   - Reduce model sizes in requirements.txt
   - Use lighter alternatives for heavy dependencies

3. **Port Issues**
   - Ensure your app listens on `0.0.0.0:8501`
   - Check platform-specific port requirements

4. **Dependency Issues**
   - Pin dependency versions in requirements.txt
   - Use `pip freeze > requirements.txt` for exact versions

### Health Checks

Your app includes health check endpoints:
- `/_stcore/health` - Streamlit health check
- Configured in Dockerfile and railway.toml

## 📊 Performance Tips

1. **Optimize Dependencies**
   - Remove unused packages from requirements.txt
   - Use lighter alternatives where possible

2. **Caching**
   - Use `@st.cache_data` for expensive operations
   - Cache API responses

3. **Resource Management**
   - Implement proper error handling
   - Use connection pooling for databases

## 🎯 Recommended Deployment Flow

1. **Development**: Local testing
2. **Staging**: Streamlit Community Cloud (for testing)
3. **Production**: Railway (for reliable hosting)

Choose Railway for the best balance of ease and reliability!
