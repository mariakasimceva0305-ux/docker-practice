
from losses import mean_squared_error, mean_absolute_error

print("Тест")

true_values = [1, 2, 3, 4, 5]
pred_values = [1.1, 1.9, 3.2, 3.8, 5.1]

print(f" true_values {true_values}")
print(f" pred_values {pred_values}")

mse = mean_squared_error(true_values, pred_values)
mae = mean_absolute_error(true_values, pred_values)

print(f"\n results ")
print(f"MSE {mse:.4f}")
print(f"MAE {mae:.4f}")

