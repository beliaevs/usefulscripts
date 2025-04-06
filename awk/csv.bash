#!/bin/bash

awk -F ',' '$3 > 0' emp.csv
