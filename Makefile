TEX := main.tex
PDF := $(TEX:.tex=.pdf)

.PHONY: all clean distclean rebuild

all: $(PDF)

$(PDF): $(TEX)
	latexmk $(TEX)

clean:
	latexmk -c $(TEX)

distclean:
	latexmk -C $(TEX)

rebuild: distclean all
