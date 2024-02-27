from nio import Client

TEST_USER = "test"


def test__should_handle_to_device_next_batch_is_none():
    assert Client(TEST_USER)._should_handle_to_device(None) == True


def test__should_handle_to_device_next_batch_not_str():
    assert Client(TEST_USER)._should_handle_to_device({}) == True


def test__should_handle_to_device_next_batch_is_empty():
    assert Client(TEST_USER)._should_handle_to_device("") == True


def test__should_handle_to_device_next_batch_too_short():
    assert Client(TEST_USER)._should_handle_to_device("s0_1_2_3_4_5_6_7_8") == True


def test__should_handle_to_device_next_batch_too_long():
    assert Client(TEST_USER)._should_handle_to_device("s0_1_2_3_4_5_6_7_8_9_10") == True


def test__should_handle_to_device_next_batch_to_device_not_int():
    assert Client(TEST_USER)._should_handle_to_device("s0_1_2_3_4_5_a_7_8_9") == True


def test__should_handle_to_device_next_batch_to_device_is_same():
    client = Client(TEST_USER)
    client.next_batch_to_device = 6
    assert client._should_handle_to_device("s0_1_2_3_4_5_6_7_8_9") == False
    assert client.next_batch_to_device == 6


def test__should_handle_to_device_next_batch_to_device_is_different():
    client = Client(TEST_USER)
    client.next_batch_to_device = 5
    assert client._should_handle_to_device("s0_1_2_3_4_5_6_7_8_9") == True
    assert client.next_batch_to_device == 6
