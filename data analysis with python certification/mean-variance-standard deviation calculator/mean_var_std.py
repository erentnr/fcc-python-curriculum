import numpy as np

def calculate(list):
    if len(list) != 9:
        raise ValueError("List must contain nine numbers.")
    else:
        calculations = {}
        new_array = np.array(list).reshape(3, 3)

        arr_mean = np.mean(new_array)
        arr_mean_a1 = np.mean(new_array, axis=0)
        arr_mean_a2 = np.mean(new_array, axis=1)
        arr_mean_all = [arr_mean_a1.tolist(), arr_mean_a2.tolist(), arr_mean]

        arr_var = np.var(new_array)
        arr_var_a1 = np.var(new_array, axis=0)
        arr_var_a2 = np.var(new_array, axis=1)
        arr_var_all = [arr_var_a1.tolist(), arr_var_a2.tolist(), arr_var]

        arr_std = np.std(new_array)
        arr_std_a1 = np.std(new_array, axis=0)
        arr_std_a2 = np.std(new_array, axis=1)
        arr_std_all = [arr_std_a1.tolist(), arr_std_a2.tolist(), arr_std]

        arr_max = np.max(new_array)
        arr_max_a1 = np.max(new_array, axis=0)
        arr_max_a2 = np.max(new_array, axis=1)
        arr_max_all = [arr_max_a1.tolist(), arr_max_a2.tolist(), arr_max]

        arr_min = np.min(new_array)
        arr_min_a1 = np.min(new_array, axis=0)
        arr_min_a2 = np.min(new_array, axis=1)
        arr_min_all = [arr_min_a1.tolist(), arr_min_a2.tolist(), arr_min]

        arr_sum = np.sum(new_array)
        arr_sum_a1 = np.sum(new_array, axis=0)
        arr_sum_a2 = np.sum(new_array, axis=1)
        arr_sum_all = [arr_sum_a1.tolist(), arr_sum_a2.tolist(), arr_sum]

        calculations.update({"mean": arr_mean_all,
                            "variance": arr_var_all,
                            "standard deviation": arr_std_all,
                            "max": arr_max_all,
                            "min": arr_min_all,
                            "sum": arr_sum_all})

        return calculations
