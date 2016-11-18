import csv
import json
import os
import subprocess

out_dir = "generated"

if not os.path.exists(out_dir):
    os.makedirs(out_dir)

in_log_filename = "log.csv"
out_log_filename ="generated/remarks.tex"

log_fields = ["time", "category", "description"]

with open(out_log_filename, "w") as outfile:
    with open(in_log_filename, "r") as infile:
        reader = csv.DictReader(infile, fieldnames=log_fields, restkey="details")
        for row in reader:
            time=row["time"].strip()
            timestamp = time[:-2] + ":" + time[-2:]
            category = "\\"+row["category"].lower()
            description = row["description"]

            good_details = []
            for detail in row["details"]:
                if len(detail) > 0:
                    good_details.append(detail)
            if len(good_details) == 0:
                pass
            elif len(good_details) == 1:
                description += " ("+good_details[0]+")"
            else:
                description += "\\begin{itemize}"
                for detail in good_details:
                    description+= "\\item "+ detail
                description += "\\end{itemize}"


            formatted = "\\logremark{" +timestamp+ "}{"+category+"}{"+description+"}\n"
            outfile.write(formatted)

in_tips_filename = "tips.json"
out_tips_filename ="generated/tips.tex"
with open(out_tips_filename, "w") as outfile:
    with open(in_tips_filename, "r") as infile:
        tip_data = json.load(infile)

        highlight_tip = "\\tipssection{\n"+ tip_data["highlight"]+"\n}\n{\n"
        outfile.write(highlight_tip)

        for i in range(len(tip_data["tips"])):
            tip ="\\item "+tip_data["tips"][i]+"\n" 
            outfile.write(tip)

        outfile.write("}\n\n")


in_data_filename = "data.json"
out_data_filename ="generated/data.tex"
with open(out_data_filename, "w") as outfile:
    with open(in_data_filename, "r") as infile:
        data = json.load(infile)

        outfile.write("\\newcommand{\matchid}{"+str(data["id"])+"}\n")
        outfile.write("\\newcommand{\hero}{"+data["hero"]+"}\n")
        outfile.write("\\newcommand{\matchdate}{"+data["date"]+"}\n")
        outfile.write("\\newcommand{\player}{"+data["player"]+"}\n")



make_args = ("make", "-f", "../Makefile")
popen = subprocess.Popen(make_args, stdout=subprocess.PIPE)
popen.wait()
output = popen.stdout.read()
print output