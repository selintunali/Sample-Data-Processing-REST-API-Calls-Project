# Database Design Considerations

## Overview
This document discusses the optimal way to organize data in the database for the script's requirements.

## Database Schema

### Normalization
- Aim for a normalized design to minimize redundancy.
- Use separate tables for portfolios, companies, and historical price data.

### Relationships
- Define foreign keys to maintain relationships between tables.
- Example: A portfolio table can reference multiple companies.

### Indexing
- Implement indexing on frequently accessed fields like `CompanyID` and `PortfolioId` to enhance query performance.

## Scalability and Performance
- Plan for scalability, considering future increases in data volume.
- Consider partitioning large tables if the dataset grows significantly.

## Data Integrity
- Ensure data types are appropriately chosen for each field.
- Implement constraints like `NOT NULL` and `UNIQUE` where applicable.
