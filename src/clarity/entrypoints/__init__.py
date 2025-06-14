"""Service Entry Points for CLARITY Platform.

This module contains standalone service entry points for:
- Analysis Service: Health data processing via Pub/Sub
- Insight Service: AI-powered insight generation via Pub/Sub

Each service runs as a separate process/container in production.
"""

from __future__ import annotations
