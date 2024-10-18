from core.db.database import engine, Users
from sqlalchemy.orm import Session
from core.middlewares.settings import settings
import requests


class DBOperations:

    @staticmethod
    def create_user(user_id: int, first_name:str,
                    last_name:str, username:str,
                    lat: float, lon: float):
        with Session(bind=engine) as session:
            user = Users(
                user_id=str(user_id),
                first_name=first_name,
                last_name=last_name,
                username=username,
                lat=lat,
                lon=lon
            )
            session.add(user)
            session.commit()


    @staticmethod
    def check_user_exists(user_id: int) -> bool:
        with Session(bind=engine) as session:
            stmt = session.query(Users).filter(Users.user_id == user_id).one_or_none()
            return bool(stmt)


    @staticmethod
    def delete_account(user_id: int):
        with Session(bind=engine) as session:
            user_to_delete = session.query(Users).filter(Users.user_id == user_id).first()

            if user_to_delete:
                session.delete(user_to_delete)
                session.commit()


    @staticmethod
    def get_lat(user_id: int):
        with Session(bind=engine) as session:
            lat = session.query(Users.lat).filter(Users.user_id == user_id).first()

            return lat


    @staticmethod
    def get_lon(user_id: int):
        with Session(bind=engine) as session:
            lon = session.query(Users.lon).filter(Users.user_id == user_id).first()

            return lon


    @classmethod
    def get_weather(cls, user_id):
        lat = (cls.get_lat(user_id))[0]
        lon = (cls.get_lon(user_id))[0]

        api = settings.bot_config.api
        https = settings.bot_config.https

        query = f"{https}?lat={lat}&lon={lon}&key={api}"

        response = requests.get(query)

        return response.text
