#!/usr/bin/python

""" 
    Starter code for exploring the Enron dataset (emails + finances);
    loads up the dataset (pickled dict of dicts).

    The dataset has the form:
    enron_data["LASTNAME FIRSTNAME MIDDLEINITIAL"] = { features_dict }

    {features_dict} is a dictionary of features associated with that person.
    You should explore features_dict as part of the mini-project,
    but here's an example to get you started:

    enron_data["SKILLING JEFFREY K"]["bonus"] = 5600000
    
"""

import pickle

enron_data = pickle.load(open("../final_project/final_project_dataset.pkl", "r"))

n_people = len(enron_data)
print "n_people:", n_people

n_feature = len(enron_data.values()[0])
print "n_feature:", n_feature

n_poi = 0
for person in enron_data:
    if enron_data[person]["poi"] == 1:
        n_poi += 1
print "n_poi:", n_poi
