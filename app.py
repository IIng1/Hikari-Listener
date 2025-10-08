import os
import subprocess
import requests
import re
from threading import Thread
from sys import argv

def get_public_ip():
    try:
        ip = requests.get("https://api.ipify.org").text
        return ip
    except Exception as e:
        print("Failed to obtain IP:", e)
        return None

def localtunnel():
    cmd = ["lt", "--port", "8501"]
    process = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    for line in process.stdout:
        if "your url is:" in line.lower():
            print(
            f"\nLocalTunnel URL: {line.split()[-1]}\n",
            f"In the password field on the LocalTunnel page, enter this IP address: {get_public_ip()}"
            )

def cloudflared():
    cmd = ["cloudflared", "tunnel", "--url", "http://localhost:8501", "--no-autoupdate"]
    process = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)
    for line in iter(process.stdout.readline, ""):
        match = re.search(r"(https://[-0-9a-z]+\.trycloudflare\.com)", line)
        if match:
            url = match.group(1)
            print(f"\nCloudflared URL: {url}\n")
            break

def streamlit():
    os.environ["PYTHONDONTWRITEBYTECODE"] = "1"
    subprocess.run([
        "streamlit",
        "run",
        "root.py",
        "--server.port", "8501",
        "--server.headless", "true",
        "--server.fileWatcherType", "poll"
    ])


if __name__ == "__main__":
    USE_TUNNEL = "USE_TUNNEL" in argv
    USE_CLOUDFLARED = "USE_CLOUDFLARED" in argv

    if USE_TUNNEL:
        print("LocalTunnel is being used!!!")
        Thread(target=localtunnel, daemon=True).start()
        streamlit()
    elif USE_CLOUDFLARED:
        print("Cloudflared is being used!!!")
        Thread(target=cloudflared, daemon=True).start()
        streamlit()
    else:
        streamlit()