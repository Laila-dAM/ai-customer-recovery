from fastapi import APIRouter, Depends, HTTPException, Query, Response, status
from sqlalchemy.orm import Session

from app.dependencies import get_current_user, get_db
from app.models import Lead, User
from app.schemas.leads import LeadCreate, LeadResponse, LeadStatus, LeadUpdate


router = APIRouter(prefix="/leads", tags=["Leads"])


def get_company_lead(
    lead_id: int,
    company_id: int,
    db: Session,
) -> Lead:
    lead = (
        db.query(Lead)
        .filter(
            Lead.id == lead_id,
            Lead.company_id == company_id,
        )
        .first()
    )

    if lead is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Lead not found",
        )

    return lead


@router.post(
    "",
    response_model=LeadResponse,
    status_code=status.HTTP_201_CREATED,
)
def create_lead(
    lead_data: LeadCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    lead = Lead(
        company_id=current_user.company_id,
        **lead_data.model_dump(),
    )

    db.add(lead)
    db.commit()
    db.refresh(lead)

    return lead


@router.get("", response_model=list[LeadResponse])
def list_leads(
    lead_status: LeadStatus | None = Query(default=None, alias="status"),
    offset: int = Query(default=0, ge=0),
    limit: int = Query(default=20, ge=1, le=100),
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    query = db.query(Lead).filter(
        Lead.company_id == current_user.company_id
    )

    if lead_status is not None:
        query = query.filter(Lead.status == lead_status)

    return (
        query.order_by(Lead.created_at.desc())
        .offset(offset)
        .limit(limit)
        .all()
    )


@router.get("/{lead_id}", response_model=LeadResponse)
def get_lead(
    lead_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    return get_company_lead(
        lead_id,
        current_user.company_id,
        db,
    )


@router.patch("/{lead_id}", response_model=LeadResponse)
def update_lead(
    lead_id: int,
    lead_data: LeadUpdate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    lead = get_company_lead(
        lead_id,
        current_user.company_id,
        db,
    )

    update_data = lead_data.model_dump(exclude_unset=True)

    if any(
        update_data.get(field) is None
        for field in ("name", "status")
        if field in update_data
    ):
        raise HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            detail="Name and status cannot be null",
        )

    for field, value in update_data.items():
        setattr(lead, field, value)

    db.commit()
    db.refresh(lead)

    return lead


@router.delete("/{lead_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_lead(
    lead_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    lead = get_company_lead(
        lead_id,
        current_user.company_id,
        db,
    )

    db.delete(lead)
    db.commit()

    return Response(status_code=status.HTTP_204_NO_CONTENT)
