# Implementation for Measuring Evolution of Cookie Dialogues.
Authors: Violeta Sizonenko.
Institution: Radboud University Nijmegen.
Abstract:
This thesis investigates the evolution of cookie dialogues in response to data protection regulations, presenting a scalable methodology that combines web archiving with machine learning to track these changes over time. Through a case study on French websites, this research examines trends in cookie dialogue adoption linked to GDPR enforcement and CNIL fines, revealing notable shifts in compliance behaviors. Despite limitations like web scraping challenges and archival constraints, the study provides valuable insights into the regulatory impact on privacy practices. This methodology offers a foundation for longitudinal analysis across various privacy compliance contexts.

## Repository Structure:
The Tranco List used in this study can be found in '.tranco'.

The XLM-RoBERTa model training code can be found in 'XLM-RoBERTa_Model_Training' folder. All files except for 'global_vars' are taken from https://github.com/koenberkhout/dark-patterns-project. 

To generate a list of URLs to analyze use 'Create_list_of_URLs.ipynb'

The functions to communicate with the model for crawling are found in 'text_and_button_classifier.ipynb'.

To get the classification results, use 'Crawler.ipynb'.
