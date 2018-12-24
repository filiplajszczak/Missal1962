import re
from typing import List, Union

from constants.common import CUSTOM_PREFACES


def match(observances: List['Observance'], patterns: Union[List[str], str]):
    if not isinstance(patterns, (list, tuple)):
        patterns = [patterns]
    for observance in observances:
        for pattern in patterns:
            if re.match(pattern, observance.id):
                return observance


def infer_custom_preface(proper_id: str) -> str:
    for pattern, preface_name in CUSTOM_PREFACES.items():
        if re.match(pattern, proper_id):
            return preface_name
