import time

def check_writable():
    try:
        with open('PaperV50.docx', 'a+b') as f:
            print("PaperV50.docx is WRITABLE (not locked)!")
            return True
    except PermissionError:
        print("PaperV50.docx is LOCKED by another process (e.g. Word).")
        return False

check_writable()
