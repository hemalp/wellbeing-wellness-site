# WellBeing Psychotherapy — Website

A plain static HTML/CSS/JS site (no build step, no server-side code) recreating the
design handoff. Upload the files as-is to any standard web host, including Namecheap
shared hosting.

## What's in this folder

```
index.html          Home
about.html           About
team.html            Team
faq.html              FAQ
contact.html         Contact
book.html             Book Now
css/style.css        All styling (colors, type, spacing — one file to edit)
js/main.js             Mobile menu, FAQ accordion, active-nav highlighting
images/                Placeholder photos — replace these (see below)
robots.txt              Tells search engines they can crawl the whole site + points to the sitemap
sitemap.xml             Lists all 6 pages for search engines
build.py                Dev-only script that generated the HTML pages. Not needed to host the site — ignore it (or delete it) when you deploy.
generate_placeholders.py  Dev-only script that generated the placeholder images. Also safe to ignore/delete when you deploy.
```

## 1. Drop in your real images

Every photo on the site is a placeholder right now, tinted in the brand colors and
labeled with what it's for. Replace each file **using the exact same filename** and
every page updates automatically — no HTML editing required.

| Replace this file          | With                                             | Used on              |
|-----------------------------|---------------------------------------------------|-----------------------|
| `images/logo.png`           | Your circular logo mark (square image is fine — it's cropped to a circle) | Header + footer, all pages |
| `images/favicon.png`        | A small square version of your logo (browser tab icon) | All pages |
| `images/hero.jpg`           | Interior or clinician photo (portrait-ish works best) | Home hero |
| `images/feature-1.jpg`      | Photo for "Understanding Therapy" card            | Home |
| `images/feature-2.jpg`      | Photo for "Answering Questions" card               | Home |
| `images/feature-3.jpg`      | Photo for "Learning More" card                      | Home |
| `images/team-yasmin.jpg`    | Photo of Yasmin Singh                              | Team |

Notes:
- Any image size/aspect ratio works — the CSS crops photos to fit (`object-fit: cover`), so just drop in reasonably high-res photos and they'll fill their frames nicely.
- Keep photos web-optimized (roughly under ~500KB each) so pages load quickly. Any image editor or a free tool like squoosh.app can compress them.
- `.jpg` or `.png` both work — if you use a different file type, just update the filename reference in the relevant `<img src="...">` tag in the HTML, or rename your file to match.

## 2. One thing worth double-checking

- **Instagram link** (`contact.html`): currently points to
  `https://www.instagram.com/well_being_wellness/` — double check this is the correct
  profile URL and update it in `contact.html` if not.

Every "Book Now" element site-wide — the nav pill (desktop + mobile, every page),
the home hero button, the footer's "here" link, the Team page's "Book With Yasmin"
button, and the Book page's own button — links directly to the Jane App booking page
(`https://yrspsychotherapy.janeapp.com/#staff_member/1`) and opens in a new tab. The
standalone `book.html` page still exists (with its intro copy and closing line) but
isn't linked from anywhere in the nav anymore, by design, since all booking clicks now
skip straight to Jane App. If you'd rather link back to it from somewhere (e.g. an
"About booking" mention), just point that link's `href` at `book.html`.

Everything else (phone `tel:` link, email `mailto:` link, all page nav links) is
already wired up.

## 3. Deploying to Namecheap

You don't need to build or compile anything — just upload the files.

**Option A — cPanel File Manager (easiest, no extra tools needed)**
1. Log in to Namecheap → Hosting → **cPanel**.
2. Open **File Manager**, and navigate into `public_html` (this is the folder your domain points to). If you're publishing this as a subfolder/subdomain instead, navigate there.
3. Click **Upload**, and upload every file and folder from this project (`index.html`, `about.html`, etc., plus the `css`, `js`, and `images` folders) — keeping the same folder structure.
4. Once uploaded, visit your domain in a browser — the site should load at `yourdomain.com/index.html` (and most hosts, including Namecheap, serve `index.html` automatically at `yourdomain.com/`).

**Option B — FTP (if you prefer an FTP client like FileZilla)**
1. In cPanel, find your FTP credentials (or create an FTP account) under **FTP Accounts**.
2. Connect with FileZilla (or any FTP client) using those credentials.
3. Drag the contents of this folder into `public_html` on the server, preserving the folder structure.

That's it — there's no database, no server-side code, and no build process, so once the
files are uploaded the site is live.

## 4. SEO — what's already set up

- **`robots.txt`** — allows all search engines to crawl the site and points to the sitemap.
- **`sitemap.xml`** — lists all 6 pages so Google/Bing can find them quickly.
- **Canonical URLs + Open Graph/Twitter tags** — every page has a proper `<title>`,
  meta description, canonical link, and social-preview tags (so links shared on
  Facebook/Instagram/iMessage/etc. show a nice title, description, and photo).
- **Structured data (JSON-LD)** — every page includes `MedicalBusiness` schema (name,
  phone, email, Instagram, service area), and the Team page additionally includes
  `Person` schema for Yasmin. This helps Google understand what the practice is and
  who provides care, which can surface richer results in search.
- **Locality + community focus** — since the practice serves the Greater Toronto Area
  and Yasmin's bio already speaks to her attunement to South Asian clients' experience
  of stigma and culturally responsive care, the meta titles/descriptions and
  structured data reflect that (e.g. "serving the Greater Toronto Area," "culturally
  responsive care"). This is pulled directly from content already on the Team page —
  nothing new was invented. If you want to lean into this further (e.g. a dedicated
  line on the homepage, or "South Asian" more prominently in page titles), that's a
  content decision worth confirming with Yasmin, since it's more visible than metadata.

**One important assumption:** all of the above (`sitemap.xml`, canonical URLs, Open
Graph image URLs, structured data) uses the domain `https://www.wellbeingwellness.ca`,
taken from the practice's existing site. If the real launch domain is different, open
`build.py`, change the `SITE_URL` constant near the top, and re-run `python3 build.py`
— that regenerates every page with the correct domain everywhere. (If you'd rather not
touch Python, you can instead find-and-replace `https://www.wellbeingwellness.ca`
across all `.html`/`.xml`/`.txt` files directly.)

**After launch:** submit `sitemap.xml` in Google Search Console and Bing Webmaster
Tools (both are free) — that's what actually gets the site indexed quickly, rather
than waiting for search engines to discover it on their own.

## 5. Customizing colors later

All brand colors live as CSS variables at the top of `css/style.css` (look for `:root {`).
Changing `--accent` there updates the terracotta color everywhere on the site at once.
The design handoff noted a few alternate options if you ever want to try a different
brand color: `#7A6A4F` (olive-tan), `#5F6B4A` (sage), `#6B4E71` (plum).

## Notes carried over from the design handoff

- Content max-width is 1300px, centered, with 40px side padding (20px on mobile).
- Mobile breakpoint is 860px — below that, the header collapses to a hamburger menu and
  multi-column layouts stack to one column.
- The FAQ's first question is open by default; each question toggles independently.
- Real, separate page URLs are used (`about.html`, `faq.html`, etc.) rather than a
  single-page app, per the handoff's recommendation for SEO and back-button support.
