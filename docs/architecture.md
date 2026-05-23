# MSSP Client Portal Architecture

## Objective

The MSSP Client Portal is a customer-facing cybersecurity platform concept for managed security services. It is designed to provide transparency across assets, SLA performance, tickets, reporting, and future security integrations in one unified portal.

## High-level view

The project is intentionally split into three layers:

- **Presentation layer** for the customer-facing portal experience
- **API layer** for service endpoints and integration contracts
- **Service and data layer** for business logic, reporting, and future persistence

This structure makes the repository easy to understand for recruiters while still showing a clear path toward a real product implementation.

## Layer overview

### 1. Presentation layer

The frontend is designed as a lightweight demo that can be reviewed quickly in a browser.

Main goals:
- Show product thinking and customer workflow design
- Present portal capabilities without login or setup friction
- Support quick review by recruiters and hiring managers

Key entry point:
- `frontend/index.html`

### 2. API layer

The backend is modeled as a FastAPI-style service skeleton.

Main goals:
- Define a clean future integration surface
- Separate customer-facing views from service logic
- Show how the platform can evolve into a production-ready application

Key entry point:
- `backend/app/main.py`

Representative API areas:
- Clients
- Assets
- Tickets
- SLA summaries
- Reporting

### 3. Service and data layer

The service layer is the future location for:
- business rules
- SLA calculations
- report generation
- tenant separation
- integration handling

The data layer can later be backed by PostgreSQL or another relational store, with optional background workers for report generation and data sync jobs.

## Suggested module map

```text
frontend/
  MSSP_client_portal.html

backend/
  app/
    main.py
    routes/
    models/
    services/
  tests/

docs/
  architecture.md
  roadmap.md
  index.html
