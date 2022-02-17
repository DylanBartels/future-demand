from fastapi import Depends, APIRouter
from sqlmodel import Session


from api import deps
from models.models import Event

router = APIRouter()


@router.get("/", response_model=list[Event])
def get_events(
    session: Session = Depends(deps.get_session),
):
    return session.query(Event).all()
