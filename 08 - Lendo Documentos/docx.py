import docx


def ler(arquivo):
    try:
        doc = docx.Document(arquivo)
        texto = []
        for paragrafo in doc.paragraphs:
            texto.append(paragrafo.text)
        return '\n'.join(texto)
    except Exception as erro:
        return "Ocorreu um erro:", erro


ler("teste.docx")