import logging

from session import engine
from models.models import Event

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def init() -> None:
    """Checks conn to db before startup

    Raises:
        e: Probably conn error when db is unreachable
    """
    try:
        session = engine()
        session.get(Event)
    except Exception as e:
        logger.error(e)
        raise e


def main() -> None:
    logger.info("Initializing service")
    init()
    logger.info("Service finished initializing")


if __name__ == "__main__":
    main()
