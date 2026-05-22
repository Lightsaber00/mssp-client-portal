
    # MSSP Client Portal

    > Asset management, SLA tracking, ticketing, reporting, and client-facing API views.

    ## Why this project

    This is the strongest recruiter-facing project for security architecture, consulting, and service delivery leadership roles.

    This repository is designed as a recruiter-friendly portfolio project: a live-demo-first frontend, backed by a documented backend/API skeleton, architecture notes, and realistic sample data.

    ## What is included

    - `app/mssp-client-portal.html` — single-file clickable demo for fast preview
    - `backend/` — mock API skeleton and route examples
    - `docs/architecture.md` — architecture and data flow overview
    - `docs/demo-walkthrough.md` — what a recruiter or hiring manager should click first
    - `README.md` — concise project context, setup, and roadmap

    ## Demo highlights

    - Client dashboard with SLA widgets
    - Asset and ticket drilldowns
    - API documentation starter
    - Executive reporting section

    ## Run locally

    ```bash
    cd app
    python3 -m http.server 8080
    ```

    Then open `http://localhost:8080/mssp-client-portal.html`.

    ## API skeleton

    - `/api/clients`
- `/api/assets`
- `/api/tickets`
- `/api/sla/status`
