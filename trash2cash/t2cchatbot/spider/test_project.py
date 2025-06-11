from project import calculate_reward, get_rate_range, get_locations

def test_get_rate_range():
    assert get_rate_range("Plastic (PET bottles)") == (80, 100)
    assert get_rate_range("Nylon (Pure water sachets)") == (70, 200)
    assert get_rate_range("Unknown") == (0, 0)

def test_calculate_reward():
    assert calculate_reward("Plastic (PET bottles)", 2) == 180.0
    assert calculate_reward("Nylon (Pure water sachets)", 1.5) == 202.5
    assert calculate_reward("Unknown", 5) == 0

def test_get_locations():
    assert "Ikeja" in get_locations("Lagos")
    assert "Wuse" in get_locations("Abuja")
    assert get_locations("Unknown") == []
