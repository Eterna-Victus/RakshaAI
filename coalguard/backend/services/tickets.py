from datetime import datetime, timezone
from typing import Any
from uuid import uuid4


TICKET_STATUSES = ("OPEN", "ASSIGNED", "IN_PROGRESS", "VERIFICATION", "CLOSED")


class TicketService:
    def __init__(self) -> None:
        self._tickets: dict[str, dict[str, Any]] = {}

    def list_tickets(self) -> list[dict[str, Any]]:
        return sorted(self._tickets.values(), key=lambda ticket: ticket["created_at"], reverse=True)

    def create_ticket(self, title: str, description: str, source: str, severity: str = "high") -> tuple[dict[str, Any], bool]:
        for ticket in self._tickets.values():
            if ticket["source"] == source and ticket["status"] != "CLOSED":
                return ticket, False
        now = datetime.now(timezone.utc).isoformat()
        ticket = {
            "id": f"TKT-{uuid4().hex[:8].upper()}",
            "title": title,
            "description": description,
            "source": source,
            "severity": severity,
            "status": "OPEN",
            "assignee": "Shift Maintenance Team",
            "created_at": now,
            "updated_at": now,
            "timeline": [{"status": "OPEN", "at": now, "note": "Automatically created from live telemetry."}],
        }
        self._tickets[ticket["id"]] = ticket
        return ticket, True

    def update_ticket(self, ticket_id: str, status: str | None = None, assignee: str | None = None, note: str | None = None) -> dict[str, Any]:
        ticket = self._tickets.get(ticket_id)
        if not ticket:
            raise KeyError(ticket_id)
        if status is not None and status not in TICKET_STATUSES:
            raise ValueError(f"Unsupported ticket status: {status}")
        if status is not None and status != ticket["status"]:
            ticket["status"] = status
        if assignee:
            ticket["assignee"] = assignee
        now = datetime.now(timezone.utc).isoformat()
        ticket["updated_at"] = now
        ticket["timeline"].append({"status": ticket["status"], "at": now, "note": note or "Ticket updated."})
        return ticket

ticket_service = TicketService()
