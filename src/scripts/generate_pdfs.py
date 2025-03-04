import os

def generate_pdfs():
    # Loop through each .tex file in the data directory
    for file in os.listdir('../data'):
        if file.endswith('.tex'):
            # Use the pdflatex command to compile the .tex file into a .pdf
            os.system(f'pdflatex ../data/{file}')

if __name__ == "__main__":
    generate_pdfs()