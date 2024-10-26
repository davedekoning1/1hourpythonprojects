coverage run --source=html_helper -m pytest

@REM for only the tests (run occasionally to see whether all tests are being run)
@REM coverage run --source=tests -m pytest

coverage html