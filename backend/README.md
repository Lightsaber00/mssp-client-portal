# Backend Skeleton

This folder contains the backend structure for the MSSP Client Portal.

## Purpose

The backend is intentionally lightweight and serves as an architecture skeleton. It shows how the portal can evolve into a production-grade cybersecurity application without forcing a full deployment at the portfolio stage.

## Suggested stack

- FastAPI for API routing
- Pydantic for request and response models
- PostgreSQL for persistence
- Redis or a queue system for background jobs
- Docker for local and production-ready environments

## Structure

- `app/main.py` — application entry point
- `app/routes/` — HTTP route definitions
- `app/models/` — request and response schemas
- `app/services/` — business logic and orchestration
- `tests/` — API and workflow tests

## What this backend will eventually support

- Client and tenant management
- Asset inventory
- SLA tracking
- Ticket management
- Report generation
- Integrations with SIEM, CMDB, and ticketing systems

## Portfolio note

This repository is meant to demonstrate architecture thinking, not just UI design. It is intentionally structured so a recruiter can see the path from demo to production.
