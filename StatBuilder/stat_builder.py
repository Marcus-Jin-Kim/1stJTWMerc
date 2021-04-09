import csv
import yaml


def main():
    with open(".config.yaml") as myconfig_file:
        config = yaml.load(myconfig_file)

    print("hello world")



if __name__ == "__main__":
    main()