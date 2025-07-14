### Files description 
The purpose of this project component is to assess whether the generated DNA sequences can be categorized as active DNAzymes. 
The structure of this section is outlined below: 

- **data/** — contains the original DNAzyme dataset, the processed data used for model training, and cofactors mapping.
- **models/** — contains code for training and evaluating two classification models: one based only on the DNA sequence, and another that takes into account both the sequence and a specific cofactor.
- **utils/** — provides utility functions for extracting features from DNA sequences.
- **classifier_script.py** — this file integrates functions for preprocessing input data for machine learning models, performing predictions using trained classifiers, and aggregating the results into an informative and structured output table
- **requirements.txt** — list of required Python libraries to run the project.
- **run_model.py** - this file serves as the entry point for executing the full analysis pipeline, which includes:
  - descriptor extraction from DNA sequences,
  - prediction generation using pre-trained machine learning models,
  - output of a results table containing classification outcomes and associated metadata.

The main function requires specification of the following **parameters**:
1. The path to the input dataset to be analyzed,
2. The paths to the trained sequence-based and cofactor-based models,
3. The name of the column containing the DNA sequences, and
4. The filename for saving the output with prediction results.
