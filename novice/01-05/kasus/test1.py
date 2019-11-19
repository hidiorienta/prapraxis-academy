import xml.dom.minidom as minidom

def main():
    # gunakan fungsi parse() untuk me-load xml ke memori 
    # dan melakukan parsing
    doc = minidom.parse("test.xml")

    # Cetak isi doc dan tag pertamanya
    print doc.nodefirstName
    print doc.lastName.tagName


if __name__ == "__main__":
    main()
