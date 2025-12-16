from __future__ import annotations

from make_crontab import __version__


class TestMain:
    def test_main(self) -> None:
        assert isinstance(__version__, str)
