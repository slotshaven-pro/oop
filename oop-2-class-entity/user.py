"""" docstring """
class User:
    """" docstring """
    def __init__(self, uid: int, uname: str, password: str = "welcome"):
        self._uid = uid
        self._uname = uname
        self._password = password

    def get_uid(self) -> int:
        """" docstring """
        return self._uid

    def set_uid(self, uid: int) -> None:
        """" docstring """
        self._uid = uid

    def get_uname(self) -> str:
        """" docstring """
        return self._uname

    def set_uname(self, uname: str) -> None:
        """" docstring """
        self._uname = uname

    def get_password(self) -> str:
        """" docstring """
        return self._password

    def set_password(self, password: str) -> None:
        """" docstring """
        self._password = password
