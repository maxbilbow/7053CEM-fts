def update_average(current_value: float, number_of_values: int, new_value: int) -> float:
    current_sum = current_value * number_of_values
    new_sum = current_sum + new_value
    return new_sum / (number_of_values + 1)

def update_bool_average(current_value: float, number_of_values: int, bool_value: bool, score: int) -> float:
    new_value: int = score * bool_value
    current_sum = current_value * number_of_values
    new_sum = current_sum + new_value
    return new_sum / (number_of_values + 1)
