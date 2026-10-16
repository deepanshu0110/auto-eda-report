from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def test_app_renders_default_sample():
    from streamlit.testing.v1 import AppTest

    app = AppTest.from_file(str(ROOT / "app.py"), default_timeout=120).run()
    assert not app.exception
    assert not app.error
