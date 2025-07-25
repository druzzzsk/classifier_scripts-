import pandas as pd
import joblib
from typing import Dict, List
from utils import get_full_descriptors_for_classifier, sel_features, cofactor_mapping


def load_model(path: str):
    return joblib.load(path)


def extract_sequence_features(df: pd.DataFrame, seq_col: str) -> pd.DataFrame:
    features = get_full_descriptors_for_classifier(df, seq_col)
    features = features[sel_features]
    features.insert(0, "sequence", df[seq_col])
    return features


def expand_with_cofactors(df: pd.DataFrame, num_classes: int) -> pd.DataFrame:
    df_expanded = df.loc[df.index.repeat(num_classes)].copy()
    df_expanded["cofactor"] = list(range(num_classes)) * len(df)
    return df_expanded.reset_index(drop=True)


def predict_with_models(
    df: pd.DataFrame,
    seq_model,
    cofactor_model,
    threshold: float
):
    seq_probs = seq_model.predict_proba(df.iloc[:, 1:-1])[:, 1]
    cof_probs = cofactor_model.predict_proba(df.iloc[:, 1:])[:, 1]

    df["seq_pred_label"] = (seq_probs > threshold).astype(int)
    df["seq_pred_proba"] = seq_probs
    df["cof_pred_label"] = (cof_probs > threshold).astype(int)
    df["cof_pred_proba"] = cof_probs
    return df


def map_cofactor_labels(df: pd.DataFrame, col: str, mapping: Dict[int, List[str]]):
    df = df.copy()
    df[col] = df[col].map(mapping)
    return df


def run_pipeline(
    input_path: str,
    seq_model_path: str,
    cof_model_path: str,
    output_path: str,
    seq_col: str = "sequence",
    threshold: float = 0.8,
    cofactor_classes: int = 23,
    save_intermediate_path: str = "prepared_data.csv"
):
    # Чтение данных
    df_raw = pd.read_csv(input_path)

    # Извлечение признаков, расширение по кофакторам
    features = extract_sequence_features(df_raw, seq_col)
    expanded_data = expand_with_cofactors(features, cofactor_classes)
    
    expanded_data.to_csv(save_intermediate_path, index=False)
    print(f"Данные подготовлены и сохранены: {save_intermediate_path}")

    # Загрузка моделей
    seq_model = load_model(seq_model_path)
    cof_model = load_model(cof_model_path)

    # Предсказания
    preds = predict_with_models(expanded_data, seq_model, cof_model, threshold)

    # Формирование финального набора
    final_df = preds[
        ["sequence", "seq_pred_label", "seq_pred_proba", "cof_pred_label", "cof_pred_proba", "cofactor"]
    ]
    final_df = map_cofactor_labels(final_df, "cofactor", cofactor_mapping)

    # Сохранение
    final_df.to_csv(output_path, index=False)
    print(f"Результаты сохранены в: {output_path}")
