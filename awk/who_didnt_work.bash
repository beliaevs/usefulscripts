#!/bin/bash

awk '$3 == 0 { print $1 }' emp.data
