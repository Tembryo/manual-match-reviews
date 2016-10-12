FILE := review
OUTDIR  := build
RESULT  := review

pdf:
	# Also see .latexmkrc
	latexmk -xelatex -outdir=$(OUTDIR) -pdf $(FILE)
	cp $(OUTDIR)/$(FILE).pdf $(RESULT).pdf 

clean:
	rm -rf $(filter-out $(OUTDIR)/$(FILE).pdf, $(wildcard $(OUTDIR)/*))

purge:
	rm -rf $(OUTDIR)

.PHONY: latexmk clean purge
