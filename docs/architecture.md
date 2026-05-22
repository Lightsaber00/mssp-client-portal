
    # Architecture Overview

    ## Goal

    MSSP Client Portal is structured to look and feel like a real product that a recruiter, hiring manager, or technical lead can understand quickly.

    ## Core Layers

    1. Presentation Layer — responsive single-page demo UI for fast exploration.
    2. Application Layer — orchestration logic for workflows, scoring, correlation, or enrichment.
    3. Data Layer — represented through mock JSON payloads.
    4. Integration Layer — documented REST endpoints for future external connections.

    ## Primary Components

    - **Asset Management** — Unified inventory for endpoints, cloud assets, identities, and business services.
- **SLA Tracking** — Visual service commitments with breach risk indicators and escalation windows.
- **Client Reporting** — Monthly security posture, incident activity, and compliance snapshots.
- **REST API Layer** — Partner-friendly endpoints for assets, tickets, reports, and service health.

    ## Example API Surface

    - `/api/clients`
- `/api/assets`
- `/api/tickets`
- `/api/sla/status`
