from classifier_script import run_pipeline

input_path = "data/test_100_sample.csv"
seq_model_path = "models/seq_model.pkl"
cof_model_path = "models/cof_model.pkl"
seq_col = 'sequence'
output_path = "final.csv"


run_pipeline(
        input_path,
        seq_model_path,
        cof_model_path,
        output_path, 
        seq_col
    )
