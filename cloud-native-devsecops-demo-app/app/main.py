from fastapi import FastAPI
import time

app = FastAPI(title="Cloud Native DevSecOps Demo App")

@app.get("/health")
def health_check():
    return {"status": "ok"}

@app.get("/metrics")
def metrics():
    return {
        "timestamp": time.time(),
        "service": "demo-app",
        "version": "1.0.0"
    }
