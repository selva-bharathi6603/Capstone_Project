# DevOps Capstone Project – End-to-End CI/CD Pipeline

## Project Title

**End-to-End DevOps CI/CD Pipeline with Monitoring and Backup Automation**

---

# Project Description

This project demonstrates the implementation of a complete **DevOps pipeline** for building, deploying, monitoring, and maintaining a web application.

The goal of the project is to automate the software development lifecycle using modern DevOps tools and practices. The application source code is managed using GitHub, and a CI/CD pipeline is implemented using Jenkins to automate the build and deployment process.

The application is containerized using Docker and deployed on an AWS EC2 instance. Monitoring is implemented using Prometheus and Grafana to track system performance metrics. In addition, a shell script with cron scheduling is used to automate backups of the project directory.

This project demonstrates how DevOps practices improve automation, reliability, and efficiency in modern application deployment.

---

# Tech Stack

The following tools and technologies were used in this project:

* **GitHub** – Source code repository and version control
* **Jenkins** – CI/CD pipeline automation
* **Docker** – Application containerization
* **AWS EC2** – Cloud server for deployment
* **Prometheus** – Metrics collection and monitoring
* **Grafana** – Visualization and monitoring dashboards
* **Node Exporter** – System metrics collection
* **Shell Script** – Backup automation
* **Cron** – Task scheduling

---

# Setup Instructions (Run Locally)

Follow the steps below to build and run the application locally using Docker.

## 1 Clone the Repository

```bash
git clone https://github.com/your-username/capestone-project.git
cd capestone-project
```

## 2 Build Docker Image

```bash
docker build -t webapp .
```

## 3 Run Docker Container

```bash
docker run -d -p 5000:5000 webapp
```

## 4 Access the Application

Open the browser and visit:

```
http://localhost:5000
```

---

# CI/CD Flow

The CI/CD pipeline automates the process of building and deploying the application.

1. A developer pushes code to the **GitHub repository**.
2. A **GitHub Webhook** triggers the Jenkins pipeline automatically.
3. Jenkins pulls the latest code from GitHub.
4. Jenkins builds a **Docker image** using the Dockerfile.
5. The Docker container is deployed on the **AWS EC2 instance**.
6. The application becomes accessible via the **EC2 public IP address**.
7. **Prometheus and Grafana** monitor system metrics and performance.
8. A **cron job runs the backup script daily** to create automated backups.

This workflow ensures automated integration, deployment, monitoring, and maintenance of the application.
