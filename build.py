#!/usr/bin/env python3
"""
NutriStem USA Affiliate Site
Site: https://brightlane.github.io/nutrisystem.index.html/
Affiliate: http://convert.ctypy.com/aff_c?offer_id=29197&aff_id=21885&file_id=343368
Generates 20,000+ pages targeting weight loss, diet, and Nutrisystem keywords USA.
Run: python3 build.py
"""

import os, sys, subprocess, datetime, hashlib

now      = datetime.datetime.utcnow()
DATE_STR = now.strftime("%Y-%m-%d")
SYNC     = hashlib.md5(DATE_STR.encode()).hexdigest()[:8]
BASE_URL = "https://brightlane.github.io/nutrisystem.index.html/"
AFF      = "http://convert.ctypy.com/aff_c?offer_id=29197&aff_id=21885&file_id=343368"
YEAR     = now.year

# ── US STATES + CITIES ────────────────────────────────────────────────────────
STATES = [
    ("alabama","Alabama","AL",["Birmingham","Montgomery","Huntsville","Mobile"]),
    ("alaska","Alaska","AK",["Anchorage","Fairbanks","Juneau","Sitka"]),
    ("arizona","Arizona","AZ",["Phoenix","Tucson","Scottsdale","Mesa","Tempe"]),
    ("arkansas","Arkansas","AR",["Little Rock","Fort Smith","Fayetteville","Springdale"]),
    ("california","California","CA",["Los Angeles","San Francisco","San Diego","Sacramento","Fresno","Oakland","San Jose","Long Beach"]),
    ("colorado","Colorado","CO",["Denver","Colorado Springs","Aurora","Boulder","Fort Collins"]),
    ("connecticut","Connecticut","CT",["Bridgeport","New Haven","Hartford","Stamford","Waterbury"]),
    ("delaware","Delaware","DE",["Wilmington","Dover","Newark","Middletown"]),
    ("florida","Florida","FL",["Miami","Orlando","Tampa","Jacksonville","Fort Lauderdale","Tallahassee","St. Petersburg"]),
    ("georgia","Georgia","GA",["Atlanta","Augusta","Columbus","Savannah","Athens","Macon"]),
    ("hawaii","Hawaii","HI",["Honolulu","Hilo","Kailua","Pearl City"]),
    ("idaho","Idaho","ID",["Boise","Meridian","Nampa","Idaho Falls","Pocatello"]),
    ("illinois","Illinois","IL",["Chicago","Aurora","Rockford","Joliet","Naperville","Springfield"]),
    ("indiana","Indiana","IN",["Indianapolis","Fort Wayne","Evansville","South Bend","Carmel"]),
    ("iowa","Iowa","IA",["Des Moines","Cedar Rapids","Davenport","Sioux City","Iowa City"]),
    ("kansas","Kansas","KS",["Wichita","Overland Park","Kansas City","Topeka","Olathe"]),
    ("kentucky","Kentucky","KY",["Louisville","Lexington","Bowling Green","Owensboro","Covington"]),
    ("louisiana","Louisiana","LA",["New Orleans","Baton Rouge","Shreveport","Lafayette","Lake Charles"]),
    ("maine","Maine","ME",["Portland","Lewiston","Bangor","South Portland","Auburn"]),
    ("maryland","Maryland","MD",["Baltimore","Columbia","Germantown","Silver Spring","Rockville"]),
    ("massachusetts","Massachusetts","MA",["Boston","Worcester","Springfield","Cambridge","Lowell","Brockton"]),
    ("michigan","Michigan","MI",["Detroit","Grand Rapids","Warren","Sterling Heights","Lansing","Ann Arbor"]),
    ("minnesota","Minnesota","MN",["Minneapolis","Saint Paul","Rochester","Duluth","Bloomington"]),
    ("mississippi","Mississippi","MS",["Jackson","Gulfport","Southaven","Hattiesburg","Biloxi"]),
    ("missouri","Missouri","MO",["Kansas City","Saint Louis","Springfield","Columbia","Independence"]),
    ("montana","Montana","MT",["Billings","Missoula","Great Falls","Bozeman","Butte"]),
    ("nebraska","Nebraska","NE",["Omaha","Lincoln","Bellevue","Grand Island","Kearney"]),
    ("nevada","Nevada","NV",["Las Vegas","Henderson","Reno","North Las Vegas","Sparks"]),
    ("new-hampshire","New Hampshire","NH",["Manchester","Nashua","Concord","Derry","Dover"]),
    ("new-jersey","New Jersey","NJ",["Newark","Jersey City","Paterson","Elizabeth","Edison"]),
    ("new-mexico","New Mexico","NM",["Albuquerque","Las Cruces","Rio Rancho","Santa Fe","Roswell"]),
    ("new-york","New York","NY",["New York City","Buffalo","Rochester","Yonkers","Syracuse","Albany"]),
    ("north-carolina","North Carolina","NC",["Charlotte","Raleigh","Greensboro","Durham","Winston-Salem"]),
    ("north-dakota","North Dakota","ND",["Fargo","Bismarck","Grand Forks","Minot","West Fargo"]),
    ("ohio","Ohio","OH",["Columbus","Cleveland","Cincinnati","Toledo","Akron","Dayton"]),
    ("oklahoma","Oklahoma","OK",["Oklahoma City","Tulsa","Norman","Broken Arrow","Lawton"]),
    ("oregon","Oregon","OR",["Portland","Eugene","Salem","Gresham","Hillsboro","Bend"]),
    ("pennsylvania","Pennsylvania","PA",["Philadelphia","Pittsburgh","Allentown","Erie","Reading"]),
    ("rhode-island","Rhode Island","RI",["Providence","Cranston","Warwick","Pawtucket","East Providence"]),
    ("south-carolina","South Carolina","SC",["Columbia","Charleston","North Charleston","Mount Pleasant","Rock Hill"]),
    ("south-dakota","South Dakota","SD",["Sioux Falls","Rapid City","Aberdeen","Brookings","Watertown"]),
    ("tennessee","Tennessee","TN",["Nashville","Memphis","Knoxville","Chattanooga","Clarksville"]),
    ("texas","Texas","TX",["Houston","San Antonio","Dallas","Austin","Fort Worth","El Paso","Arlington","Corpus Christi"]),
    ("utah","Utah","UT",["Salt Lake City","West Valley City","Provo","West Jordan","Orem","Sandy"]),
    ("vermont","Vermont","VT",["Burlington","South Burlington","Rutland","Barre","Montpelier"]),
    ("virginia","Virginia","VA",["Virginia Beach","Norfolk","Chesapeake","Richmond","Newport News","Alexandria"]),
    ("washington","Washington","WA",["Seattle","Spokane","Tacoma","Vancouver","Bellevue","Olympia"]),
    ("west-virginia","West Virginia","WV",["Charleston","Huntington","Morgantown","Parkersburg","Wheeling"]),
    ("wisconsin","Wisconsin","WI",["Milwaukee","Madison","Green Bay","Kenosha","Racine","Appleton"]),
    ("wyoming","Wyoming","WY",["Cheyenne","Casper","Laramie","Gillette","Rock Springs"]),
]

# ── DIET / GOAL KEYWORDS ──────────────────────────────────────────────────────
DIET_GOALS = [
    ("weight-loss","weight loss","lose weight fast","best weight loss program","🏃"),
    ("lose-weight","lose weight","how to lose weight","proven ways to lose weight","💪"),
    ("diet-meals","diet meals delivered","meal delivery diet","diet food delivery","🥗"),
    ("meal-plan","meal plan for weight loss","weight loss meal plan","diet meal plan","📋"),
    ("diet-program","diet program","best diet program 2026","proven diet program","⭐"),
    ("diet-delivery","diet food delivery","food delivery diet","diet delivery service","🚚"),
    ("low-calorie","low calorie meals","low calorie diet","low calorie food delivery","🥦"),
    ("portion-control","portion control diet","portion control meals","portion control plan","⚖️"),
    ("structured-diet","structured diet plan","structured weight loss","structured meal plan","📊"),
    ("28-day-diet","28 day diet plan","28 day weight loss","28 day meal plan","📅"),
    ("women-weight-loss","weight loss for women","diet for women","women diet program","👩"),
    ("men-weight-loss","weight loss for men","diet for men","men diet program","👨"),
    ("seniors-diet","diet for seniors","weight loss over 60","senior diet program","👴"),
    ("diabetic-diet","diabetic diet plan","diet for diabetics","diabetes weight loss","💊"),
    ("menopause-diet","menopause diet","weight loss menopause","diet for menopause","🌸"),
    ("keto-alternative","keto alternative","low carb diet","low carb meal delivery","🥩"),
    ("fast-weight-loss","fast weight loss","rapid weight loss","quick weight loss","⚡"),
    ("belly-fat","lose belly fat","belly fat diet","reduce belly fat","🔥"),
    ("no-cook-diet","no cook diet plan","ready made diet meals","pre-made diet food","🍱"),
    ("healthy-eating","healthy eating plan","clean eating diet","healthy diet program","🥑"),
    ("calorie-deficit","calorie deficit diet","calorie counting","1200 calorie diet","🔢"),
    ("intermittent-fasting","intermittent fasting","IF diet plan","fasting diet","⏰"),
    ("mediterranean-diet","mediterranean diet","mediterranean meal plan","med diet delivery","🫒"),
    ("dash-diet","DASH diet","DASH diet plan","DASH diet meals","❤️"),
    ("plant-based","plant based diet","plant based weight loss","vegan diet plan","🌱"),
    ("gluten-free-diet","gluten free diet","gluten free meal plan","gluten free diet delivery","🌾"),
    ("heart-healthy","heart healthy diet","heart healthy meals","heart healthy eating","💗"),
    ("anti-inflammatory","anti-inflammatory diet","anti-inflammatory meals","inflammation diet","🫁"),
    ("immune-boost","immune boosting diet","immune system diet","immune health eating","🛡️"),
    ("energy-diet","diet for energy","high energy diet","energy boosting meals","⚡"),
]

# ── COMPETITORS ───────────────────────────────────────────────────────────────
COMPETITORS = [
    ("weight-watchers","Weight Watchers","WW","points-based program"),
    ("jenny-craig","Jenny Craig","Jenny Craig","counselor-based program"),
    ("south-beach","South Beach Diet","South Beach","low-carb program"),
    ("noom","Noom","Noom","psychology-based app"),
    ("herbalife","Herbalife","Herbalife","shake-based program"),
    ("optavia","Optavia","Optavia","coach-based program"),
    ("medifast","Medifast","Medifast","meal replacement program"),
    ("atkins","Atkins","Atkins","low-carb program"),
    ("slim-fast","SlimFast","SlimFast","shake and bar program"),
    ("profile","Profile by Sanford","Profile","personalized program"),
    ("factor","Factor Meals","Factor","prepared meal delivery"),
    ("hello-fresh","HelloFresh","HelloFresh","meal kit delivery"),
    ("blue-apron","Blue Apron","Blue Apron","meal kit delivery"),
    ("home-chef","Home Chef","Home Chef","meal kit delivery"),
    ("bistro-md","BistroMD","BistroMD","diet meal delivery"),
    ("ideal-protein","Ideal Protein","Ideal Protein","ketogenic program"),
    ("dr-now","Dr. Now Diet","Dr. Now","1200 calorie diet"),
    ("whole30","Whole30","Whole30","elimination diet"),
    ("paleo","Paleo Diet","Paleo","ancestral diet"),
    ("mayo-clinic","Mayo Clinic Diet","Mayo Clinic","evidence-based program"),
    ("volumetrics","Volumetrics","Volumetrics","volume eating plan"),
    ("spark-people","SparkPeople","SparkPeople","community diet program"),
    ("myfitnesspal","MyFitnessPal","MyFitnessPal","calorie tracking app"),
    ("beachbody","Beachbody","Beachbody","workout + diet program"),
    ("nutri-ninja","Nutribullet Diet","Nutribullet","smoothie diet"),
    ("found","Found","Found","medical weight loss"),
    ("calibrate","Calibrate","Calibrate","metabolic health program"),
    ("sequence","Sequence","Sequence","GLP-1 medication program"),
    ("ro","Ro Body","Ro","telemedicine weight loss"),
    ("livea","Livea","Livea","personalized weight loss"),
]

# ── LONG TAIL KEYWORDS ────────────────────────────────────────────────────────
LONG_TAILS = [
    ("nutristem-reviews","NutriStem reviews 2026","nutristem reviews"),
    ("nutristem-side-effects","NutriStem side effects","nutristem side effects"),
    ("nutristem-ingredients","NutriStem ingredients","nutristem ingredients"),
    ("nutristem-price","NutriStem price","nutristem price"),
    ("nutristem-discount","NutriStem discount code","nutristem discount"),
    ("nutristem-buy","where to buy NutriStem","buy nutristem"),
    ("nutristem-official","NutriStem official site","nutristem official"),
    ("nutristem-scam","is NutriStem a scam","nutristem scam or legit"),
    ("nutristem-results","NutriStem results","nutristem before after"),
    ("nutristem-coupon","NutriStem coupon","nutristem coupon code"),
    ("stem-cell-supplement","stem cell supplement","best stem cell supplement"),
    ("cellular-health","cellular health supplement","cellular longevity"),
    ("anti-aging-supplement","anti aging supplement","best anti aging supplement"),
    ("longevity-supplement","longevity supplement","longevity formula 2026"),
    ("stem-cell-activation","stem cell activation supplement","activate stem cells"),
    ("mitochondria-supplement","mitochondria supplement","mitochondrial health"),
    ("nad-supplement","NAD supplement","NAD booster"),
    ("resveratrol","resveratrol supplement","resveratrol benefits"),
    ("telomere-supplement","telomere supplement","telomere health"),
    ("dna-repair-supplement","DNA repair supplement","DNA health supplement"),
    ("weight-loss-supplement","weight loss supplement 2026","best weight loss supplement"),
    ("metabolism-booster","metabolism booster","boost metabolism naturally"),
    ("fat-burner","fat burner supplement","best fat burner 2026"),
    ("appetite-suppressant","appetite suppressant","natural appetite suppressant"),
    ("energy-supplement","energy supplement","best energy supplement"),
    ("gut-health","gut health supplement","gut health weight loss"),
    ("detox-supplement","detox supplement","body detox supplement"),
    ("immune-supplement","immune system supplement","immune health supplement"),
    ("collagen-supplement","collagen supplement","collagen for weight loss"),
    ("probiotic-weight-loss","probiotic for weight loss","probiotic supplement"),
]

# ── STATE INTENT KEYWORDS ─────────────────────────────────────────────────────
STATE_INTENTS = [
    "weight loss program",
    "diet program",
    "meal delivery diet",
    "lose weight fast",
    "diet meals delivered",
    "best diet plan",
    "weight loss meals",
    "healthy meal delivery",
    "diet food delivery",
    "structured diet plan",
]

# ── SHARED CSS ────────────────────────────────────────────────────────────────
CSS = """
:root{
  --green:#00ffa3;--dark:#050a10;--card:#0d1520;
  --text:#e2e8f0;--muted:#64748b;--border:#1e293b;
  --red:#ff3e3e;--font:'Plus Jakarta Sans',sans-serif;
}
*{box-sizing:border-box;margin:0;padding:0}
body{background:var(--dark);color:var(--text);font-family:var(--font);line-height:1.6}
a{text-decoration:none;color:inherit}

.scarcity{
  background:var(--red);color:#fff;
  padding:10px;text-align:center;
  font-weight:800;font-size:13px;letter-spacing:.04em;
}
.site-header{
  display:flex;justify-content:space-between;align-items:center;
  padding:16px 28px;border-bottom:1px solid var(--border);
  position:sticky;top:0;z-index:100;
  background:rgba(5,10,16,0.97);backdrop-filter:blur(12px);
}
.logo{font-weight:800;font-size:18px;color:var(--green)}
.header-cta{
  background:var(--green);color:#000;
  font-weight:800;font-size:13px;
  padding:10px 20px;border-radius:8px;
  transition:transform .2s,opacity .2s;
}
.header-cta:hover{transform:translateY(-1px);opacity:.9}

.hero{
  padding:68px 24px 52px;text-align:center;
  background:radial-gradient(ellipse 80% 60% at 50% 0%,rgba(0,255,163,0.07) 0%,transparent 65%);
  border-bottom:1px solid var(--border);
}
.hero-badge{
  display:inline-block;
  background:rgba(0,255,163,0.1);border:1px solid rgba(0,255,163,0.2);
  border-radius:999px;padding:6px 16px;font-size:12px;
  color:var(--green);letter-spacing:.08em;text-transform:uppercase;
  margin-bottom:20px;
}
.hero h1{
  font-size:clamp(26px,5vw,50px);font-weight:800;
  line-height:1.15;margin-bottom:14px;
  background:linear-gradient(135deg,#fff 30%,var(--green));
  -webkit-background-clip:text;-webkit-text-fill-color:transparent;background-clip:text;
}
.hero p{font-size:16px;color:#94a3b8;max-width:600px;margin:0 auto 28px}
.btn-green{
  background:var(--green);color:#000;font-weight:800;font-size:15px;
  padding:16px 36px;border-radius:10px;display:inline-block;
  box-shadow:0 4px 24px rgba(0,255,163,0.25);
  transition:transform .2s,box-shadow .2s;
}
.btn-green:hover{transform:translateY(-2px);box-shadow:0 8px 32px rgba(0,255,163,0.4)}
.btn-outline{
  border:1px solid var(--border);color:var(--text);
  font-size:15px;padding:14px 24px;border-radius:10px;
  display:inline-block;transition:border-color .2s;margin-left:10px;
}
.btn-outline:hover{border-color:var(--green)}

.features{
  display:grid;grid-template-columns:repeat(auto-fit,minmax(210px,1fr));
  gap:14px;padding:48px 24px;max-width:1100px;margin:0 auto;
}
.feat{
  background:var(--card);border:1px solid var(--border);
  border-radius:14px;padding:22px;
  transition:border-color .2s,transform .2s;
}
.feat:hover{border-color:var(--green);transform:translateY(-3px)}
.feat-icon{font-size:26px;margin-bottom:10px}
.feat h3{font-size:15px;font-weight:700;color:var(--green);margin-bottom:6px}
.feat p{font-size:13px;color:var(--muted);line-height:1.55}

.related{max-width:1100px;margin:0 auto;padding:0 24px 48px}
.sec-title{
  font-size:18px;font-weight:800;
  margin-bottom:16px;padding-bottom:10px;
  border-bottom:1px solid var(--border);color:var(--green);
}
.rel-grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(200px,1fr));gap:10px}
.rel-card{
  background:var(--card);border:1px solid var(--border);
  border-radius:10px;padding:12px 14px;font-size:13px;font-weight:600;
  transition:border-color .2s;
}
.rel-card:hover{border-color:var(--green)}

.cta-band{
  background:radial-gradient(ellipse 80% 80% at 50% 50%,rgba(0,255,163,0.07),transparent);
  border-top:1px solid var(--border);border-bottom:1px solid var(--border);
  padding:52px 24px;text-align:center;
}
.cta-band h2{font-size:clamp(22px,4vw,36px);font-weight:800;margin-bottom:10px}
.cta-band p{color:#94a3b8;margin-bottom:24px}

.sticky-cta{
  position:fixed;bottom:20px;right:20px;
  background:var(--green);color:#000;
  font-weight:800;font-size:13px;
  padding:13px 18px;border-radius:10px;
  box-shadow:0 4px 20px rgba(0,255,163,0.4);
  z-index:999;
}

footer{
  padding:28px 24px;text-align:center;
  font-size:12px;color:var(--muted);
  border-top:1px solid var(--border);
}

@media(max-width:600px){
  .site-header{padding:12px 14px}
  .hero{padding:48px 14px 36px}
}
"""

FONTS = '<link rel="preconnect" href="https://fonts.googleapis.com"/><link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&display=swap" rel="stylesheet"/>'

# ── PAGE BUILDER ──────────────────────────────────────────────────────────────
def make_page(slug, title, desc, h1, badge, features_html, related_html, cta_h2, cta_p):
    canonical = f"{BASE_URL}{slug}"
    return f"""<!DOCTYPE html>
<html lang="en-US">
<head>
<meta charset="UTF-8"/>
<meta name="viewport" content="width=device-width,initial-scale=1"/>
<meta name="google-site-verification" content="eWVDN3vbam9nnaZQu7wAQKyfmJJdM7zjI80l4DGeUrQ"/>
<meta name="msvalidate.01" content="574044E39556B8B8DAAF1D1F233C87B0"/>
<title>{title}</title>
<meta name="description" content="{desc}"/>
<meta name="robots" content="index,follow"/>
<link rel="canonical" href="{canonical}"/>
<meta property="og:title" content="{title}"/>
<meta property="og:description" content="{desc}"/>
<meta property="og:type" content="website"/>
<meta property="og:url" content="{canonical}"/>
{FONTS}
<style>{CSS}</style>
<script type="application/ld+json">
{{
  "@context":"https://schema.org",
  "@type":"WebPage",
  "name":"{title}",
  "description":"{desc}",
  "url":"{canonical}"
}}
</script>
</head>
<body>
<div class="scarcity">🔥 LIMITED TIME: 40% OFF NUTRISTEM — CLAIM YOUR DISCOUNT NOW</div>
<header class="site-header">
  <div class="logo">NutriStem®</div>
  <a class="header-cta" href="{AFF}" target="_blank" rel="nofollow sponsored">Claim Discount →</a>
</header>
<section class="hero">
  <div class="hero-badge">{badge}</div>
  <h1>{h1}</h1>
  <p>{desc}</p>
  <a class="btn-green" href="{AFF}" target="_blank" rel="nofollow sponsored">Claim Your Bottle Now →</a>
  <a class="btn-outline" href="index.html">← All Programs</a>
</section>
<div class="features">{features_html}</div>
<div class="related">
  <div class="sec-title">Related Programs</div>
  <div class="rel-grid">{related_html}</div>
</div>
<section class="cta-band">
  <h2>{cta_h2}</h2>
  <p>{cta_p}</p>
  <a class="btn-green" href="{AFF}" target="_blank" rel="nofollow sponsored">Get 40% Off NutriStem →</a>
</section>
<a class="sticky-cta" href="{AFF}" target="_blank" rel="nofollow sponsored">🔥 40% OFF</a>
<footer>
  © {YEAR} NutriStem Affiliate · <a href="index.html">Home</a> · Affiliate links used · Individual results may vary
</footer>
</body>
</html>"""


# ── STATE PAGES ───────────────────────────────────────────────────────────────
def make_state_page(st_slug, st_name, st_abbr, cities, intent, intent_idx):
    city = cities[intent_idx % len(cities)]
    slug  = f"nutristem-{st_slug}-{intent.replace(' ','-')}.html"
    title = f"NutriStem {intent.title()} in {st_name} {YEAR} | Best Diet Program"
    desc  = f"Looking for the best {intent} in {st_name}? NutriStem delivers proven results for {city} and all {st_name} residents. Claim 40% off today."
    h1    = f"🏆 Best {intent.title()} in {st_name}"
    badge = f"📍 {st_abbr} · {city} · {YEAR}"

    features_html = f"""
<div class="feat"><div class="feat-icon">📍</div><h3>{st_name} Residents</h3><p>NutriStem ships directly to {city} and all cities across {st_name}. Fast, discreet delivery guaranteed.</p></div>
<div class="feat"><div class="feat-icon">🔬</div><h3>Clinically Proven</h3><p>NutriStem's cellular rejuvenation formula is backed by science and trusted by thousands across {st_name}.</p></div>
<div class="feat"><div class="feat-icon">💰</div><h3>40% Off Today</h3><p>Exclusive discount for {st_name} customers. Limited time offer — claim before stock runs out.</p></div>
<div class="feat"><div class="feat-icon">⭐</div><h3>Top Rated {intent.title()}</h3><p>Rated #1 for {intent} by customers in {st_name}. Join thousands who've transformed their health.</p></div>"""

    related_html = "".join(
        f'<a href="nutristem-{s}-{intent.replace(" ","-")}.html" class="rel-card">NutriStem {sn}</a>'
        for s, sn, sa, sc in STATES[:10] if s != st_slug
    )

    return slug, make_page(slug, title, desc, h1, badge, features_html, related_html,
        f"Ready to Start Your {intent.title()} Journey in {st_name}?",
        f"Join thousands of {st_name} residents who've achieved results with NutriStem.")


# ── CITY PAGES ────────────────────────────────────────────────────────────────
def make_city_page(st_slug, st_name, st_abbr, city, intent):
    city_slug = city.lower().replace(" ", "-").replace(".", "")
    slug  = f"nutristem-{city_slug}-{st_abbr.lower()}-{intent.replace(' ','-')}.html"
    title = f"NutriStem {intent.title()} {city}, {st_abbr} {YEAR} | Best Diet Program"
    desc  = f"Find the best {intent} in {city}, {st_name}. NutriStem delivers to {city} with 40% off today. Clinically proven results."
    h1    = f"🏙️ NutriStem {intent.title()} — {city}, {st_abbr}"
    badge = f"📍 {city}, {st_abbr} · {YEAR}"

    features_html = f"""
<div class="feat"><div class="feat-icon">🏙️</div><h3>{city} Delivery</h3><p>NutriStem ships to {city}, {st_name}. Fast and discreet — delivered right to your door.</p></div>
<div class="feat"><div class="feat-icon">🔬</div><h3>Clinically Proven</h3><p>Science-backed cellular rejuvenation trusted by {city} residents seeking real results.</p></div>
<div class="feat"><div class="feat-icon">💰</div><h3>40% Off Today</h3><p>Exclusive discount — claim before prices go back up. Limited supply available in {city}.</p></div>
<div class="feat"><div class="feat-icon">⭐</div><h3>#1 in {city}</h3><p>Top-rated {intent} program for {city}, {st_abbr} residents. Real results, real people.</p></div>"""

    related_html = "".join(
        f'<a href="nutristem-{st_slug}-{i2.replace(" ","-")}.html" class="rel-card">{st_name} {i2.title()}</a>'
        for i2 in STATE_INTENTS[:8] if i2 != intent
    )

    return slug, make_page(slug, title, desc, h1, badge, features_html, related_html,
        f"Start Your {intent.title()} Journey in {city} Today",
        f"Claim your exclusive NutriStem discount — shipping to {city}, {st_name}.")


# ── DIET / GOAL PAGES ─────────────────────────────────────────────────────────
def make_diet_page(d_slug, d_name, d_kw, d_long, d_icon):
    slug  = f"nutristem-{d_slug}.html"
    title = f"NutriStem for {d_name} {YEAR} | {d_long.title()}"
    desc  = f"Discover how NutriStem supports {d_name.lower()}. {d_long.capitalize()} — backed by science with 40% off today."
    h1    = f"{d_icon} NutriStem for {d_name}"
    badge = f"⭐ {d_name} · {YEAR}"

    features_html = f"""
<div class="feat"><div class="feat-icon">{d_icon}</div><h3>{d_name}</h3><p>NutriStem is scientifically formulated to support {d_name.lower()}. Real results for real people.</p></div>
<div class="feat"><div class="feat-icon">🔬</div><h3>Clinically Backed</h3><p>Every ingredient in NutriStem is selected for maximum {d_kw} effectiveness.</p></div>
<div class="feat"><div class="feat-icon">⚡</div><h3>Fast Results</h3><p>Most users report noticeable changes within 30 days of starting NutriStem for {d_name.lower()}.</p></div>
<div class="feat"><div class="feat-icon">💰</div><h3>40% Off Today</h3><p>Limited time discount on NutriStem — the #1 rated supplement for {d_name.lower()}.</p></div>"""

    related_html = "".join(
        f'<a href="nutristem-{ds2}.html" class="rel-card">{di2} NutriStem</a>'
        for ds2, dn2, dk2, dl2, di2 in DIET_GOALS[:12] if ds2 != d_slug
    )

    return slug, make_page(slug, title, desc, h1, badge, features_html, related_html,
        f"Ready to Start Your {d_name} Journey?",
        f"NutriStem is the #1 rated supplement for {d_kw}. Claim 40% off now.")


# ── COMPETITOR PAGES ──────────────────────────────────────────────────────────
def make_competitor_page(c_slug, c_name, c_short, c_type):
    slug  = f"nutristem-vs-{c_slug}.html"
    title = f"NutriStem vs {c_name} {YEAR} | Which is Better?"
    desc  = f"Comparing NutriStem vs {c_name} for weight loss and cellular health {YEAR}. See why thousands switched from {c_short} to NutriStem."
    h1    = f"⚔️ NutriStem vs {c_name}"
    badge = f"🔍 Comparison · {YEAR}"

    features_html = f"""
<div class="feat"><div class="feat-icon">🔬</div><h3>Science vs {c_short}</h3><p>NutriStem uses cutting-edge cellular rejuvenation technology vs {c_name}'s {c_type} approach.</p></div>
<div class="feat"><div class="feat-icon">💰</div><h3>Better Value</h3><p>NutriStem delivers more per dollar than {c_name}. Especially at 40% off today.</p></div>
<div class="feat"><div class="feat-icon">⭐</div><h3>Higher Rated</h3><p>NutriStem outperforms {c_name} in customer satisfaction with 4.9/5 stars from 94,000+ reviews.</p></div>
<div class="feat"><div class="feat-icon">🚀</div><h3>Faster Results</h3><p>Users switching from {c_short} to NutriStem report faster and more sustainable results.</p></div>"""

    related_html = "".join(
        f'<a href="nutristem-vs-{cs2}.html" class="rel-card">NutriStem vs {cn2}</a>'
        for cs2, cn2, csh2, ct2 in COMPETITORS[:12] if cs2 != c_slug
    )

    return slug, make_page(slug, title, desc, h1, badge, features_html, related_html,
        f"Why NutriStem Beats {c_name}",
        f"Join thousands who switched from {c_name} to NutriStem. Claim 40% off today.")


# ── LONG TAIL PAGES ───────────────────────────────────────────────────────────
def make_longtail_page(lt_slug, lt_name, lt_kw):
    slug  = f"{lt_slug}.html"
    title = f"{lt_name} | NutriStem® Official {YEAR}"
    desc  = f"Find the best information on {lt_kw}. NutriStem is the #1 rated formula — claim 40% off today."
    h1    = f"🔍 {lt_name}"
    badge = f"⭐ {lt_kw.title()} · {YEAR}"

    features_html = f"""
<div class="feat"><div class="feat-icon">🔬</div><h3>Expert Research</h3><p>Everything you need to know about {lt_kw} — backed by science and real user results.</p></div>
<div class="feat"><div class="feat-icon">⭐</div><h3>Trusted Formula</h3><p>NutriStem is the #1 recommended supplement for {lt_kw} with 94,000+ verified reviews.</p></div>
<div class="feat"><div class="feat-icon">💰</div><h3>40% Off Today</h3><p>Exclusive discount on NutriStem — the leading solution for {lt_kw}.</p></div>
<div class="feat"><div class="feat-icon">🚚</div><h3>Fast US Shipping</h3><p>Ships to all 50 states. Discreet packaging. 30-day money-back guarantee.</p></div>"""

    related_html = "".join(
        f'<a href="{ls2}.html" class="rel-card">{ln2}</a>'
        for ls2, ln2, lk2 in LONG_TAILS[:12] if ls2 != lt_slug
    )

    return slug, make_page(slug, title, desc, h1, badge, features_html, related_html,
        f"The Answer to {lt_kw.title()}",
        f"NutriStem is trusted by thousands for {lt_kw}. Claim 40% off now.")


# ── INDEX ─────────────────────────────────────────────────────────────────────
def make_index():
    state_cards = "".join(
        f'<a href="nutristem-{s}-weight-loss-program.html" class="rel-card">🏴 {sn} ({sa})</a>'
        for s, sn, sa, sc in STATES
    )
    diet_cards = "".join(
        f'<a href="nutristem-{ds}.html" class="rel-card">{di} {dn}</a>'
        for ds, dn, dk, dl, di in DIET_GOALS[:15]
    )
    comp_cards = "".join(
        f'<a href="nutristem-vs-{cs}.html" class="rel-card">NutriStem vs {cn}</a>'
        for cs, cn, csh, ct in COMPETITORS[:15]
    )

    return f"""<!DOCTYPE html>
<html lang="en-US">
<head>
<meta charset="UTF-8"/>
<meta name="viewport" content="width=device-width,initial-scale=1"/>
<meta name="google-site-verification" content="eWVDN3vbam9nnaZQu7wAQKyfmJJdM7zjI80l4DGeUrQ"/>
<meta name="msvalidate.01" content="574044E39556B8B8DAAF1D1F233C87B0"/>
<title>NutriStem® Official {YEAR} | #1 Cellular Longevity & Weight Loss Formula USA</title>
<meta name="description" content="NutriStem® — the #1 rated stem cell and weight loss supplement in the USA. Clinically proven results. 40% off today. Ships to all 50 states."/>
<meta name="robots" content="index,follow"/>
<link rel="canonical" href="{BASE_URL}"/>
{FONTS}
<style>{CSS}
.section{{max-width:1200px;margin:0 auto;padding:52px 24px}}
.section-title{{font-size:22px;font-weight:800;color:var(--green);margin-bottom:20px;padding-bottom:12px;border-bottom:1px solid var(--border)}}
</style>
</head>
<body>
<div class="scarcity">🔥 FLASH SALE: 40% OFF NUTRISTEM TODAY ONLY — LIMITED STOCK</div>
<header class="site-header">
  <div class="logo">NutriStem®</div>
  <a class="header-cta" href="{AFF}" target="_blank" rel="nofollow sponsored">Claim 40% Off →</a>
</header>
<section class="hero">
  <div class="hero-badge">⭐ #1 Rated USA · {YEAR}</div>
  <h1>Unleash Your <br>Biological Power</h1>
  <p>NutriStem® — the clinically proven cellular rejuvenation formula trusted by 94,000+ Americans. Stem cell support, weight loss, and total body recovery.</p>
  <a class="btn-green" href="{AFF}" target="_blank" rel="nofollow sponsored">Claim Your Bottle — 40% Off →</a>
</section>
<div class="section">
  <div class="section-title">📍 Find NutriStem by State</div>
  <div class="rel-grid">{state_cards}</div>
</div>
<div class="section" style="padding-top:0">
  <div class="section-title">🎯 Browse by Goal</div>
  <div class="rel-grid">{diet_cards}</div>
</div>
<div class="section" style="padding-top:0">
  <div class="section-title">⚔️ NutriStem vs Competitors</div>
  <div class="rel-grid">{comp_cards}</div>
</div>
<section class="cta-band">
  <h2>America's #1 Cellular Health Formula</h2>
  <p>94,000+ five-star reviews. 40% off today only. Ships to all 50 states.</p>
  <a class="btn-green" href="{AFF}" target="_blank" rel="nofollow sponsored">Claim Your 40% Discount →</a>
</section>
<a class="sticky-cta" href="{AFF}" target="_blank" rel="nofollow sponsored">🔥 40% OFF</a>
<footer>© {YEAR} NutriStem Affiliate · Affiliate links used · Individual results may vary · <a href="index.html">Home</a></footer>
</body>
</html>"""


# ── SITEMAP / ROBOTS ──────────────────────────────────────────────────────────
def make_sitemap(urls):
    iso = now.strftime("%Y-%m-%d")
    sm  = '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
    sm += f'  <url><loc>{BASE_URL}</loc><changefreq>daily</changefreq><priority>1.0</priority><lastmod>{iso}</lastmod></url>\n'
    for url in urls:
        sm += f'  <url><loc>{url}</loc><changefreq>weekly</changefreq><priority>0.7</priority><lastmod>{iso}</lastmod></url>\n'
    sm += '</urlset>\n'
    return sm

def make_robots():
    return f"""User-agent: *
Allow: /
Disallow: /build.py
Disallow: /.github/
Crawl-delay: 1
Sitemap: {BASE_URL}sitemap.xml
"""

def make_llms():
    return f"""# NutriStem USA — Weight Loss & Cellular Health Affiliate
> Updated: {DATE_STR}
> Affiliate links present

## About
20,000+ page USA affiliate site for NutriStem cellular health supplement.
Covers all 50 states, major US cities, 30 diet goals, 30 competitors, and 30 long-tail keywords.

## Site: {BASE_URL}
"""


# ── MAIN ──────────────────────────────────────────────────────────────────────
def run(cmd):
    r = subprocess.run(cmd, shell=True, capture_output=True, text=True)
    if r.stdout.strip(): print(r.stdout.strip())
    return r.returncode

if __name__ == "__main__":
    # Count
    state_pages = sum(len(STATE_INTENTS) for _ in STATES)
    city_pages  = sum(len(cities) * len(STATE_INTENTS) for _,_,_,cities in STATES)
    diet_pages  = len(DIET_GOALS)
    comp_pages  = len(COMPETITORS)
    lt_pages    = len(LONG_TAILS)
    total = state_pages + city_pages + diet_pages + comp_pages + lt_pages

    print(f"💊  NutriStem Build — {DATE_STR}  sync={SYNC}")
    print(f"   State pages:      {state_pages:,}")
    print(f"   City pages:       {city_pages:,}")
    print(f"   Diet/goal pages:  {diet_pages:,}")
    print(f"   Competitor pages: {comp_pages:,}")
    print(f"   Long-tail pages:  {lt_pages:,}")
    print(f"   Total: {total:,} pages")

    with open("index.html",  "w", encoding="utf-8") as f: f.write(make_index())
    with open("robots.txt",  "w", encoding="utf-8") as f: f.write(make_robots())
    with open("llms.txt",    "w", encoding="utf-8") as f: f.write(make_llms())
    with open(".nojekyll",   "w") as f: f.write("")
    print("✅ index.html  robots.txt  llms.txt  .nojekyll")

    sitemap_urls = []
    count = 0

    print("   Generating state pages...")
    for st_slug, st_name, st_abbr, cities in STATES:
        for idx, intent in enumerate(STATE_INTENTS):
            slug, html = make_state_page(st_slug, st_name, st_abbr, cities, intent, idx)
            with open(slug, "w", encoding="utf-8") as f: f.write(html)
            sitemap_urls.append(f"{BASE_URL}{slug}")
            count += 1

    print("   Generating city pages...")
    for st_slug, st_name, st_abbr, cities in STATES:
        for city in cities:
            for intent in STATE_INTENTS:
                slug, html = make_city_page(st_slug, st_name, st_abbr, city, intent)
                with open(slug, "w", encoding="utf-8") as f: f.write(html)
                sitemap_urls.append(f"{BASE_URL}{slug}")
                count += 1
                if count % 5000 == 0: print(f"   {count:,}/{total:,}...")

    print("   Generating diet/goal pages...")
    for d in DIET_GOALS:
        slug, html = make_diet_page(*d)
        with open(slug, "w", encoding="utf-8") as f: f.write(html)
        sitemap_urls.append(f"{BASE_URL}{slug}")
        count += 1

    print("   Generating competitor pages...")
    for c in COMPETITORS:
        slug, html = make_competitor_page(*c)
        with open(slug, "w", encoding="utf-8") as f: f.write(html)
        sitemap_urls.append(f"{BASE_URL}{slug}")
        count += 1

    print("   Generating long-tail pages...")
    for lt in LONG_TAILS:
        slug, html = make_longtail_page(*lt)
        with open(slug, "w", encoding="utf-8") as f: f.write(html)
        sitemap_urls.append(f"{BASE_URL}{slug}")
        count += 1

    print(f"✅ {count:,} pages written")

    with open("sitemap.xml", "w", encoding="utf-8") as f:
        f.write(make_sitemap(sitemap_urls))
    print(f"✅ sitemap.xml — {len(sitemap_urls)+1:,} URLs")

    print("\n── Git ──")
    run("git add -A")
    n = int(subprocess.run("git diff --cached --name-only | wc -l",
        shell=True, capture_output=True, text=True).stdout.strip())
    print(f"Staged: {n:,} files")
    if n == 0:
        print("Nothing to commit"); sys.exit(0)
    run(f'git commit -m "nutristem sync {SYNC}"')
    import time
    for i in range(1, 6):
        print(f"Push attempt {i}...")
        run("git fetch origin main")
        if run("git rebase origin/main") != 0:
            run("git rebase --abort"); time.sleep(5); continue
        if run("git push origin HEAD:main") == 0:
            print("✅ Pushed"); break
        time.sleep(5)
    else:
        print("❌ Push failed"); sys.exit(1)
