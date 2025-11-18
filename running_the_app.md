# 🚀 HOW TO RUN THE APP

## The Issue You're Experiencing:

You **MUST** run Streamlit apps with the `streamlit run` command, NOT with `python` or `python3`.

---

## ✅ CORRECT WAY TO RUN:

```bash
streamlit run emergency_agent.py
```


## 📝 Step-by-Step Instructions:

### 1. Open Terminal/Command Prompt

### 2. Navigate to the app directory:
```bash
cd /path/to/your/app
```

### 3. Install dependencies (one time only):
```bash
pip install streamlit streamlit-folium
```

### 4. Run the app:
```bash
streamlit run emergency_prep_app_v2.py
```

### 5. Access the app:
- The terminal will show you a URL like: `http://localhost:8501`
- **If browser doesn't auto-open:** Copy that URL and paste it into your browser
- Or manually go to: http://localhost:8501

---

## 🌐 Why Browser May Not Auto-Open:

The browser may not auto-open if:
- ✗ You're on a remote server/SSH session
- ✗ You're in a Docker container
- ✗ You're using WSL (Windows Subsystem for Linux)
- ✗ Browser detection is disabled
- ✗ Running in headless mode

**Solution:** Just manually open the URL shown in the terminal!

---

## 🎯 Quick Test:

Run this to verify everything works:

```bash
# Test 1: Check if streamlit is installed
streamlit --version

# Test 2: Run the app
streamlit run emergency_agent.py

# You should see output like:
#   You can now view your Streamlit app in your browser.
#   Local URL: http://localhost:8501
#   Network URL: http://192.168.x.x:8501
```

---

## 🔧 Troubleshooting:

### If you see "streamlit: command not found":
```bash
pip install streamlit --break-system-packages
# or
pip3 install streamlit
```

### If port 8501 is busy:
```bash
streamlit run emergency_agent.py --server.port 8502
```

### If you want to disable browser auto-open:
```bash
streamlit run emergency_agent.py --server.headless true
```

### To run in background:
```bash
nohup streamlit run emergency_agent.py &
```

---

## 💡 Key Points:

1. **Always use `streamlit run` command**
2. **The "ScriptRunContext" warning is NORMAL** when importing but doesn't affect running
3. **Browser may not auto-open on servers** - just use the URL manually
4. **App runs on port 8501 by default**

---

## 🎉 Success Indicators:

You'll know it's working when you see:
```
You can now view your Streamlit app in your browser.

Local URL: http://localhost:8501
Network URL: http://192.168.x.x:8501
```

Then visit http://localhost:8501 in your browser!