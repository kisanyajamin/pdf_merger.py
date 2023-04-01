from PyPDF2 import PdfFileMerger, PdfFileReader

def merge_pdfs(paths, output):
    merger = PdfFileMerger()

    for path in paths:
        pdf = PdfFileReader(open(path, 'rb'))
        merger.append(pdf)

    merger.write(output)
    merger.close()

if __name__ == '__main__':
    paths = ['file1.pdf', 'file2.pdf', 'file3.pdf']
    output = 'merged.pdf'
    merge_pdfs(paths, output)
