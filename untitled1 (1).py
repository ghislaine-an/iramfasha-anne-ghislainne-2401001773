# -*- coding: utf-8 -*-
"""Untitled1.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1-XYWj0LumWiOiecng3iETec_-qdW63V-
"""



import pandas as pd

phishing_keywords = ["urgent", "password reset", "bank","verify","account suspended"]
emails = pd.read_csv("/2401001773.csv")
if 'content' in emails.columns:
  emails["is_phishing"] = emails["content"].apply(
      lambda x: any(keyword in str(x).lower for keyword in phishing_keywords)
  )
  emails.to_csv("/content/analysed_emails.csv", index=False)
  print("phishing detection complete.")
else:
  print("Error: 'content' column is missing from the dataset.")

