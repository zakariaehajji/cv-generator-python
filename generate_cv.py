from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from reportlab.lib import colors
import os

def get_multiple_inputs(label):
    print(f"\n➤ {label} (entre 'stop' pour terminer)")
    results = []
    while True:
        item = input(" - ")
        if item.lower() == "stop":
            break
        results.append(item)
    return results

def create_cv(lang="fr"):
    print("=== Générateur de CV Complet ===")

    labels = {
        "title": "Curriculum Vitae" if lang == "fr" else "Resume",
        "name": "Nom" if lang == "fr" else "Name",
        "email": "E-mail",
        "phone": "Téléphone" if lang == "fr" else "Phone",
        "linkedin": "Profil LinkedIn",
        "education": "Formation" if lang == "fr" else "Education",
        "skills": "Compétences" if lang == "fr" else "Skills",
        "experience": "Expériences" if lang == "fr" else "Experience",
        "languages": "Langues" if lang == "fr" else "Languages",
        "interests": "Centres d’intérêt" if lang == "fr" else "Interests"
    }

    # INFORMATIONS
    nom = input(f"{labels['name']} : ")
    email = input(f"{labels['email']} : ")
    tel = input(f"{labels['phone']} : ")
    linkedin = input(f"{labels['linkedin']} : ")

    formations = get_multiple_inputs(labels["education"])
    competences = get_multiple_inputs(labels["skills"])
    experiences = get_multiple_inputs(labels["experience"])
    langues = get_multiple_inputs(labels["languages"])
    interets = get_multiple_inputs(labels["interests"])

    # Créer le fichier
    os.makedirs("outputs", exist_ok=True)
    filename = os.path.join("outputs", f"{nom.replace(' ', '_')}_CV.pdf")
    c = canvas.Canvas(filename, pagesize=A4)
    width, height = A4

    # BARRE LATERALE
    c.setFillColor(colors.HexColor("#003366"))
    c.rect(0, 0, 160, height, stroke=0, fill=1)

    c.setFont("Helvetica-Bold", 20)
    c.setFillColor(colors.white)
    c.drawString(20, height - 60, nom)

    c.setFont("Helvetica", 10)
    c.drawString(20, height - 90, email)
    c.drawString(20, height - 105, tel)
    c.drawString(20, height - 120, linkedin)

    def section_title(y, text):
        c.setFillColor(colors.HexColor("#003366"))
        c.setFont("Helvetica-Bold", 14)
        c.drawString(180, y, text)
        return y - 20

    def section_content(y, items):
        c.setFont("Helvetica", 11)
        c.setFillColor(colors.black)
        for item in items:
            c.drawString(200, y, f"- {item}")
            y -= 15
        return y - 5

    y = height - 60
    c.setFont("Helvetica-Bold", 16)
    c.setFillColor(colors.black)
    c.drawString(180, y, labels["title"])
    y -= 40

    # Ajouter les sections
    for section, items in [
        (labels["education"], formations),
        (labels["skills"], competences),
        (labels["experience"], experiences),
        (labels["languages"], langues),
        (labels["interests"], interets)
    ]:
        if items:
            y = section_title(y, section)
            y = section_content(y, items)

    c.save()
    print(f"\n✅ CV généré avec succès : {filename}")

# Choix de la langue
lang = input("Langue du CV (fr/en) : ").strip().lower()
if lang not in ["fr", "en"]:
    lang = "fr"

create_cv(lang)
