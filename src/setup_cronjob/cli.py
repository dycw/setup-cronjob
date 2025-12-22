from __future__ import annotations

from click import command
from rich.pretty import pretty_repr
from typed_settings import EnvLoader, click_options
from utilities.click import CONTEXT_SETTINGS
from utilities.logging import basic_config

from setup_cronjob.lib import setup_cronjob
from setup_cronjob.logging import LOGGER
from setup_cronjob.settings import Settings


@command(**CONTEXT_SETTINGS)
@click_options(Settings, [EnvLoader("")], show_envvars_in_help=True)
def _main(settings: Settings, /) -> None:
    LOGGER.info("Settings = %s", pretty_repr(settings))
    if settings.dry_run:
        LOGGER.info("Dry-run; exiting...")
        return
    setup_cronjob(
        name=settings.name,
        prepend_path=settings.prepend_path,
        schedule=settings.schedule,
        user=settings.user,
        timeout=settings.timeout,
        kill_after=settings.kill_after,
        command=settings.command,
        args=settings.args,
        logs_keep=settings.logs_keep,
    )


if __name__ == "__main__":
    basic_config(obj=LOGGER)
    _main()
