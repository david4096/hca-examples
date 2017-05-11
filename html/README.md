To generate the csv for the scatter matrix, make a cluster.tsv using the
clustergrammer notebook and then run

`cat ../cluster.tsv | python transpose.py > demo.csv`
