#Copyright David Locke, 2012

.PHONY: all clean

all: ../Data/train_rel_2.tsv ../Data/public_leaderboard_rel_2.tsv
	python mk_feat.py
	R --no-save -f train.R

clean:
	rm -f *.csv
