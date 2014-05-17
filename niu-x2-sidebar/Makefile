SHELL := /bin/bash
PYGMENTS_MIN_DIR = static/css/pygments.min
PYGMENTS_SOURCE = ${wildcard static/css/pygments/*.css}
PYGMENTS = ${subst /pygments/,/pygments.min/,${patsubst %.css,%.min.css,${PYGMENTS_SOURCE}}}

all: compress

compress: static/css/niu2.min.css static/js/niu2.min.js ${PYGMENTS}

static/js/niu2.min.js: static/js/niu2.js
	yui-compressor -o $@ $<

static/css/niu2.min.css: static/css/niu2.css
	yui-compressor -o $@ $<

${PYGMENTS}: static/css/pygments.min/%.min.css: static/css/pygments/%.css
	@[ -d ${PYGMENTS_MIN_DIR} ] || mkdir -p ${PYGMENTS_MIN_DIR}
	yui-compressor -o $@ $<

clean:
	rm -rf static/js/niu2.min.js static/css/niu2.min.css ${PYGMENTS_MIN_DIR}

.PHONY: all compress pygments.min clean

