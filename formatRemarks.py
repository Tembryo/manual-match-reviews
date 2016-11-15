import csv

in_filename = "log.csv"
out_filename ="remarks.tex"

log_fields = ["time", "category", "description"]

with open(out_filename, "w") as outfile:
    with open("log.csv", "r") as infile:
        reader = csv.DictReader(infile, fieldnames=log_fields)
        for row in reader:
            time=row["time"].strip()
            timestamp = time[:-2] + ":" + time[-2:]
            category = "\\"+row["category"].lower()
            
            formatted = "\\logremark{" +timestamp+ "}{"+category+"}{"+row["description"]+"}\n"
            outfile.write(formatted)
