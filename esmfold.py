
import streamlit as st
from stmol import showmol
import py3Dmol
import requests
import biotite.structure.io as bsio

# Homebutton
if st.sidebar.button('Home'):
    st.markdown('<meta http-equiv="refresh" content="0;URL=https://cloud.wijerathne.com">', unsafe_allow_html=True)

#st.set_page_config(layout = 'wide')
st.sidebar.title(':rainbow[ESMFold] - :orange[Protein Predictor]')
st.sidebar.subheader(':gray[Evolutionary-scale prediction of atomic-level protein structure with a language model]')

# stmol
def render_mol(pdb):
    pdbview = py3Dmol.view()
    pdbview.addModel(pdb,'pdb')
    pdbview.setStyle({'cartoon':{'color':'spectrum'}})
    pdbview.setBackgroundColor('white')#('0xeeeeee')
    pdbview.zoomTo()
    pdbview.zoom(2, 800)
    pdbview.spin(True)
    showmol(pdbview, height = 500,width=800)

# Protein sequence input
DEFAULT_SEQ = "MGSSHHHHHHSQDLMVTSTYIPMSQRRSWADVKPIMQDDGPNPVVPIMYSEEYKDAMDYFRAIAAKEEKSERALELTEIIVRMNPAHYTVWQYRFSLLTSLNKSLEDELRLMNEFAVQNLKSYQVWHHRLLLLDRISPQDPVSEIEYIHGSLLPDPKNYHTWAYLHWLYSHFSTLGRISEAQWGSELDWCNEMLRVDGRNNSAWGWRWYLRVSRPGAETSSRSLQDELIYILKSIHLIPHNVSAWNYLRGFLKHFSLPLVPILPAILPYTASKLNPDIETVEAFGFPMPSDPLPEDTPLPVPLALEYLADSFIEQNRVDDAAKVFEKLSSEYDQMRAGYWEFRRRECAE "
txt = st.sidebar.text_area(':orange[Input sequence]', DEFAULT_SEQ, height=275)


# ESMfold
def update(sequence=txt):
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded',
    }
    response = requests.post('https://api.esmatlas.com/foldSequence/v1/pdb/', headers=headers, data=sequence, verify=False)  # Added verify=False
    name = sequence[:3] + sequence[-3:]
    pdb_string = response.content.decode('utf-8')

    with open('predicted.pdb', 'w') as f:
        f.write(pdb_string)

    struct = bsio.load_structure('predicted.pdb', extra_fields=["b_factor"])
    b_value = round(struct.b_factor.mean(), 5)

    # Display protein structure
    st.subheader(':orange[Predicted Protein Structure]')
    st.write('Predictions are coloured from :red[red] (worst) to :blue[blue] (best) according to pLDDT values.')
    render_mol(pdb_string)
   

    # plDDT value is stored in the B-factor field
    st.subheader('Per-residue confidence score (pLDDT)', divider='rainbow')
    percentage_value = round(b_value * 100, 2)
    st.info(f'plDDT: {percentage_value}%')
    st.write('plDDT is a per-residue estimate of the confidence in prediction on a scale from 0-100. Values greater than 90 indicating high confidence, and values below 50 indicating low confidence.')
    

    st.download_button(
        label="Download PDB File",
        data=pdb_string,
        file_name='predicted-protein-PDB.pdb',
        mime='text/plain',
    )

predict = st.sidebar.button('Predict', on_click=update)

if not predict:
    st.warning('👈 Enter protein sequence data!')



st.sidebar.write('[*ESMFold*](https://esmatlas.com/about) is an end-to-end single sequence protein structure predictor based on the ESM-2 language model. The model and this app is based on Meta AI ESMfold. For more information, please follow the [metaAi](https://ai.meta.com/blog/protein-folding-esmfold-metagenomics/).')
