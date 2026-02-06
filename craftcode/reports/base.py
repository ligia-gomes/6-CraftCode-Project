from dataclasses import dataclass
from typing import Callable, TYPE_CHECKING

import pandas as pd

if TYPE_CHECKING:
    from craftcode.core.context import RunContext


@dataclass(frozen=True)
class ReportSpec:
    report_id: str
    name: str
    file_prefix: str
    builder: Callable[[pd.DataFrame, 'RunContext'], pd.DataFrame]
