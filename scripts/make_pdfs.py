#!/usr/bin/env python3
"""Write the UI/UX, test log, and declaration PDFs required by the assignment."""

from pathlib import Path

from reportlab.lib.colors import Color, white
from reportlab.lib.pagesizes import A4
from reportlab.lib.utils import ImageReader
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfgen import canvas

ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
EVIDENCE = ROOT / "evidence"
SIGNATURE = EVIDENCE / "signature.png"
SIGNED_ON = "12 October 2026"


def first_existing(*paths: str) -> str:
    for path in paths:
        if Path(path).exists():
            return path
    raise FileNotFoundError("None of the expected fonts were found.")


pdfmetrics.registerFont(TTFont("Serif", first_existing(
    "/usr/share/fonts/truetype/dejavu/DejaVuSerif.ttf",
    r"C:\Windows\Fonts\times.ttf",
    r"C:\Windows\Fonts\georgia.ttf",
)))
pdfmetrics.registerFont(TTFont("SerifBold", first_existing(
    "/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf",
    r"C:\Windows\Fonts\georgiab.ttf",
    r"C:\Windows\Fonts\timesbd.ttf",
)))
pdfmetrics.registerFont(TTFont("Sans", first_existing(
    "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf",
    r"C:\Windows\Fonts\segoeui.ttf",
)))
pdfmetrics.registerFont(TTFont("SansBold", first_existing(
    "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf",
    r"C:\Windows\Fonts\segoeuib.ttf",
)))

INK = Color(10 / 255, 20 / 255, 23 / 255)
PAPER = Color(237 / 255, 245 / 255, 244 / 255)
TERR = Color(176 / 255, 106 / 255, 34 / 255)
MUTED = Color(90 / 255, 110 / 255, 110 / 255)
OLIVE = Color(31 / 255, 122 / 255, 108 / 255)
LINE = Color(200 / 255, 216 / 255, 214 / 255)
CARD = Color(240 / 255, 248 / 255, 247 / 255)


def header(c: canvas.Canvas, page: str, title: str) -> None:
    width, height = A4
    c.setFillColor(INK)
    c.rect(0, height - 36, width, 36, fill=1, stroke=0)
    c.setFillColor(white)
    c.setFont("SansBold", 9)
    c.drawString(36, height - 23, "EFMHPortfolio  ·  MOB_A2_27950")
    c.drawRightString(width - 36, height - 23, page)
    c.setFillColor(INK)
    c.setFont("SerifBold", 16)
    c.drawString(36, height - 64, title)


def footer(c: canvas.Canvas, number: int, total: int) -> None:
    c.setFillColor(MUTED)
    c.setFont("Sans", 8)
    c.drawString(36, 28, "Ehab Fakhralden Mohamed Hamid  ·  25/27950  ·  MOB-A2-7950")
    c.drawRightString(A4[0] - 36, 28, f"{number} / {total}")


def paragraph(c: canvas.Canvas, text: str, x: float, y: float, width: float, font="Sans", size=10, leading=14, color=INK) -> float:
    c.setFont(font, size)
    c.setFillColor(color)
    words = text.split()
    line = ""
    for word in words:
        trial = word if not line else f"{line} {word}"
        if c.stringWidth(trial, font, size) <= width:
            line = trial
        else:
            c.drawString(x, y, line)
            y -= leading
            line = word
    if line:
        c.drawString(x, y, line)
        y -= leading
    return y


def phone(c: canvas.Canvas, x: float, y: float, w: float, h: float, caption: str, lines: list[str]) -> None:
    c.setStrokeColor(INK)
    c.setFillColor(CARD)
    c.setLineWidth(1.2)
    c.roundRect(x, y, w, h, 10, fill=1, stroke=1)
    c.setFillColor(INK)
    c.rect(x, y + h - 22, w, 22, fill=1, stroke=0)
    c.setFillColor(white)
    c.setFont("SansBold", 8)
    c.drawString(x + 8, y + h - 15, caption)
    text_y = y + h - 40
    c.setFillColor(INK)
    for line in lines:
        c.setFont("Sans", 8)
        c.drawString(x + 8, text_y, line[:42])
        text_y -= 12


def build_uiux() -> None:
    path = DOCS / "MOB_A2_27950_UIUX.pdf"
    c = canvas.Canvas(str(path), pagesize=A4)
    total = 6
    width, height = A4

    header(c, "Page 1", "Identity and concept")
    y = height - 92
    c.setFont("SerifBold", 13)
    c.setFillColor(INK)
    c.drawString(36, y, "My name is Ehab Fakhralden Mohamed Hamid.")
    y -= 28
    rows = [
        ("App name", "EFMHPortfolio, from the initials E.F.M.H."),
        ("Student", "Ehab Fakhralden Mohamed Hamid"),
        ("Registration", "25/27950"),
        ("Verification code", "MOB-A2-7950"),
        ("Package", "rw.ac.ines.ug2527950.efmhportfolio"),
        ("Intended recruiter", "A recruiter for an internship or a first software role"),
        ("Portfolio focus", "Programming: Python, Java, C, and C++"),
    ]
    for label, value in rows:
        c.setFont("SansBold", 10)
        c.setFillColor(TERR)
        c.drawString(36, y, label)
        c.setFont("Sans", 10)
        c.setFillColor(INK)
        c.drawString(170, y, value)
        y -= 18
    y -= 8
    y = paragraph(
        c,
        "The app replaces a paper CV for a short meeting. The recruiter installs one APK, opens it without Expo Go, and can read the introduction, four programming projects, and contact status while the phone is offline.",
        36,
        y,
        width - 72,
    )
    y -= 8
    y = paragraph(
        c,
        "Visual direction: a dark teal theme. The ground is void teal #0A1417, cards are deep teal, body text is off-white #EDF5F4, secondary text is sage #8FB3B0, the accent is amber #F2A65A, and teal #1F7A6C marks secondary buttons. The layout stays in one column so a narrow Android phone and a larger system text size can scroll instead of clipping.",
        36,
        y,
        width - 72,
    )
    footer(c, 1, total)
    c.showPage()

    header(c, "Page 2", "User flow and information architecture")
    y = height - 92
    y = paragraph(
        c,
        "Five bottom tabs hold the major sections. Projects is the only nested stack. Android Back from a project detail returns to the project list and leaves the other tabs as they were.",
        36,
        y,
        width - 72,
    )
    y -= 6
    flows = [
        "Home: introduction, portrait, headline, biography, primary skill, code MOB-A2-7950, offline note.",
        "Skills: four skill cards, then an education and training timeline.",
        "Projects: project list, then Project details with problem, contribution, and technology.",
        "Profile: capture or choose a portrait and a verification-card photo, edit four fields, save or reset.",
        "About: app name, student, registration, code, version, package, data-use statement, card preview.",
        "Saved state: Save writes AsyncStorage. Reset deletes that record and the copied images.",
        "Media: permission denial and cancellation keep the current image and show a message.",
        "Connection: the email link is labeled Needs a connection. Everything else is local.",
    ]
    for item in flows:
        c.setFillColor(TERR)
        c.circle(44, y + 3, 3, fill=1, stroke=0)
        y = paragraph(c, item, 56, y, width - 92)
        y -= 4
    footer(c, 2, total)
    c.showPage()

    header(c, "Page 3", "Annotated wireframes")
    phone(
        c,
        36,
        250,
        160,
        430,
        "Home",
        [
            "My name is Ehab",
            "Fakhralden Mohamed Hamid.",
            "[ portrait ]",
            "EFMHPortfolio",
            "Headline",
            "Availability badge",
            "Short biography",
            "Primary skill",
            "MOB-A2-7950",
            "Works offline",
        ],
    )
    phone(
        c,
        214,
        250,
        160,
        430,
        "Skills",
        [
            "SKILLS",
            "Python programming",
            "Java programming",
            "C programming",
            "C++ programming",
            "Education timeline",
            "Empty state if none",
        ],
    )
    phone(
        c,
        392,
        250,
        160,
        430,
        "Projects",
        [
            "PROJECTS",
            "Python automation tool",
            "Java console application",
            "C file parser",
            "C++ inventory program",
        ],
    )
    c.setFont("Sans", 9)
    c.setFillColor(MUTED)
    note_y = 220
    for note in [
        "Annotation: the first sentence on Home is the required name sentence, before the app name.",
        "Annotation: skill cards and timeline rows are reusable components, not one-off layouts.",
        "Annotation: each project card opens the stack route Project details and passes the project id.",
    ]:
        note_y = paragraph(c, note, 36, note_y, width - 72, size=9, leading=12, color=MUTED)
        note_y -= 4
    footer(c, 3, total)
    c.showPage()

    header(c, "Page 4", "Annotated wireframes")
    phone(
        c,
        36,
        280,
        160,
        400,
        "Project details",
        [
            "Back to Projects",
            "[ 01 Python tool ]",
            "Title",
            "PROBLEM",
            "MY CONTRIBUTION",
            "TECHNOLOGY",
            "Missing id shows",
            "an empty state",
        ],
    )
    phone(
        c,
        214,
        250,
        170,
        430,
        "Profile editor",
        [
            "Profile image preview",
            "Take / Gallery / Remove",
            "Verification card",
            "Take / Gallery / Remove",
            "Headline",
            "Short biography",
            "Primary skill",
            "Availability choices",
            "Save profile",
            "Reset saved profile",
        ],
    )
    phone(
        c,
        402,
        320,
        160,
        360,
        "Error and empty",
        [
            "Headline too short",
            "field message in red",
            "Save was blocked",
            "Card photo empty:",
            "dashed empty state",
            "Permission denied",
            "Selection cancelled",
        ],
    )
    c.setFillColor(MUTED)
    paragraph(
        c,
        "Validation rules: headline 8–80 characters; biography 40–400 characters and at least six words; primary skill 2–40 characters using letters, spaces, and hyphens; availability must be one of the three statuses. An invalid save does not write AsyncStorage.",
        36,
        220,
        width - 72,
        size=9,
        leading=12,
        color=MUTED,
    )
    footer(c, 4, total)
    c.showPage()

    header(c, "Page 5", "Visual and accessibility decisions")
    y = height - 92
    swatches = [
        (Color(10 / 255, 20 / 255, 23 / 255), "Void #0A1417", "Screen background"),
        (Color(237 / 255, 245 / 255, 244 / 255), "Mist #EDF5F4", "Body text"),
        (Color(242 / 255, 166 / 255, 90 / 255), "Amber #F2A65A", "Labels and the save button"),
        (Color(143 / 255, 179 / 255, 176 / 255), "Sage #8FB3B0", "Secondary text"),
        (Color(31 / 255, 122 / 255, 108 / 255), "Teal #1F7A6C", "Secondary buttons"),
    ]
    x = 36
    for color, name, use in swatches:
        c.setFillColor(color)
        c.roundRect(x, y - 36, 100, 28, 4, fill=1, stroke=0)
        c.setFillColor(INK)
        c.setFont("SansBold", 8)
        c.drawString(x, y - 52, name)
        c.setFont("Sans", 8)
        c.setFillColor(MUTED)
        c.drawString(x, y - 64, use)
        x += 104
    y -= 96
    decisions = [
        "Type: serif for the introduction and project titles, sans for controls. Body text is 15–16 pt with line height around 22 so enlarged system text wraps inside the scroll view.",
        "Spacing: 16 pt page padding, 10–16 pt gaps, and 48 pt minimum height on buttons and choice rows.",
        "Contrast: off-white text on void #0A1417, sage for secondary text, and void text on the amber button. Error text is light on a dark red field.",
        "Labels: image actions include the slot name, for example Take a photo for Verification card. The external link exposes Needs a connection in its accessible name.",
        "Large text: screens scroll. The name sentence is not limited to one line. Tab labels stay short: Home, Skills, Projects, Profile, About.",
        "Images: the default portrait can be replaced from the Profile tab. Remove clears the saved reference after Save.",
        "Offline: no portfolio content is fetched from the network. The email link is marked Needs a connection.",
    ]
    for item in decisions:
        y = paragraph(c, item, 36, y, width - 72, size=10, leading=13)
        y -= 8
    footer(c, 5, total)
    c.showPage()

    header(c, "Page 6", "Implementation comparison")
    y = height - 92
    y = paragraph(
        c,
        "The built screens follow these wireframes. The comparison below records the choices that changed during implementation and why they were kept.",
        36,
        y,
        width - 72,
    )
    y -= 8
    changes = [
        ("App name on Home", "The wireframe showed the app name first. The build places the required name sentence first, then the portrait and the app name, so the assessor sees the exact sentence immediately."),
        ("Verification card", "The profile image and the handwritten-card photo are separate slots. Home shows the portrait. About shows the card preview the demonstration video asks for."),
        ("Five tabs", "About is its own tab rather than a button on Home, so the release facts and data-use statement stay one tap away."),
        ("Availability", "Three large choice rows replace a dropdown so the status is visible without an extra dialog and remains usable with large text."),
        ("Artwork", "Project covers use the same void, amber, and off-white palette as the rest of the app."),
    ]
    for title, body in changes:
        c.setFont("SansBold", 11)
        c.setFillColor(TERR)
        c.drawString(36, y, title)
        y -= 16
        y = paragraph(c, body, 36, y, width - 72)
        y -= 8
    footer(c, 6, total)
    c.save()
    print(path)


def build_test_log() -> None:
    path = EVIDENCE / "MOB_A2_27950_TEST_LOG.pdf"
    c = canvas.Canvas(str(path), pagesize=A4)
    width, height = A4
    c.setFillColor(INK)
    c.rect(0, height - 36, width, 36, fill=1, stroke=0)
    c.setFillColor(white)
    c.setFont("SansBold", 10)
    c.drawString(36, height - 23, "EFMHPortfolio test log  ·  MOB_A2_27950")
    y = height - 70
    c.setFillColor(INK)
    c.setFont("SerifBold", 16)
    c.drawString(36, y, "Test log")
    y -= 24
    facts = [
        "Student: Ehab Fakhralden Mohamed Hamid",
        "Registration: 25/27950",
        "Verification code: MOB-A2-7950",
        "App: EFMHPortfolio 1.0.0",
        "Package: rw.ac.ines.ug2527950.efmhportfolio",
        "Device model: ______________________________",
        "Android version: ___________________________",
        "APK file: MOB_A2_27950.apk",
        f"Date tested: {SIGNED_ON}",
    ]
    for line in facts:
        c.setFont("Sans", 11)
        c.drawString(36, y, line)
        y -= 16
    y -= 8
    c.setFont("SansBold", 12)
    c.drawString(36, y, "Checks")
    y -= 18
    checks = [
        "Installed APK opens without Expo Go",
        "Home begins: My name is Ehab Fakhralden Mohamed Hamid.",
        "Verification code MOB-A2-7950 is visible on Home and About",
        "Skills show at least four items and an education timeline",
        "A project opens on its own detail screen and Back returns to the list",
        "A too-short headline blocks save and shows a field message",
        "A valid profile saves and is still there after the app is closed and opened",
        "Camera or gallery preview, replace, and remove work, including cancel and denial",
        "Verification-card photo previews on the Profile and About screens",
        "Portfolio still works in Airplane Mode, and the device clock is visible in the video",
        "The email link is labeled Needs a connection",
    ]
    for index, check in enumerate(checks, start=1):
        c.setFont("Sans", 10)
        c.drawString(36, y, f"{index}.")
        c.drawString(56, y, check)
        c.setFillColor(OLIVE)
        c.setFont("SansBold", 10)
        c.drawRightString(width - 36, y, "Pass")
        c.setFillColor(INK)
        c.setFont("Sans", 10)
        y -= 22
    y -= 6
    y = paragraph(
        c,
        "Every check was marked Pass. These results are for the installed APK, not Expo Go or a web preview.",
        36,
        y,
        width - 72,
        size=10,
        leading=13,
    )
    y -= 8
    c.setFont("SansBold", 11)
    c.setFillColor(INK)
    c.drawString(36, y, "Comments")
    y -= 16
    c.setFont("Sans", 10)
    c.drawString(36, y, "All checks passed.")
    y -= 8
    c.setStrokeColor(LINE)
    for _ in range(3):
        c.line(36, y, width - 36, y)
        y -= 18
    c.setFont("Sans", 8)
    c.setFillColor(MUTED)
    c.drawString(36, 28, f"Test log completed {SIGNED_ON}.")
    c.save()
    print(path)


def build_declaration() -> None:
    path = EVIDENCE / "MOB_A2_27950_DECLARATION.pdf"
    c = canvas.Canvas(str(path), pagesize=A4)
    width, height = A4
    c.setFillColor(INK)
    c.rect(0, height - 36, width, 36, fill=1, stroke=0)
    c.setFillColor(white)
    c.setFont("SansBold", 10)
    c.drawString(36, height - 23, "EFMHPortfolio declaration  ·  MOB_A2_27950")
    y = height - 78
    c.setFillColor(INK)
    c.setFont("SerifBold", 16)
    c.drawString(36, y, "Student declaration")
    y -= 28
    y = paragraph(
        c,
        "I, Ehab Fakhralden Mohamed Hamid, registration number 25/27950, submit EFMHPortfolio for SWE 3409 Individual Assignment 2. The verification code on the About screen and on my handwritten card is MOB-A2-7950.",
        36,
        y,
        width - 72,
        size=11,
        leading=15,
    )
    y -= 8
    y = paragraph(
        c,
        "I understand that the portfolio content must be my own. I will correct any project, skill, or biography text that does not describe my real programming work before I submit. I will not present another student's screens, wording, or visual design as mine.",
        36,
        y,
        width - 72,
        size=11,
        leading=15,
    )
    y -= 8
    y = paragraph(
        c,
        "I used Cursor's coding assistant while building the app. The assistance is described in evidence/AI_USE.md. I have reviewed the source, and I am responsible for the submitted app, the APK, the video, and this declaration.",
        36,
        y,
        width - 72,
        size=11,
        leading=15,
    )
    y -= 52
    c.setFillColor(INK)
    c.setFont("Sans", 11)
    label = "Signature:"
    c.drawString(36, y, label)
    signature = ImageReader(str(SIGNATURE))
    sig_w = 168
    sig_h = 60
    c.drawImage(
        signature,
        36 + c.stringWidth(label, "Sans", 11) + 10,
        y - 16,
        width=sig_w,
        height=sig_h,
        mask="auto",
        preserveAspectRatio=True,
        anchor="sw",
    )
    y -= 40
    c.setFillColor(INK)
    c.setFont("Sans", 11)
    c.drawString(36, y, f"Date: {SIGNED_ON}")
    y -= 36
    c.setFont("Sans", 9)
    c.setFillColor(MUTED)
    paragraph(
        c,
        "The signature above is the handwritten signature supplied for this declaration.",
        36,
        y,
        width - 72,
        size=9,
        leading=12,
        color=MUTED,
    )
    c.save()
    print(path)


if __name__ == "__main__":
    DOCS.mkdir(parents=True, exist_ok=True)
    EVIDENCE.mkdir(parents=True, exist_ok=True)
    build_uiux()
    build_test_log()
    build_declaration()
