from typing import Tuple, List, Union, TypedDict


class Role:

    permissions: Union[str, List[str]]

    def __init__(self, permissions: Union[str, List[str]]):
        """
        :param permissions:
        """
        self.permissions = permissions
