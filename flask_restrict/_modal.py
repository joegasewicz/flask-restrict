from sqlalchemy import Column, String

FLASK_RESTRICT_PERMS = [("super", 1), ("admin", 2), ("user", 3)]


class Modal:

    def __init__(self, sql_modal: object):

        for perm_name, position in FLASK_RESTRICT_PERMS:
            setattr(sql_modal, f"__fr_{perm_name}__", Column(String()))
        return sql_modal
