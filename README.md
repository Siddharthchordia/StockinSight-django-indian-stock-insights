# StockInSight - Indian Stock Insights

StockInSight is a powerful, comprehensive stock analysis and screening tool designed for the Indian market (NSE/BSE). It provides deep insights into company financials, historical price data, and key performance metrics, all wrapped in a modern, glassmorphic user interface.

## 🚀 Features

*   **Comprehensive Financial Analysis**: View detailed Profit & Loss, Balance Sheet, and Cash Flow statements.
*   **Interactive Visualizations**:
    *   Dynamic charts for price history and volume.
    *   Visual representation of financial trends over time.
    *   Quarterly and Annual data breakdown.
*   **Real-time Data**: Integration with `yfinance` for daily market snapshots and historical price data.
*   **Excel Data Import**: Seamlessly import financial data using standard Screener.in Excel exports.
*   **Advanced Search**: Fast, autocomplete-enabled stock search by ticker or company name.
*   **Modern UI/UX**:
    *   **Glassmorphism Design**: sleek, translucent panels with backdrop blur.
    *   **Responsive Layout**: Fully optimized for desktop and mobile devices.
    *   **Dark-themed Aesthetics**: Built with a polished, professional look using TailwindCSS.

## 🛠 Tech Stack

### Backend
*   **Framework**: [Django 5](https://www.djangoproject.com/) (Python 3.12)
*   **Database**: PostgreSQL
*   **Task Queue**: Celery with Redis (for background jobs like data fetching)
*   **Data Analysis**: Pandas, NumPy
*   **Financial Data**: `yfinance` API

### Frontend
*   **Structure**: Django Templates
*   **Styling**: [TailwindCSS](https://tailwindcss.com/) & [DaisyUI](https://daisyui.com/)
*   **Interactivity**: [HTMX](https://htmx.org/) (for SPA-like feel without complexity)
*   **Charts**: Chart.js

### DevOps & Infrastructure
*   **Containerization**: Docker & Docker Compose

## ⚡ Setup Guidance

### Prerequisites
*   [Docker](https://www.docker.com/) and Docker Compose installed on your machine.

### Installation Steps

1.  **Clone the Repository**
    ```bash
    git clone <repository_url>
    cd StockinSight
    ```

2.  **Environment Configuration**
    Create a `.env` file in the root directory. You can use the following template:
    ```env
    # Django Settings
    SECRET_KEY=your_secret_key_here
    DEBUG=1
    ALLOWED_HOSTS=localhost,127.0.0.1

    # Database Settings
    POSTGRES_DB=stockinsight_db
    POSTGRES_USER=postgres
    POSTGRES_PASSWORD=your_password
    POSTGRES_HOST=postgres
    POSTGRES_PORT=5432

    # Redis Settings
    REDIS_URL=redis://redis:6379/0
    ```

3.  **Build and Run**
    Start the application using Docker Compose:
    ```bash
    docker-compose up --build
    ```
    This will spin up the web server, PostgreSQL database, Redis, and Celery workers.

4.  **Apply Migrations**
    Once the containers are running, apply database migrations:
    ```bash
    docker-compose exec stockinsightbackend python manage.py makemigrations
    ```
    ```bash
    docker-compose exec stockinsightbackend python manage.py migrate
    ```

5.  **Access the Application**
    Open your browser and navigate to: [http://localhost:8000](http://localhost:8000)

## 🔐 Superuser Creation

To access the admin panel, you need to create a superuser account:

```bash
docker-compose exec stockinsightbackend python manage.py createsuperuser
```
Follow the prompts to set a username, email, and password.

## 🏢 Adding Companies

StockInSight uses a hybrid approach to add companies: manual creation coupled with financial data import via Excel.

1.  **Login to Admin Panel**
    Navigate to [http://localhost:8000/admin](http://localhost:8000/admin) and log in with your superuser credentials.

2.  **Add a Company**
    *   Go to **Companies** -> **Add company**.
    *   Enter the essential details:
        *   **Name**: Company Name
        *   **Ticker**: Stock Ticker (e.g., RELIANCE, TCS)
        *   **Exchange**: NSE or BSE
        *   **Sector**: Sector of Company
    *   **Upload Financial Data (Crucial Step)**:
        *   In the **Excel file** field, upload a standard financial export file (compatible with Screener.in format).
        *   **Required Format**: The Excel file must contain a sheet named `Data Sheet` with sections for "PROFIT & LOSS", "QUARTERS", "BALANCE SHEET", and "CASH FLOW".

3.  **Save**
    *   Click **Save**.
    *   **Behind the Scenes**: The system will automatically:
        *   Save the company record.
        *   Parse the Excel file to populate comprehensive financial data (metrics, time periods, values).
        *   Fetch live price snapshots from Yahoo Finance.
        *   Fetch historical price data.
        *   Calculate fundamental ratios (Fundamentals).

## 🎛 Management Commands

The project includes custom Django management commands for maintenance and data updates:

*   **`import_financials`**: Manual import financials.
*   **`generate_fundamentals`**: Recalculate fundamental ratios for companies.
*   **`get_snapshot`**: Fetch latest market price/snapshot for companies.
*   **`get_all_histories`**: Fetch complete historical price data for all companies.

Run them via Docker:
```bash
docker-compose exec stockinsightbackend python manage.py <command_name>
```

---
*Built by Siddharth Chordia*
