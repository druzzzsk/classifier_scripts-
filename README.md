#### Classifier models
The purpose of this project component is to assess whether the generated DNA sequences can be categorized as active DNAzymes. 
The structure of this section is outlined below: 
- classifier_models/ — contains code for training and evaluating two classification models: one based only on the DNA sequence, and another that takes into account both the sequence and a specific cofactor.
- data/ — contains the original DNAzyme dataset, the processed data used for model training, and cofactors mapping.
- utils/ — provides utility functions for extracting descriptors (features) from DNA sequences.
- classifier_script.py — script for running classification on generated DNA sequences using trained models.
- get_training_data.py — script to prepare or generate the data needed for model training.
- requirements.txt — list of required Python libraries to run the project.
