from losses import mean_absolute_error

true_values = [1, 2, 3, 4, 5]
pred_values = [1.1, 1.9, 3.2, 3.8, 5.1]

mae = mean_absolute_error(true_values, pred_values)
print(f"mae: {mae:.4f}")