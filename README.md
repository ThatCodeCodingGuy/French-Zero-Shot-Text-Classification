# French-Zero-Shot-Text-Classification

This project applies "camembert-base-xnli" and "xlm-roberta-large-xnli" models to make a French zero-shot text classification web application.

## Model Descriptions:

### camembert-base-xnli:

This model was made by [Baptiste Doyen](https://huggingface.co/BaptisteDoyen) by fine-tuning the base model of CamemBERT on French part of the XNLI dataset. 

For the full description of the original CamemBERT base model:

* [arXiv](https://arxiv.org/abs/1911.03894)
* [GitHub](https://github.com/facebookresearch/fairseq/blob/main/examples/camembert/README.md)
* [Hugging Face](https://huggingface.co/docs/transformers/model_doc/camembert)
* [CamemBERT Website](https://camembert-model.fr/)

and on "camembert-base-xnli":

* [Hugging Face](https://huggingface.co/BaptisteDoyen/camembert-base-xnli)

### xlm-roberta-large-xnli:

This model was obtained by [Joe Davison](https://huggingface.co/joeddav) by taking xlm-roberta-large and fine-tuning it on a combination of NLI data in 15 languages.

For further details on the original XLM-R model:

* [arxiv](https://arxiv.org/abs/1911.02116)
* [Github](https://github.com/facebookresearch/fairseq/tree/main/examples/xlmr)

and on "xlm-roberta-large-xnli":

* [Hugging Face](https://huggingface.co/joeddav/xlm-roberta-large-xnli)

### XNLI Dataset:

XNLI is a cross-lingual "Natural Language Understanding" (NLI) corpus consisting of 14 languages besides English. It is heavily used as an evaluation for sentence understanding classification in multiple languages. For further details about the corpus:

* [arXiv](https://arxiv.org/abs/1809.05053)
* [GitHub](https://github.com/facebookresearch/XNLI)

## Web Application:
Streamlit was used as the basic framework to turn the python script into an app. Then, for the final deployment, Hugging Face's Spaces was used.

You can check and try it out [here](https://huggingface.co/spaces/azizbarank/French-Zero-Shot-Text-Classification).

## Screenshot of the web page:
![Screenshot of the web page](https://github.com/ThatCodeCodingGuy/French-Zero-Shot-Text-Classification/blob/main/web_app.jpg)

## Example Text:
### Original Text Input:

Avec la Ligue 1 qui reprend ses droits à partir de vendredi 5 août, et un premier match pour ce qui les concerne samedi soir, à Clermont-Ferrand, l’heure est désormais arrivée pour les Parisiens d’apporter les preuves que ce changement d’ère est bien une réalité.

### Label List: monde,économie,sciences,culture,santé,politique,sport,technologie



### Output:
![Output](https://github.com/ThatCodeCodingGuy/French-Zero-Shot-Text-Classification/blob/main/result.jpg)
