#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from sklearn.datasets import load_wine

# https://scikit-learn.org/stable/modules/generated/sklearn.datasets.load_wine.html#sklearn.datasets.load_wine
data = load_wine(as_frame=True)  # New in version 0.23.
data.frame.to_csv('dataset_wine.csv')
