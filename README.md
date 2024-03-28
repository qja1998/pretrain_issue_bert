# Get start

### Install necessary package for train
`pip install datsets transformers tokenizers`

and install pytorch [here](https://pytorch.org/)

### Install utility package
`pip install pandas tqdm gihub`


# How to use

1. Preprocessing

  `data/preprocessing.ipynb`

2. Training and masking testing

  `train_issue_bert.ipynb`


# Data Format

### Project data
|id|name|language|total|issues|forked|
|--|----|--------|-----|------|------|
|1334|rails|Ruby|37188|12833|24355|
|1018|node|NaN|11155|7211|3944|
|4095|elasticsearch|Java|10157|6587|3570|
|340|netty|Java|9313|4647|4666|
|6815|vagrant|Ruby|9018|6618|2400|

It was used to filter prject names

### Train data
body|id|title
----|--|----
Bumps [rfc3986](https://github.com/python-hype...|596220186|Bump rfc3986 from 1.3.2 to 1.4.0
Bumps [boto3](https://github.com/boto/boto3...|596136922|Bump boto3 from 1.12.36 to 1.12.38
Bumps [botocore](https://github.com/boto/botoc...|596133846|Bump botocore from 1.15.36 to 1.15.38
Translations update from [Weblate](https://hos...|596128315|Translations update from Weblate
this will help to ensure that new projects are...|596064726|add rel="nofollow" to trending/latest on index...

We extracted this data from our issue database with the name we chose from the project data.
