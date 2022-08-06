import os
os.system("pip install torch")
os.system("pip install transformers")
os.system("pip install sentencepiece")
os.system("pip install plotly")


from transformers import AutoTokenizer, AutoModelForSequenceClassification, pipeline
import sentencepiece
import torch
import plotly.graph_objects as go
import streamlit as st

text_1 = """Avec la Ligue 1 qui reprend ses droits à partir de vendredi 5 août, et un premier match pour ce qui les concerne samedi soir, à Clermont-Ferrand, l’heure est désormais arrivée pour les Parisiens d’apporter les preuves que ce changement d’ère est bien une réalité."""

text_2 = """Créées en 1991 sur un modèle inspiré de la Fête de la musique, les Nuits des étoiles ont pour thème en 2022 l’exploration spatiale, en partenariat avec l’Agence spatiale européenne."""

@st.cache(allow_output_mutation=True)
def list2text(label_list):
    labels = ""
    for label in label_list:
        labels = labels + label + ","
    labels = labels[:-1]
    return labels

label_list_1 = ["monde", "économie", "sciences", "culture", "santé", "politique", "sport", "technologie"]
label_list_2 = ["positif", "négatif", "neutre"]

st.title("French Zero-Shot Text Classification \
    with CamemBERT and XLM-R")

# Body
st.markdown(
    """
    
    This application makes use of [CamemBERT](https://camembert-model.fr/) and [XLM-R](https://arxiv.org/abs/1911.02116) models that were fine-tuned on the XNLI corpus. While CamemBERT was fine-tuned only on the French part of the corpus by [Baptiste Doyen](https://huggingface.co/BaptisteDoyen), XLM-R was done so on all parts of it by [Joe Davison](https://huggingface.co/joeddav), including French. Therefore, in this app, both of these two models are intended to be used and made comparison of each other for zero-shot classification in French. 

    """
)

model_list = ['BaptisteDoyen/camembert-base-xnli',
             'joeddav/xlm-roberta-large-xnli']

st.sidebar.header("Select Model")
model_checkpoint = st.sidebar.radio("", model_list)

st.sidebar.write("For the full descriptions of the models:")
st.sidebar.write("[camembert-base-xnli](https://huggingface.co/BaptisteDoyen/camembert-base-xnli)")
st.sidebar.write("[xlm-roberta-large-xnli](https://huggingface.co/joeddav/xlm-roberta-large-xnli)")

st.sidebar.write("For the XNLI Dataset:")
st.sidebar.write("[XNLI](https://huggingface.co/datasets/xnli)")

st.subheader("Select Text and Label List")
st.text_area("Text #1", text_1, height=128)
st.text_area("Text #2", text_2, height=128)
st.write(f"Label List #1: {list2text(label_list_1)}")
st.write(f"Label List #2: {list2text(label_list_2)}")

text = st.radio("Select Text", ("Text #1", "Text #2", "New Text"))
labels = st.radio("Select Label List", ("Label List #1", "Label List #2", "New Label List"))

if text == "Text #1": selected_text = text_1
elif text == "Text #2": selected_text = text_2
elif text == "New Text":
    selected_text = st.text_area("New Text", value="", height=128)

if labels == "Label List #1": selected_labels = label_list_1
elif labels == "Label List #2": selected_labels = label_list_2
elif labels == "New Label List":
    selected_labels = st.text_area("New Label List (Pls Input as comma-separated)", value="", height=16).split(",")

@st.cache(allow_output_mutation=True)
def setModel(model_checkpoint):
    model = AutoModelForSequenceClassification.from_pretrained(model_checkpoint)
    tokenizer = AutoTokenizer.from_pretrained(model_checkpoint)
    return pipeline("zero-shot-classification", model=model, tokenizer=tokenizer)
        
Run_Button = st.button("Run", key=None)
if Run_Button == True:
    
    zstc_pipeline = setModel(model_checkpoint)
    output = zstc_pipeline(sequences=selected_text, candidate_labels=selected_labels)
    output_labels = output["labels"]
    output_scores = output["scores"]

    st.header("Result")
    import plotly.graph_objects as go
    fig = go.Figure([go.Bar(x=output_labels, y=output_scores)])
    st.plotly_chart(fig, use_container_width=False, sharing="streamlit")
