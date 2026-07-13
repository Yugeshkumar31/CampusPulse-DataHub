# CampusPulse

A data engineering project for campus data processing and analytics.

## Project Structure

```
CampusPulse/
├── data/
│   ├── raw/              # Raw input data
│   └── processed/        # Processed/cleaned data
├── scripts/
│   ├── generate_data.py   # Data generation script
│   ├── spark_etl.py       # Spark ETL operations
│   └── load_to_postgres.py # Database loader
├── sql/
│   ├── schema.sql        # Database schema
│   └── queries.sql       # Analytical queries
├── dashboard/            # Dashboard configurations
└── README.md
```

## Getting Started

### Prerequisites
- Python 3.x
- Apache Spark
- PostgreSQL

### Installation

1. Clone the repository
2. Install dependencies
3. Configure database connection

### Usage

1. Generate data: `python scripts/generate_data.py`
2. Run ETL: `python scripts/spark_etl.py`
3. Load to database: `python scripts/load_to_postgres.py`

## Contributing

Pull requests are welcome.

## License

MIT License
