from src.Stats import StatisticsSystem


def setup_system():
    system = StatisticsSystem("data.csv")
    return system


def test_file_validation():
    system = setup_system()
    assert system.validate_file_name() is True


def test_mean():
    system = setup_system()
    system.weights = [10, 20, 30]
    assert system.get_mean() == 20.0


def test_median_odd():
    system = setup_system()
    system.weights = [10, 20, 30]
    assert system.get_median() == 20.0


def test_median_even():
    system = setup_system()
    system.weights = [10, 20, 30, 40]
    assert system.get_median() == 25.0


def test_mode():
    system = setup_system()
    system.weights = [80, 80, 90, 100]
    assert system.get_mode() > 0