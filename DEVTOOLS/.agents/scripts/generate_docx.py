#!/usr/bin/env python3
"""
Generator Dokumen DOCX Resmi - Standar Diskominfo Kota Yogyakarta
Mendukung pembuatan 5 tipe dokumen formal:
1. Dokumen KAK (Kerangka Acuan Kerja) -> docs/Dokumen_KAK_Resmi.docx
2. Laporan Pengujian QA (Fungsional & Negative Testing) -> docs/Laporan_Pengujian_QA.docx
3. Dokumen Laporan Pentest Resmi -> docs/Dokumen_Laporan_Pentest_Resmi.docx
4. Dokumen Spesifikasi API Developer Luar -> docs/Dokumen_Spesifikasi_API.docx
5. Panduan Pengguna (User Manual) -> docs/Panduan_Pengguna_[NamaAplikasi].docx

Atau mengonversi file Markdown terstruktur ke format DOCX resmi dengan styling elegan:
- Cover Page resmi
- Header & Footer (Page X of Y)
- Heading berhierarki warna tema Pemkot (#1E3A8A / #0F172A)
- Tabel ber-header navy dengan alternate row zebra striping
- Callout info/warning box dengan garis samping
"""

import os
import sys
import re
import argparse
from datetime import datetime
from docx import Document
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT, WD_ALIGN_VERTICAL
from docx.oxml import parse_xml
from docx.oxml.ns import nsdecls

# --- PALET WARNA RESMI PEMKOT YOGYAKARTA ---
COLOR_PRIMARY_HEX = "1E3A8A"      # Navy Blue
COLOR_SECONDARY_HEX = "0D9488"    # Teal Accent
COLOR_DARK_HEX = "0F172A"         # Slate Dark
COLOR_LIGHT_BG_HEX = "F8FAFC"     # Slate Light Background
COLOR_BORDER_HEX = "CBD5E1"       # Light Border
COLOR_MUTED_HEX = "64748B"        # Slate Muted Text
COLOR_WARNING_HEX = "D97706"      # Amber Warning
COLOR_DANGER_HEX = "DC2626"       # Red Danger
COLOR_SUCCESS_HEX = "16A34A"      # Green Success

COLOR_PRIMARY = RGBColor(30, 58, 138)
COLOR_DARK = RGBColor(15, 23, 42)
COLOR_MUTED = RGBColor(100, 116, 139)

def set_cell_background(cell, fill_hex):
    """Set background color of a table cell."""
    tcPr = cell._tc.get_or_add_tcPr()
    shd = parse_xml(f'<w:shd {nsdecls("w")} w:fill="{fill_hex}"/>')
    tcPr.append(shd)

def set_cell_margins(cell, top=120, bottom=120, left=150, right=150):
    """Set inner padding of a table cell (in twentieths of a point / dxa)."""
    tcPr = cell._tc.get_or_add_tcPr()
    tcMar = parse_xml(
        f'<w:tcMar {nsdecls("w")}>'
        f'<w:top w:w="{top}" w:type="dxa"/>'
        f'<w:bottom w:w="{bottom}" w:type="dxa"/>'
        f'<w:left w:w="{left}" w:type="dxa"/>'
        f'<w:right w:w="{right}" w:type="dxa"/>'
        f'</w:tcMar>'
    )
    tcPr.append(tcMar)

def set_table_borders(table, border_color="CBD5E1"):
    """Set clean subtle borders for a table."""
    tblPr = table._tbl.tblPr
    tblBorders = parse_xml(
        f'<w:tblBorders {nsdecls("w")}>'
        f'<w:top w:val="single" w:sz="4" w:space="0" w:color="{border_color}"/>'
        f'<w:bottom w:val="single" w:sz="6" w:space="0" w:color="{border_color}"/>'
        f'<w:insideH w:val="single" w:sz="4" w:space="0" w:color="{border_color}"/>'
        f'<w:left w:val="none"/>'
        f'<w:right w:val="none"/>'
        f'<w:insideV w:val="none"/>'
        f'</w:tblBorders>'
    )
    tblPr.append(tblBorders)

def add_callout(doc, text, callout_type="info"):
    """Add a stylized callout box (Info, Warning, Danger, Success)."""
    color_map = {
        "info": (COLOR_PRIMARY_HEX, "1E3A8A"),
        "warning": (COLOR_WARNING_HEX, "D97706"),
        "danger": (COLOR_DANGER_HEX, "DC2626"),
        "success": (COLOR_SUCCESS_HEX, "16A34A")
    }
    border_hex, text_hex = color_map.get(callout_type, (COLOR_PRIMARY_HEX, "1E3A8A"))
    
    table = doc.add_table(rows=1, cols=1)
    table.alignment = WD_TABLE_ALIGNMENT.CENTER
    table.autofit = False
    table.columns[0].width = Inches(6.5)
    
    cell = table.cell(0, 0)
    set_cell_background(cell, COLOR_LIGHT_BG_HEX)
    set_cell_margins(cell, top=140, bottom=140, left=200, right=180)
    
    # Left thick border only
    tcPr = cell._tc.get_or_add_tcPr()
    borders = parse_xml(
        f'<w:tcBorders {nsdecls("w")}>'
        f'<w:left w:val="single" w:sz="24" w:space="0" w:color="{border_hex}"/>'
        f'<w:top w:val="none"/>'
        f'<w:right w:val="none"/>'
        f'<w:bottom w:val="none"/>'
        f'</w:tcBorders>'
    )
    tcPr.append(borders)
    
    p = cell.paragraphs[0]
    p.paragraph_format.space_before = Pt(2)
    p.paragraph_format.space_after = Pt(2)
    p.paragraph_format.line_spacing = 1.15
    run = p.add_run(text)
    run.font.name = 'Arial'
    run.font.size = Pt(9.5)
    run.font.color.rgb = RGBColor(15, 23, 42)
    
    # add empty spacing after table
    sp = doc.add_paragraph()
    sp.paragraph_format.space_before = Pt(0)
    sp.paragraph_format.space_after = Pt(4)

def setup_document_styles(doc):
    """Setup base typography and styles."""
    for section in doc.sections:
        section.top_margin = Inches(1.0)
        section.bottom_margin = Inches(1.0)
        section.left_margin = Inches(1.0)
        section.right_margin = Inches(1.0)
        section.different_first_page_header_footer = True
        
        # Header / Footer
        header = section.header
        hp = header.paragraphs[0]
        hp.alignment = WD_ALIGN_PARAGRAPH.RIGHT
        hrun = hp.add_run("Pemerintah Kota Yogyakarta — Diskominfo dan Persandian")
        hrun.font.name = "Arial"
        hrun.font.size = Pt(8)
        hrun.font.color.rgb = COLOR_MUTED
        
        footer = section.footer
        fp = footer.paragraphs[0]
        fp.alignment = WD_ALIGN_PARAGRAPH.RIGHT
        frun = fp.add_run("Dokumen Resmi Standar Arsitektur Sistem Informasi")
        frun.font.name = "Arial"
        frun.font.size = Pt(8)
        frun.font.color.rgb = COLOR_MUTED

    # Normal Style
    normal_style = doc.styles['Normal']
    normal_font = normal_style.font
    normal_font.name = 'Arial'
    normal_font.size = Pt(10)
    normal_font.color.rgb = COLOR_DARK
    normal_style.paragraph_format.line_spacing = 1.15
    normal_style.paragraph_format.space_after = Pt(4)

def add_cover_page(doc, doc_type, title, app_name, version="1.0.0", date_str=None, author="Dinas Komunikasi Informatika dan Persandian Kota Yogyakarta"):
    """Generate formal cover page."""
    if date_str is None:
        date_str = datetime.now().strftime("%d %B %Y")
        
    p_spacer = doc.add_paragraph()
    p_spacer.paragraph_format.space_before = Pt(40)
    
    p_inst = doc.add_paragraph()
    p_inst.alignment = WD_ALIGN_PARAGRAPH.LEFT
    r_inst = p_inst.add_run("PEMERINTAH KOTA YOGYAKARTA\nDINAS KOMUNIKASI INFORMATIKA DAN PERSANDIAN")
    r_inst.font.name = "Arial"
    r_inst.font.size = Pt(11)
    r_inst.font.bold = True
    r_inst.font.color.rgb = COLOR_MUTED
    p_inst.paragraph_format.space_after = Pt(20)

    p_line = doc.add_paragraph()
    r_line = p_line.add_run("―" * 28)
    r_line.font.bold = True
    r_line.font.color.rgb = COLOR_PRIMARY
    p_line.paragraph_format.space_after = Pt(30)

    p_type = doc.add_paragraph()
    r_type = p_type.add_run(doc_type.upper())
    r_type.font.name = "Arial"
    r_type.font.size = Pt(13)
    r_type.font.bold = True
    r_type.font.color.rgb = RGBColor(13, 148, 136)
    p_type.paragraph_format.space_after = Pt(8)

    p_title = doc.add_paragraph()
    r_title = p_title.add_run(title)
    r_title.font.name = "Arial"
    r_title.font.size = Pt(22)
    r_title.font.bold = True
    r_title.font.color.rgb = COLOR_PRIMARY
    p_title.paragraph_format.space_after = Pt(12)

    p_app = doc.add_paragraph()
    r_app = p_app.add_run(f"Sistem / Aplikasi: {app_name} (v{version})")
    r_app.font.name = "Arial"
    r_app.font.size = Pt(12)
    r_app.font.color.rgb = COLOR_DARK
    p_app.paragraph_format.space_after = Pt(80)

    meta_table = doc.add_table(rows=4, cols=2)
    meta_table.alignment = WD_TABLE_ALIGNMENT.LEFT
    meta_table.autofit = False
    meta_table.columns[0].width = Inches(1.8)
    meta_table.columns[1].width = Inches(4.5)
    
    meta_rows = [
        ("Tanggal Rilis / Terbit", date_str),
        ("Status Dokumen", "Resmi / Final"),
        ("Penyusun & Pemilik", author),
        ("Klasifikasi Dokumen", "Rahasia Terbatas / Dinas Internal & Rekanan Resmi")
    ]
    
    for i, (k, v) in enumerate(meta_rows):
        row = meta_table.rows[i]
        c0 = row.cells[0]
        c1 = row.cells[1]
        set_cell_margins(c0, top=60, bottom=60, left=60, right=60)
        set_cell_margins(c1, top=60, bottom=60, left=60, right=60)
        
        p0 = c0.paragraphs[0]
        r0 = p0.add_run(k)
        r0.font.name = 'Arial'
        r0.font.size = Pt(9)
        r0.font.bold = True
        r0.font.color.rgb = COLOR_MUTED
        
        p1 = c1.paragraphs[0]
        r1 = p1.add_run(f":  {v}")
        r1.font.name = 'Arial'
        r1.font.size = Pt(9)
        r1.font.color.rgb = COLOR_DARK
        
    doc.add_page_break()

def parse_markdown_to_docx(md_content, doc, base_dir=None):
    """Convert structured Markdown content into formatted Word elements."""
    lines = md_content.split('\n')
    i = 0
    in_code_block = False
    code_buffer = []
    
    while i < len(lines):
        line = lines[i]
        stripped = line.strip()
        
        # Handle code blocks
        if stripped.startswith('```'):
            if in_code_block:
                in_code_block = False
                code_text = '\n'.join(code_buffer)
                add_callout(doc, code_text, callout_type="info")
                code_buffer = []
            else:
                in_code_block = True
                code_buffer = []
            i += 1
            continue
            
        if in_code_block:
            code_buffer.append(line)
            i += 1
            continue
            
        # Empty line
        if not stripped:
            i += 1
            continue
            
        # Horizontal Rule
        if re.match(r'^(-{3,}|\*{3,}|_{3,})$', stripped):
            p = doc.add_paragraph()
            p.paragraph_format.space_before = Pt(6)
            p.paragraph_format.space_after = Pt(6)
            r = p.add_run("―" * 35)
            r.font.color.rgb = RGBColor(203, 213, 225)
            i += 1
            continue
            
        # Blockquote / Callout
        if stripped.startswith('>'):
            callout_text = stripped.lstrip('>').strip()
            j = i + 1
            while j < len(lines) and lines[j].strip().startswith('>'):
                callout_text += " " + lines[j].strip().lstrip('>').strip()
                j += 1
            i = j
            
            ctype = "info"
            if "⚠️" in callout_text or "WARNING" in callout_text or "PERINGATAN" in callout_text:
                ctype = "warning"
            elif "❌" in callout_text or "DANGER" in callout_text or "FAIL" in callout_text:
                ctype = "danger"
            elif "✅" in callout_text or "SUCCESS" in callout_text or "PASS" in callout_text:
                ctype = "success"
                
            add_callout(doc, callout_text, callout_type=ctype)
            continue
            
        # Markdown Image Detection: ![Alt text](path/to/image.png)
        img_match = re.match(r'^!\[(.*?)\]\((.*?)\)$', stripped)
        if img_match:
            alt_text = img_match.group(1).strip()
            img_rel_path = img_match.group(2).strip()
            
            # Resolve image file path
            resolved_path = None
            possible_paths = [
                img_rel_path,
                os.path.join(base_dir, img_rel_path) if base_dir else None,
                os.path.join(os.getcwd(), img_rel_path),
                os.path.join(os.getcwd(), "docs", img_rel_path.lstrip("./")),
                os.path.join(os.getcwd(), "docs", "screenshots", os.path.basename(img_rel_path))
            ]
            for candidate in possible_paths:
                if candidate and os.path.exists(candidate) and os.path.isfile(candidate):
                    resolved_path = candidate
                    break
                    
            if resolved_path:
                try:
                    p_img = doc.add_paragraph()
                    p_img.alignment = WD_ALIGN_PARAGRAPH.CENTER
                    p_img.paragraph_format.space_before = Pt(8)
                    p_img.paragraph_format.space_after = Pt(2)
                    run_img = p_img.add_run()
                    run_img.add_picture(resolved_path, width=Inches(5.8))
                except Exception as e:
                    add_callout(doc, f"📸 [Screenshot: {alt_text} ({img_rel_path})]", callout_type="info")
            else:
                add_callout(doc, f"📸 [Tangkapan Layar: {alt_text}]\nFile: {img_rel_path}", callout_type="info")
                
            i += 1
            # Check if next line is caption like *Gambar X.X: ...*
            if i < len(lines) and lines[i].strip().startswith('*Gambar') and lines[i].strip().endswith('*'):
                caption_text = lines[i].strip().strip('*')
                p_cap = doc.add_paragraph()
                p_cap.alignment = WD_ALIGN_PARAGRAPH.CENTER
                p_cap.paragraph_format.space_before = Pt(2)
                p_cap.paragraph_format.space_after = Pt(8)
                r_cap = p_cap.add_run(caption_text)
                r_cap.font.name = 'Arial'
                r_cap.font.size = Pt(8.5)
                r_cap.font.italic = True
                r_cap.font.color.rgb = COLOR_MUTED
                i += 1
            continue

        # Headings
        if stripped.startswith('# '):
            p = doc.add_paragraph()
            p.paragraph_format.space_before = Pt(16)
            p.paragraph_format.space_after = Pt(6)
            p.paragraph_format.keep_with_next = True
            r = p.add_run(stripped[2:].strip())
            r.font.name = 'Arial'
            r.font.size = Pt(16)
            r.font.bold = True
            r.font.color.rgb = COLOR_PRIMARY
            i += 1
            continue
        elif stripped.startswith('## '):
            p = doc.add_paragraph()
            p.paragraph_format.space_before = Pt(14)
            p.paragraph_format.space_after = Pt(4)
            p.paragraph_format.keep_with_next = True
            r = p.add_run(stripped[3:].strip())
            r.font.name = 'Arial'
            r.font.size = Pt(13)
            r.font.bold = True
            r.font.color.rgb = COLOR_PRIMARY
            i += 1
            continue
        elif stripped.startswith('### '):
            p = doc.add_paragraph()
            p.paragraph_format.space_before = Pt(10)
            p.paragraph_format.space_after = Pt(2)
            p.paragraph_format.keep_with_next = True
            r = p.add_run(stripped[4:].strip())
            r.font.name = 'Arial'
            r.font.size = Pt(11)
            r.font.bold = True
            r.font.color.rgb = RGBColor(15, 23, 42)
            i += 1
            continue
        elif stripped.startswith('#### '):
            p = doc.add_paragraph()
            p.paragraph_format.space_before = Pt(8)
            p.paragraph_format.space_after = Pt(2)
            p.paragraph_format.keep_with_next = True
            r = p.add_run(stripped[5:].strip())
            r.font.name = 'Arial'
            r.font.size = Pt(10)
            r.font.bold = True
            r.font.color.rgb = RGBColor(13, 148, 136)
            i += 1
            continue
            
        # Markdown Table Detection
        if '|' in stripped and ('|' in lines[min(i+1, len(lines)-1)] if i+1 < len(lines) else False):
            table_lines = []
            while i < len(lines) and '|' in lines[i].strip():
                table_lines.append(lines[i].strip())
                i += 1
            
            if len(table_lines) >= 2:
                headers = [c.strip() for c in table_lines[0].split('|')[1:-1]]
                data_rows = []
                for tline in table_lines[1:]:
                    if re.match(r'^[\|\s\-:]+$', tline):
                        continue
                    cols = [c.strip() for c in tline.split('|')[1:-1]]
                    if cols:
                        data_rows.append(cols)
                        
                if headers:
                    num_cols = len(headers)
                    tbl = doc.add_table(rows=len(data_rows)+1, cols=num_cols)
                    tbl.alignment = WD_TABLE_ALIGNMENT.CENTER
                    tbl.autofit = True
                    set_table_borders(tbl)
                    
                    # Header Row
                    hdr_row = tbl.rows[0]
                    trPr = hdr_row._tr.get_or_add_trPr()
                    trPr.append(parse_xml(f'<w:tblHeader {nsdecls("w")}/>'))
                    
                    for ci, htext in enumerate(headers):
                        cell = hdr_row.cells[ci]
                        set_cell_background(cell, COLOR_PRIMARY_HEX)
                        set_cell_margins(cell, top=100, bottom=100, left=120, right=120)
                        p = cell.paragraphs[0]
                        p.paragraph_format.space_before = Pt(0)
                        p.paragraph_format.space_after = Pt(0)
                        r = p.add_run(htext)
                        r.font.name = 'Arial'
                        r.font.size = Pt(9)
                        r.font.bold = True
                        r.font.color.rgb = RGBColor(255, 255, 255)
                        
                    # Data Rows
                    for ri, rdata in enumerate(data_rows):
                        d_row = tbl.rows[ri+1]
                        bg_color = COLOR_LIGHT_BG_HEX if ri % 2 == 1 else "FFFFFF"
                        for ci in range(num_cols):
                            cell = d_row.cells[ci]
                            val = rdata[ci] if ci < len(rdata) else ""
                            set_cell_background(cell, bg_color)
                            set_cell_margins(cell, top=80, bottom=80, left=120, right=120)
                            p = cell.paragraphs[0]
                            p.paragraph_format.space_before = Pt(0)
                            p.paragraph_format.space_after = Pt(0)
                            p.paragraph_format.line_spacing = 1.1
                            r = p.add_run(val)
                            r.font.name = 'Arial'
                            r.font.size = Pt(8.5)
                            r.font.color.rgb = COLOR_DARK
                            
                    doc.add_paragraph().paragraph_format.space_after = Pt(4)
            continue

        # Unordered List
        if stripped.startswith('- ') or stripped.startswith('* '):
            p = doc.add_paragraph(style='List Bullet')
            p.paragraph_format.space_before = Pt(1)
            p.paragraph_format.space_after = Pt(2)
            p.paragraph_format.line_spacing = 1.15
            parse_inline_formatting(p, stripped[2:].strip())
            i += 1
            continue

        # Ordered List
        numbered_match = re.match(r'^(\d+)\.\s+(.*)$', stripped)
        if numbered_match:
            text = numbered_match.group(2)
            p = doc.add_paragraph(style='List Number')
            p.paragraph_format.space_before = Pt(1)
            p.paragraph_format.space_after = Pt(2)
            p.paragraph_format.line_spacing = 1.15
            parse_inline_formatting(p, text)
            i += 1
            continue

        # Regular Paragraph
        p = doc.add_paragraph()
        p.paragraph_format.space_before = Pt(2)
        p.paragraph_format.space_after = Pt(4)
        p.paragraph_format.line_spacing = 1.15
        parse_inline_formatting(p, stripped)
        i += 1

def parse_inline_formatting(paragraph, text):
    """Parse basic inline markdown (bold, italic, inline code)."""
    tokens = re.split(r'(\*\*.*?\*\*|\`.*?\`|\[.*?\]\(.*?\))', text)
    for token in tokens:
        if not token:
            continue
        if token.startswith('**') and token.endswith('**'):
            r = paragraph.add_run(token[2:-2])
            r.font.name = 'Arial'
            r.font.bold = True
        elif token.startswith('`') and token.endswith('`'):
            r = paragraph.add_run(token[1:-1])
            r.font.name = 'Courier New'
            r.font.size = Pt(9)
            r.font.color.rgb = RGBColor(180, 40, 40)
        elif token.startswith('[') and '](' in token and token.endswith(')'):
            link_match = re.match(r'\[(.*?)\]\((.*?)\)', token)
            if link_match:
                r = paragraph.add_run(f"{link_match.group(1)} ({link_match.group(2)})")
                r.font.name = 'Arial'
                r.font.color.rgb = COLOR_PRIMARY
                r.font.underline = True
            else:
                r = paragraph.add_run(token)
                r.font.name = 'Arial'
        else:
            r = paragraph.add_run(token)
            r.font.name = 'Arial'

def convert_md_to_docx(input_md_path, output_docx_path, doc_type="DOKUMEN TEKNIS RESMI", title="Dokumen Spesifikasi", app_name="Aplikasi Pemkot Yogyakarta", version="1.0.0"):
    """Convert a markdown file to a fully styled DOCX file."""
    if not os.path.exists(input_md_path):
        print(f"Error: input file {input_md_path} not found.")
        return False
        
    with open(input_md_path, 'r', encoding='utf-8') as f:
        content = f.read()
        
    doc = Document()
    setup_document_styles(doc)
    add_cover_page(doc, doc_type=doc_type, title=title, app_name=app_name, version=version)
    base_dir = os.path.dirname(os.path.abspath(input_md_path))
    parse_markdown_to_docx(content, doc, base_dir=base_dir)
    
    os.makedirs(os.path.dirname(os.path.abspath(output_docx_path)), exist_ok=True)
    doc.save(output_docx_path)
    print(f"✅ Berhasil menghasilkan dokumen DOCX: {output_docx_path}")
    return True

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generator Dokumen DOCX Resmi Diskominfo Kota Yogyakarta")
    parser.add_argument("--input", "-i", help="Path ke file input Markdown", required=False)
    parser.add_argument("--output", "-o", help="Path ke file output DOCX", required=False)
    parser.add_argument("--type", "-t", default="DOKUMEN RESMI", help="Tipe dokumen (e.g. KERANGKA ACUAN KERJA, LAPORAN PENGUJIAN QA, LAPORAN PENTEST, SPESIFIKASI API, PANDUAN PENGGUNA)")
    parser.add_argument("--title", default="Dokumen Resmi Aplikasi", help="Judul dokumen")
    parser.add_argument("--app", default="Sistem Informasi Diskominfo", help="Nama aplikasi")
    parser.add_argument("--version", default="1.0.0", help="Versi aplikasi")
    
    args = parser.parse_args()
    if args.input and args.output:
        convert_md_to_docx(args.input, args.output, doc_type=args.type, title=args.title, app_name=args.app, version=args.version)
    else:
        print("Usage: python3 generate_docx.py -i input.md -o docs/output.docx -t 'KERANGKA ACUAN KERJA' --title 'Pengembangan Aplikasi X' --app 'Aplikasi X'")
