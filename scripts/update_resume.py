"""Replace deleted project references in the site's one-page resume PDF."""
from pathlib import Path
import os
import fitz

pdf_path = Path(__file__).resolve().parent.parent / "Behrooz_Koshani_Resume.pdf"
doc = fitz.open(pdf_path)
if len(doc) != 1:
    raise RuntimeError("Expected one-page portfolio resume")
page = doc[0]
text = page.get_text()
if "Simple TCP Port Scanner" in text:
    doc.close()
    print("Resume already current")
    raise SystemExit(0)
if "TECHNICAL PROJECTS" not in text or "Cloud Security Analyzer" not in text:
    raise RuntimeError("Original project section differs; refusing unsafe PDF modification")

# Only replace the project entries, preserving the rest of the existing PDF layout.
page.add_redact_annot(fitz.Rect(44, 570, 584, 655), fill=(1, 1, 1))
page.apply_redactions(images=0, graphics=0, text=0)
fonts = Path("/usr/share/fonts/truetype/crosextra")
page.insert_font(fontname="ResumeCarlito", fontfile=str(fonts / "Carlito-Regular.ttf"))
page.insert_font(fontname="ResumeCarlitoBold", fontfile=str(fonts / "Carlito-Bold.ttf"))
black = (0, 0, 0)
blue = (31/255, 64/255, 120/255)
rows = [
    (581, "LogShield — ", 48.7926, "AI-assisted log analyzer for failed logins, suspicious IPs, and anomalies.", None),
    (598, "Metasploit Attack Simulation — ", 123.5607, "Authorized Kali/Windows VM lab with documented steps and screenshots.", "https://github.com/behroozkoshani/metasploit-attack-simulation-lab"),
    (615, "Simple TCP Port Scanner — ", 105.2116, "C++20 TCP connect scans, localhost testing, worker threads, and JSON/CSV reports.", "https://github.com/behroozkoshani/simple-port-scanner")
]
for y, title, width, description, url in rows:
    page.insert_text((49.1, y), "•", fontname="ResumeCarlito", fontsize=9, color=black)
    page.insert_text((64, y), title, fontname="ResumeCarlitoBold", fontsize=9.15, color=black)
    page.insert_text((64 + width, y), description, fontname="ResumeCarlito", fontsize=8.45, color=black)
    if url:
        page.insert_text((542, y), "GitHub", fontname="ResumeCarlito", fontsize=8.8, color=blue)
        page.insert_link({"kind": fitz.LINK_URI, "from": fitz.Rect(540, y-11, 582, y+3), "uri": url})
url = "https://github.com/behroozkoshani/simple-port-scanner"
page.insert_text((64, 632), "github.com/behroozkoshani/simple-port-scanner", fontname="ResumeCarlito", fontsize=8.3, color=blue)
page.draw_line((64, 633.2), (237, 633.2), color=blue, width=0.35)
page.insert_link({"kind": fitz.LINK_URI, "from": fitz.Rect(64, 623, 250, 635), "uri": url})

temp = pdf_path.with_suffix(".updated.pdf")
doc.save(temp, garbage=4, deflate=True)
doc.close()
updated = fitz.open(temp)
content = updated[0].get_text()
links = [item.get("uri") for item in updated[0].get_links()]
if ("Simple TCP Port Scanner" not in content
        or "github.com/behroozkoshani/simple-port-scanner" not in content
        or url not in links
        or any(t in content for t in ("Cloud Security Analyzer", "Vulnerability Prioritization", "Active Directory Security Audit"))):
    raise RuntimeError("Updated resume failed validation")
updated.close()
os.replace(temp, pdf_path)
print("Updated one-page resume with live scanner GitHub link")
