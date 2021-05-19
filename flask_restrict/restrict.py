from typing import Tuple, List, Union, TypedDict


from flask_restrict._modal import Modal
from flask_restrict._role import Role


class TypePermMeta(TypedDict):
    pass


class Restrict:

    permissions: List[Tuple[str, int]]

    _perm_meta: TypePermMeta

    Modal = Modal

    Role = Role

    def init(self, *args, **kwargs):
        """

        :param args:
        :param kwargs:
        :return:
        """

    def create_table(self):
        """
        Create tables
        :return:
        """

    def view(self):
        """

        :return:
        """


