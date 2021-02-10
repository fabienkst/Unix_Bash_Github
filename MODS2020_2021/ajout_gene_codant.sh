#!/bin/bash

cd ~/MODS2020_2021
RESULT="genomic.gff?dl=0"
cut -f3 $RESULT | grep 'CDS' > cds.txt
cut -f3 $RESULT | grep 'gene' > genes.txt


touch genes_codant.txt

