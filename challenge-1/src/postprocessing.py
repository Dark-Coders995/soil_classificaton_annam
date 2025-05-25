import json
import numpy as np
from sklearn.metrics import (
    f1_score,
    fbeta_score,
    classification_report,
    confusion_matrix,
    ConfusionMatrixDisplay,
)
import matplotlib.pyplot as plt


def evaluate_model(model, validation_generator, output_json_path="metrics.json"):

    y_pred_probs = model.predict(validation_generator)
    y_pred = np.argmax(y_pred_probs, axis=1)
    y_true = validation_generator.classes
    class_labels = list(validation_generator.class_indices.keys())

    f1_macro = f1_score(y_true, y_pred, average="macro")
    f2_macro = fbeta_score(y_true, y_pred, beta=2, average="macro")
    f1_per_class = f1_score(y_true, y_pred, average=None)
    f2_per_class = fbeta_score(y_true, y_pred, beta=2, average=None)

    report = classification_report(
        y_true, y_pred, target_names=class_labels, output_dict=True
    )

    loss, accuracy = model.evaluate(validation_generator)

    metrics = {
        "accuracy": float(accuracy),
        "loss": float(loss),
        "f1_macro": float(f1_macro),
        "f2_macro": float(f2_macro),
        "f1_per_class": {
            label: float(score) for label, score in zip(class_labels, f1_per_class)
        },
        "f2_per_class": {
            label: float(score) for label, score in zip(class_labels, f2_per_class)
        },
        "classification_report": report,
    }

    with open(output_json_path, "w") as f:
        json.dump(metrics, f, indent=4)

    print(f"✅ Metrics saved to: {output_json_path}")

