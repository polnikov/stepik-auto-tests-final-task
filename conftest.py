import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def pytest_addoption(parser):
    parser.addoption(
        '--language',
        action='store',
        default='en',
        help="Choose language"
    )


@pytest.fixture(scope="function")
def browser(request):
    user_language = request.config.getoption("language")
    if user_language:
        print("\nstart browser for test...")
        options = Options()
        options.add_experimental_option(
            'prefs',
            {'intl.accept_languages': user_language}
        )
        browser = webdriver.Chrome(options=options)
    else:
        raise pytest.UsageError("--language should be es or ru and etc")
    yield browser
    print("\nquit browser...")
    browser.quit()
