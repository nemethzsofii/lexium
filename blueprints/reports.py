from flask import Blueprint, render_template
from sqlalchemy import func
from db import db
from models import Case, CaseWork, Client

reports_bp = Blueprint("reports", __name__)
@reports_bp.route("/reports")
def reports():
    # Calculate total worked hours per case
    results = (
        db.session.query(
            Case.id.label("case_id"),
            Case.number.label("case_number"),
            Case.name.label("case_name"),
            Client.name.label("client_name"),
            func.sum(
                func.extract(
                    'epoch',
                    CaseWork.end_time - CaseWork.start_time
                ) / 3600
            ).label("total_hours")
        )
        .join(CaseWork, CaseWork.case_id == Case.id)
        .join(Client, Client.id == Case.client_id)
        .group_by(Case.id, Client.name)
        .order_by(Case.number)
        .all()
    )

    return render_template("reports.html", reports=results)
