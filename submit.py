def process_list(input_list):
    # Check if the length of the list is a multiple of 10
    if len(input_list) % 10 != 0:
        raise ValueError(
            "Error: The length of the list must be a multiple of 10.")

    # Remove items at positions which are a multiple of 2 or 3
    processed_list = []
    for i in input_list:
        if i % 2 == 0 or i % 3 == 0:
            continue
        processed_list.append(i)
    return processed_list


def run_tests():
    # Test valid input
    input_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10,
                  11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
    result = process_list(input_list)
    assert result == [1, 5, 7, 11, 13, 17,
                      19], f"Test failed for valid input: {result}"

    # Test empty input
    input_list = []
    result = process_list(input_list)
    assert result == [], f"Test failed for empty input: {result}"

    # Test invalid length
    input_list = [1, 2, 3]
    try:
        process_list(input_list)
        print("Test failed: Expected ValueError for invalid length.")
    except ValueError as e:
        assert str(
            e) == "Error: The length of the list must be a multiple of 10.", f"Unexpected error message: {e}"

    print("All tests passed.")


run_tests()
