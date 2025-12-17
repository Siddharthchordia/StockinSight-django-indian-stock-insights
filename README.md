# 📈 StockinSight

**Repository**: `Siddharthchordia/StockinSight-django-indian-stock-insights
**Status**: Public
**Tech Stack**: Django · PostgreSQL · Docker · Yahoo Finance (yfinance) · HTMX · TailwindCSS

---

## 🚀 Overview

Stock Market Analysis Tool is a **full‑stack Django application** designed for analyzing Indian stock market companies with a focus on **fundamentals, price history, and daily market snapshots**.

The project is inspired by platforms like *Screener.in*, but is built from scratch with:

* Structured financial data models
* Automated background jobs
* Scalable ingestion pipelines
* Clean, modern UI

---

## ✨ Key Features

### 📊 Company & Market Data

* Company master data (name, sector, exchange, ticker)
* Daily market snapshot (price, market cap, PE, PB, 52W high/low)
* Automatic updates using **Yahoo Finance API**

### 📈 Price History & Charting

* Historical OHLCV storage (`CompanyHistory`)
* Daily price append at **3:30 PM IST (10:00 AM UTC)**
* Efficient querying for chart rendering

### 📚 Fundamentals Engine

* P&L, Balance Sheet, Cash Flow support
* Quarterly and annual periods
* Metric‑driven design (EPS, Revenue, EBITDA, etc.)
* Excel import support (admin‑driven, replaceable later)

### ⏱ Background Jobs & Cron

* Daily price history update
* Daily market snapshot refresh
* Cron‑based execution (UTC aligned)

### 🧠 Architecture Highlights

* Normalized financial schema
* Idempotent data ingestion
* Optimized Django ORM usage
* Dockerized for easy deployment

---

## 🗂 Project Structure

```text
.
├── stock_tracker/      # Django project config
├── stocks/             # Core app (models, views, utils, cron jobs)
├── tracker/            # Frontend / UI layer
├── static/             # Static assets (CSS, JS)
├── tests/              # Test suite
├── Dockerfile
├── docker-compose.yaml
├── requirements.txt
├── manage.py
└── README.md
```

---

## 🐳 Local Setup (Docker)

### 1️⃣ Build containers

```bash
docker-compose build
```

### 2️⃣ Start services

```bash
docker-compose up -d
```

---

## 🧱 Django Setup (First Run)

### 3️⃣ Run migrations

```bash
docker-compose exec web python manage.py makemigrations
docker-compose exec web python manage.py migrate
```

### 4️⃣ Create superuser

```bash
docker-compose exec web python manage.py createsuperuser
```

---

## ⚙️ Initial Admin Configuration (IMPORTANT)

After logging into the Django admin panel:

### 1️⃣ Create **Metric Categories**

Create the following **three MetricCategory entries**:

* `Profit & Loss`
* `Balance Sheet`
* `Cash Flow`

These are required before importing any fundamentals data.

---

## 🧪 Excel Import (Fundamentals)

* Upload Screener‑style Excel files via Admin Panel
* System auto‑maps:

  * Metrics
  * Time periods
  * Companies
* Safe re‑runs without duplication

*(This is planned to be replaced with automated ingestion)*

---

## ⏰ Cron Jobs

Configured cron jobs handle:

* Daily price history update
* Daily market snapshot refresh

**Execution Time**:

* **3:30 PM IST / 10:00 AM UTC**

Cron jobs are defined within the Django app and executed via Docker environment.

---

## 🛣 Roadmap

* Automated fundamentals ingestion (no Excel)
* Historical valuation metrics (EPS, PE trends)
* Advanced charts & indicators
* Performance optimizations (ORM + SQL)
* Public API endpoints

---

## 👤 Author

**Siddharth Chordia**
GitHub: [@Siddharthchordia](https://github.com/Siddharthchordia)

---

## 📜 License

This project is currently unlicensed. All rights reserved by the author.

---

> ⚠️ **Disclaimer**: This project is for educational and research purposes only. It is not financial advice.
