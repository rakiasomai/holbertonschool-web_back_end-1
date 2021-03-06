#!/usr/bin/env python3
""" Hash password in database
"""
from db import DB
import bcrypt
from user import User
from sqlalchemy.orm.exc import NoResultFound
from uuid import uuid4


def _hash_password(password: str) -> str:
    """ takes in a password string arguments and returns a string
    """
    salt = bcrypt.gensalt()
    hashed = bcrypt.hashpw(password.encode('utf-8'), salt)
    return hashed


def _generate_uuid() -> str:
    """ generate uuid
    """
    return str(uuid4())


class Auth:
    """Auth class to interact with the authentication database.
    """

    def __init__(self):
        """ Auth class constructor
        """
        self._db = DB()

    def register_user(self, email: str, password: str) -> User:
        """ Register user with email and password
        """
        if email and password:
            try:
                self._db.find_user_by(email=email)
            except NoResultFound:
                new_user = self._db.add_user(email, _hash_password(password))
                return new_user
            else:
                raise ValueError("User {} already exists".format(email))

    def valid_login(self, email: str, password: str) -> bool:
        """ Credentials validation
        """
        try:
            self._db.find_user_by(email=email)
        except NoResultFound:
            return False
        pwd = _hash_password(password)
        return bcrypt.checkpw(password.encode('utf-8'), pwd)

    def create_session(self, email: str) -> str:
        """ Create session
        """
        try:
            user = self._db.find_user_by(email=email)
        except NoResultFound:
            return
        sess_id = _generate_uuid()
        self._db.update_user(user.id, session_id=sess_id)
        return sess_id

    def get_user_from_session_id(self, session_id: str) -> str:
        """ get user from session id
        """
        if session_id:
            try:
                return self._db.find_user_by(session_id=session_id)
            except NoResultFound:
                return

    def destroy_session(self, user_id: int) -> None:
        """ destroy session
        """
        if user_id:
            self._db.update_user(user_id, session_id=None)

    def get_reset_password_token(self, email: str) -> str:
        """ get reset password token.
        """
        if email:
            try:
                user = self._db.find_user_by(email=email)
            except NoResultFound:
                raise ValueError
            else:
                token = _generate_uuid()
                self._db.update_user(user.id, reset_token=token)
                return token

    def update_password(self, reset_token: str, password: str) -> None:
        """ update password
        """
        if reset_token and password:
            try:
                user = self._db.find_user_by(email=email)
            except NoResultFound:
                raise ValueError
            else:
                hashed = _hash_password(password)
                self._db.update_user(user.id, password=hashed)
                self._db.update_user(user.id, reset_token=None)
