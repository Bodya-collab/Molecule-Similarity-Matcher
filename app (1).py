import streamlit as st
from rdkit import Chem
from rdkit.Chem import AllChem
from rdkit import DataStructs
from rdkit.Chem import Draw

# Page design
st.set_page_config(page_title="Molecule Matcher", page_icon="🔗", layout="centered")

st.title("🔗 Molecule Similarity Scanner")
st.markdown("Tanimoto coeficcien")

# Function
def calculate_similarity(smiles1, smiles2):
    # Generating smiles
    mol1 = Chem.MolFromSmiles(smiles1)
    mol2 = Chem.MolFromSmiles(smiles2)

    if mol1 is None or mol2 is None:
        return None, None  # break

    # Fingerprints
    fp1 = AllChem.GetMorganFingerprintAsBitVect(mol1, 2, nBits=2048)
    fp2 = AllChem.GetMorganFingerprintAsBitVect(mol2, 2, nBits=2048)

    # Counting similarity
    similarity = DataStructs.TanimotoSimilarity(fp1, fp2)

    return similarity, [mol1, mol2]

# Introducing 2 column system
col1, col2 = st.columns(2)

with col1:
    st.subheader('Molecule 1')
    smiles1 = st.text_area("Import smiles 1", value="CN1CCC23C4C1CC5=C2C(=C(C=C5)O)OC3C(C=C4)O") # ex

with col2:
    st.subheader("Molecule 2")
    smiles2 = st.text_area("Import smiles 2", value="CN1CCC23C4C1CC5=C2C(=C(C=C5)OC)OC3C(C=C4)O") # ex

# Start button
if st.button('Count similarity'):

    # recall function
    score, mols = calculate_similarity(smiles1, smiles2)

    if score is None:
        st.error("Error")
    else:
        # print res
        st.success(f"Coefficient: **{score:.2f}** (out 1.0)")

        # Progress bar
        st.progress(score)

        # Drawing
        st.write("---")
        st.write("Visual:")
        img = Draw.MolsToGridImage(mols, molsPerRow=2, subImgSize=(300, 300), legends=["Molecule 1", "Molecule 2"])
        st.image(img)
