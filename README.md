# SmartGuard — Online Scam Verification & Entity Knowledge Graph

[![Platform](https://img.shields.io/badge/Platform-Web%20%7C%20Android%20Native-0d1117?style=flat-square&logo=android&logoColor=white)](#tech-stack)
[![Backend](https://img.shields.io/badge/Backend-FastAPI%20(Python%203.11)-009688?style=flat-square&logo=fastapi&logoColor=white)](https://fastapi.tiangolo.com)
[![Graph DB](https://img.shields.io/badge/Graph_DB-Neo4j%205.18-008CC1?style=flat-square&logo=neo4j&logoColor=white)](https://neo4j.com)
[![Database](https://img.shields.io/badge/Database-PostgreSQL%2016-336791?style=flat-square&logo=postgresql&logoColor=white)](https://www.postgresql.org)
[![Frontend](https://img.shields.io/badge/Frontend-Next.js%2014-black?style=flat-square&logo=nextdotjs&logoColor=white)](https://nextjs.org)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue?style=flat-square)](LICENSE)

A multi-modal fraud detection platform designed to verify suspicious transactions, unmask organized scam syndicates via Entity Knowledge Graphs (Neo4j), and protect vulnerable individuals with native Android background monitoring and automated Family SOS alerts.

---

## Key Features

- **Multi-Modal Verification Engine:** High-throughput verification of bank accounts, phone numbers, VietQR (Napas EMVCo) strings, phishing URLs, and duplicate scam imagery using 64-bit perceptual hashing (`pHash`).
- **Entity Knowledge Graph (Neo4j):** Real-time multi-hop graph traversal linking accounts, phone numbers, and community reports to instantly unmask burner SIMs belonging to known fraud networks.
- **Android Background Guardian:** Native Kotlin services (`CallScreeningService` & `NotificationListenerService`) intercepting high-risk scam calls pre-ringtone (< 500 ms) and parsing payment metadata safely.
- **Family SOS Emergency Protocol:** Automated high-priority push notifications via Firebase Cloud Messaging (FCM) dispatched to family guardians within 1 second upon critical threat detection.
- **Interactive Forensic Dashboard:** Web-based investigation canvas built with Next.js and Cytoscape.js for exploring entity clusters, transaction pathways, and syndicate heatmaps.

---

## Tech Stack

| Component | Technologies | Key Role |
| :--- | :--- | :--- |
| **Mobile Client** | Android Native (Kotlin), Jetpack Compose | Pre-ring call screening, notification parsing, 1-touch SOS overlay |
| **Web Frontend** | Next.js 14, React, TypeScript, Cytoscape.js | Interactive graph explorer, forensic analysis console, dispute review |
| **API Server** | FastAPI (Python 3.11, AsyncIO), Pydantic v2 | High-concurrency REST endpoints, JWT auth, business logic routing |
| **Graph Database** | Neo4j Community 5.18, Cypher | Entity relationship traversal (`Phone`, `BankAccount`, `ImageHash`) |
| **Relational Database** | PostgreSQL 16, SQLAlchemy ORM | User accounts, audit logs, dispute cases, and administrative tables |
| **Integrations** | FCM, Google Safe Browsing, Gemini Flash | Guardian emergency push, phishing URL checks, What-If simulations |

---

## Project Structure

```text
antiscam-system/
├── backend/          # FastAPI REST API, database models, and scoring services
├── web/              # Next.js 14 web application & Cytoscape graph canvas
├── mobile/           # Android native app (CallScreening & Notification services)
├── docs/             # Technical specifications, API contracts, and schema designs
├── scripts/          # Mock data generator and Neo4j graph seeding utilities
└── docker-compose.yml# Local orchestration (Backend + Neo4j + PostgreSQL)
```

---

## Risk Scoring Model

SmartGuard computes a normalized **Trust Score (0 – 100)** by aggregating signals from graph proximity, verified community reports, perceptual image matching, and linguistic urgency indicators:

| Trust Score | Risk Tier | Badge | System Action |
| :---: | :---: | :---: | :--- |
| **80 – 100** | **Low Risk** | 🟢 Green | Verified clean reputation; normal operation. |
| **50 – 79** | **Moderate** | 🟡 Yellow | Cautionary banner; highlight unverified attributes. |
| **25 – 49** | **High Risk** | 🟠 Orange | Prominent warning banner; prompt secondary confirmation. |
| **0 – 24** | **Critical Danger** | 🔴 Red | Pre-ring call block (< 500 ms); instant Family SOS dispatch. |

---

## Quick Start

### 1. Clone & Configure

```bash
git clone https://github.com/your-org/antiscam-system.git
cd antiscam-system
cp .env.example .env
```

### 2. Launch Services

```bash
docker compose up -d
```

### 3. Seed Demo Data

```bash
docker compose exec backend python scripts/seed_data.py
```

### 4. Service Endpoints

* **Web Application:** [http://localhost:3000](http://localhost:3000)
* **API Documentation (Swagger):** [http://localhost:8000/docs](http://localhost:8000/docs)
* **Neo4j Browser Console:** [http://localhost:7474](http://localhost:7474) *(User: `neo4j` / Password: `antiscam_neo4j_pass`)*

---

## Core API Endpoints

| Method | Endpoint | Description |
| :--- | :--- | :--- |
| `POST` | `/api/v1/verify/quick-lookup` | Fast pre-ring check for phone numbers or bank accounts (< 500 ms) |
| `POST` | `/api/v1/verify/post` | Comprehensive multi-modal inspection (text, pHash, URL, VietQR) |
| `POST` | `/api/v1/sos/trigger` | Dispatch emergency SOS alert to linked guardians via FCM |
| `GET` | `/api/v1/graph/explore` | Query entity subgraph nodes and edges for Cytoscape visualization |
| `POST` | `/api/v1/reports/submit` | Submit a community fraud report with evidence attachments |

---

## Documentation

* 📑 [RESTful API Contract Specification](docs/API_CONTRACT.md)
* 🗄️ [Database Architecture & Graph Schema](docs/DATABASE_SCHEMA.md)
* 🌿 [Git Branching Strategy & Workflow Conventions](docs/GIT_WORKFLOW.md)
* 📐 [System Technical Proposal & Requirements](docs/PROPOSAL.md)

---

## Contributors

- Đặng Quang Tiến
- Hoàng Khang
- Trương Bảo Nguyên
- Sỉn Thăng Quyền

---

## License

This project is licensed under the [MIT License](LICENSE).
