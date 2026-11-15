from pathlib import Path
from html import escape
import shutil
import argparse

ROOT = Path(__file__).resolve().parent
OUT = ROOT / 'dist'
OUT.mkdir(exist_ok=True)
(OUT / 'assets').mkdir(exist_ok=True)
(OUT / 'files').mkdir(exist_ok=True)
shutil.copy2(ROOT / 'site.css', OUT / 'assets' / 'site.css')
shutil.copy2(ROOT.parent / 'assets' / 'portrait.jpg', OUT / 'assets' / 'portrait.jpg')
shutil.copy2(ROOT.parent / 'files' / 'Mengfei_Zhao_CV.pdf', OUT / 'files' / 'Mengfei_Zhao_CV.pdf')
(OUT / '.nojekyll').write_text('')

NAV = [('home','Home','index.html'),('papers','Papers','papers.html'),('talks','Talks','talks.html'),('activities','Activities','activities.html'),('cv','CV','cv.html'),('personal','Personal','personal.html')]

def page(key, title, body):
    nav = ''.join(f'<li><a href="{url}"'+(' aria-current="page"' if k == key else '')+f'>{label}</a></li>' for k,label,url in NAV)
    html = f'''<!doctype html>
<html lang="en">
<head>
 <meta charset="utf-8">
 <meta name="viewport" content="width=device-width, initial-scale=1">
 <title>{escape(title)} · Mengfei Zhao</title>
 <meta name="description" content="Mengfei Zhao, PhD student in mathematics at Fudan University. Geometric group theory, Thompson groups, ample groupoids and topological dynamics.">
 <meta name="theme-color" content="#25443c">
 <link rel="stylesheet" href="assets/site.css">
 <link rel="icon" href="assets/favicon.svg" type="image/svg+xml">
</head>
<body>
 <a class="skip" href="#main">Skip to content</a>
 <header class="masthead">
  <a class="name" href="index.html">Mengfei Zhao</a>
  <span class="chinese-name" lang="zh-CN">赵梦飞</span>
  <p class="affiliation">Mathematics · Fudan University</p>
 </header>
 <nav class="site-nav" aria-label="Main navigation"><ul>{nav}</ul></nav>
 <main id="main">{body}</main>
 <footer class="footer"><span>Mengfei Zhao · Fudan University</span><a href="mailto:mfzhao22@m.fudan.edu.cn">mfzhao22@m.fudan.edu.cn</a></footer>
</body>
</html>'''
    (OUT / next(n[2] for n in NAV if n[0] == key)).write_text(html, encoding='utf-8')

def timeline(items, compact=False):
    rows = []
    for date, title, detail, *extra in items:
        body = f'<div class="item-body">{extra[0]}</div>' if extra else ''
        rows.append(f'<li><span class="date">{date}</span><div><span class="item-title">{title}</span><span class="item-detail">{detail}</span>{body}</div></li>')
    return '<ul class="year-list'+(' compact' if compact else '')+'">'+''.join(rows)+'</ul>'

page('home','Home','''
<section class="intro" aria-labelledby="about-heading">
 <div class="intro-copy">
  <h1 id="about-heading">About me</h1>
  <p class="opening">I am a PhD student at the <a href="https://scms.fudan.edu.cn/">Shanghai Center for Mathematical Sciences</a>, Fudan University, advised by <a href="https://wuxiaolei.org/">Xiaolei Wu</a>.</p>
  <p>My research is in geometric group theory and topological dynamics, with a focus on Thompson groups and their generalizations, ample groupoids, and topological full groups.</p>
  <p>I expect to complete my PhD in 2027. Before coming to Fudan, I received my B.S. in Mathematics and Applied Mathematics from Sichuan University in 2022.</p>
  <div class="inline-links"><a href="files/Mengfei_Zhao_CV.pdf">Curriculum vitae (PDF)</a><a href="papers.html">Publications & preprints</a></div>
 </div>
 <img class="portrait" src="assets/portrait.jpg" alt="Mengfei Zhao" width="170" height="190">
</section>
<section aria-labelledby="research-heading">
 <h2 id="research-heading">Research interests</h2>
 <ul class="research-list">
  <li><strong>Geometric group theory.</strong> Thompson groups and their generalizations; embedding problems for groups; finiteness properties; group cohomology and bounded cohomology; Dehn functions; amenability; Hopficity.</li>
  <li><strong>Groupoids and dynamics.</strong> Ample groupoids, topological full groups, homology, and K-theory.</li>
  <li><strong>Geometric topology.</strong> <i>L</i><sup>2</sup>-invariants, BNSR invariants, hyperbolic geometry, and manifolds fibering over the circle.</li>
 </ul>
</section>
<section aria-labelledby="contact-heading">
 <h2 id="contact-heading">Contact</h2>
 <div class="contact-grid">
  <p><span class="contact-label">Affiliation</span>Shanghai Center for Mathematical Sciences<br>Fudan University<br>Shanghai, China</p>
  <p><span class="contact-label">Email</span><a href="mailto:mfzhao22@m.fudan.edu.cn">mfzhao22@m.fudan.edu.cn</a><br><a href="mailto:mfzhaomath@gmail.com">mfzhaomath@gmail.com</a></p>
 </div>
</section>
''')

page('papers','Papers','''
<h1>Publications & preprints</h1>
<section aria-labelledby="preprints-heading">
 <h2 class="section-kicker" id="preprints-heading">Preprint</h2>
 <ol class="papers">
  <li class="paper"><span class="paper-number" aria-hidden="true">3.</span><div>
   <h3 class="paper-title">Hopficity of braided and labeled Thompson groups</h3>
   <p class="paper-authors">Mengfei Zhao</p>
   <p>Preprint, 2026.</p>
   <p class="paper-links"><a href="https://arxiv.org/abs/2610.42050">arXiv:2610.42050</a></p>
  </div></li>
 </ol>
</section>
<section aria-labelledby="journal-heading">
 <h2 class="section-kicker" id="journal-heading">Journal articles</h2>
 <ol class="papers">
  <li class="paper"><span class="paper-number" aria-hidden="true">2.</span><div>
   <h3 class="paper-title">Ample groupoids that are neither almost finite nor purely infinite</h3>
   <p class="paper-authors">Xiaolei Wu, Mengfei Zhao, and Xin Ma</p>
   <p><em>Journal of Topology and Analysis</em> (2026), 1–23.</p>
   <p class="paper-links"><a href="https://arxiv.org/abs/2512.01325">arXiv:2512.01325</a></p>
  </div></li>
  <li class="paper"><span class="paper-number" aria-hidden="true">1.</span><div>
   <h3 class="paper-title">Embedding groups into boundedly acyclic groups</h3>
   <p class="paper-authors">Fan Wu, Xiaolei Wu, Mengfei Zhao, and Zixiang Zhou</p>
   <p><em>Journal of the London Mathematical Society</em> (2), <strong>111</strong> (2025), no. 5, e70164.</p>
   <p class="paper-links"><a href="https://arxiv.org/abs/2407.07703">arXiv:2407.07703</a></p>
  </div></li>
 </ol>
</section>
''')

teaching = [
 ('Fall 2026','Geometric Group Theory','Teaching assistant · Shanghai Center for Mathematical Sciences, Fudan University'),
 ('Fall 2026','Geometric Group Theory (graduate course)','Teaching assistant · Shanghai Center for Mathematical Sciences, Fudan University'),
 ('Fall 2024','Algebraic Topology (graduate course)','Teaching assistant · School of Mathematical Sciences, Fudan University'),
 ('Fall 2024','Algebraic Topology (honors course)','Teaching assistant · School of Mathematical Sciences, Fudan University'),
]
talks = [
 ('July 2026','Embedding groups into boundedly acyclic groups','<a href="https://science.ybu.edu.cn/info/1199/2193.htm">12th National Young Topologist Forum</a> · Yanbian University, Yanji'),
 ('June 2026','Embedding groups into boundedly acyclic groups','Topology Seminar · SIMIS, Shanghai'),
 ('May 2026','Twisted topological groupoids','Topology Seminar · SIMIS, Shanghai'),
 ('May 2024','An introduction to Thompson groups','Tianyuan Conference on Geometric Group Theory · Online'),
 ('Dec. 2023','Embedding groups into boundedly acyclic groups','Tongji Topology Forum · Tongji University, Shanghai'),
]
posters = [
 ('June 2026','Embedding groups into boundedly acyclic groups','<a href="https://sites.google.com/view/yggt2026/home-page">14th Young Geometric Group Theory Conference</a> · KIAS, Seoul'),
 ('June 2025','Generalizations of Thompson groups with applications in group embedding','<a href="https://newsen.pku.edu.cn/events/14732.html">Geometric Group Theory and Related Topics</a> · Peking University, Beijing'),
]
page('talks','Talks','''
<h1>Talks & posters</h1>
<section id="talks" aria-labelledby="talks-heading"><h2 id="talks-heading">Talks</h2>'''+timeline(talks)+'''</section>
<section id="posters" aria-labelledby="posters-heading"><h2 id="posters-heading">Posters</h2>'''+timeline(posters)+'''</section>''')

education = [
 ('2022–2027<br><span class="note">expected</span>','PhD in Mathematics','Shanghai Center for Mathematical Sciences, Fudan University', 'Advisor: <a href="https://wuxiaolei.org/">Xiaolei Wu</a><br>Thesis: <em>Twisted topological groupoids and their full groups</em>'),
 ('2018–2022','B.S. in Mathematics and Applied Mathematics (Honors)','School of Mathematics, Sichuan University', 'Thesis advisor: Bohui Chen<br>Thesis: <em>Compactification of the moduli space of Riemannian surfaces</em>'),
]
awards = [
 ('2025','QuantPi Scholarship','QuantPi Investment, Shanghai'),
 ('2023, 2025','Fudan University Scholarship','Fudan University'),
 ('2022','Excellent Student of Higher Education','Sichuan Province'),
 ('2020','First Prize, National College Student Mathematics Competition','China'),
 ('2019','National Scholarship','Ministry of Education, China'),
 ('2018, 2020,<br>2021','Sichuan University Scholarship','Sichuan University'),
]
seminars = [
 ('Fall 2026','ℓ²-invariants and fibering','SCMS, Shanghai'),
 ('Spring 2026','Special cube complexes','SCMS, Shanghai'),
 ('Fall 2025','Topological full groups','SCMS, Shanghai'),
 ('Fall 2024 &<br>Spring 2025','Finiteness properties and ℓ²-invariants','SCMS, Shanghai'),
 ('Spring 2024','CAT(0) cube complexes','Co-organizer · SCMS, Shanghai'),
 ('Spring 2024','Bounded cohomology of groups','SCMS, Shanghai'),
 ('Fall 2023','Amenable groups','Co-organizer · SCMS, Shanghai'),
 ('Fall 2023','Sigma invariants of groups','SCMS, Shanghai'),
 ('Fall 2023','Characteristic classes','School of Mathematical Sciences, Fudan University'),
 ('Spring 2023','Finiteness properties of groups','SCMS, Shanghai'),
 ('Fall 2022','Thompson groups','SCMS, Shanghai'),
 ('Fall 2022','Homotopy theory','School of Mathematical Sciences, Fudan University'),
]
conferences = [
 ('July 2026','<a href="https://science.ybu.edu.cn/info/1199/2193.htm">12th National Young Topologist Forum</a>','Yanbian University, Yanji'),
 ('July 2026','<a href="https://scms.fudan.edu.cn/info/6203/12081.htm">Shanghai Geometric Group Theory Workshop</a>','SCMS, Fudan University, Shanghai'),
 ('June 2026','<a href="https://sites.google.com/view/yggt2026/home-page">14th Young Geometric Group Theory Conference</a>','KIAS, Seoul'),
 ('Winter 2025','<a href="https://www.simis.cn/workshop-on-hyperbolic-geometry-and-geometric-group-theory/">Workshop on Hyperbolic Geometry and Geometric Group Theory</a>','SIMIS, Shanghai'),
 ('June 2025','<a href="https://newsen.pku.edu.cn/events/14732.html">Geometric Group Theory and Related Topics</a>','BICMR, Peking University, Beijing'),
 ('March 2025','<a href="https://tsimf.tsinghua.edu.cn/info/1120/1302.htm">Geometric Topology and Their Related Topics</a>','TSIMF, Sanya'),
 ('Winter 2024','<a href="https://news.fudan.edu.cn/2024/0102/c31a138883/page.htm">International Congress of Chinese Mathematicians</a>','SIMIS, Shanghai'),
 ('July 2024','<a href="https://scms.fudan.edu.cn/info/4589/6471.htm">Shanghai Geometric Group Theory Workshop</a>','SCMS, Fudan University, Shanghai'),
 ('Summer 2024','<a href="https://dgt3.kimsh.kr/">Dynamical Group Theory III</a>','KIAS, Seoul'),
 ('Aug. 2023','<a href="https://scms.fudan.edu.cn/info/4502/5721.htm">SCMS Geometric Group Theory Workshop</a>','SCMS, Fudan University, Shanghai'),
 ('Aug. 2022','<a href="https://scms.fudan.edu.cn/info/4352/5030.htm">Geometric Group Theory Graduate Summer School</a>','SCMS, Fudan University · Online'),
]
service = [
 ('2022, 2023,<br>2024, 2026','Geometric Group Theory Workshop','Volunteer · SCMS, Shanghai'),
 ('Summer 2025','Student Seminar: Thompson groups','Mentor'),
 ('Winter 2024','International Congress of Chinese Mathematicians','Volunteer'),
]
page('activities','Academic Activities','''
<h1>Academic activities</h1>
<nav class="jump-links" aria-label="On this page"><a href="#seminars">Seminars</a><a href="#conferences">Conferences</a><a href="#teaching">Teaching</a></nav>
<section id="seminars"><h2>Seminars</h2>
<p class="seminar-intro">The seminars below cover topics I am particularly interested in. I participated in each of them and gave presentations.</p>'''+timeline(seminars,True)+'''</section>
<section id="conferences"><h2>Conferences attended</h2>
<p class="conference-intro">You may have met me at one of the following conferences.</p>'''+timeline(conferences,True)+'''</section>
<section id="teaching"><h2>Teaching</h2>'''+timeline(teaching)+'''</section>
''')

page('cv','Curriculum Vitae','''
<div class="cv-heading"><h1>Curriculum vitae</h1><a class="download" href="files/Mengfei_Zhao_CV.pdf">Download CV (PDF) ↓</a></div>
<nav class="jump-links" aria-label="On this page"><a href="#education">Education</a><a href="#awards">Awards</a><a href="#service">Service</a></nav>
<section id="education"><h2>Education</h2>'''+timeline(education)+'''</section>
<section id="awards"><h2>Awards & scholarships</h2>'''+timeline(awards,True)+'''</section>
<section id="service"><h2>Academic service</h2>'''+timeline(service,True)+'''</section>
<section><p>See also my <a href="papers.html">publications and preprints</a>, <a href="talks.html">talks and posters</a>, and <a href="activities.html">seminars, conferences, and teaching experience</a>.</p></section>
''')

page('personal','Personal','''
<h1>Personal</h1>
<div class="personal-copy">
 <p>Outside mathematics, I enjoy card games and strategy games. I have been playing <em>Hearthstone</em> for ten years.</p>
 <p>I like swimming, table tennis, and hiking. I also enjoy watching basketball, football, and esports competitions.</p>
 <p>I am also fond of tea and coffee, and like trying different varieties.</p>
</div>
''')

(OUT / 'assets' / 'favicon.svg').write_text('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64"><rect width="64" height="64" rx="8" fill="#25443c"/><text x="32" y="45" text-anchor="middle" font-family="Georgia,serif" font-size="42" fill="#f7f4ed">M</text></svg>')

# Keep the previous site's main public URLs usable after the static redesign.
REDIRECTS = {'publications': '/papers.html', 'talks': '/talks.html', 'cv': '/cv.html', 'teaching': '/activities.html#teaching'}
for old, target in REDIRECTS.items():
    directory = OUT / old
    directory.mkdir(exist_ok=True)
    (directory / 'index.html').write_text(f'''<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Page moved · Mengfei Zhao</title><meta http-equiv="refresh" content="0;url={target}"><link rel="canonical" href="https://mengfeizhao-math.github.io{target}"></head><body><p>This page has moved. <a href="{target}">Continue to Mengfei Zhao’s website</a>.</p></body></html>''', encoding='utf-8')

parser = argparse.ArgumentParser(description='Build Mengfei Zhao’s static website.')
parser.add_argument('--publish', action='store_true', help='Copy the generated site into the repository root for GitHub Pages.')
args = parser.parse_args()
if args.publish:
    deploy_files = [url for _, _, url in NAV] + ['.nojekyll', 'assets/site.css', 'assets/portrait.jpg', 'assets/favicon.svg', 'files/Mengfei_Zhao_CV.pdf'] + [f'{old}/index.html' for old in REDIRECTS]
    for name in deploy_files:
        destination = ROOT.parent / name
        destination.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(OUT / name, destination)
    print(f'Prepared {len(deploy_files)} files at the repository root for GitHub Pages.')
print(f'Built {len(NAV)} static pages in', OUT)
