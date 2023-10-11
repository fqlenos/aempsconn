"""
Base filter class for creating queries
"""


from ..utils import ConfigModel


class Filter:
    conditions: dict  # just for typing

    def __init__(self, config: ConfigModel) -> None:
        self.config: ConfigModel = config

    def query(self) -> str:
        """
        Creates the query to add in the URL for each HTTP Request.
        Gets the conditions that are created in its Filter Class.
        """
        query = "?"
        for key, value in self.conditions.items():
            if isinstance(value, bool):
                if value == True:
                    value = 1
                else:
                    value = 0

            query += f"{key}={str(value)}&"
        query: str = query[:-1]  # so it removes the last "&"

        if self.config.logger is not None:
            self.config.logger.debug(f"Query created: {query}")

        return query
