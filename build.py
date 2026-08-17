#!/usr/bin/env python3
"""
Generates the 6 static HTML pages for the WellBeing Psychotherapy site
from shared header/footer partials. Run with: python3 build.py
This script is a dev convenience only — the OUTPUT .html files are the
deliverable and need no build step to host.
"""
import os
import json

ROOT = os.path.dirname(os.path.abspath(__file__))

# ---------------------------------------------------------------------------
# SITE CONFIG — the one spot to change if the live domain differs.
# Based on the practice's existing domain named in the design handoff
# (wellbeingwellness.ca). Update this if the real domain is different, then
# re-run this script (or find/replace this string across the generated
# .html/.xml/.txt files).
# ---------------------------------------------------------------------------
SITE_URL = "https://www.wellbeingwellness.ca"

# Real booking system (Jane App). All "Book Now" style links/buttons across the
# site point straight here and open in a new tab, per the client's request.
JANE_APP_URL = "https://yrspsychotherapy.janeapp.com/#staff_member/1"
JANE_ATTRS = f'href="{JANE_APP_URL}" target="_blank" rel="noopener"'

NAV_ITEMS = [
    ("home", "index.html", "Home"),
    ("about", "about.html", "About"),
    ("team", "team.html", "Team"),
    ("faq", "faq.html", "FAQ"),
    ("contact", "contact.html", "Contact"),
]

# Pages included in the sitemap / used to loop robots-adjacent config
ALL_PAGES = [k for k, _, _ in NAV_ITEMS] + ["book"]

# ---------------------------------------------------------------------------
# Structured data (JSON-LD). Practice is virtual-only (no public storefront),
# so no street address is published — areaServed covers Ontario / GTA instead.
# See README.md "SEO" section for how to edit this.
# ---------------------------------------------------------------------------
ORG_JSONLD = {
    "@context": "https://schema.org",
    "@type": "MedicalBusiness",
    "name": "WellBeing Psychotherapy",
    "url": SITE_URL + "/",
    "image": SITE_URL + "/images/logo.png",
    "logo": SITE_URL + "/images/logo.png",
    "telephone": "+1-437-747-3941",
    "email": "yasmin.singh@wellbeingwellness.ca",
    "description": "Compassionate, one-on-one virtual therapy with a Registered Psychotherapist, offering culturally responsive care for individuals across the Greater Toronto Area and Ontario, including South Asian clients.",
    "medicalSpecialty": "Psychiatric",
    "areaServed": [
        {"@type": "AdministrativeArea", "name": "Greater Toronto Area"},
        {"@type": "State", "name": "Ontario"},
    ],
    "sameAs": [
        "https://www.instagram.com/well_being_wellness/",
    ],
    "employee": {
        "@type": "Person",
        "name": "Yasmin Singh",
        "jobTitle": "Registered Psychotherapist (RP), CRPO",
    },
}

PERSON_JSONLD = {
    "@context": "https://schema.org",
    "@type": "Person",
    "name": "Yasmin Singh",
    "jobTitle": "Registered Psychotherapist",
    "description": "Registered Psychotherapist with the College of Registered Psychotherapists of Ontario (CRPO), offering culturally responsive virtual therapy across the Greater Toronto Area, including for South Asian clients.",
    "worksFor": {"@type": "Organization", "name": "WellBeing Psychotherapy", "url": SITE_URL + "/"},
    "url": SITE_URL + "/team.html",
    "image": SITE_URL + "/images/team-yasmin.jpg",
    "affiliation": {"@type": "Organization", "name": "College of Registered Psychotherapists of Ontario (CRPO)"},
}

def jsonld_script(*data_objs):
    blocks = "\n".join(
        f'<script type="application/ld+json">{json.dumps(d, indent=2)}</script>'
        for d in data_objs
    )
    return blocks

def head(title, description, canonical_file, og_image="images/hero.jpg", extra_jsonld=None):
    canonical_url = f"{SITE_URL}/{canonical_file}"
    og_image_url = f"{SITE_URL}/{og_image}"
    jsonld_objs = [ORG_JSONLD] + (extra_jsonld or [])
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{description}">
<link rel="canonical" href="{canonical_url}">
<meta name="theme-color" content="#8A3F1F">
<link rel="icon" href="images/favicon.png" type="image/png">

<meta property="og:type" content="website">
<meta property="og:site_name" content="WellBeing Psychotherapy">
<meta property="og:locale" content="en_CA">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{description}">
<meta property="og:url" content="{canonical_url}">
<meta property="og:image" content="{og_image_url}">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{title}">
<meta name="twitter:description" content="{description}">
<meta name="twitter:image" content="{og_image_url}">

<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Source+Serif+4:opsz,wght@8..60,400;8..60,500;8..60,600;8..60,700&family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="css/style.css">

{jsonld_script(*jsonld_objs)}
</head>"""

def header(active):
    desktop_links = "\n        ".join(
        f'<a href="{href}" class="nav-link" data-nav="{key}">{label}</a>'
        for key, href, label in NAV_ITEMS
    )
    mobile_links = "\n        ".join(
        f'<a href="{href}" class="nav-mobile-link" data-nav="{key}">{label}</a>'
        for key, href, label in NAV_ITEMS
    )
    return f"""<header class="site-header">
  <div class="container">
    <div class="header-row">
      <a href="index.html" class="brand" aria-label="WellBeing Psychotherapy — Home">
        <img class="logo-mark" src="images/logo.png" alt="WellBeing Psychotherapy logo">
        <span class="wordmark">WellBeing<br>Psychotherapy</span>
      </a>
      <nav class="nav-desktop" aria-label="Primary">
        {desktop_links}
        <a {JANE_ATTRS} class="btn-nav">Book Now</a>
      </nav>
      <button class="hamburger" aria-label="Menu" aria-expanded="false">☰</button>
    </div>
    <nav class="nav-mobile" aria-label="Primary mobile">
      {mobile_links}
      <a {JANE_ATTRS} class="btn-nav-mobile">Book Now</a>
    </nav>
  </div>
</header>"""

FOOTER = f"""<footer class="site-footer">
  <div class="container">
    <div class="footer-grid">
      <div class="footer-brand">
        <img class="logo-mark" src="images/logo.png" alt="WellBeing Psychotherapy logo">
        <span class="wordmark">WellBeing<br>Psychotherapy</span>
      </div>
      <div class="footer-col">
        <h3 class="footer-h">Book Now</h3>
        <p>Click <a {JANE_ATTRS}>here</a> to book a session or your free 15 minute consultation.</p>
      </div>
      <div class="footer-col">
        <h3 class="footer-h">Connect With Us</h3>
        <div><a href="mailto:yasmin.singh@wellbeingwellness.ca">yasmin.singh@wellbeingwellness.ca</a></div>
        <div><a href="tel:+14377473941">437-747-3941</a></div>
      </div>
    </div>
  </div>
  <div class="footer-bottom">© 2026 WellBeing Psychotherapy. All rights reserved.</div>
</footer>"""

def page(filename, title, description, active, body_attrs, main_html, og_image="images/hero.jpg", extra_jsonld=None):
    html = f"""{head(title, description, filename, og_image=og_image, extra_jsonld=extra_jsonld)}
<body data-page="{active}"{body_attrs}>

{header(active)}

{main_html}

{FOOTER}

<script src="js/main.js"></script>
</body>
</html>
"""
    with open(os.path.join(ROOT, filename), "w") as f:
        f.write(html)
    print("wrote", filename)


# ---------------------------------------------------------------------------
# HOME
# ---------------------------------------------------------------------------
home_main = f"""<main>
<section class="hero">
  <div class="container hero-grid">
    <div class="hero-text">
      <h1>Because every being deserves mental wellness</h1>
      <p class="subhead">Compassionate, one-on-one virtual therapy with a Registered Psychotherapist. A safe, confidential space to be heard and supported.</p>
      <div class="hero-actions">
        <a {JANE_ATTRS} class="btn">Book Now</a>
        <a href="about.html" class="btn-ghost">Learn More</a>
      </div>
    </div>
    <div class="hero-image">
      <img class="hero-photo" src="images/hero.jpg" alt="WellBeing Psychotherapy — interior / clinician photo">
    </div>
  </div>
</section>

<section class="cta-band">
  <div class="container cta-band-inner">
    <h2 class="h2 md">Making the move for your mental health</h2>
    <p>Too often, mental health is overlooked — by others, and sometimes by ourselves. At WellBeing, we believe your mental health is the foundation of a full, meaningful life. You are not alone, and you don't have to face it alone.</p>
    <p>Your mental wellness matters. Let's take the first step together.</p>
    <a href="about.html" class="btn">Learn More</a>
  </div>
</section>

<section class="features">
  <div class="container features-grid">
    <div class="feature-card">
      <img class="feature-photo" src="images/feature-1.jpg" alt="Understanding Therapy">
      <h3 class="h3">Understanding Therapy</h3>
      <p>Therapy is a safe and confidential space guided by a trained mental health professional — a space where you can feel truly heard, understood, and supported.</p>
    </div>
    <div class="feature-card">
      <img class="feature-photo" src="images/feature-2.jpg" alt="Answering Questions">
      <h3 class="h3">Answering Questions</h3>
      <p>Whether you're starting therapy for the first time or continuing your journey, it's completely normal to have questions.</p>
    </div>
    <div class="feature-card">
      <img class="feature-photo" src="images/feature-3.jpg" alt="Learning More">
      <h3 class="h3">Learning More</h3>
      <p>Stay informed, curious and connected. From everyday topics to deeper reflections, support your journey your way.</p>
    </div>
  </div>
</section>
</main>"""

page("index.html", "WellBeing Psychotherapy | Virtual Therapy in the Greater Toronto Area",
     "Compassionate, one-on-one virtual therapy with a Registered Psychotherapist, serving individuals across the Greater Toronto Area with culturally responsive, affirming care. A safe, confidential space to be heard and supported.",
     "home", "", home_main, og_image="images/hero.jpg")

# ---------------------------------------------------------------------------
# ABOUT
# ---------------------------------------------------------------------------
about_main = """<main>
<section class="about-section">
  <div class="container about-inner">
    <h2 class="h2">About WellBeing</h2>
    <p>At WellBeing, therapy is more than a service — it's a space of wellness, comfort, and safety. Our environment is designed to help you feel at ease as you explore your thoughts, emotions, and experiences. Each session is guided by a trained and compassionate mental health professional who works with your needs. Whether you're just beginning or continuing your journey, WellBeing is here to support your healing and growth — every step of the way.</p>
    <h2 class="h2">About Therapy</h2>
    <p>Therapy is a safe and confidential space where you can explore your experiences, thoughts, and emotions without judgment. Therapy offers support, insight, and tools to help you navigate challenges and grow. Sessions can be tailored to address specific concerns or focus on overall personal development. It's a space where you can feel truly heard, understood, and supported.</p>
  </div>
</section>
</main>"""

page("about.html", "About Us | WellBeing Psychotherapy — GTA Virtual Therapy",
     "Learn about WellBeing Psychotherapy, a virtual therapy practice serving the Greater Toronto Area and Ontario with a culturally responsive, affirming approach to mental wellness.",
     "about", "", about_main, og_image="images/hero.jpg")

# ---------------------------------------------------------------------------
# TEAM
# ---------------------------------------------------------------------------
team_main = f"""<main>
<section class="team-section">
  <div>
    <img class="team-photo" src="images/team-yasmin.jpg" alt="Yasmin Singh, Registered Psychotherapist">
    <div class="team-name">Yasmin Singh</div>
    <div class="team-title">Registered Psychotherapist</div>
  </div>
  <div class="team-bio">
    <h2 class="h2 left">Meet The Team</h2>
    <p>Yasmin Singh is a Registered Psychotherapist with the College of Registered Psychotherapists of Ontario (CRPO). She holds a Master's degree in Counselling Psychology with a concentration in Health from the Chicago School of Professional Psychology.</p>
    <p>Yasmin brings a diverse range of experience to her practice, including one-on-one psychotherapy at Concordia University's Counselling Centre, a Disability Case Manager, and grief therapy for end-of-life support to families. Additionally, she has held positions at various private clinics in Ontario. She has worked with individuals across a wide range of ages, backgrounds, sexual orientations, genders, and abilities.</p>
    <p>Her clinical focus includes supporting clients with depression, anxiety, self-esteem, ADHD, relationship concerns, goal development, relationships, and change/adjustment. Yasmin works collaboratively with each client to create personalized treatment plans rooted in health, care, and practical coping tools.</p>
    <p>As a South Asian woman, Yasmin is especially attuned to the stigma surrounding mental health and the barriers to culturally responsive care. She is passionate about creating a safe, affirming, and culturally aware space for all her clients.</p>
    <a {JANE_ATTRS} class="btn">Book With Yasmin</a>
  </div>
</section>
</main>"""

page("team.html", "Meet Yasmin Singh, RP | WellBeing Psychotherapy",
     "Meet Yasmin Singh, a Registered Psychotherapist (CRPO) serving the Greater Toronto Area. As a South Asian woman, Yasmin offers culturally responsive, affirming care to clients from all backgrounds.",
     "team", "", team_main, og_image="images/team-yasmin.jpg", extra_jsonld=[PERSON_JSONLD])

# ---------------------------------------------------------------------------
# FAQ
# ---------------------------------------------------------------------------
faq_data = [
    ("How do I know when to see a Therapist?",
     "<p>There is not always a \"right\" moment to start therapy, and you don't need to be in crisis to seek support. Many people reach out when they begin to notice things like:</p>"
     "<ul><li>You don't feel like yourself</li><li>Your emotions feel overwhelming or out of control</li><li>Others have noticed a change in you</li>"
     "<li>You want to talk to someone, but don't know who to turn to</li><li>You find yourself constantly adjusting your life to accommodate your feelings</li>"
     "<li>You're simply feeling curious about what therapy could offer you</li></ul>"
     "<p>Therapy can be a powerful space for support, self-reflection, and growth—whether you're struggling or simply ready to explore. If something doesn't feel quite right, it's okay to reach out. We're here when you're ready.</p>",
     True),
    ("How do I know a Therapist is right for me?",
     "<p>Finding the right therapist is an important part of the therapeutic process. A good fit can make all the difference in how supported and empowered you feel. Here are some signs that a therapist may be the right match for you:</p>"
     "<ul><li>You feel safe, comfortable, and respected in their presence</li><li>You feel heard, understood, and validated</li><li>There is a sense of trust and good rapport</li>"
     "<li>They promote your autonomy and involve you in your treatment</li><li>They take the time to educate themselves about your lived experience or background</li>"
     "<li>They know when to challenge you in healthy, growth-oriented ways</li><li>They're willing to go at your pace, not rush your process</li></ul>"
     "<p>Remember, therapy is a collaborative relationship. It's okay to ask questions, try a few sessions, or even explore other options if something doesn't feel right. You deserve a therapist who truly aligns with your needs. A 15 minute consultation can be a great way to start learning about a therapist's style.</p>",
     False),
    ("What can I expect in my first session?",
     "<p>Your first therapy session is a gentle introduction to the process. It typically lasts 50 minutes and is often an intake appointment—a chance for your therapist to get to know you better.</p>"
     "<p>You'll be invited to share at your own pace and comfort level; there's no pressure to disclose anything you're not ready to. Your therapist may ask questions to understand your concerns, background, and goals for therapy.</p>"
     "<p>Together, you'll begin to discuss a treatment plan and decide what your journey may look like moving forward. At the end of the session, you'll have the option to book a follow-up appointment and continue building a path toward your well-being.</p>",
     False),
    ("How do I prepare for my first session?",
     "<p>It's normal to feel a little nervous before your first therapy session. To help you feel more prepared, you might consider writing down any specific topics, concerns, or questions you'd like to explore. Your therapist will guide the session at your pace, creating a space where you can begin to share your thoughts and emotions freely and safely.</p>"
     "<p>Therapy is a process, and it's okay if things don't unfold all at once. Trusting the journey and showing up as you are is more than enough for your first step.</p>",
     False),
    ("Can I do sessions virtually?",
     "<p>Yes! At this time, all sessions are offered virtually only.</p>"
     "<p>We use a secure, confidential platform that supports video sessions, chat features, and screen sharing to make it easy and safe to connect with you. Virtual therapy offers flexibility while still ensuring the same level of support, care, and professionalism you'd expect in person.</p>",
     False),
    ("How do I prepare for a virtual session?",
     "<p>Preparing for your virtual therapy session can help you feel more focused and comfortable. Here are a few helpful tips:</p>"
     "<ul><li>Find a quiet, private space where you feel safe and free from interruptions—this could be your home, bedroom, car, private office, backyard, or even a cozy closet.</li>"
     "<li>Log in a few minutes early to ensure your video is working and your internet connection is stable.</li>"
     "<li>Have anything you might need close by: water, tissues, tea, coffee, or something comforting.</li>"
     "<li>Keep a notebook and pen handy in case you want to jot down thoughts, insights, or anything you'd like to revisit later.</li></ul>",
     False),
]

faq_items_html = ""
for i, (q, a, open_default) in enumerate(faq_data):
    open_class = " open" if open_default else ""
    icon = "−" if open_default else "+"
    faq_items_html += f"""      <div class="faq-item{open_class}">
        <button class="faq-row" aria-expanded="{'true' if open_default else 'false'}">
          <span class="faq-q">{q}</span>
          <span class="faq-icon">{icon}</span>
        </button>
        <div class="faq-answer">
{a}
        </div>
      </div>
"""

faq_main = f"""<main>
<section class="faq-head">
  <div class="container">
    <h2 class="h2 lg">Frequently Asked Questions</h2>
  </div>
</section>
<section class="faq-list-section">
  <div class="container faq-list">
{faq_items_html}  </div>
</section>
</main>"""

page("faq.html", "FAQ | WellBeing Psychotherapy — Virtual Therapy, GTA",
     "Answers to common questions about starting virtual therapy, what to expect in your first session, and how to prepare — for clients across the Greater Toronto Area.",
     "faq", "", faq_main, og_image="images/hero.jpg")

# ---------------------------------------------------------------------------
# CONTACT
# ---------------------------------------------------------------------------
contact_main = """<main>
<section class="contact-section">
  <div class="container contact-inner">
    <h2 class="h2">Contact Us</h2>

    <a class="contact-row" href="tel:+14377473941">
      <span class="contact-icon" aria-hidden="true">
        <svg viewBox="0 0 24 24"><path d="M6.6 10.8c1.4 2.8 3.8 5.1 6.6 6.6l2.2-2.2c.3-.3.7-.4 1-.2 1.1.4 2.3.6 3.6.6.6 0 1 .4 1 1V20c0 .6-.4 1-1 1C10.6 21 3 13.4 3 4c0-.6.4-1 1-1h3.5c.6 0 1 .4 1 1 0 1.2.2 2.5.6 3.6.1.4 0 .8-.3 1.1L6.6 10.8z"></path></svg>
      </span>
      <span class="contact-text">437-747-3941</span>
    </a>

    <a class="contact-row" href="mailto:yasmin.singh@wellbeingwellness.ca">
      <span class="contact-icon" aria-hidden="true">
        <svg viewBox="0 0 24 24"><path d="M2 5c0-.6.4-1 1-1h18c.6 0 1 .4 1 1v14c0 .6-.4 1-1 1H3c-.6 0-1-.4-1-1V5zm2.2.5L12 12l7.8-6.5H4.2z"></path></svg>
      </span>
      <span class="contact-text">yasmin.singh@wellbeingwellness.ca</span>
    </a>

    <a class="contact-row" href="https://www.instagram.com/well_being_wellness/" target="_blank" rel="noopener">
      <span class="contact-icon" aria-hidden="true">
        <svg viewBox="0 0 24 24"><path d="M9 3h6l1 2h3a2 2 0 0 1 2 2v10a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V7a2 2 0 0 1 2-2h3l1-2zm3 5a4.5 4.5 0 1 0 0 9 4.5 4.5 0 0 0 0-9z"></path></svg>
      </span>
      <span class="contact-text">well_being_wellness</span>
    </a>

  </div>
</section>
</main>"""

page("contact.html", "Contact | WellBeing Psychotherapy — GTA Virtual Therapy",
     "Get in touch with WellBeing Psychotherapy by phone, email, or Instagram — serving clients virtually across the Greater Toronto Area.",
     "contact", "", contact_main, og_image="images/hero.jpg")

# ---------------------------------------------------------------------------
# BOOK NOW
# ---------------------------------------------------------------------------
book_main = """<main>
<section class="book-section">
  <div class="container book-inner">
    <h2 class="h2 lg">Book Your Session Now</h2>
    <div class="book-intro">
      <p>Whether it's your first session, a consultation, your first time with WellBeing, or you're a returning client — we're glad you're here.</p>
      <p>Click below to book your appointment and take a meaningful step towards your wellness.</p>
    </div>
    <a href="https://yrspsychotherapy.janeapp.com/#staff_member/1" class="btn" id="book-now-cta" target="_blank" rel="noopener">Book Now</a>
    <p class="book-closing">This is for you — thank yourself for showing up.</p>
  </div>
</section>
</main>"""

page("book.html", "Book Now | WellBeing Psychotherapy — GTA Virtual Therapy",
     "Book your virtual therapy session or free 15-minute consultation with WellBeing Psychotherapy, serving the Greater Toronto Area.",
     "book", "", book_main, og_image="images/hero.jpg")

print("\n6 pages generated.")

# ---------------------------------------------------------------------------
# robots.txt
# ---------------------------------------------------------------------------
robots_txt = f"""User-agent: *
Allow: /

Sitemap: {SITE_URL}/sitemap.xml
"""
with open(os.path.join(ROOT, "robots.txt"), "w") as f:
    f.write(robots_txt)
print("wrote robots.txt")

# ---------------------------------------------------------------------------
# sitemap.xml
# ---------------------------------------------------------------------------
import datetime
LASTMOD = datetime.date.today().isoformat()

sitemap_entries = {
    "index.html": "1.0",
    "about.html": "0.8",
    "team.html": "0.8",
    "faq.html": "0.7",
    "contact.html": "0.7",
    "book.html": "0.9",
}

urls_xml = "\n".join(
    f"""  <url>
    <loc>{SITE_URL}/{fname}</loc>
    <lastmod>{LASTMOD}</lastmod>
    <changefreq>monthly</changefreq>
    <priority>{priority}</priority>
  </url>"""
    for fname, priority in sitemap_entries.items()
)

sitemap_xml = f"""<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
{urls_xml}
</urlset>
"""
with open(os.path.join(ROOT, "sitemap.xml"), "w") as f:
    f.write(sitemap_xml)
print("wrote sitemap.xml")

print("\nDone.")
