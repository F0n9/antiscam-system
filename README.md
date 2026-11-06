# SmartGuard — Online Scam Verification & Entity Knowledge Graph Warning System

[![Platform: Web & Mobile](https://img.shields.io/badge/Platform-Web%20%7C%20Android%20Native-0d1117?style=flat-square&logo=android&logoColor=white)](#system-architecture)
[![Backend: FastAPI](https://img.shields.io/badge/Backend-FastAPI%20(Python%203.11)-009688?style=flat-square&logo=fastapi&logoColor=white)](https://fastapi.tiangolo.com)
[![Graph DB: Neo4j](https://img.shields.io/badge/Graph_DB-Neo4j%205.18-008CC1?style=flat-square&logo=neo4j&logoColor=white)](https://neo4j.com)
[![Database: PostgreSQL](https://img.shields.io/badge/Database-PostgreSQL%2016-336791?style=flat-square&logo=postgresql&logoColor=white)](https://www.postgresql.org)
[![Frontend: Next.js](https://img.shields.io/badge/Frontend-Next.js%2014-black?style=flat-square&logo=nextdotjs&logoColor=white)](https://nextjs.org)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue?style=flat-square)](LICENSE)

A multi-modal cybersecurity and fraud prevention platform designed to verify suspicious online postings, uncover organized scam syndicates using Entity Knowledge Graphs, and provide real-time protection for vulnerable individuals and families via native Android background monitoring and automated emergency SOS alerts.

---

## Key Features

- **Multi-Modal Verification Engine:** High-throughput verification of bank accounts, phone numbers, VietQR Napas strings, suspect URLs, and duplicate fraud image detection via 64-bit Perceptual Hashing (`pHash` with Hamming distance threshold $\le 10$).
- **Entity Knowledge Graph (Neo4j):** Real-time multi-hop graph traversal (up to 3 hops) linking phone numbers, bank accounts, perceptual image hashes, and community reports to instantly unmask new throwaway SIM cards belonging to known fraud networks.
- **Android Background Guardian:** Native Kotlin background services utilizing `CallScreeningService` to intercept high-risk scam calls pre-ringtone (< 500 ms) and `NotificationListenerService` to passively parse payment entities from Zalo, Messenger, and SMS without privacy infringement.
- **Family SOS Emergency Protocol:** Automated high-priority push notification dispatch via Firebase Cloud Messaging (FCM) to designated family guardians within 1 second when an elderly family member receives high-risk calls (< 25 trust score).
- **Psychological Manipulation & Scenario Simulation:** Natural language processing flagging 4 major manipulation patterns (urgency, financial lures, authority impersonation, secrecy) with automated 3-step What-If scenario forecasts.
- **Interactive Graph Visualization:** Web-based forensic analysis dashboard built with Next.js and Cytoscape.js for exploring entity clusters, transaction pathways, and geographic scam density heatmaps.

---

## Tech Stack & Architecture

| Layer | Technology | Key Modules & Purpose |
| :--- | :--- | :--- |
| **Mobile Client** | Android Native (Kotlin), Jetpack Compose | `CallScreeningService` (call interceptor), `NotificationListenerService` (passive parser), CameraX (VietQR scanner), 1-touch SOS overlay |
| **Web Frontend** | Next.js 14, React, TypeScript, Tailwind CSS | Cytoscape.js interactive graph explorer, forensic analysis console, community report portal, dispute review workflow |
| **API Server** | FastAPI (Python 3.11, AsyncIO), Pydantic v2 | High-concurrency RESTful API endpoints, JWT authentication, rate limiting, and business logic routing |
| **Graph Database** | Neo4j Community 5.18, Cypher | Entity relationship storage (`Phone`, `BankAccount`, `ImageHash`, `Report`), multi-hop traversal, syndication clustering |
| **Relational Database** | PostgreSQL 16, SQLAlchemy ORM | User authentication, RBAC authorization, lookup audit logs, dispute cases, and administrative tables |
| **Algorithms & Workers** | Redis, Celery, ImageHash, PhoBERT | 64-bit DCT perceptual hashing, regex EMVCo parsing, async task delegation, and trust score computation |
| **Third-Party Services** | Firebase Admin SDK, Google Safe Browsing, Gemini Flash | Push notifications (FCM), phishing URL verification, and AI-driven What-If deception scenario generation |

---

## Directory Structure

```text
antiscam-system/
├── backend/                   # FastAPI application, database drivers & core logic
│   ├── app/
│   │   ├── api/v1/endpoints/  # API routers (auth, verify, reports, sos, graph)
│   │   ├── core/              # Config, security, DB connections (Neo4j & Postgres)
│   │   ├── models/            # Pydantic schemas & SQLAlchemy models
│   │   └── services/          # Graph traversal, scoring engine, pHash, VietQR parser
│   ├── init-db/               # PostgreSQL auto-migration scripts
│   ├── tests/                 # Unit & integration test suites
│   ├── Dockerfile             # Container specification for backend server
│   └── requirements.txt       # Python dependencies
├── web/                       # Next.js 14 frontend web application
│   ├── src/
│   │   ├── components/        # UI components, layout, and Cytoscape graph canvas
│   │   ├── pages/             # App routing (dashboard, lookup, graph, admin)
│   │   └── services/          # API client for backend integration
│   └── package.json
├── mobile/                    # Android native application (Kotlin)
│   ├── app/src/main/
│   │   ├── java/com/smartguard/
│   │   │   ├── services/      # CallScreeningService & NotificationListenerService
│   │   │   ├── ui/            # Jetpack Compose screens (WF-01 SOS & WF-02 VietQR)
│   │   │   └── utils/         # VietQR Napas EMVCo decoder & Clipboard auto-detect
│   │   └── AndroidManifest.xml
│   └── build.gradle.kts
├── scripts/                   # Database seeding and migration utilities (seed_data.py)
├── docs/                      # Engineering specifications & design documents
│   ├── API_CONTRACT.md        # Detailed REST API specification between modules
│   ├── DATABASE_SCHEMA.md     # Neo4j Cypher schema & PostgreSQL DDL
│   ├── PROPOSAL.md            # System requirements & technical design proposal
│   └── GIT_WORKFLOW.md        # Branching model and engineering conventions
├── docker-compose.yml         # Local container orchestration (PostgreSQL + Neo4j + Backend)
├── .env.example               # Environment variables template
└── .gitignore                 # Build artifact and credential exclusions
```

---

## Scoring Engine & Trust Metrics

The system computes a normalized **Credit Score** ($0 \dots 100$) for every verified entity based on multi-factor penalty aggregation:

$$\text{Credit Score} = 100 - \min\Big(100,\; W_g \cdot S_g + W_p \cdot S_p + W_i \cdot S_i + W_s \cdot S_s\Big)$$

* $S_g \in [0, 100]$: **Graph Penalty** — derived from shortest path distance and severity of linked fraudulent nodes in the Neo4j knowledge graph.
* $S_p \in [0, 100]$: **Community Report Penalty** — volume, recency, and verification level of approved dispute-free reports.
* $S_i \in \{0, 100\}$: **Perceptual Image Penalty** — triggered when Hamming distance $\le 10$ against the blacklisted image hash database.
* $S_s \in [0, 100]$: **Scenario & Linguistic Penalty** — detected psychological pressure and urgency indicators.
* **Weights:** $W_g = 0.35,\; W_p = 0.30,\; W_i = 0.20,\; W_s = 0.15$ ($\sum W = 1.0$).

### Risk Level Classification

| Score Range | Risk Tier | Badge Color | System Action |
| :---: | :---: | :---: | :--- |
| **80 – 100** | **An toàn** (Safe) | 🟢 Green | Normal operation; verified safe status. |
| **50 – 79** | **Cần thận trọng** (Caution) | 🟡 Yellow | Display cautionary note; highlight missing verifiable info. |
| **25 – 49** | **Nguy cơ cao** (High Risk) | 🟠 Orange | Prominent warning banner; prompt secondary confirmation. |
| **0 – 24** | **Cực kỳ nguy hiểm** (Critical) | 🔴 Red | Full-screen overlay; block call; trigger instant Family SOS. |

---

## Quick Start

### Prerequisites

* [Docker](https://www.docker.com/) (Engine 24.0+) & Docker Compose v2.
* [Git](https://git-scm.com/).
* Python 3.11+ *(optional, for local development outside Docker)*.

### 1. Clone the repository

```bash
git clone https://github.com/your-org/antiscam-system.git
cd antiscam-system
```

### 2. Configure environment variables

```bash
cp .env.example .env
# Review and adjust ports/passwords if necessary in .env
```

### 3. Spin up infrastructure with Docker

```bash
docker compose up -d
```

### 4. Verify running services

* **FastAPI Swagger Documentation:** [http://localhost:8000/docs](http://localhost:8000/docs)
* **FastAPI ReDoc:** [http://localhost:8000/redoc](http://localhost:8000/redoc)
* **Neo4j Browser Console:** [http://localhost:7474](http://localhost:7474) *(User: `neo4j` / Password: `antiscam_neo4j_pass`)*
* **PostgreSQL Database:** Port `5432` *(DB: `antiscam_db` / User: `antiscam_user`)*

### 5. Seed initial mock graph & audit data

```bash
# Seed mock scam network with 10+ entities and fraud relationships
docker compose exec backend python scripts/seed_data.py
```

---

## Core API Endpoints

| Method | Endpoint | Description |
| :--- | :--- | :--- |
| `POST` | `/api/v1/auth/login` | Authenticate user & issue JWT bearer token |
| `POST` | `/api/v1/verify/post` | Comprehensive multi-modal inspection (text, pHash, URL, VietQR) |
| `POST` | `/api/v1/verify/quick-lookup` | Fast pre-ring check for incoming phone numbers or bank accounts (< 500 ms) |
| `POST` | `/api/v1/sos/trigger` | Dispatch emergency SOS alert to linked family guardians via FCM |
| `GET` | `/api/v1/graph/explore` | Query entity subgraph nodes and edges for Cytoscape visualization |
| `POST` | `/api/v1/reports/submit` | Submit a community scam report with evidence attachments |
| `POST` | `/api/v1/disputes/create` | File a dispute claim for falsely flagged entities |

---

## Technical Documentation

Detailed architectural contracts, schemas, and development guides are maintained in the `/docs` directory:

* 📑 [RESTful API Contract Specification](docs/API_CONTRACT.md)
* 🗄️ [Database Architecture & Graph Schema](docs/DATABASE_SCHEMA.md)
* 🌿 [Git Branching Strategy & Workflow Conventions](docs/GIT_WORKFLOW.md)
* 📐 [System Technical Proposal & Requirements](docs/PROPOSAL.md)

---

## License

This project is licensed under the [MIT License](LICENSE).
