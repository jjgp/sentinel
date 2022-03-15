pythonpath = $(abspath ..)
python     = PYTHONPATH=$(pythonpath) python -m
sentinel   = $(python) src.sentinel.cli.cli
tar        = BigEarthNet-S2-v1.0.tar.gz
url        = https://bigearth.net/downloads/$(tar)

$(tar):
	curl -LOC - $(url)
