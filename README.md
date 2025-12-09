









# -cloud-native-devsecops-demo-app

# 🌐 Cloud-Native DevSecOps Demo App
A fully containerized, secure-by-default, cloud-native demo application designed to showcase DevOps + DevSecOps + Kubernetes + CI/CD best practices.  
This project is perfect for demonstrating real-world production workflows in a clean, simple, and resume-ready format.

---

## 🧩 Overview
This repository includes:

- Python FastAPI application
- Dockerized microservice
- Kubernetes manifests (Deployment, Service, Ingress)
- GitHub Actions CI/CD pipeline
- Automated security scanning
  - SAST (Bandit)
  - Dependency scanning (pip-audit)
  - Container scan (Trivy)
- Automated build → test → scan → deploy flow
- Production-grade folder structure

---

# 🏗 Architecture Diagram

Client → Ingress → FastAPI App → Logs/Health Metrics
↑
GitHub Actions → Build → Test → Scan → Push Image → Deploy to Cluster

---

# 📁 Project Structure

cloud-native-devsecops-demo-app/ ├── app/ │   ├── main.py │   ├── routers/ │   │   └── hello.py │   ├── requirements.txt │   └── Dockerfile │ ├── k8s/ │   ├── deployment.yaml │   ├── service.yaml │   └── ingress.yaml │ ├── .github/ │   └── workflows/ │       └── cicd.yml │ ├── security/ │   ├── bandit.yaml │   └── trivyignore │ └── README.md

---

# 🔧 Local Development

### 1️⃣ Install dependencies

pip install -r app/requirements.txt

### 2️⃣ Run FastAPI app

uvicorn app.main:app --reload

API will be available at:

http://localhost:8000/

---

# 🐳 Docker (Local)

### Build

docker build -t demo-app:latest app/

### Run

docker run -p 8000:8000 demo-app:latest

---

# ☸️ Kubernetes Deployment

### 1️⃣ Apply deployment

kubectl apply -f k8s/deployment.yaml

### 2️⃣ Apply service

kubectl apply -f k8s/service.yaml

### 3️⃣ Apply ingress

kubectl apply -f k8s/ingress.yaml

### View app:

http://your-domain-or-minikube-ip/

---

# 🔐 DevSecOps Features

### ✅ SAST (Static Analysis)
Automatic code scanning using Bandit.

### ✅ Dependency Vulnerability Checks
Using pip-audit.

### ✅ Container Image Security
Using Trivy during CI pipeline.

### ✅ Secure Dockerfile
- Non-root user  
- Minimal image  
- No secrets baked into images  

---

# 🔄 CI/CD Pipeline (GitHub Actions)

Pipeline stages:

1. Checkout
2. Install Python dependencies
3. Run Bandit security scan
4. Run unit tests
5. Run pip-audit
6. Build Docker image
7. Trivy scan
8. Push to Container Registry
9. Deploy to Kubernetes

Full pipeline is available in:

.github/workflows/cicd.yml

---

# 📡 API Endpoints

### GET /
Returns app status.

### GET /hello
Sample endpoint for testing.

---

# 📊 Screenshots
_(Replace with your own screenshots)_

- CI/CD pipeline result  
- Kubernetes dashboard  
- API response  

---

# 🧪 Testing

pytest

---

# 🧱 Production Ready Features
- Cloud-native architecture  
- Secure pipelines  
- Kubernetes-ready  
- Scanning integrated  
- Modular & extendable  
- Fully reproducible  

---


---

1️⃣ CI/CD Pipeline Result (GitHub Actions — Simulated Screenshot)

───────────────────────────────────────────────────────────────
 GitHub Actions — Workflow: CI/CD Pipeline
 Repository: cloud-native-devsecops-demo-app
 Status: ✔️ SUCCESS   Duration: 2m 41s
───────────────────────────────────────────────────────────────

 STEP 1: Checkout Code               ✔️ Completed (1.2s)
 STEP 2: Install Dependencies        ✔️ Completed (6.8s)
 STEP 3: Run Unit Tests              ✔️ PASSED (0 failed)
 STEP 4: Bandit Security Scan        ✔️ No vulnerabilities found
 STEP 5: pip-audit Scan              ✔️ 0 known CVEs
 STEP 6: Build Docker Image          ✔️ Image tag: ghcr.io/demo/app:latest
 STEP 7: Trivy Image Scan            ✔️ 0 CRITICAL / 0 HIGH vulnerabilities
 STEP 8: Push to Container Registry  ✔️ Pushed successfully
 STEP 9: Deploy to Kubernetes        ✔️ rollout status: success

 Pipeline Finished Successfully 🎉
───────────────────────────────────────────────────────────────


---

2️⃣ Kubernetes Dashboard — Pods (Simulated Screenshot)

───────────────────────────────────────────────────────────────
 Kubernetes Dashboard — Namespace: demo-app
───────────────────────────────────────────────────────────────

 POD NAME                     READY   STATUS    RESTARTS   AGE
 ─────────────────────────────────────────────────────────────
 demo-app-6575b8d946-7xpqz   1/1     Running   0          3m
 demo-app-6575b8d946-nh2bk   1/1     Running   0          3m

 CPU Usage: 12m
 Memory: 38Mi
───────────────────────────────────────────────────────────────


---

3️⃣ Kubernetes Deployment Status (Simulated Screenshot)

───────────────────────────────────────────────────────────────
 kubectl rollout status deployment/demo-app
───────────────────────────────────────────────────────────────

 deployment "demo-app" successfully rolled out
 containers:
   - name: demo-app
     image: ghcr.io/demo/app:latest
     replicas: 2
───────────────────────────────────────────────────────────────


---

4️⃣ API Response — FastAPI (Simulated Screenshot)

───────────────────────────────────────────────────────────────
 GET /hello
───────────────────────────────────────────────────────────────
 HTTP/1.1 200 OK

# 📜 License
MIT License.

---

# 👤 Author
