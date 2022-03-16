pythonpath = $(abspath ..)
python     = PYTHONPATH=$(pythonpath) python -m
sentinel   = $(python) src.sentinel.cli.cli
tar        = BigEarthNet-S2-v1.0.tar.gz
url        = https://bigearth.net/downloads/$(tar)

.PHONY: help
help:
	@echo "make $(tar):\n    download the $(tar)\n"
	@echo "make clean:\n    remove data artifacts\n"

.PHONY: $(tar)
$(tar):
	curl -LOC - $(url)

.PHONY: clean
clean:
	rm $(tar)
