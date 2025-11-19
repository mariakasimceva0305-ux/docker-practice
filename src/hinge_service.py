from losses import squared_hinge_loss

true_class = [1, -1, 1, -1, 1]
pred_class = [2.5, -0.5, 1.8, -1.2, 0.8]

hinge = squared_hinge_loss(true_class, pred_class)
print(f"hinge loss: {hinge:.4f}")