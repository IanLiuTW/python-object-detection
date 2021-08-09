from app import __version__


def test_version():
    assert __version__ == '0.1.0'


def test_main():
    import main
    assert main.main() == None
