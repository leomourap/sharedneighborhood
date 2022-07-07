# sharedneighborhood.py
 
Intended use: compare annotation data between two gff extraction outputs with the objective of detect shared neighborhood between DNA sequences in different genome / long reads samples.

The first step would be treat the gffextraction output from Blastn or NCRF results (https://github.com/leomourap/blastgffextractor ; https://github.com/leomourap/ncrfgffextractor) with the treat4sn.py script.

Then, two treated annotation data can be compared utilizing the sharedneighborhood.py script, that returns you a list with all the annotation information that are present in these two datasets.

In my context i did a Blastn or NCRF with a satDNA sequence in assambled genomes from different species, and developed these tools to automatize the process of comparing annotation data of genomic regions adjacent from these satDNAs, in different species.
The result was a list of all the genes that are present in the neighborhood of the satDNAs in all compared different species.
