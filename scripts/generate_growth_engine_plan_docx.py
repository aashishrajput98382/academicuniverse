import os
from docx import Document
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.oxml import parse_xml
from docx.oxml.ns import nsdecls

def set_cell_background(cell, fill_hex):
    tcPr = cell._element.get_or_add_tcPr()
    shd = parse_xml(f'<w:shd {nsdecls("w")} w:fill="{fill_hex}"/>')
    tcPr.append(shd)

def set_cell_margins(cell, top=140, bottom=140, left=180, right=180):
    tcPr = cell._element.get_or_add_tcPr()
    tcMar = parse_xml(
        f'<w:tcMar {nsdecls("w")}>'
        f'<w:top w:w="{top}" w:type="dxa"/>'
        f'<w:bottom w:w="{bottom}" w:type="dxa"/>'
        f'<w:left w:w="{left}" w:type="dxa"/>'
        f'<w:right w:w="{right}" w:type="dxa"/>'
        f'</w:tcMar>'
    )
    tcPr.append(tcMar)

def add_callout_box(doc, title, text, border_color="0052CC", bg_color="F0F4F9"):
    tbl = doc.add_table(rows=1, cols=1)
    tbl.alignment = WD_TABLE_ALIGNMENT.CENTER
    tbl.autofit = False
    
    cell = tbl.cell(0, 0)
    cell.width = Inches(6.5)
    set_cell_background(cell, bg_color)
    set_cell_margins(cell, top=160, bottom=160, left=200, right=200)
    
    tcPr = cell._element.get_or_add_tcPr()
    borders = parse_xml(
        f'<w:tcBorders {nsdecls("w")}>'
        f'<w:top w:val="none"/>'
        f'<w:left w:val="single" w:sz="36" w:space="0" w:color="{border_color}"/>'
        f'<w:bottom w:val="none"/>'
        f'<w:right w:val="none"/>'
        f'</w:tcBorders>'
    )
    tcPr.append(borders)
    
    p = cell.paragraphs[0]
    p.paragraph_format.space_before = Pt(2)
    p.paragraph_format.space_after = Pt(4)
    r_title = p.add_run(f"💡 {title}\n")
    r_title.bold = True
    r_title.font.name = "Calibri"
    r_title.font.size = Pt(11)
    r_title.font.color.rgb = RGBColor(0, 51, 153)
    
    r_text = p.add_run(text)
    r_text.font.name = "Calibri"
    r_text.font.size = Pt(10)
    r_text.font.color.rgb = RGBColor(40, 40, 40)
    
    p_after = doc.add_paragraph()
    p_after.paragraph_format.space_before = Pt(2)
    p_after.paragraph_format.space_after = Pt(4)

def style_table_header(row, col_widths, headers, bg_color="1A365D"):
    for idx, cell in enumerate(row.cells):
        cell.width = Inches(col_widths[idx])
        set_cell_background(cell, bg_color)
        set_cell_margins(cell, top=120, bottom=120, left=140, right=140)
        p = cell.paragraphs[0]
        p.alignment = WD_ALIGN_PARAGRAPH.LEFT
        p.paragraph_format.space_before = Pt(2)
        p.paragraph_format.space_after = Pt(2)
        r = p.add_run(headers[idx])
        r.bold = True
        r.font.name = "Calibri"
        r.font.size = Pt(10)
        r.font.color.rgb = RGBColor(255, 255, 255)

def format_table_rows(table, col_widths, row_data, alt_bg="F8FAFC"):
    for r_idx, data in enumerate(row_data):
        row = table.rows[r_idx + 1]
        bg = alt_bg if r_idx % 2 == 1 else "FFFFFF"
        for c_idx, cell in enumerate(row.cells):
            cell.width = Inches(col_widths[c_idx])
            set_cell_background(cell, bg)
            set_cell_margins(cell, top=100, bottom=100, left=120, right=120)
            p = cell.paragraphs[0]
            p.paragraph_format.space_before = Pt(2)
            p.paragraph_format.space_after = Pt(2)
            r = p.add_run(str(data[c_idx]))
            r.font.name = "Calibri"
            r.font.size = Pt(9.5)
            r.font.color.rgb = RGBColor(34, 34, 34)

def generate_doc():
    doc = Document()
    
    for section in doc.sections:
        section.top_margin = Inches(0.75)
        section.bottom_margin = Inches(0.75)
        section.left_margin = Inches(0.75)
        section.right_margin = Inches(0.75)
        
        header = section.header
        hp = header.paragraphs[0]
        hp.alignment = WD_ALIGN_PARAGRAPH.RIGHT
        hr = hp.add_run("ACADEMIC UNIVERSE | Part 2: Student Growth Intelligence Engine (SGIE)")
        hr.font.name = "Calibri"
        hr.font.size = Pt(8.5)
        hr.font.color.rgb = RGBColor(140, 140, 140)
        
        footer = section.footer
        fp = footer.paragraphs[0]
        fp.alignment = WD_ALIGN_PARAGRAPH.CENTER
        fr = fp.add_run("Confidential — Official Architectural Specification & Research Roadmap")
        fr.font.name = "Calibri"
        fr.font.size = Pt(8.5)
        fr.font.color.rgb = RGBColor(140, 140, 140)

    # Document Header
    p_title = doc.add_paragraph()
    p_title.paragraph_format.space_before = Pt(10)
    p_title.paragraph_format.space_after = Pt(4)
    r_badge = p_title.add_run("OFFICIAL PRODUCT SPECIFICATION & RESEARCH BLUEPRINT\n")
    r_badge.font.name = "Calibri"
    r_badge.font.size = Pt(9.5)
    r_badge.bold = True
    r_badge.font.color.rgb = RGBColor(0, 102, 204)
    
    r_title = p_title.add_run("Academic Universe: Part 2 — Student Growth Intelligence Engine (SGIE)")
    r_title.font.name = "Arial"
    r_title.font.size = Pt(19)
    r_title.bold = True
    r_title.font.color.rgb = RGBColor(26, 54, 93)

    p_sub = doc.add_paragraph()
    p_sub.paragraph_format.space_before = Pt(2)
    p_sub.paragraph_format.space_after = Pt(12)
    r_sub = p_sub.add_run("Student Growth Analysis, Pattern Mining, Pragmatic Industry Remediation & Conversational AI Integration")
    r_sub.font.name = "Calibri"
    r_sub.font.size = Pt(11)
    r_sub.font.italic = True
    r_sub.font.color.rgb = RGBColor(74, 85, 104)

    # Meta Table
    meta_table = doc.add_table(rows=2, cols=3)
    meta_table.alignment = WD_TABLE_ALIGNMENT.CENTER
    meta_widths = [2.2, 2.2, 2.1]
    headers_meta = ["SYSTEM", "VERSION / SCOPE", "RESEARCH PUBLICATION TARGET"]
    style_table_header(meta_table.rows[0], meta_widths, headers_meta, bg_color="2B6CB0")
    meta_rows = [
        ["Academic Universe (AU Core)", "Part 2 — SGIE Production Engine", "IEEE TLT / ACM EDM Ready"]
    ]
    format_table_rows(meta_table, meta_widths, meta_rows)
    doc.add_paragraph().paragraph_format.space_after = Pt(6)

    # The Real College Engineering Reality (Executive Context)
    h_reality = doc.add_heading("1. Executive Vision: The Real College Engineering Reality", level=1)
    h_reality.paragraph_format.space_before = Pt(12)
    h_reality.paragraph_format.space_after = Pt(6)

    p_real = doc.add_paragraph(
        "Engineering college ke dauraan har semester mein 6 se 8 subjects hote hain. Lekin aaj tak kisi bhi college ERP ya platform "
        "par student ko ye samjhane wala koi nahi hota ki:\n\n"
        '• "Bhai, tu Digital Electronics ya Environmental Science mein fail hone par ro raha hai, jabki Software/IT industry mein iska 0% role hai! Isme bas minimum passing marks le aao."\n'
        '• "Lekin Operating Systems aur DBMS mein agar tere marks gire hain, toh ye RED ALERT hai kyunki Google se lekar Infosys tak har interview yahan se shuru hota hai!"\n\n'
        "Students bina guidance ke har subject par barabar sar marte hain, anxiety mein aate hain, aur jo cheezein industry ke liye sabse zyada zaroori hain "
        "(Core CS, practical dev) unpar focus nahi kar paate. Academic Universe ka Part 2 — Student Growth Intelligence Engine (SGIE) isi problem ko root se solve karta hai."
    )
    p_real.style.font.name = "Calibri"
    p_real.style.font.size = Pt(10.5)

    add_callout_box(
        doc,
        "CORE MISSION STATEMENT",
        "Part 2 ka mission hai: Student ke saare academic data (Sem-wise marks, CA scores, Attendance) ko analyze karke unka real Growth Trajectory (UP vs DOWN) nikalna, "
        "unka subject pattern aur cognitive affinity discover karna, agar wo fail ya weak huye toh uska exact root cause nikalna aur pragmatically industry relevance "
        "ke hisab se guide karna ki kisme deep effort lagana hai aur kisme bas passing marks la kar aage badhna hai. Aur ye saara context Campus AI Chatbot ko de dena "
        "taaki student se real Senior Mentor ki tarah baat ho sake!",
        border_color="0052CC",
        bg_color="EEF4FB"
    )

    # The 4 Core Pillars
    h_pillars = doc.add_heading("2. The 4 Core Engine Pillars (Exact Implementation Scope)", level=1)
    h_pillars.paragraph_format.space_before = Pt(12)
    h_pillars.paragraph_format.space_after = Pt(6)

    # Pillar 1
    h_p1 = doc.add_heading("Pillar 1: Student Growth Analysis (Trajectory: UP vs DOWN)", level=2)
    h_p1.paragraph_format.space_before = Pt(8)
    h_p1.paragraph_format.space_after = Pt(4)

    p_p1 = doc.add_paragraph(
        "Student ki academic growth UP direction mein ho rahi hai ya DOWN ja rahi hai, ye analyze karna Semester-wise marks aur attendance ke through:\n\n"
        "• Longitudinal Trendline: Semester 1 se current semester tak ke SGPA/CGPA ka velocity vector track karna.\n"
        "• Delta SGPA Momentum:\n"
        "   - ΔSGPA > 0: Positive Momentum / Upward Growth (Student improve kar raha hai).\n"
        "   - ΔSGPA < 0: Downward Decline / Academic Stress Alert (Student ka performance gir raha hai).\n"
        "   - |ΔSGPA| <= 0.05: Stagnation / Plateau (Performance ruk chuki hai, nudge ki zaroorat hai).\n"
        "• Attendance vs Marks Correlation: Kya marks girne ki asli wajah attendance ka 75% threshold se niche drop hona thi? "
        "System Covariance calculate karke student ko batayega ki problem subject samajhne mein nahi, class bunk karne mein thi!"
    )
    p_p1.style.font.name = "Calibri"
    p_p1.style.font.size = Pt(10)

    # Pillar 2
    h_p2 = doc.add_heading("Pillar 2: Pattern Recognition (Subject Affinity & Weakness Mining)", level=2)
    h_p2.paragraph_format.space_before = Pt(8)
    h_p2.paragraph_format.space_after = Pt(4)

    p_p2 = doc.add_paragraph(
        "Student ke semester-wise marks ko analyze karke latent patterns find karna: Student kis type ke subjects mein weak hai, "
        "kisme uska genuine interest hai, aur kisme wo consistently accha score kar raha hai.\n\n"
        "University ke saare subjects ko 5 industry clusters mein baant kar pattern pakda jata hai:"
    )
    p_p2.style.font.name = "Calibri"
    p_p2.style.font.size = Pt(10)

    cluster_table = doc.add_table(rows=6, cols=3)
    cluster_table.alignment = WD_TABLE_ALIGNMENT.CENTER
    c_widths = [1.8, 2.5, 2.2]
    style_table_header(cluster_table.rows[0], c_widths, ["SUBJECT CLUSTER", "TYPICAL COURSES", "PATTERN DISCOVERY BEHAVIOR"], bg_color="1A365D")
    c_rows = [
        ["Applied Dev & Coding", "Java, Python, Web Dev, Programming Labs", "Practical coding aptitude & software engineering interest."],
        ["Core CS Theory", "DSA, Operating Systems, DBMS, Networks", "Foundational algorithmic & systems thinking capability."],
        ["Maths & Analytical", "Discrete Maths, Stats, Linear Algebra, TOC", "Theoretical/analytical depth vs cognitive friction."],
        ["Hardware & Electronics", "Digital Logic, Microprocessors (8085), COA", "Low-level hardware affinity vs software preference."],
        ["General & Auxiliary", "EVS, Professional Ethics, English, Management", "Compliance & non-technical institutional subjects."]
    ]
    format_table_rows(cluster_table, c_widths, c_rows)

    add_callout_box(
        doc,
        "REAL-WORLD PATTERN INSIGHT EXAMPLE",
        'Engine Pattern Dhoondhega: "Ye student Applied Dev/Labs mein 85%+ score karta hai aur GitHub par projects bana raha hai, '
        'lekin Theoretical Maths aate hi 45% par drop ho jata hai. Iska core strength Practical Software Building hai, aur iska friction point '
        'abstract theoretical math proofs hain."',
        border_color="2B6CB0",
        bg_color="F7FAFC"
    )

    # Pillar 3
    h_p3 = doc.add_heading("Pillar 3: Pragmatic Industry-Aligned Remediation (Fail Kyu Hua? Aur Kya Karna Chahiye?)", level=2)
    h_p3.paragraph_format.space_before = Pt(8)
    h_p3.paragraph_format.space_after = Pt(4)

    p_p3 = doc.add_paragraph(
        "Agar student kisi subject mein fail hua ya low marks aaye, toh unko generic gyaan dene ke bajaye do-level actionable analysis milega:\n\n"
        "1. Root-Cause Analysis (Fail kyu hua / marks kyu kate?):\n"
        "   • Attendance Deficit (< 75%): Kya student ko exam eligibility ya attendance marks ka penalty laga?\n"
        "   • Continuous Assessment (CA) Miss: Kya CA-1, CA-2 ya assignments submit nahi huye (CA marks < 12/25)?\n"
        "   • Terminal Exam Drop: Internal CA mein 22/25 the, par 3-ghante ke theoretical exam mein marks kate?\n\n"
        "2. Pragmatic Industry Relevance Filter (Game Changer Strategy):\n"
        "   Kya wo subject aaj ki modern software/IT industry ke hisaab se zaroori tha? Kya student ko usme deep sikhna chahiye, "
        "ya sirf passing marks la kar faltu time waste nahi karna chahiye?"
    )
    p_p3.style.font.name = "Calibri"
    p_p3.style.font.size = Pt(10)

    triage_tbl = doc.add_table(rows=3, cols=3)
    triage_tbl.alignment = WD_TABLE_ALIGNMENT.CENTER
    t_widths = [1.8, 2.3, 2.4]
    style_table_header(triage_tbl.rows[0], t_widths, ["INDUSTRY RELEVANCE", "COURSES", "ENGINE KI ACTIONABLE ADVICE"], bg_color="2C5282")
    t_rows = [
        [
            "High Industry Value\n(Red Alert Core)",
            "DBMS, Operating Systems, DSA, Networks",
            "CRITICAL REMEDIATION: 'Is subject ko ignore mat karna! Google/TCS interview mein 80% sawal yahin se aayenge. Ye lo curated topic checklist aur SQL/OS practical questions.'"
        ],
        [
            "Low/Zero Industry Value\n(Pass-Only Auxiliary)",
            "EVS, Microprocessor 8085, Professional Ethics",
            "PASSING CLEARANCE ADVICE: 'Is par poora mahina ro kar time waste mat karo! Software jobs mein 8085 ya EVS koi nahi puchega. 40 marks ka passing plan follow karo aur bacha hua time Full-Stack/GitHub par lagao.'"
        ]
    ]
    format_table_rows(triage_tbl, t_widths, t_rows)

    # Pillar 4
    h_p4 = doc.add_heading("Pillar 4: Context-Aware Conversational AI Chatbot", level=2)
    h_p4.paragraph_format.space_before = Pt(8)
    h_p4.paragraph_format.space_after = Pt(4)

    p_p4 = doc.add_paragraph(
        "Academic Universe mein AI Chatbot already built hai (aiController.ts). Ab hum uske context generator "
        "getStudentContext(userId) ko update karke student ki growth ka poora context Chatbot ko feed karenge:\n\n"
        "• Current Trajectory: 'Ashish ka Sem 4 mein SGPA +0.8 up hua hai (Upward Momentum).'\n"
        "• Weak Subjects & Root Cause: 'DBMS mein CA marks kam the assignment submit na hone ki wajah se.'\n"
        "• Industry Advice Matrix: 'Core CS par focused rehna hai, non-core subjects mein pass-only strategy lagani hai.'\n\n"
        "Jab student Chatbot se chat karega, Chatbot ek real Senior Tech Mentor ki tarah baat karega jisko pata hai ki student kahan weak hai, "
        "kahan strong hai, aur usko kis direction mein grow karna chahiye!"
    )
    p_p4.style.font.name = "Calibri"
    p_p4.style.font.size = Pt(10)

    # Benchmark & Research Paper Section
    h_paper = doc.add_heading("3. Isse Fast Research Paper Kaise Banega? (Empirical Results Pipeline)", level=1)
    h_paper.paragraph_format.space_before = Pt(12)
    h_paper.paragraph_format.space_after = Pt(6)

    p_paper = doc.add_paragraph(
        "Aapki sabse important requirement thi: 'Kam time mein implement ho sake, jiska hum result nikaal sakein, "
        "then research paper publish kar sakein!'\n\n"
        "Is system par ek high-impact IEEE / Springer-grade research paper banega:\n"
        "Paper Title: 'Explainable Multi-Semester Student Growth Trajectory and Industry-Aligned Curricular Remediation Engine (SGIE)'\n\n"
        "Hum AU-DIC benchmark ki tarah ek automated Python evaluation script banayenge (run_growth_engine_benchmark.py):"
    )
    p_paper.style.font.name = "Calibri"
    p_paper.style.font.size = Pt(10)

    paper_tbl = doc.add_table(rows=5, cols=3)
    paper_tbl.alignment = WD_TABLE_ALIGNMENT.CENTER
    p_widths = [1.8, 2.3, 2.4]
    style_table_header(paper_tbl.rows[0], p_widths, ["PAPER COMPONENT", "METHODOLOGY / BENCHMARK", "OUTPUT ARTIFACTS"], bg_color="1A365D")
    paper_rows = [
        ["Experiment Dataset", "N = 100 to 200 Multi-Semester Student Profiles across 4 years", "Synthesized ground-truth cohort with diverse trajectories."],
        ["Trajectory Classification", "Direction accuracy (UP, DOWN, STABLE) vs static CGPA baselines", "McNemar's test & Wilcoxon p < 0.001 proof."],
        ["Pattern Affinity F1", "Subject domain clustering precision & recall against actual student outcomes", "Bootstrap 95% Confidence Interval graphs."],
        ["Paper Artifact Generator", "Automatic rendering of publication figures & LaTeX tables", "LaTeX tables + 300 DPI Matplotlib figures + Paper draft DOCX."]
    ]
    format_table_rows(paper_tbl, p_widths, paper_rows)

    # Technical Implementation Steps
    h_tech = doc.add_heading("4. Phased Technical Implementation Plan", level=1)
    h_tech.paragraph_format.space_before = Pt(12)
    h_tech.paragraph_format.space_after = Pt(6)

    tech_tbl = doc.add_table(rows=5, cols=3)
    tech_tbl.alignment = WD_TABLE_ALIGNMENT.CENTER
    t_widths_arch = [1.3, 2.3, 2.9]
    style_table_header(tech_tbl.rows[0], t_widths_arch, ["PHASE", "COMPONENT FILE", "EXACT RESPONSIBILITY"], bg_color="1A365D")
    tech_rows = [
        [
            "Phase 1",
            "backend/src/services/\nstudentGrowthEngine.service.ts",
            "Longitudinal trajectory calculation (velocity/acceleration), 5-tier taxonomy classification, affinity scores, root-cause diagnostics, and industry relevance triage."
        ],
        [
            "Phase 2",
            "backend/src/routes/\ngrowthEngineRoutes.ts",
            "Express routes exposing /api/growth-engine/analysis, /patterns, /remediation for frontend & chatbot consumption."
        ],
        [
            "Phase 3",
            "backend/src/controllers/\naiController.ts",
            "Chatbot context hook ko augment karna: getStudentContext() ab trajectory direction, domain strengths, aur pragmatic advice inject karega."
        ],
        [
            "Phase 4",
            "research/growth_engine_benchmark/\nrun_growth_engine_benchmark.py",
            "Fast benchmark script jo N=100-200 cohort par run hoga, tables/figures export karega aur publication-ready paper draft tayyar karega."
        ]
    ]
    format_table_rows(tech_tbl, t_widths_arch, tech_rows)

    # Output file
    output_path = os.path.join("c:\\github\\academicuniverse", "Academic_Universe_Part2_Student_Growth_Engine_Plan.docx")
    doc.save(output_path)
    print(f"Updated Plan DOCX created successfully at: {output_path}")

if __name__ == "__main__":
    generate_doc()
