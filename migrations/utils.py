from typing import Literal
from pathlib import Path


def read_sql(
    migration_filepath: str, direction: Literal["upgrade", "downgrade"]
) -> str:
    """Read a SQL file and return the raw SQL statement as a string."""

    fp = Path(migration_filepath)
    base = fp.stem
    sql_fp = fp.parent / f"{base}_{direction}.sql"

    with open(sql_fp, "r") as f:
        sql = f.read()
    return sql
