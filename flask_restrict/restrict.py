import functools
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

    def permissions(self):
        """

        :return:
        """

    def modal(self, func=None):
        sql_modal = func
        tablename = getattr(sql_modal, "__tablename__", None)
        modal_keys = sql_modal.__dict__.keys()
        for m in modal_keys:
            if isinstance(getattr(sql_modal, m), Role):
                role: Role = getattr(sql_modal, m)
        @functools.wraps
        def inner():
            pass
        return inner
