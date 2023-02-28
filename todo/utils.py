import os
from ast import literal_eval
from typing import Any, Optional

from dotenv import load_dotenv

load_dotenv()


class Empty:
    """
    This class is used to represent no data being provided for a given input
    or output value.

    It is required because `None` may be a valid input or output value.
    """


def get_safe_env(
    variable_name: str,
    is_required: bool = True,
    default: Any = Empty,
    need_eval: bool = False,
) -> Any:
    value: Optional[str] = os.getenv(variable_name, None)
    if default is Empty and is_required and value is None:
        raise ValueError(f"{variable_name} is required. Check your .env file.")
    if value is None and default is not Empty:
        return default
    if need_eval:
        value = literal_eval(value)  # type: ignore
    return value


def preprocessing_filter_spec(endpoints):
    filtered = []
    for path, path_regex, method, callback in endpoints:
        # Remove all but DRF API endpoints
        if path.startswith("/api/"):
            filtered.append((path, path_regex, method, callback))
    return filtered
