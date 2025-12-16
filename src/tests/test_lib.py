from __future__ import annotations

from setup_cronjob.lib import _get_crontab


class TestGetCronTab:
    def test_main(self) -> None:
        result = _get_crontab()
        expected = """\
PATH=/usr/local/bin:/usr/bin:/bin

* * * * * nonroot (echo "[$(date '+\\%Y-\\%m-\\%d \\%H:\\%M:\\%S') | $$] Starting 'name'..."; flock --nonblock --verbose /tmp/cron-name.lock timeout --kill-after=10s --verbose 60s script.py; echo "[$(date '+\\%Y-\\%m-\\%d \\%H:\\%M:\\%S') | $$] Finished 'name' with exit code $?") 2>&1 | sudo tee -a /var/log/name.log
"""
        assert result == expected
