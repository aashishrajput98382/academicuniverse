import os
import shutil
import docx
import zipfile

IMG_PATH = 'docs/paper/extracted_figures/image3.png'
BUNDLE_PATH = 'LATEST_RELEASE_BUNDLE_V46/3_HIGH_RES_FIGURES/image3.png'
DOCX_PATH = 'PaperV50.docx'
BACKUP_PATH = 'scratch/PaperV50_pre_fig2_update_backup.docx'

def update_fig2():
    # 1. Update bundle if directory exists
    if os.path.exists(os.path.dirname(BUNDLE_PATH)):
        shutil.copy2(IMG_PATH, BUNDLE_PATH)
        print(f"Copied updated image to {BUNDLE_PATH}")

    # 2. Backup PaperV50.docx
    shutil.copy2(DOCX_PATH, BACKUP_PATH)
    print(f"Backed up {DOCX_PATH} to {BACKUP_PATH}")

    # 3. Read updated image bytes
    with open(IMG_PATH, 'rb') as f:
        img_bytes = f.read()

    # 4. Open PaperV50.docx and update image part
    doc = docx.Document(DOCX_PATH)
    # Target is rId7 which points to media/image3.png
    part = doc.part.related_parts['rId7']
    print(f"Target part: {part.partname}")
    assert 'image3.png' in part.partname, f"Unexpected target part: {part.partname}"

    part._blob = img_bytes
    doc.save(DOCX_PATH)
    print(f"Successfully saved updated {DOCX_PATH}!")

    # 5. Verify image in docx zip
    with zipfile.ZipFile(DOCX_PATH, 'r') as z:
        data = z.read('word/media/image3.png')
        print(f"Verified image3.png in docx: {len(data)} bytes (Expected: {len(img_bytes)} bytes)")
        assert len(data) == len(img_bytes), "Byte size mismatch!"

if __name__ == '__main__':
    update_fig2()
