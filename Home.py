from flask import Flask,render_template

app = Flask(__name__)



@app.route('/')
def Home():
    return render_template('index.html')

@app.route('/doctor_profile')
def doctor_profile():
    return render_template('doctor_profile.html')

@app.route('/services')
def services():
    return render_template('services.html')

@app.route('/squint_surgery')
def squint_surgery():
    description="""
    <p>Embark on a transformative journey to clear vision with Squint Surgery at SitapurNethralaya. Our renowned specialists, armed with a wealth of experience and expertise, are dedicated to correcting misalignments, not only ensuring visual harmony but also boosting your self-assurance.<br><br>

    At SitapurNethralaya, we believe in prioritizing personalized care. Each Squint Surgery is tailored to your unique needs, as we understand that no two cases are alike. Our commitment to delivering exceptional outcomes is reflected in our state-of-the-art facilities, equipped with advanced technologies that enable precision and optimal results.<br><br>
                                    
    What sets SitapurNethralaya apart is our comprehensive approach to evaluations. Our experienced team conducts thorough assessments to gain a deep understanding of your case, allowing for a precise diagnosis and the development of a targeted treatment plan.<br><br>
                                    
    Choose SitapurNethralaya for specialized expertise in squint correction. Our renowned surgeons offer solutions for various types of misalignments, ensuring that you receive the most effective and appropriate care.<br><br>
                                    
    Experience the difference of patient-centric care at SitapurNethralaya, where we provide a warm and supportive environment throughout your squint correction journey. Your path to clear vision begins here<br></p>

    """
    why_choose_us=["<b>Expert Team:</b> Skilled surgeons dedicated to squint correction",
                   "<b>Advanced Techniques:</b> Cutting-edge methods for precise results",
                   "<b>Personalized Solutions:</b> Tailored treatments for your unique needs",
                   "<b>Proven Success:</b> Join our satisfied patients who've achieved clear, coordinated vision"]
    
    services=["<strong>squint correction</strong>",
              "<strong>squint by visiting surgeon</strong>",
              "<strong>squint correction</strong> (3 or 4 muscles horizontal) (both / single eye)",
              "<strong>squint vertical</strong>(both / single)",
              "<strong>squint correction</strong> (2 muscles horizontal) (both / single eye)",
              "<strong>squint</strong> correction vertical + horizontal (both / single)"]
    return render_template('service_details.html',description=description,why_choose_us=why_choose_us,services=services)


@app.route('/galucoma_surgery')
def galucoma_surgery():
    description="""
    <p>Embark on a journey of advanced glaucoma surgery, where our skilled ophthalmologists employ cutting-edge techniques tailored to your specific needs. Combat the "silent thief of sight" with procedures ranging from laser treatments to minimally invasive surgeries.<br><br>
    immerse yourself in our state-of-the-art facilities, where the latest eye care technology meets a comforting environment. Our commitment is to provide the most effective treatments while ensuring your relaxation throughout your eye care journey.<br><br>
    Discover comprehensive eye care services extending beyond glaucoma surgery. From routine eye exams to cataract surgery, our goal is to be your go-to destination for all your eye care needs.<br><br>
    Experience patient-centered care that transcends traditional healthcare. At Sitapur Nethralaya, you're not just a patient – you're an integral part of our family. Our dedicated team guides you with compassion through every step of your treatment, ensuring your comfort and understanding.<br><br>
    Don't let eye conditions dim your perspective on the world. Choose Sitapur Nethralaya and step into a realm of clearer vision and a brighter future. Contact us today to embark on this transformative journey.<br><br>
    
    """
    
    why_choose_us=["<b><strong>Expert Ophthalmologists:</strong></b> Our skilled specialists bring precision and expertise to glaucoma surgery.",
                   "<b><strong>Cutting-Edge Techniques:</strong></b> Experience tailored, advanced procedures, from lasers to minimally invasive options.",
                   "<b><strong>State-of-the-Art Facilities:</strong></b> Modern facilities with the latest technology ensure optimal treatment in a comfortable environment.",
                   "<b><strong>Comprehensive Approach:</strong></b> Beyond surgery, our holistic glaucoma care includes thorough evaluations and personalized plans.",
                   "<b><strong>Patient-Centric Care:</strong></b> Join our family for compassionate guidance at every step, ensuring you feel supported on your journey."
]
    services = [
    "<strong>AGV</strong> (Ahmed Glaucoma Valve)",
    "<strong>AADI</strong> (Argon Anterior Direct Iridoplasty)",
    "<strong>Trabe + Trabe</strong> (Trabeculectomy)",
    "<strong>Trabeculectomy</strong>",
    "<strong>Trabeculectomy + MMC</strong> (Mitomycin C)",
    "Bleb Repair",
    "<strong>SICS + Trab</strong> (Small Incision Cataract Surgery with Trabeculectomy)",
    "<strong>Trab + ICCE</strong> (Intracapsular Cataract Extraction with Trabeculectomy)",
    "<strong>Trab + ECCE</strong> (Extracapsular Cataract Extraction with Trabeculectomy)",
    "<strong>Trab + SICS with AC IOL</strong> (Small Incision Cataract Surgery with Trabeculectomy and Anterior Chamber Intraocular Lens)",
    "<strong>Trab + ICCE with ACIOL</strong> (Intracapsular Cataract Extraction with Trabeculectomy and Anterior Chamber Intraocular Lens)",
    "<strong>Trab + SICS + IOL Square Edge</strong> (Small Incision Cataract Surgery with Trabeculectomy and Intraocular Lens with Square Edge)",
    "<strong>Trab + SICS + Foreign Lens</strong> (Small Incision Cataract Surgery with Trabeculectomy and Foreign Intraocular Lens)",
    "<strong>Trab + Phaco Foldable Lens</strong> (Phacoemulsification with Trabeculectomy and Foldable Intraocular Lens)",
    "<strong>Trab + Phaco + Asph Fold</strong> (Phacoemulsification with Trabeculectomy and Aspheric Foldable Intraocular Lens)",
    "<strong>Trab + Phaco Hydrophobic</strong> (Phacoemulsification with Trabeculectomy and Hydrophobic Intraocular Lens)",
    "<strong>Trab + Phaco Fold + IQ</strong> (Phacoemulsification with Trabeculectomy, Foldable Intraocular Lens, and Intelligent Quadrant)",
    "<strong>Trab + Phaco + Technis</strong> (Phacoemulsification with Trabeculectomy and Technis Intraocular Lens)",
    "<strong>Trab + Aaris Hydrophobic</strong> (Trabeculectomy with Aaris Hydrophobic Intraocular Lens)",
    "AGV Removal with Local Reconstruction",
    "Iridectomy",
    "PI (Peripheral Iridectomy)",
    "<strong>Cyclo Cryo</strong> (Cyclo Cryotherapy)"
]


    
    return render_template('service_details.html',description=description,why_choose_us=why_choose_us,services=services)


@app.route('/gallery')
def gallery():
    return render_template('gallery.html')

@app.route('/about')
def about():
    return render_template('about_us.html')
@app.route('/contact')
def contact():
    return  render_template('contact.html')
@app.route('/appointment')
def appointment():
    return render_template('appointment.html')
if __name__ == '__main__':
    app.run(debug=True)
