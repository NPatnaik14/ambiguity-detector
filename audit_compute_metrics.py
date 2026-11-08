import pandas as pd, numpy as np, os, sys

def compute(csv_path):
    df = pd.read_csv(csv_path)
    # booleans may be strings
    gold = df['gold_is_ambig'].astype(str).str.lower() == 'true'
    pred = df['predicted_is_ambig'].astype(str).str.lower() == 'true'
    TP = int(((gold) & (pred)).sum())
    FP = int(((~gold) & (pred)).sum())
    FN = int(((gold) & (~pred)).sum())
    TN = int(((~gold) & (~pred)).sum())
    precision = TP / (TP + FP) if TP + FP else 0.0
    recall = TP / (TP + FN) if TP + FN else 0.0
    f1 = 2 * precision * recall / (precision + recall) if precision + recall else 0.0
    accuracy = (TP + TN) / len(df) if len(df) else 0.0
    # type accuracy for ambiguous items
    amb = df[gold]
    type_acc = None
    if not amb.empty:
        type_acc = (amb['predicted_type'] == amb['gold_label']).mean()
    print('TP', TP, 'FP', FP, 'FN', FN, 'TN', TN)
    print('Accuracy', round(accuracy,4), 'Precision', round(precision,4), 'Recall', round(recall,4), 'F1', round(f1,4))
    if type_acc is not None:
        print('TypeAccuracy', round(type_acc,4))

if __name__ == '__main__':
    path = sys.argv[1] if len(sys.argv)>1 else os.path.join(os.path.dirname(__file__), 'sample_output', 'test_evaluation_results.csv')
    compute(path)

