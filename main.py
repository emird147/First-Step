# main.py
from gui import collect_data
from pdf import generate_pdf

def main():
    collect_data(generate_pdf)

if __name__ == "__main__":
    main()
