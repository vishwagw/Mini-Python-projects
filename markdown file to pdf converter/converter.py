# a simple converter script for .md to .pdf converting.
from markdown_pdf import MarkdownPdf, Section

def convert_markdown_to_pdf(markdown_file_path, pdf_file_path, toc_level=1, optimize=True):
    """
    Converts a markdown file to a PDF file.

    Args:
        markdown_file_path (str): Path to the markdown file.
        pdf_file_path (str): Path to save the generated PDF file.
        toc_level (int, optional): Maximum heading level to include in the table of contents. Defaults to 1.
        optimize (bool, optional): Whether to optimize the PDF size. Defaults to True.
    """
    pdf = MarkdownPdf(toc_level=toc_level, optimize=optimize)

    with open(markdown_file_path, 'r', encoding='utf-8') as f:
        markdown_content = f.read()
    
    pdf.add_section(Section(markdown_content))
    pdf.save(pdf_file_path)

if __name__ == "__main__":
    markdown_file = "sample.markdown"
    pdf_file = "sample.pdf"
    convert_markdown_to_pdf(markdown_file, pdf_file)
    print(f"Successfully converted '{markdown_file}' to '{pdf_file}'")