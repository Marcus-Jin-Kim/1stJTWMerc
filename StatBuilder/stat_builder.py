import csv
import yaml
import os


def main():

    statdict = dict()

    with open("config.yaml") as myconfig_file:
        config = yaml.safe_load(myconfig_file)

    for dirpath, dnames, fnames in os.walk(config["CSV_FOLDER"]):
        for fn in fnames:
            if fn.endswith(".csv"):
                # csv loader too much, do it later
                fp = open(os.path.join(dirpath, fn), "r")
                for line in fp.readlines():
                    items = line.replace("\n","").split(",")
                    # print(items)
                    pn = items[0]
                    if pn not in statdict:
                        statdict[pn] = dict()

                    for i in range(1, len(items)):
                        colname = config["COLNAMES"][i]
                        if colname not in statdict[pn]:
                            statdict[pn][colname] = 0

                        statdict[pn][colname] += int(items[i])

                fp.close()
            # elif f.endswith(".xc"):
            #     xc(os.path.join(dirpath, f))
            # import pprint
            # pprint.pprint(statdict)

    # write
    fw = open(config["OUTPUT_FOLDER"] + os.sep + "output.csv", "w")

    # write header

    fw.write( ",".join(config["COLNAMES"]))
    fw.write("\n")

    for pn in statdict:
        fw.write(pn)
        for i in range(1, len(config["COLNAMES"])):
            colname = config["COLNAMES"][i]
            fw.write(",")
            fw.write(str(statdict[pn][colname]))
        fw.write("\n")
    fw.close()



if __name__ == "__main__":
    main()