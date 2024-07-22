# Information Extraction from Electricity Invoices

This is the repository for the A Bag-of-Words Approach for Information Extraction from Electricity Invoices paper.

[A Bag-of-Words Approach for Information Extraction from Electricity Invoices](https://www.preprints.org/manuscript/202405.1564/v1), preprint.

*by Javier Sánchez and Giovanny A. Cuervo-Londoño* 

Resources including the test and train dataset, and ML code are released here.

## Repository structure

The downloaded files are organized as the following hierarchy:

```plain
├── root
│   ├── dictionaries
│   │   ├── label_codes.txt
│   │   ├── spanish_stop_words.txt
│   ├── test_files
|   |   ├── T1.txt
|   |   ├── T2.txt
|   |   ├── T3.txt
|   |   ├── T4.txt
|   |   ├── T5.txt
|   |   ├── T6.txt
|   |   ├── T7.txt
│   ├── train_files
|   |   ├── T1.txt
|   |   ├── T2.txt
|   |   ├── T3.txt
|   |   ├── T4.txt
|   |   ├── T5.txt
|   |   ├── T6.txt
|   ├── main.ipynb
|   ├── idsem2list.py
|   ├── LICENSE
|   ├── README.md
```

## Bag-of-Words Approach for Information Extraction from Electricity Invoices

### Overview
This repository contains the implementation of a method to extract information from electricity invoices using machine learning techniques. The approach is based on a bag-of-words model and evaluates various classifiers to accurately capture invoice details.

### Features
  * **Input:** PDF electricity invoices
  * **Output:** Key information such as customer data, bill breakdown, and consumption details
  * **Techniques:** Utilizes Naive Bayes, Logistic Regression, Random Forests, and Support Vector Machines
  * **Dataset:** IDSEM with 75,000 invoices
### Methodology
  1. **Preprocessing:** Convert PDF invoices to raw text.
  2. **Feature Extraction:** Use TF-IDF and custom features for each word.
  3. **Classification:** Apply machine learning models to categorize extracted information.
  4. **Evaluation:** Measure performance using precision, recall, and F1-scores.
### Results
  * **Support Vector Machines** achieved the highest precision of 91.86%.
  * **Random Forests** demonstrated adaptability with 91.58% precision on new documents.
  * High precision rates for most labels, with 41.4% above 99%.

### Installation
  1. Clone the repository:
  ```bash
  git clone https://github.com/jsanchezperez/electricity_invoice_extraction.git
  ```
  2. Install dependencies:
  ```bash
  pip install -r requirements.txt
  ```
### Usage
Run the main script to process invoices:
  ```bash
  ipython -c "%run main.ipynb"
  ```
### Data Availability
The IDSEM dataset ([Sánchez et al.](https://www.nature.com/articles/s41597-022-01885-3)) is publicly available in Figshare at [https://doi.org/10.6084/m9.figshare.c.6045245.v1](https://doi.org/10.6084/m9.figshare.c.6045245.v1).


### Contributions
Contributions are welcome. Please submit a pull request or open an issue for any suggestions.

### License
This project is licensed under the Creative Commons Attribution License. See the [LICENSE](https://github.com/jsanchezperez/electricity_invoice_extraction/blob/main/LICENSE) file for details.

### Contact
For any inquiries, please contact:

  Javier Sánchez: [jsanchez@ulpgc.es](URL)
 
  GA. C-Londoño: [giovanny.cuervo101@alu.ulpgc.es](URL)

### Acknowledgments
Special thanks to the Servicio Canario de Salud, Gobierno de Canarias, for funding this project.

## References
If you use the resource in your research, please cite our paper:
```tex
@article{202405.1564,
	doi = {10.20944/preprints202405.1564.v1},
	url = {https://doi.org/10.20944/preprints202405.1564.v1},
	year = 2024,
	month = {May},
	publisher = {Preprints},
	author = {Javier Sánchez and Giovanny A. Cuervo-Londoño},
	title = {A Bag-of-Words Approach for Information Extraction from Electricity Invoices},
	journal = {Preprints}
}
```

