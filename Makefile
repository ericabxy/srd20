DEST = docs/*
MKDIR = mkdir -p
SRC = markdown/*

normal: $(SRC)
	python scripts/format.py $^

clean:
	$(RM) $(DEST)
