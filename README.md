# Molecule-Similarity-Matcher
A web-based bioinformatics tool for comparing the structural similarity of chemical compounds. This application calculates the Tanimoto Coefficient based on Morgan Fingerprints to quantify how "alike" two molecules are.






A lightweight tool for calculating structural similarity between chemical compounds using RDKit and Streamlit. This application enables the comparison of two molecules via Tanimoto Coefficient analysis based on Morgan Fingerprints (ECFP4-like).

<img width="770" height="815" alt="image" src="https://github.com/user-attachments/assets/73e4ab1e-9b09-47c8-a322-ead7a42eed2f" />

## ⚙️ Installation & Setup

### Prerequisites
* Python 3.8+
* RDKit
* Streamlit

### Option 1: Quick Install (pip)
```bash
# Clone the repository
git clone [https://github.com/YOUR-USERNAME/Molecule-Matcher.git](https://github.com/YOUR-USERNAME/Molecule-Matcher.git)
cd Molecule-Matcher

# Install required packages
pip install streamlit rdkit
conda create -c conda-forge -n my-rdkit-env rdkit streamlit
conda activate my-rdkit-env
streamlit run app.py
