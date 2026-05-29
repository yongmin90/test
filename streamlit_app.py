from pathlib import Path
import base64

import streamlit as st


BASE_DIR = Path(__file__).parent
ASSET_DIR = BASE_DIR / "assets" / "official"


st.set_page_config(
    page_title="ATEC Official USA",
    page_icon="A",
    layout="wide",
    initial_sidebar_state="collapsed",
)


def asset(name: str) -> str:
    return str(ASSET_DIR / name)


def image_data(name: str) -> str:
    path = ASSET_DIR / name
    suffix = path.suffix.lower()
    mime = "image/jpeg" if suffix in {".jpg", ".jpeg"} else "image/png"
    encoded = base64.b64encode(path.read_bytes()).decode("ascii")
    return f"data:{mime};base64,{encoded}"


st.markdown(
    """
    <style>
      :root {
        --ink: #121827;
        --muted: #5c6678;
        --line: #dce2ea;
        --navy: #163a63;
        --blue: #1f6fb2;
        --red: #c7352f;
        --soft: #f5f7fa;
      }

      .block-container {
        max-width: 1440px;
        padding-top: 1rem;
        padding-bottom: 0;
      }

      [data-testid="stHeader"] {
        background: rgba(255, 255, 255, 0.88);
      }

      h1, h2, h3, p {
        letter-spacing: 0;
      }

      .topbar {
        position: sticky;
        top: 0;
        z-index: 10;
        display: flex;
        align-items: center;
        justify-content: space-between;
        gap: 28px;
        padding: 14px 0 18px;
        background: rgba(255,255,255,0.94);
        border-bottom: 1px solid var(--line);
        backdrop-filter: blur(12px);
      }

      .brand {
        display: flex;
        align-items: center;
        gap: 12px;
        min-width: 180px;
      }

      .brand img {
        width: 116px;
      }

      .brand span {
        color: var(--muted);
        font-size: 11px;
        font-weight: 800;
        text-transform: uppercase;
      }

      .nav {
        display: flex;
        flex-wrap: wrap;
        justify-content: center;
        gap: 20px;
        color: #273349;
        font-size: 14px;
        font-weight: 800;
      }

      .cta {
        display: inline-flex;
        align-items: center;
        justify-content: center;
        min-height: 42px;
        padding: 0 18px;
        color: #fff !important;
        background: var(--red);
        border-radius: 6px;
        font-weight: 900;
        text-decoration: none !important;
        white-space: nowrap;
      }

      .hero {
        display: grid;
        grid-template-columns: minmax(320px, 0.88fr) minmax(440px, 1.12fr);
        gap: 0;
        min-height: 680px;
        margin-top: 12px;
        background: linear-gradient(90deg, #f7f9fc 0%, #ffffff 46%, #edf2f7 100%);
      }

      .hero-copy {
        display: flex;
        flex-direction: column;
        justify-content: center;
        padding: 70px 48px;
      }

      .eyebrow {
        margin-bottom: 12px;
        color: var(--blue);
        font-size: 12px;
        font-weight: 900;
        text-transform: uppercase;
      }

      .hero h1 {
        margin-bottom: 22px;
        color: var(--ink);
        font-size: clamp(42px, 5vw, 70px);
        line-height: 0.98;
        font-weight: 900;
      }

      .hero p {
        color: var(--muted);
        font-size: 18px;
      }

      .hero-actions {
        display: flex;
        flex-wrap: wrap;
        gap: 12px;
        margin-top: 18px;
      }

      .button-secondary {
        display: inline-flex;
        align-items: center;
        justify-content: center;
        min-height: 42px;
        padding: 0 18px;
        color: var(--navy) !important;
        background: #fff;
        border: 1px solid var(--line);
        border-radius: 6px;
        font-weight: 900;
        text-decoration: none !important;
      }

      .hero-image {
        min-height: 560px;
        background-image:
          linear-gradient(90deg, rgba(255,255,255,0.82), rgba(255,255,255,0.05) 30%, rgba(255,255,255,0)),
          url("app/static-placeholder");
        background-size: cover;
        background-position: center;
      }

      .official-band {
        display: grid;
        grid-template-columns: 0.9fr 1.1fr;
        gap: 36px;
        padding: 46px 42px;
        color: #fff;
        background: #12243d;
      }

      .official-band p {
        color: #dbe8f5;
        font-size: 17px;
      }

      .section-title {
        margin-top: 72px;
        margin-bottom: 22px;
      }

      .section-title h2 {
        color: var(--ink);
        font-size: clamp(30px, 3.4vw, 46px);
        line-height: 1.05;
        font-weight: 900;
      }

      .section-title p {
        color: var(--muted);
        font-size: 17px;
      }

      .cards {
        display: grid;
        grid-template-columns: repeat(4, minmax(0, 1fr));
        gap: 18px;
      }

      .card {
        overflow: hidden;
        min-height: 330px;
        background: #fff;
        border: 1px solid var(--line);
        border-top: 5px solid var(--blue);
        border-radius: 8px;
        box-shadow: 0 10px 28px rgba(18,24,39,0.06);
      }

      .card.red { border-top-color: var(--red); }
      .card.gray { border-top-color: #6b7888; }
      .card.green { border-top-color: #26745f; }

      .card img {
        width: 100%;
        height: 132px;
        object-fit: cover;
      }

      .card-body {
        padding: 24px;
      }

      .card h3 {
        margin-bottom: 10px;
        color: var(--ink);
        font-size: 22px;
        font-weight: 900;
      }

      .card p {
        color: var(--muted);
      }

      .product-grid {
        display: grid;
        grid-template-columns: repeat(5, minmax(0, 1fr));
        gap: 14px;
      }

      .product {
        overflow: hidden;
        background: #fff;
        border: 1px solid var(--line);
        border-radius: 8px;
      }

      .product .image-wrap {
        display: flex;
        align-items: center;
        justify-content: center;
        height: 230px;
        background: #f8fafc;
      }

      .product img {
        max-width: 100%;
        max-height: 100%;
        padding: 18px;
        object-fit: contain;
      }

      .product-body {
        padding: 18px;
        border-top: 1px solid var(--line);
      }

      .product-body p {
        margin-bottom: 6px;
        color: var(--blue);
        font-size: 12px;
        font-weight: 900;
        text-transform: uppercase;
      }

      .product-body h3 {
        margin: 0;
        color: var(--ink);
        font-weight: 900;
      }

      .dark-section {
        margin-top: 76px;
        padding: 66px 42px;
        color: #fff;
        background: linear-gradient(rgba(18,24,39,0.94), rgba(18,24,39,0.94));
        border-radius: 0;
      }

      .tech-grid {
        display: grid;
        grid-template-columns: repeat(4, minmax(0, 1fr));
        gap: 16px;
      }

      .tech-card {
        min-height: 190px;
        padding: 24px;
        border: 1px solid rgba(255,255,255,0.2);
        border-radius: 8px;
        background: rgba(255,255,255,0.08);
      }

      .tech-card p {
        color: #d2d9e4;
      }

      .contact {
        display: grid;
        grid-template-columns: 0.9fr 1.1fr;
        gap: 48px;
        margin-top: 76px;
        padding: 70px 42px;
        color: #fff;
        background: linear-gradient(120deg, #12243d, #173f6c);
      }

      .contact p {
        color: #d7e7f6;
      }

      .footer {
        display: flex;
        justify-content: space-between;
        align-items: center;
        gap: 20px;
        margin-top: 0;
        padding: 26px 0;
        color: #d3deea;
        background: #0c1727;
      }

      .footer-inner {
        width: 100%;
        padding: 0 42px;
      }

      .footer img {
        width: 82px;
        filter: brightness(0) invert(1);
        vertical-align: middle;
        margin-right: 12px;
      }

      @media (max-width: 1100px) {
        .topbar,
        .hero,
        .official-band,
        .contact {
          grid-template-columns: 1fr;
        }

        .topbar {
          align-items: flex-start;
          flex-direction: column;
        }

        .cards,
        .tech-grid,
        .product-grid {
          grid-template-columns: repeat(2, minmax(0, 1fr));
        }
      }

      @media (max-width: 720px) {
        .hero-copy,
        .official-band,
        .dark-section,
        .contact,
        .footer-inner {
          padding-left: 20px;
          padding-right: 20px;
        }

        .hero {
          min-height: 0;
        }

        .hero h1 {
          font-size: 42px;
        }

        .cards,
        .tech-grid,
        .product-grid {
          grid-template-columns: 1fr;
        }
      }
    </style>
    """,
    unsafe_allow_html=True,
)


st.markdown(
    f"""
    <div class="topbar">
      <div class="brand">
        <img src="{image_data("atec-logo.png")}" alt="ATEC" />
        <span>Official USA</span>
      </div>
      <div class="nav">
        <span>Solutions</span>
        <span>Products</span>
        <span>Technology</span>
        <span>Industries</span>
        <span>Company</span>
        <span>Resources</span>
        <span>Support</span>
      </div>
      <a class="cta" href="#contact">Contact ATEC</a>
    </div>
    """,
    unsafe_allow_html=True,
)


left, right = st.columns([0.9, 1.1], gap="large")
with left:
    st.markdown(
        """
        <div class="hero-copy">
          <div class="eyebrow">ATEC official platform for the U.S. market</div>
          <h1>Global cash automation technology for American financial and retail operations.</h1>
          <p>
            A manufacturer-led gateway for U.S. institutions, retailers, and strategic partners looking for reliable
            ATM, cash recycling, kiosk, and branch transformation solutions.
          </p>
          <div class="hero-actions">
            <a class="cta" href="#solutions">Explore Solutions</a>
            <a class="button-secondary" href="#contact">Request Consultation</a>
          </div>
        </div>
        """,
        unsafe_allow_html=True,
    )
with right:
    st.image(asset("main-hero-financial.jpg"), use_container_width=True)


st.markdown(
    """
    <div class="official-band">
      <div>
        <div class="eyebrow">Official distinction</div>
        <h2>Built as the manufacturer-owned U.S. presence.</h2>
      </div>
      <p>
        This site positions ATEC directly for U.S. customers, partners, and institutions. The tone is official,
        engineering-led, and designed to separate corporate representation from reseller or distributor websites.
      </p>
    </div>
    """,
    unsafe_allow_html=True,
)


st.markdown(
    """
    <div class="section-title" id="solutions">
      <div class="eyebrow">Solutions</div>
      <h2>Designed around U.S. operational needs.</h2>
      <p>Visitors can start with their business goal instead of hunting through product model numbers.</p>
    </div>
    """,
    unsafe_allow_html=True,
)

solution_cards = [
    ("solution-financial.jpg", "Financial Automation", "ATM, cash recycling, and teller automation for banks and credit unions.", ""),
    ("solution-retail.jpg", "Retail Cash Automation", "Cash handling, recycling, and reconciliation workflows for high-volume retail sites.", "red"),
    ("solution-overseas.jpg", "Self-Service Kiosk Solutions", "Configurable kiosks for secure transactions and customer service.", "gray"),
    ("main-hero-retail.jpg", "Branch Transformation", "Technology strategy for lower wait times, stronger controls, and staff productivity.", "green"),
]

st.markdown('<div class="cards">', unsafe_allow_html=True)
for image, title, body, tone in solution_cards:
    st.markdown(
        f"""
        <div class="card {tone}">
          <img src="{image_data(image)}" alt="{title}" />
          <div class="card-body">
            <h3>{title}</h3>
            <p>{body}</p>
          </div>
        </div>
        """,
        unsafe_allow_html=True,
    )
st.markdown("</div>", unsafe_allow_html=True)


st.markdown(
    """
    <div class="section-title">
      <div class="eyebrow">Products</div>
      <h2>Official ATEC product imagery from the Korean corporate website.</h2>
      <p>Product naming and categories are adapted for a U.S. official-market interface.</p>
    </div>
    """,
    unsafe_allow_html=True,
)

products = [
    ("product-lc96.png", "STM", "LC96"),
    ("product-dd01.png", "KIOSK", "DD01"),
    ("product-rc95.png", "Retail Cash Automation", "RC95"),
    ("product-lta100.png", "TCR", "LTA-100"),
    ("product-lc71a.png", "KIOSK", "LC71A"),
]

st.markdown('<div class="product-grid">', unsafe_allow_html=True)
for image, category, name in products:
    st.markdown(
        f"""
        <div class="product">
          <div class="image-wrap"><img src="{image_data(image)}" alt="ATEC {name}" /></div>
          <div class="product-body">
            <p>{category}</p>
            <h3>{name}</h3>
          </div>
        </div>
        """,
        unsafe_allow_html=True,
    )
st.markdown("</div>", unsafe_allow_html=True)


st.markdown(
    """
    <div class="dark-section">
      <div class="eyebrow">Technology</div>
      <h2>Manufacturer-grade engineering signals.</h2>
      <div class="tech-grid">
        <div class="tech-card">
          <h3>Cash Recycling</h3>
          <p>Reduce idle cash, teller touches, and armored service dependency with recycling-first workflows.</p>
        </div>
        <div class="tech-card">
          <h3>Security Architecture</h3>
          <p>Support controlled access, transaction integrity, and enterprise-grade operational oversight.</p>
        </div>
        <div class="tech-card">
          <h3>Remote Monitoring</h3>
          <p>Service visibility for uptime planning, proactive maintenance, and fleet management.</p>
        </div>
        <div class="tech-card">
          <h3>Accessible UI</h3>
          <p>Interface planning for American users, compliance expectations, and clear self-service flows.</p>
        </div>
      </div>
    </div>
    """,
    unsafe_allow_html=True,
)


st.markdown(
    """
    <div class="contact" id="contact">
      <div>
        <div class="eyebrow">U.S. inquiry</div>
        <h2>Talk with ATEC about the official U.S. market channel.</h2>
        <p>Route visitors by inquiry type so sales, partnership, and support requests do not blend together.</p>
      </div>
      <div>
    """,
    unsafe_allow_html=True,
)

with st.form("contact_form"):
    inquiry_type = st.selectbox(
        "Inquiry Type",
        ["Sales Inquiry", "Partnership Inquiry", "Technical Support", "Media / Corporate"],
    )
    email = st.text_input("Work Email", placeholder="name@company.com")
    company = st.text_input("Company", placeholder="Company name")
    message = st.text_area("Message", placeholder="Tell us about your project or business need")
    submitted = st.form_submit_button("Request Official Consultation")

if submitted:
    st.success(f"Prototype form submitted for {inquiry_type}.")

st.markdown("</div></div>", unsafe_allow_html=True)

st.markdown(
    f"""
    <div class="footer">
      <div class="footer-inner">
        <img src="{image_data("atec-footlogo.png")}" alt="ATEC" />
        Official USA Streamlit prototype
      </div>
    </div>
    """,
    unsafe_allow_html=True,
)
