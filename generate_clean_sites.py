import json, os

with open('manifest.json') as f:
    sites = json.load(f)

# ============================================================
# NICHE CONFIG — accent color + content only, everything else
# is a shared premium design system (dark, minimal, type-driven)
# ============================================================

NICHES = {
    'real_estate':     {'accent':'#c9a55a','hero':'luxury-house','about':'modern-interior','gallery':'real-estate','tagline':'Find Your Dream Home','sub':'Premium properties in prime locations','services':['Property Sales','Property Valuation','Property Management','Investment Advisory'],'about':'With deep market expertise and a passion for exceptional properties, we help you find the perfect home or investment. Our team brings unparalleled local knowledge and personalized service to every transaction.','cta':'Ready to Find Your Dream Property?','stats':[('500','Properties Sold'),('15','Years Experience'),('98','% Client Satisfaction'),('50','Active Listings')]},
    'restaurant':      {'accent':'#e8a87c','hero':'gourmet-food','about':'restaurant-interior','gallery':'fine-dining','tagline':'A Culinary Experience','sub':'Where every dish tells a story','services':['Fine Dining','Private Events','Catering Services','Wine Pairing'],'about':'Our chefs craft each dish with passion, using the finest locally sourced ingredients. From intimate dinners to grand celebrations, we create unforgettable culinary experiences.','cta':'Reserve Your Table Today','stats':[('10K','Meals Served'),('8','Years Open'),('4.9','Google Rating'),('25','Signature Dishes')]},
    'dental':          {'accent':'#4cc9b8','hero':'dental-clinic','about':'modern-dental','gallery':'dentistry','tagline':'Your Smile, Our Priority','sub':'Gentle, modern dental care','services':['General Dentistry','Cosmetic Dentistry','Orthodontics','Emergency Care'],'about':'We provide comprehensive dental care using state-of-the-art technology in a comfortable, welcoming environment. Your oral health and comfort are our top priorities.','cta':'Book Your Appointment Today','stats':[('5K','Patients Treated'),('12','Years Experience'),('4.9','Patient Rating'),('20','Procedures')]},
    'physiotherapy':   {'accent':'#5b9df9','hero':'physiotherapy','about':'physical-therapy','gallery':'wellness','tagline':'Move Better, Live Better','sub':'Expert physiotherapy for recovery and wellness','services':['Manual Therapy','Sports Rehabilitation','Post-Surgery Recovery','Pain Management'],'about':'Our certified physiotherapists create personalized treatment plans to help you recover from injury, manage pain, and improve mobility with modern techniques and equipment.','cta':'Start Your Recovery Journey','stats':[('3K','Patients Helped'),('10','Years Experience'),('95','% Recovery Rate'),('15','Specialists')]},
    'fitness':         {'accent':'#ff6b35','hero':'yoga-studio','about':'fitness','gallery':'yoga','tagline':'Transform Your Body & Mind','sub':'Where fitness meets community','services':['Yoga Classes','Personal Training','Group Fitness','Meditation Sessions'],'about':'Join our vibrant community and discover the transformative power of movement. Our expert instructors guide all levels, from beginners to advanced practitioners.','cta':'Start Your Fitness Journey','stats':[('2K','Active Members'),('50','Classes Weekly'),('15','Expert Coaches'),('4.9','Member Rating')]},
    'bakery':          {'accent':'#e0a458','hero':'artisan-bakery','about':'baking','gallery':'bread-pastries','tagline':'Freshly Baked Every Day','sub':'Artisan breads and pastries','services':['Artisan Breads','Fresh Pastries','Custom Cakes','Gluten-Free Options'],'about':'Every morning, we bake fresh with the finest organic ingredients. From sourdough to croissants, each creation is crafted with love and traditional techniques.','cta':'Visit Us for Fresh Bakes','stats':[('500','Daily Customers'),('20','Bread Varieties'),('10','Years Baking'),('4.8','Customer Rating')]},
    'salon':           {'accent':'#e63946','hero':'hair-salon','about':'beauty-salon','gallery':'hairstyle','tagline':'Beauty, Redefined','sub':'Where style meets artistry','services':['Hair Styling & Coloring','Manicure & Pedicure','Facial Treatments','Bridal Packages'],'about':'Our master stylists and beauty therapists create looks that express your unique personality. Using premium products and the latest techniques to make you look stunning.','cta':'Book Your Beauty Session','stats':[('1.5K','Happy Clients'),('8','Years Experience'),('15','Beauty Services'),('4.9','Client Rating')]},
    'auto_repair':     {'accent':'#f77f00','hero':'auto-repair','about':'car-service','gallery':'automotive','tagline':'Expert Auto Care','sub':'Your trusted garage for all vehicles','services':['General Repairs','Diagnostics & Inspection','Tire Services','Oil & Maintenance'],'about':'Our certified mechanics deliver honest, reliable service for all vehicle makes and models. From routine maintenance to complex repairs, we keep you on the road.','cta':'Book Your Service Today','stats':[('8K','Cars Repaired'),('12','Years Experience'),('15','Certified Mechanics'),('4.8','Customer Rating')]},
    'legal':           {'accent':'#b8a890','hero':'law-office','about':'legal','gallery':'law-firm','tagline':'Your Legal Advocates','sub':'Experienced counsel you can trust','services':['Corporate Law','Family Law','Civil Litigation','Estate Planning'],'about':'With decades of combined experience, our attorneys provide strategic legal counsel tailored to your unique situation. We fight tirelessly to protect your rights and interests.','cta':'Schedule a Consultation','stats':[('1K','Cases Won'),('25','Years Experience'),('15','Legal Experts'),('98','% Success Rate')]},
    'veterinary':      {'accent':'#4cc9b8','hero':'veterinary','about':'animal-care','gallery':'pets','tagline':'Caring for Your Best Friend','sub':'Compassionate veterinary care','services':['General Check-ups','Surgery & Dentistry','Vaccinations','Emergency Care'],'about':'We treat your pets like family. Our experienced veterinarians provide comprehensive medical care in a warm, stress-free environment designed for animal comfort.','cta':'Book a Visit for Your Pet','stats':[('5K','Pets Treated'),('10','Years Experience'),('4.9','Pet Parent Rating'),('24/7','Emergency Care')]},
    'jewelry':         {'accent':'#d4af37','hero':'luxury-jewelry','about':'jewelry-craft','gallery':'jewelry','tagline':'Timeless Elegance','sub':'Crafted to perfection, worn with pride','services':['Custom Jewelry Design','Fine Rings & Bands','Jewelry Repair','Appraisals'],'about':'Each piece is meticulously crafted by master goldsmiths, combining traditional techniques with contemporary design. We create heirlooms that last generations.','cta':'Discover Our Collection','stats':[('2K','Pieces Created'),('30','Years Craftsmanship'),('50','Designs Available'),('100','% Satisfaction')]},
    'cafe':            {'accent':'#d4a574','hero':'coffee-shop','about':'cafe-interior','gallery':'coffee','tagline':'Coffee, Crafted with Love','sub':'Your neighborhood coffee house','services':['Specialty Coffee','Fresh Pastries','Light Lunch','Catering'],'about':'We roast our beans in-house and source the finest coffee from around the world. Every cup is brewed with care, every customer treated like family.','cta':'Come Sit and Sip','stats':[('300','Cups Daily'),('12','Bean Origins'),('8','Years Roasting'),('4.8','Customer Rating')]},
    'florist':         {'accent':'#e76f51','hero':'flower-shop','about':'flowers','gallery':'floral','tagline':'Beautiful Blooms for Every Occasion','sub':'Fresh flowers, creative arrangements','services':['Bouquets & Arrangements','Wedding Flowers','Event Decoration','Plant Care'],'about':"We source the freshest blooms daily and create stunning arrangements for every occasion. From romantic bouquets to grand event decorations, we bring nature's beauty to you.",'cta':'Order Fresh Flowers Today','stats':[('1.5K','Arrangements Made'),('8','Years Experience'),('40','Flower Varieties'),('4.9','Customer Rating')]},
    'pharmacy':        {'accent':'#52b788','hero':'pharmacy','about':'medicine','gallery':'health','tagline':'Your Health, Our Commitment','sub':'Trusted pharmaceutical care','services':['Prescriptions','Health Consultations','Vaccinations','Medical Supplies'],'about':'Our licensed pharmacists provide expert advice and quality medications with a personal touch. We are your trusted partner in health and wellness.','cta':'Visit Us for Your Health Needs','stats':[('10K','Prescriptions Filled'),('15','Years Service'),('5','Pharmacists'),('4.9','Patient Rating')]},
    'optician':        {'accent':'#00b4d8','hero':'eyewear','about':'optical','gallery':'glasses','tagline':'See the World Clearly','sub':'Designer eyewear and expert eye care','services':['Eye Examinations','Designer Frames','Contact Lenses','Sunglasses'],'about':'We combine comprehensive eye care with an extensive collection of designer frames. Our opticians help you find the perfect eyewear for your style and vision needs.','cta':'Book an Eye Exam','stats':[('3K','Eye Exams'),('10','Years Experience'),('200','Frame Styles'),('4.8','Customer Rating')]},
    'tattoo':          {'accent':'#e63946','hero':'tattoo-art','about':'tattoo-studio','gallery':'tattoo','tagline':'Art on Skin','sub':'Where ink meets imagination','services':['Custom Tattoos','Cover-ups','Fine Line Work','Piercings'],'about':'Our artists create unique, custom designs that tell your story. We maintain the highest standards of hygiene and artistry, ensuring each piece is a masterpiece.','cta':'Book Your Tattoo Session','stats':[('3K','Tattoos Done'),('8','Years Experience'),('5','Resident Artists'),('4.9','Client Rating')]},
    'pet_grooming':    {'accent':'#ee9b00','hero':'dog-grooming','about':'pet-care','gallery':'pets','tagline':'Pamper Your Furry Friend','sub':'Professional pet grooming with love','services':['Full Grooming','Nail Trimming','Bath & Brush','De-shedding Treatment'],'about':'We treat every pet with gentle care and lots of love. Our professional groomers make your furry friends look and feel their best in a calm, safe environment.','cta':'Book a Grooming Session','stats':[('5K','Pets Groomed'),('6','Years Experience'),('8','Expert Groomers'),('4.9','Pet Parent Rating')]},
    'interior':        {'accent':'#dda15e','hero':'interior-design','about':'home-decor','gallery':'interior','tagline':'Spaces That Inspire','sub':'Interior design that transforms','services':['Residential Design','Commercial Spaces','Color Consultation','Furnishing & Styling'],'about':'We create spaces that reflect your personality and lifestyle. Our designers blend aesthetics with functionality to deliver interiors that are both beautiful and practical.','cta':'Start Your Design Project','stats':[('200','Projects Completed'),('10','Years Experience'),('15','Design Awards'),('4.9','Client Rating')]},
    'photography':     {'accent':'#c9a87c','hero':'photography','about':'camera','gallery':'portrait','tagline':'Capturing Moments, Telling Stories','sub':'Professional photography studio','services':['Portrait Sessions','Wedding Photography','Commercial Shoots','Event Coverage'],'about':'We capture the moments that matter most. Our photographers combine technical excellence with artistic vision to create images that tell your unique story.','cta':'Book a Photo Session','stats':[('1K','Photoshoots'),('10','Years Behind Camera'),('50','Weddings Covered'),('4.9','Client Rating')]},
    'bar':             {'accent':'#f77f00','hero':'bar','about':'cocktail','gallery':'cocktails','tagline':'Crafted Cocktails, Great Vibes','sub':'Your favorite night spot','services':['Craft Cocktails','Premium Spirits','Live Music Nights','Private Events'],'about':'We pour passion into every drink. From classic cocktails to innovative creations, our bartenders craft the perfect drink for every mood in a warm, inviting atmosphere.','cta':'Join Us for a Drink','stats':[('50','Cocktail Recipes'),('8','Years Open'),('4.8','Google Rating'),('500','Daily Guests')]},
    'travel':          {'accent':'#48cae4','hero':'travel','about':'adventure','gallery':'travel-destination','tagline':'Your Journey Starts Here','sub':'Unforgettable travel experiences','services':['Custom Itineraries','Flight & Hotel Booking','Group Tours','Travel Insurance'],'about':'We turn your travel dreams into reality. Our experienced travel consultants create personalized itineraries that match your interests, budget, and schedule.','cta':'Plan Your Next Adventure','stats':[('5K','Trips Planned'),('15','Years Experience'),('100','Destinations'),('4.9','Traveler Rating')]},
}

NICHE_MAP = {}
for k, v in [
    ('Real Estate','real_estate'),('Real Estate (Immobilien)','real_estate'),
    ('Restaurant','restaurant'),
    ('Dental/Medical','dental'),('Dental/Medical (Zahnarzt)','dental'),('Dental/Medical (Zahnarzt/Arzt)','dental'),
    ('Physiotherapy','physiotherapy'),('Physiotherapy (Physiotherapie)','physiotherapy'),
    ('Yoga/Fitness','fitness'),
    ('Bakery','bakery'),('Bakery (Bäckerei)','bakery'),
    ('Hair/Nails Salon','salon'),('Hair/Nails Salon (Friseur/Nagelstudio)','salon'),
    ('Auto Repair','auto_repair'),('Auto Repair (Werkstatt)','auto_repair'),
    ('Legal/Law Firm','legal'),('Legal/Kanzlei (Rechtsanwalt)','legal'),
    ('Veterinary','veterinary'),('Veterinary (Tierarzt)','veterinary'),
    ('Jewelry','jewelry'),('Goldschmiede/Jewelry','jewelry'),
    ('Cafe/Coffee Shop','cafe'),
    ('Florist','florist'),('Florist (Blumenladen)','florist'),
    ('Pharmacy','pharmacy'),('Pharmacy (Apotheke)','pharmacy'),
    ('Optician/Eyewear','optician'),('Optician/Eyewear (Optiker)','optician'),
    ('Tattoo Studio','tattoo'),
    ('Pet Grooming','pet_grooming'),('Pet Grooming (Hundeschule/Hundeauslauf)','pet_grooming'),
    ('Interior Design','interior'),('Interior Design (Inneneinrichtung)','interior'),
    ('Photography Studio','photography'),('Photography Studio (Fotostudio)','photography'),
    ('Bar/Pub','bar'),
    ('Travel Agency','travel'),('Travel Agency (Reisebüro)','travel'),
]:
    NICHE_MAP[k] = v


CSS = """*{margin:0;padding:0;box-sizing:border-box}
:root{--accent:__A__;--bg:#0a0a0b;--surface:#111113;--surface2:#161618;--text:#f5f5f7;--muted:#86868b;--border:rgba(255,255,255,.06);--radius:14px}
html{scroll-behavior:smooth;-webkit-font-smoothing:antialiased;text-rendering:optimizeLegibility}
body{font-family:'Inter',sans-serif;background:var(--bg);color:var(--text);line-height:1.6;overflow-x:hidden;font-weight:400}
img{display:block;max-width:100%}
a{text-decoration:none;color:inherit}
::selection{background:var(--accent);color:#fff}

/* PRELOADER */
#loader{position:fixed;inset:0;z-index:99999;background:var(--bg);display:flex;align-items:center;justify-content:center;transition:opacity .5s}
#loader.hide{opacity:0;pointer-events:none}
.loader-ring{width:32px;height:32px;border:2px solid var(--border);border-top-color:var(--accent);border-radius:50%;animation:spin .7s linear infinite}
@keyframes spin{to{transform:rotate(360deg)}}

/* PROGRESS */
#progress{position:fixed;top:0;left:0;height:2px;width:0;background:var(--accent);z-index:9998;transition:width .15s}

/* NAV */
nav{position:fixed;top:0;width:100%;z-index:1000;padding:1.4rem 3rem;display:flex;justify-content:space-between;align-items:center;transition:all .4s}
nav.scrolled{padding:.9rem 3rem;background:rgba(10,10,11,.8);backdrop-filter:blur(20px);-webkit-backdrop-filter:blur(20px);border-bottom:1px solid var(--border)}
.logo{font-family:'Playfair Display',serif;font-size:1.3rem;font-weight:600;color:var(--accent);letter-spacing:.3px}
.nav-links{display:flex;gap:2rem;list-style:none;align-items:center}
.nav-links a{font-size:.88rem;font-weight:400;color:var(--muted);transition:color .3s}
.nav-links a:hover{color:var(--text)}
.nav-links a.cta{color:var(--bg);background:var(--accent);padding:.5rem 1.3rem;border-radius:100px;font-weight:500}
.nav-links a.cta:hover{opacity:.85}
@media(max-width:768px){nav{padding:1rem 1.5rem}nav.scrolled{padding:.8rem 1.5rem}.nav-links{display:none}}

/* SECTIONS */
section{padding:7rem 2rem;position:relative}
@media(max-width:768px){section{padding:4.5rem 1.5rem}}
.container{max-width:1080px;margin:0 auto}
.s-title{text-align:center;margin-bottom:4rem}
.s-title h2{font-family:'Playfair Display',serif;font-size:clamp(2rem,4vw,3.2rem);font-weight:500;letter-spacing:-.5px;margin-bottom:.7rem}
.s-title p{color:var(--muted);font-size:1.05rem;font-weight:300}

/* HERO */
.hero{min-height:100vh;display:flex;align-items:center;justify-content:center;text-align:center;overflow:hidden;position:relative}
.hero-img{position:absolute;inset:0;z-index:-1}
.hero-img img{width:100%;height:100%;object-fit:cover;opacity:.1}
.hero-img::after{content:"";position:absolute;inset:0;background:linear-gradient(180deg,rgba(10,10,11,.3) 0%,rgba(10,10,11,.5) 40%,rgba(10,10,11,.95) 100%)}
.hero-content{position:relative;z-index:1;padding:0 1rem}
.hero h1{font-family:'Playfair Display',serif;font-size:clamp(3rem,7vw,5.5rem);font-weight:500;letter-spacing:-1.5px;line-height:1.05;margin-bottom:1.5rem;max-width:900px;margin-left:auto;margin-right:auto}
.hero p{color:var(--muted);font-size:clamp(1.05rem,2vw,1.3rem);font-weight:300;margin-bottom:2.5rem;max-width:580px;margin-left:auto;margin-right:auto}
.hero-cta{display:flex;gap:1rem;justify-content:center;flex-wrap:wrap}
.scroll-hint{position:absolute;bottom:2rem;left:50%;transform:translateX(-50%);color:var(--muted);font-size:.8rem;letter-spacing:1px;text-transform:uppercase;opacity:.5;animation:bounce 2s infinite}
@keyframes bounce{0%,100%{transform:translateX(-50%) translateY(0)}50%{transform:translateX(-50%) translateY(6px)}}

/* BUTTONS */
.btn{padding:.85rem 2rem;border-radius:100px;font-weight:500;font-size:.95rem;transition:all .3s;display:inline-block;cursor:pointer;border:none}
.btn-fill{background:var(--accent);color:#0a0a0b}
.btn-fill:hover{opacity:.85;transform:translateY(-1px)}
.btn-ghost{color:var(--text);border:1px solid var(--border)}
.btn-ghost:hover{border-color:var(--accent);color:var(--accent)}

/* ABOUT */
.about{background:var(--surface)}
.about-grid{display:grid;grid-template-columns:1fr 1fr;gap:4rem;align-items:center}
@media(max-width:768px){.about-grid{grid-template-columns:1fr;gap:2.5rem}}
.about-img{border-radius:var(--radius);overflow:hidden}
.about-img img{width:100%;height:420px;object-fit:cover;transition:transform .6s ease}
.about-img:hover img{transform:scale(1.03)}
.about-text h2{font-family:'Playfair Display',serif;font-size:clamp(1.8rem,3.5vw,2.6rem);font-weight:500;letter-spacing:-.5px;margin-bottom:1.3rem;line-height:1.15}
.about-text p{color:var(--muted);margin-bottom:1rem;font-size:1.05rem;font-weight:300}
.about-tags{display:flex;gap:.7rem;flex-wrap:wrap;margin-top:1.8rem}
.about-tags span{font-size:.82rem;padding:.4rem 1rem;border:1px solid var(--border);border-radius:100px;color:var(--muted)}

/* SERVICES */
.svc-grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(250px,1fr));gap:1.5rem}
.svc-card{background:var(--surface);border:1px solid var(--border);border-radius:var(--radius);padding:2.5rem 2rem;transition:all .4s ease}
.svc-card:hover{background:var(--surface2);border-color:rgba(255,255,255,.1);transform:translateY(-4px)}
.svc-num{font-family:'Playfair Display',serif;font-size:.9rem;color:var(--accent);font-weight:600;margin-bottom:1rem;letter-spacing:1px}
.svc-card h3{font-size:1.2rem;font-weight:500;margin-bottom:.7rem}
.svc-card p{color:var(--muted);font-size:.95rem;font-weight:300;line-height:1.6}

/* STATS */
.stats{background:var(--surface);padding:4.5rem 2rem}
.stats-grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(180px,1fr));gap:2rem;max-width:900px;margin:0 auto;text-align:center}
.stat-num{font-family:'Playfair Display',serif;font-size:clamp(2.5rem,4vw,3.5rem);font-weight:500;color:var(--accent);line-height:1}
.stat-label{color:var(--muted);font-size:.92rem;margin-top:.5rem;font-weight:300}

/* GALLERY */
.gallery-grid{display:grid;grid-template-columns:repeat(3,1fr);gap:1rem}
@media(max-width:768px){.gallery-grid{grid-template-columns:repeat(2,1fr);gap:.7rem}}
.gal-item{border-radius:var(--radius);overflow:hidden;cursor:pointer;position:relative}
.gal-item img{width:100%;height:260px;object-fit:cover;transition:transform .5s ease}
.gal-item:hover img{transform:scale(1.06)}

/* TESTIMONIALS */
.tst-grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(300px,1fr));gap:1.5rem}
.tst-card{background:var(--surface);border:1px solid var(--border);border-radius:var(--radius);padding:2.5rem;transition:all .4s ease}
.tst-card:hover{background:var(--surface2);transform:translateY(-3px)}
.tst-stars{color:var(--accent);font-size:.9rem;margin-bottom:1.2rem;letter-spacing:2px}
.tst-card p{color:var(--muted);font-style:italic;margin-bottom:1.5rem;line-height:1.7;font-weight:300}
.tst-author{display:flex;align-items:center;gap:.8rem}
.tst-author img{width:42px;height:42px;border-radius:50%;object-fit:cover}
.tst-author h4{font-size:.92rem;font-weight:500}
.tst-author small{color:var(--muted);font-size:.8rem}

/* FAQ */
.faq-container{max-width:720px;margin:0 auto}
.faq-item{border-bottom:1px solid var(--border);transition:border-color .3s}
.faq-item[open]{border-color:var(--accent)}
.faq-item summary{padding:1.5rem 0;cursor:pointer;font-weight:500;font-size:1.05rem;list-style:none;display:flex;justify-content:space-between;align-items:center}
.faq-item summary::-webkit-details-marker{display:none}
.faq-item summary::after{content:'+';color:var(--accent);font-size:1.4rem;font-weight:300;transition:transform .3s}
.faq-item[open] summary::after{transform:rotate(45deg)}
.faq-item p{padding:0 0 1.5rem;color:var(--muted);line-height:1.7;font-weight:300}

/* CONTACT */
.contact{text-align:center;padding:8rem 2rem;position:relative;overflow:hidden}
.contact h2{font-family:'Playfair Display',serif;font-size:clamp(2.2rem,4.5vw,3.8rem);font-weight:500;letter-spacing:-.8px;margin-bottom:1rem}
.contact p{color:var(--muted);margin-bottom:2.5rem;font-size:1.1rem;font-weight:300}
.contact-btns{display:flex;gap:1rem;justify-content:center;flex-wrap:wrap}

/* FOOTER */
footer{padding:3rem 2rem;text-align:center;border-top:1px solid var(--border)}
.social{display:flex;justify-content:center;gap:.8rem;margin-bottom:1.5rem}
.social a{width:40px;height:40px;border-radius:50%;border:1px solid var(--border);display:flex;align-items:center;justify-content:center;transition:all .3s}
.social a:hover{background:var(--accent);border-color:var(--accent)}
.social svg{width:16px;height:16px;fill:var(--muted);transition:fill .3s}
.social a:hover svg{fill:#0a0a0b}
.footer-info{display:flex;justify-content:center;gap:2.5rem;flex-wrap:wrap;margin-bottom:1.2rem}
.footer-info span,.footer-info a{color:var(--muted);font-size:.85rem;font-weight:300}
.footer-info a:hover{color:var(--accent)}
.copyright{color:var(--muted);font-size:.8rem;padding-top:1.2rem;border-top:1px solid var(--border);font-weight:300}
.copyright a{color:var(--accent)}

/* LIGHTBOX */
#lightbox{position:fixed;inset:0;background:rgba(0,0,0,.92);z-index:99999;display:none;align-items:center;justify-content:center;cursor:pointer}
#lightbox.show{display:flex}
#lightbox img{max-width:90%;max-height:85%;border-radius:10px}

/* BACK TOP */
#backtop{position:fixed;bottom:88px;right:22px;z-index:999;width:44px;height:44px;border-radius:50%;background:var(--surface2);border:1px solid var(--border);display:flex;align-items:center;justify-content:center;cursor:pointer;opacity:0;transform:translateY(10px);transition:all .3s}
#backtop.show{opacity:1;transform:translateY(0)}
#backtop:hover{background:var(--accent)}
#backtop svg{width:17px;height:17px;stroke:var(--muted);transition:stroke .3s}
#backtop:hover svg{stroke:#0a0a0b}

/* WHATSAPP */
.wa{position:fixed;bottom:22px;right:22px;z-index:999;width:54px;height:54px;background:#25d366;border-radius:50%;display:flex;align-items:center;justify-content:center;box-shadow:0 8px 24px rgba(0,0,0,.2);transition:transform .3s}
.wa:hover{transform:scale(1.08)}
.wa svg{width:28px;height:28px;fill:#fff}

/* REVEAL */
.reveal{opacity:0;transform:translateY(30px)}"""


JS = """<script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.12.5/gsap.min.js"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.12.5/ScrollTrigger.min.js"></script>
<script>
gsap.registerPlugin(ScrollTrigger);

// Preloader
window.addEventListener('load',function(){
  var l=document.getElementById('loader');
  setTimeout(function(){l.classList.add('hide');setTimeout(function(){l.style.display='none'},500)},200);
});

// Progress bar
var p=document.getElementById('progress');
window.addEventListener('scroll',function(){
  var s=document.documentElement.scrollHeight-document.documentElement.clientHeight;
  p.style.width=(document.documentElement.scrollTop/s*100)+'%';
});

// Navbar scroll
var n=document.querySelector('nav');
window.addEventListener('scroll',function(){
  if(window.scrollY>50){n.classList.add('scrolled')}else{n.classList.remove('scrolled')}
});

// GSAP reveals
gsap.utils.toArray('.reveal').forEach(function(el){
  gsap.to(el,{opacity:1,y:0,duration:.9,ease:'power3.out',scrollTrigger:{trigger:el,start:'top 90%'}});
});

// Hero entrance
gsap.from('.hero h1',{opacity:0,y:50,duration:1.1,delay:.3,ease:'power3.out'});
gsap.from('.hero p',{opacity:0,y:30,duration:.9,delay:.6,ease:'power3.out'});
gsap.from('.hero-cta',{opacity:0,y:20,duration:.7,delay:.9,ease:'power3.out'});
gsap.from('.scroll-hint',{opacity:0,duration:.8,delay:1.3});

// Counters
ScrollTrigger.create({trigger:'.stats',start:'top 82%',once:true,onEnter:function(){
  document.querySelectorAll('.counter').forEach(function(c){
    var t=c.dataset.target,num=parseInt(t.replace(/[^0-9]/g,'')),suf=t.replace(/[0-9]/g,''),cur=0,step=Math.max(1,Math.ceil(num/30));
    var timer=setInterval(function(){cur+=step;if(cur>=num){cur=num;clearInterval(timer)}c.textContent=cur+suf},28);
  });
}});

// Lightbox
var lb=document.getElementById('lightbox'),lbI=document.getElementById('lb-img');
document.querySelectorAll('.gal-item img').forEach(function(img){
  img.addEventListener('click',function(){lbI.src=this.src.replace('800/600','1200/900');lb.classList.add('show')});
});
lb.addEventListener('click',function(){lb.classList.remove('show')});

// Back to top
var bt=document.getElementById('backtop');
window.addEventListener('scroll',function(){if(window.scrollY>500){bt.classList.add('show')}else{bt.classList.remove('show')}});
bt.addEventListener('click',function(){window.scrollTo({top:0,behavior:'smooth'})});
</script>"""


def build(site):
    n = NICHES[NICHE_MAP.get(site['niche'],'real_estate')]
    biz = site['business_name']
    phone = site.get('phone','')
    email = site.get('email','')
    city = site['city']
    niche = site['niche'].split('(')[0].strip()
    pc = phone.replace(' ','')
    logo = biz.split()[0] if biz else 'OnyxDigital'
    a = n['accent']

    # Services
    svc = ''
    for i, s in enumerate(n['services']):
        num = '0' + str(i+1)
        svc += '<div class="svc-card reveal"><div class="svc-num">' + num + '</div><h3>' + s + '</h3><p>Professional ' + s.lower() + ' delivered with expertise and dedication to excellence.</p></div>\n'

    # Gallery (6 images in grid)
    gal = ''
    for i in range(1, 7):
        gal += '<div class="gal-item reveal"><img src="https://loremflickr.com/800/600/' + n['gallery'] + '?lock=' + str(i+10) + '" alt="Gallery ' + str(i) + '" loading="lazy"></div>\n'

    # Stats
    st = ''
    for num, label in n['stats']:
        st += '<div class="stat-num reveal"><span class="counter" data-target="' + num + '">' + num + '</span></div>\n<div class="stat-label reveal">' + label + '</div>\n'
    # Better: pair them
    st = ''
    for num, label in n['stats']:
        st += '<div class="reveal"><div class="stat-num"><span class="counter" data-target="' + num + '">' + num + '</span></div><div class="stat-label">' + label + '</div></div>\n'

    # Testimonials
    tsts = ''
    for i, (name, role) in enumerate([('Sarah Johnson','Verified Client'),('Michael Chen','Verified Client'),('Emma Williams','Verified Client')]):
        quotes = [
            'Absolutely outstanding service! The team went above and beyond our expectations. Highly recommended.',
            'Professional, reliable, and truly exceptional results. They transformed our experience completely.',
            'From start to finish, the experience was seamless. The attention to detail is second to none.',
        ]
        tsts += '<div class="tst-card reveal"><div class="tst-stars">\u2605\u2605\u2605\u2605\u2605</div><p>"' + quotes[i].replace('They', biz) + '"</p><div class="tst-author"><img src="https://loremflickr.com/100/100/person?lock=' + str(20+i) + '" alt="Client"><div><h4>' + name + '</h4><small>' + role + '</small></div></div></div>\n'

    # FAQ
    faqs = [
        ('What services do you offer?', 'We offer a comprehensive range of professional ' + niche.lower() + ' services. Contact us for a detailed consultation and personalized service plan.'),
        ('How can I book an appointment?', 'You can book by calling ' + phone + ', emailing ' + email + ', or using the WhatsApp button to chat with us directly.'),
        ('What are your operating hours?', 'Our standard hours are Monday to Friday, 9:00 AM to 6:00 PM. Weekend appointments are available by prior arrangement.'),
        ('Do you offer services for businesses?', 'Yes, we provide both individual and business services with customized solutions tailored to your specific needs.'),
        ('How do I get a quote?', 'Reach out via phone, email, or WhatsApp for a free, no-obligation quote tailored to your specific requirements.'),
    ]
    faq_html = ''
    for q, ans in faqs:
        faq_html += '<details class="faq-item reveal"><summary>' + q + '</summary><p>' + ans + '</p></details>\n'

    # Social
    social = '<a href="https://wa.me/9233390025902" target="_blank" aria-label="WhatsApp"><svg viewBox="0 0 24 24"><path d="M12 2C6.5 2 2 6.5 2 12c0 1.8.5 3.5 1.3 5L2 22l5.2-1.4c1.4.8 3.1 1.2 4.8 1.2 5.5 0 10-4.5 10-10S17.5 2 12 2zm0 18c-1.5 0-3-.4-4.3-1.1l-.3-.2-3.1.8.8-3-.2-.3C4.4 14.9 4 13.5 4 12c0-4.4 3.6-8 8-8s8 3.6 8 8-3.6 8-8 8z"/></svg></a><a href="mailto:' + email + '" aria-label="Email"><svg viewBox="0 0 24 24"><path d="M20 4H4c-1.1 0-2 .9-2 2v12c0 1.1.9 2 2 2h16c1.1 0 2-.9 2-2V6c0-1.1-.9-2-2-2zm0 4l-8 5-8-5V6l8 5 8-5v2z"/></svg></a><a href="tel:' + pc + '" aria-label="Phone"><svg viewBox="0 0 24 24"><path d="M6.6 10.8c1.4 2.8 3.8 5.2 6.6 6.6l2.2-2.2c.3-.3.7-.4 1-.2 1.1.4 2.3.6 3.6.6.6 0 1 .4 1 1V20c0 .6-.4 1-1 1-9.4 0-17-7.6-17-17 0-.6.4-1 1-1h3.5c.6 0 1 .4 1 1 0 1.2.2 2.4.6 3.6.1.4 0 .8-.3 1l-2.2 2.2z"/></svg></a>'

    # CSS with accent color
    css = CSS.replace("__A__", a)

    nav_links = '<li><a href="#about">About</a></li><li><a href="#services">Services</a></li><li><a href="#gallery">Gallery</a></li><li><a href="#reviews">Reviews</a></li><li><a href="#faq">FAQ</a></li><li><a href="#contact" class="cta">Contact</a></li>'

    return ('''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>''' + biz + ''' | OnyxDigital</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Playfair+Display:wght@400;500;600&family=Inter:wght@300;400;500;600&display=swap" rel="stylesheet">
<style>
''' + css + '''
</style>
</head>
<body>
<div id="loader"><div class="loader-ring"></div></div>
<div id="progress"></div>
<nav><div class="logo">''' + logo + '''</div><ul class="nav-links">''' + nav_links + '''</ul></nav>

<section class="hero" id="home">
<div class="hero-img"><img src="https://loremflickr.com/1920/1080/''' + n['hero'] + '''?lock=1" alt=""></div>
<div class="hero-content">
<h1>''' + n['tagline'] + '''</h1>
<p>''' + n['sub'] + '''</p>
<div class="hero-cta">
<a href="#contact" class="btn btn-fill">Get in Touch</a>
<a href="#services" class="btn btn-ghost">Our Services</a>
</div>
</div>
<div class="scroll-hint">Scroll</div>
</section>

<section class="about" id="about">
<div class="container">
<div class="about-grid">
<div class="about-img reveal"><img src="https://loremflickr.com/600/420/''' + n['about'] + '''?lock=3" alt="About ''' + biz + '''"></div>
<div class="about-text reveal">
<h2>About ''' + biz + '''</h2>
<p>''' + n['about'] + '''</p>
<p>Located in ''' + city + ''', we are committed to delivering exceptional service and building lasting relationships with every client we serve.</p>
<div class="about-tags"><span>Certified Professionals</span><span>Quality Guaranteed</span><span>Trusted &amp; Reliable</span></div>
</div>
</div>
</div>
</section>

<section id="services">
<div class="container">
<div class="s-title reveal"><h2>Our Services</h2><p>What we offer</p></div>
<div class="svc-grid">''' + svc + '''</div>
</div>
</section>

<section class="stats">
<div class="stats-grid">''' + st + '''</div>
</section>

<section id="gallery">
<div class="container">
<div class="s-title reveal"><h2>Gallery</h2><p>A glimpse of our work</p></div>
<div class="gallery-grid">''' + gal + '''</div>
</div>
</section>

<section class="about" id="reviews">
<div class="container">
<div class="s-title reveal"><h2>What Our Clients Say</h2><p>Trusted by satisfied customers</p></div>
<div class="tst-grid">''' + tsts + '''</div>
</div>
</section>

<section id="faq">
<div class="container">
<div class="s-title reveal"><h2>Frequently Asked Questions</h2><p>Got questions? We have answers</p></div>
<div class="faq-container">''' + faq_html + '''</div>
</div>
</section>

<section class="contact" id="contact">
<h2>''' + n['cta'] + '''</h2>
<p>Contact ''' + biz + ''' today and experience the difference</p>
<div class="contact-btns">
<a href="https://wa.me/9233390025902" target="_blank" class="btn btn-fill">WhatsApp Us</a>
<a href="tel:''' + pc + '''" class="btn btn-ghost">Call Now</a>
<a href="mailto:''' + email + '''" class="btn btn-ghost">Email Us</a>
</div>
</section>

<footer>
<div class="social">''' + social + '''</div>
<div class="footer-info"><span>''' + city + '''</span><a href="tel:''' + pc + '''">''' + phone + '''</a><a href="mailto:''' + email + '''">''' + email + '''</a></div>
<div class="copyright">&copy; 2026 ''' + biz + '''. Premium website by <a href="https://onyx-digital-sidd.vercel.app/" target="_blank">OnyxDigital</a>.</div>
</footer>

<div id="lightbox"><img id="lb-img" src="" alt=""></div>
<div id="backtop"><svg viewBox="0 0 24 24" fill="none" stroke-width="2" stroke-linecap="round"><path d="M12 4l-8 8h5v8h6v-8h5z"/></svg></div>
<a href="https://wa.me/9233390025902" target="_blank" class="wa"><svg viewBox="0 0 24 24"><path d="M17.5 14.4c-.3-.1-1.8-.9-2-.9-.3-.1-.5-.1-.7.1-.2.3-.8 1-.9 1.2-.2.2-.3.2-.6.1-.3-.1-1.3-.5-2.4-1.5-.9-.8-1.5-1.8-1.7-2-.2-.3 0-.5.1-.6.1-.1.3-.4.4-.5.1-.2.2-.3.3-.5.1-.2 0-.4 0-.5-.1-.1-.7-1.6-.9-2.2-.2-.6-.5-.5-.7-.5h-.6c-.2 0-.5.1-.8.4-.3.3-1 1-1 2.5s1.1 2.9 1.2 3.1c.1.2 2.1 3.3 5.1 4.5.7.3 1.3.5 1.7.6.7.2 1.4.2 1.9.1.6-.1 1.8-.7 2-1.4.2-.7.2-1.3.2-1.4-.1-.1-.3-.2-.6-.3M12 2C6.5 2 2 6.5 2 12c0 1.8.5 3.5 1.3 5L2 22l5.2-1.4c1.4.8 3.1 1.2 4.8 1.2 5.5 0 10-4.5 10-10S17.5 2 12 2z"/></svg></a>

''' + JS + '''
</body>
</html>''')


count = 0
errors = []
for s in sites:
    try:
        with open(s['filename'], 'w', encoding='utf-8') as f:
            f.write(build(s))
        count += 1
    except Exception as e:
        errors.append((s['filename'], str(e)))

print(f"Generated {count} sites")
if errors:
    for f, e in errors[:5]:
        print(f"  ERROR: {f}: {e}")
