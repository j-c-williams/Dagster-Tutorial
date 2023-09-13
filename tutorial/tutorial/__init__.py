from dagster import (
    AssetSelection,
    Definitions,
    ScheduleDefinition,
    define_asset_job,
    load_assets_from_modules,
    FilesystemIOManager,
    EnvVar,
)
from dagster_duckdb_pandas import DuckDBPandasIOManager
from .resources import DataGeneratorResource

from . import assets

all_assets = load_assets_from_modules([assets])


hackernews_job = define_asset_job("hackernews_job", selection=AssetSelection.all())

hackernews_schedule = ScheduleDefinition(
    job=hackernews_job,
    cron_schedule="0 * * * *",  # every hour
)

io_manager = FilesystemIOManager(
    base_dir="data", # Path is relative to where dagster dev runs
)

database_io_manager = DuckDBPandasIOManager(database="analytics.hackernews")

datagen = DataGeneratorResource(
    num_days=EnvVar.int("HACKERNEWS_NUM_DAYS_WINDOW"),
)


defs = Definitions(
    assets=all_assets,
    schedules=[hackernews_schedule],
    resources={
        "io_manager": io_manager,
        "database_io_manager": database_io_manager,
        "hackernews_api": datagen,
    },
)