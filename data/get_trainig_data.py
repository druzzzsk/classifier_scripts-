import pandas as pd
from utils import get_full_descriptors_for_classifier
import random
from sklearn.preprocessing import LabelEncoder
import numpy as np

# Загрузка исходного датасета с ДНКзимами
def load_and_prepare_data(filepath):

    data = pd.read_csv(filepath)
    data = data[['e', 'kobs', 'metal_ions']]
    data = data.drop_duplicates(subset='e')
    data = data.dropna()
    
    data.rename(columns={
        'e': 'sequence',
        'kobs': 'target',
        'metal_ions': 'cofactor'
    }, inplace=True)
    
    data['target'] = (data['target'] > 1e-07).astype(int)
    data = data[data['target'] == 1] # Оставляем только активные последовательности
    
    return data

# Генерация отрицательного класса
def generate_negative_sequences(data, # Данные с активными последовательностями 
                                seq_col, 
                                num_of_seq, # Количество последовательностей для генерации
                                random_state):
    random.seed(random_state)
    lengths = [len(i) for i in data[seq_col]]

    def generate_random_sequences(length):
        return ''.join(random.choices(['A', 'T', 'C', 'G'], k=length))
    
    sampled_lengths = random.choices(lengths, k=num_of_seq)
    
    # Распределение длинны последовательностей такое же как в исходных данных
    new_sequences = [generate_random_sequences(length) for length in sampled_lengths] 
    generated = pd.DataFrame({'sequence' : new_sequences, 'target':0})
    
    return generated

# Выбор уникальных кофакторов (и их комбинаций) и перевод их в числовые лейблы
def cofactor_encoding(data, cofactor_col):
    
    metals_to_drop = ["['Histidine']", "['UO22+']", "['metal ion dependency not reported']"]
    data = data[~data[cofactor_col].isin(metals_to_drop)]

    data[cofactor_col] = data[cofactor_col].replace({
    "['Na+', 'M2+-independent']": "['Na+']",
    "['M2+-independent']": "['No cofactor']",
    "['Mg2+-independent']": "['No cofactor']",
    "[]" : "['No cofactor']"})
    
    le = LabelEncoder()
    data[cofactor_col] = le.fit_transform(data[cofactor_col])

    mapping_df = pd.DataFrame({
    'label': range(len(le.classes_)),
    'category': le.classes_})
    mapping_df.to_csv('mapping.csv')

    return data

# Добавление кофакторов к негативному классу
def get_cofactors_for_negative(generated, data, cofactor_col):
    value_counts = data[cofactor_col].value_counts(normalize=True)
    categories = value_counts.index
    probabilities = value_counts.values
    n_samples = len(generated)
    generated['cofactor'] = np.random.choice(categories, size=n_samples, p=probabilities)
    return generated

# Объединение таблиц
def get_final_df(data, generated):
    final_df = pd.concat([data, generated], ignore_index=True)
    return final_df

# Получение дескрипторов для последовательностей
def prepare_seq_features(df: pd.DataFrame, seq_column: str):
    descriptors = get_full_descriptors_for_classifier(
        df, seq_column_name=seq_column
    )
    descriptors.insert(0, "sequence", df[seq_column])
    return descriptors

# Итоговый пайплайн
def prepare_final_dataset(filepath: str,
                          num_negatives: int,
                          output_path: str):
  
    data = load_and_prepare_data(filepath)
    generated = generate_negative_sequences(data, seq_col='sequence', num_of_seq=num_negatives, random_state=42)
    data = cofactor_encoding(data, 'cofactor')
    generated = get_cofactors_for_negative(generated, data, 'cofactor')
    final_df = get_final_df(data, generated)

    cofactors = final_df['cofactor'].copy()
    labels = final_df['target'].copy()

    final_df = prepare_seq_features(final_df, 'sequence')

    final_df['cofactor'] = cofactors
    final_df['target'] = labels

  
    final_df.to_csv(output_path, index=False)
    print(f"[✔] Data saved to {output_path}")

    return final_df

# Получение данных
df = prepare_final_dataset('data\db_dnazymes_v2.csv', 1000, 'training_data.csv')
