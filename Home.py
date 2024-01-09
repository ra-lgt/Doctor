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
    heading="Transformative Squint Surgery Unveiled"
    side_heading="Squint Correction Services We Offer"
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
    return render_template('service_details.html',heading=heading,description=description,why_choose_us=why_choose_us,services=services)


@app.route('/galucoma_surgery')
def galucoma_surgery():
    heading="Revolutionary Glaucoma Treatment Revealed"
    side_heading="Glaucoma Treatment Services We Offer"
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
    "<strong>Bleb Repair</strong>",
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
    "<strong>AGV Removal with Local Reconstruction</strong>",
    "<strong>Iridectomy</strong>",
    "<strong>PI</strong> (Peripheral Iridectomy)",
    "<strong>Cyclo Cryo</strong> (Cyclo Cryotherapy)"
]


    
    return render_template('service_details.html',heading=heading,side_heading=side_heading,description=description,why_choose_us=why_choose_us,services=services)

@app.route('/corneal_surgery')
def corneal_surgery():
    heading="Corneal Surgery Unveiled"
    side_heading= "Corneal Surgery Services We Offer"
    
    description="""
    <p>Corneal surgery is a specialized procedure aimed at treating various conditions affecting the cornea, the transparent front part of the eye. This surgery addresses issues such as corneal infections, dystrophies, injuries, and refractive errors. Our dedicated team of experts brings a wealth of experience and skill to provide optimal care for your corneal health.<br><br>
    
    At our hospital, we take pride in being at the forefront of corneal surgery. Our specialists are well-versed in the latest techniques and technologies, ensuring precision and successful outcomes. Whether you require a corneal transplant, refractive surgery, or treatment for a specific corneal condition, trust in our expertise to deliver the highest standard of care.<br><br>
    
    Experience the difference with our patient-centric approach, advanced facilities, and a commitment to your visual well-being. Your journey to clearer, healthier vision begins with our proficiency in corneal surgery.</p>
    """
    
    why_choose_us = [
    "<b><strong>Expert Ophthalmologists:</strong></b> Our skilled specialists bring precision and expertise to corneal surgery.",
    "<b><strong>Laser-Sharp Focus:</strong></b> Our surgeons specialize in intricate corneal surgeries, utilizing the latest advancements with a laser-sharp focus on precision.",
    "<b><strong>Innovative Techniques:</strong></b> Experience cutting-edge corneal procedures customized to your unique condition, utilizing innovative techniques for optimal outcomes.",
    "<b><strong>Personalized Precision:</strong></b> Recognizing the individuality of each case, we provide personalized precision in every aspect of your corneal surgery, ensuring a bespoke approach to your needs.",
    "<b><strong>Technologically Advanced Facilities:</strong></b> Navigate your corneal surgery journey with confidence in our state-of-the-art facilities, equipped with the latest technology for unparalleled precision.",
    "<b><strong>Proven Excellence:</strong></b> Rely on our proven track record of successful corneal surgeries, driven by a team committed to achieving excellence in every procedure."
]
    services=[
    "<strong>CIR</strong> (Corneal Injury Repair)",
    "<strong>PK</strong> (Penetrating Keratoplasty) - Optical",
    "<strong>PK</strong> (Penetrating Keratoplasty) - Therapeutic",
    "<strong>Therapeutic PK + C&S</strong> (Culture + Sensitivity)",
    "<strong>PK + ECCE + PMMA IOL</strong>",
    "<strong>PK + ECCE + Square Edge PMMA IOL</strong>",
    "<strong>PK + ECCE + Foreign PMMA IOL</strong>",
    "<strong>PK + ECCE + 3P Aurolab IOL</strong>",
    "<strong>PK + ECCE + 3P Foldable IOL</strong>",
    "<strong>DSEK</strong> (Descemet Stripping Endothelial Keratoplasty)",
    "<strong>DSEK + SICS + PMMA IOL</strong>",
    "<strong>DSEK + SICS + PMMA Square Edge IOL</strong>",
    "<strong>DSEK + SICS + Foreign PMMA IOL</strong>",
    "<strong>DSEK + SICS + 3P Aurolab IOL</strong>",
    "<strong>DSEK + SICS + 3P Foldable IOL</strong>",
    "<strong>DSEK + Phaco + 3P Foldable IOL</strong>",
    "<strong>DSEK + Phaco + Hydrophobic Foldable IOL</strong>",
    "<strong>DSEK + Phaco + Tecnis/Alcon IQ Foldable IOL</strong>",
    "<strong>DSEK + Phaco + 3P Foldable IOL</strong>",
    "<strong>DSEK + SFIOL (3P Foldable)</strong>",
    "<strong>DSEK + SFIOL (3P Aurolab)</strong>",
    "<strong>DSEK + SFIOL (Sutured)</strong>",
    "<strong>DALK</strong> (Deep Anterior Lamellar Keratoplasty)",
    "<strong>DALK + SICS + PMMA IOL</strong>",
    "<strong>DALK + SICS + PMMA Square Edge IOL</strong>",
    "<strong>DALK + SICS + Foreign PMMA IOL</strong>",
    "<strong>DALK + SICS + 3P Aurolab IOL</strong>",
    "<strong>DALK + Phaco + Hydrophilic Foldable IOL</strong>",
    "<strong>DALK + Phaco + Foldable Aspheric IOL</strong>",
    "<strong>DALK + Phaco + Foldable Hydrophobic IOL</strong>",
    "<strong>DALK + Phaco + Tecnis/Alcon IQ IOL</strong>",
    "<strong>DALK + Phaco + Hanita IOL</strong>",
    "<strong>DALK + Phaco + 3P Foldable IOL</strong>",
    "<strong>PG</strong> (Patch Graft)",
    "<strong>FND</strong> (Fine Needle Diathermy)",
    "<strong>SLET</strong> (Simple Limbal Epithelial Transplantation)",
    "<strong>AMT</strong> (Amniotic Membrane Transplantation)",
    "<strong>Gunderson Flap</strong>",
    "<strong>Conjunctival Hooding</strong>",
    "<strong>Suture Removal (in OT)</strong>",
    "<strong>Pterygium Excision + AG</strong> (Autograft) + <strong>FG</strong> (Fibrin Glue)",
    "<strong>Pterygium Excision + AG</strong> (Autograft)",
    "<strong>DP</strong> (Double Pterygium) + <strong>AG</strong> (Autograft)",
    "<strong>DP</strong> (Double Pterygium) + <strong>AG</strong> (Autograft) + <strong>FG</strong> (Fibrin Glue)",
    "<strong>PE + AMT</strong> (Amniotic Membrane Transplantation)",
    "<strong>PE + AMT</strong> (Amniotic Membrane Transplantation) + <strong>MMC</strong>",
    "<strong>PE + AMT</strong> (Amniotic Membrane Transplantation) + <strong>FG</strong> (Fibrin Glue)",
    "<strong>MMG</strong> (Mucous Membrane Graft)",
    "<strong>EB</strong> (Excision Biopsy) - Major + <strong>HA</strong> (Histopathological Analysis)",
    "<strong>EB</strong> (Excision Biopsy) - Minor + <strong>HA</strong> (Histopathological Analysis)",
    "<strong>EB</strong> (Excision Biopsy) - Major",
    "<strong>EB</strong> (Excision Biopsy) - Minor",
    "<strong>C&S</strong> (Culture & Sensitivity)",
    "<strong>CS</strong> (Corneal Scraping)",
    "<strong>CS + C&S</strong> (Corneal Scraping + Culture & Sensitivity)",
    "<strong>CB + C&S + PFG</strong> (Corneal Biopsy + Culture & Sensitivity + Patch/Full Graft)",
    "<strong>ACW + C&S</strong> (AC Wash + Culture & Sensitivity)",
    "<strong>IV/A IV/B</strong> (Intrastromal/Intracameral Voriconazole/Amphotericin B)",
    "<strong>FBR</strong> (Foreign Body Removal) - OT",
    "<strong>FBR</strong> - Intraocular (Anterior Segment)",
    "<strong>Resuturing</strong>",
    "<strong>ACW</strong> (AC Wash)",
    "<strong>POR</strong> (Post-operative Repair or AC Wash)",
    "<strong>CG + BCL</strong> (Cyanoacrylate Glue + BCL)"

    ]
    return render_template('service_details.html',heading=heading,side_heading=side_heading,description=description,why_choose_us=why_choose_us,services=services)

@app.route('/refractive_surgery')
def refractive_surgery():
    heading="Refractive Precision Unveiled"
    side_heading="Explore Our Advanced Refractive Surgery Services"
    
    description="""
    <p>Embark on a journey to redefine your vision with our state-of-the-art Refractive Surgery services. At our esteemed institution, we take pride in being leaders in the field, offering a range of cutting-edge procedures designed to enhance and restore your eyesight. Our team of skilled surgeons brings a wealth of experience and expertise to ensure optimal outcomes tailored to your unique needs.<br><br>
    Refractive Surgery goes beyond correcting vision; it's about unveiling a world of clarity and visual freedom. Whether it's LASIK, PRK, or other advanced techniques, we are committed to providing personalized care that prioritizes your safety, comfort, and satisfaction. Our dedication to excellence is reflected in the precision of our procedures and the comprehensive assessments conducted to determine the most suitable treatment plan for you.<br><br>
    What sets us apart is not just our proficiency in Refractive Surgery but our unwavering commitment to delivering exceptional patient-centric care. From the moment you step into our facility, you become part of our family, and we guide you through each step of the process, ensuring a seamless and comfortable experience. Trust us to be your partners in achieving the clear, vibrant vision you deserve. Your journey to visual excellence begins here, where expertise meets compassion.</p>
    """
    why_choose_us = [
    "<b><strong>Refractive Pioneers:</strong></b> Our skilled specialists bring precision and expertise to refractive surgery.",
    "<b><strong>Cutting-Edge Vision:</strong></b> Surgeons specializing in intricate refractive surgeries, utilizing the latest advancements with a laser-sharp focus on precision.",
    "<b><strong>Innovative Refraction:</strong></b> Experience cutting-edge refractive procedures customized to your unique condition, utilizing innovative techniques for optimal outcomes.",
    "<b><strong>Personalized Clarity:</strong></b> Recognizing the individuality of each case, we provide personalized precision in every aspect of your refractive surgery, ensuring a bespoke approach to your needs.",
    "<b><strong>Technologically Advanced Facilities:</strong></b> Navigate your refractive surgery journey with confidence in our state-of-the-art facilities, equipped with the latest technology for unparalleled precision.",
    "<b><strong>Proven Refractive Excellence:</strong></b> Rely on our proven track record of successful refractive surgeries, driven by a team committed to achieving excellence in every procedure."
]
    services = [
    "<strong>ICL Spherical</strong> (per eye)",
    "<strong>ICL Toric</strong> (per eye)",
    "<strong>IPCL Spherical</strong> (per eye)",
    "<strong>IPCL Toric</strong> (per eye)",
    "<strong>OCULOPLASTY</strong>",
    "<strong>ABSCESS DRAINAGE</strong>",
    "<strong>AMRIOTEC MEMBRANCE GRAFT</strong>",
    "<strong>ANTERIOR STROMAL PUNCTURE</strong>",
    "<strong>BLEPHARO Plasty</strong>",
    "<strong>CANALICULAR TEAR REPAIR WITH MINI MONOKA STENT</strong>",
    "<strong>CHALAZION</strong>",
    "<strong>Conformer + Tasorrphy</strong>",
    "<strong>CONJUCTIVAL REPAIR MINOR</strong>",
    "<strong>CRYOTHERAPY</strong>",
    "<strong>CUTTER BEARD STAGE 1</strong>",
    "<strong>CUTTER BEARD STAGE 2</strong>",
    "<strong>DCR (CONVENTIONAL)</strong>",
    "<strong>DCT</strong>",
    "<strong>DERMIS FAT GRAFT</strong>",
    "<strong>ECTROPION</strong>",
    "<strong>EDTA CHELATION</strong>",
    "<strong>Electroepilation</strong>",
    "<strong>ENTROPION (LOWER LID)</strong>",
    "<strong>ENTROPION (UPPER LID)</strong>",
    "<strong>ENUCLEATION + BALL IMPLANT (CONFORMER)</strong>",
    "<strong>ENUCLEATION + BALL IMPLANT ( Therapeutec)</strong>",
    "<strong>EPICANTHUS</strong>",
    "<strong>Everting Sutures</strong>",
    "<strong>EVISCERATION</strong>",
    "<strong>EVISCERATION + BALL IMPLANT (CONFORMER)</strong>",
    "<strong>EVISCERATION + BALL IMPLANT (THERAPEUTEC)</strong>",
    "<strong>EVISERATION BIOPORE/HYDROX</strong>",
    "<strong>EXCISION BIOPSY (MAJOR)</strong>",
    "<strong>EXCISION BIOPSY (MINOR)</strong>",
    "<strong>EXENTERATION</strong>",
    "<strong>TENZELS FLAP (EYELID RECONSTRUCTION)</strong>",
    "<strong>EYELID TEAR REPAIR (MAJOR)</strong>",
    "<strong>EYELID TEAR REPAIR (MINOR)</strong>",
    "<strong>FISTULECTOMY</strong>",
    "<strong>FORNIX RECONSTRUCTION</strong>",
    "<strong>FRACTURE REPAIR (FLOOR)</strong>",
    "<strong>FRONIX FORNING SUTURES ONE EYELID</strong>",
    "<strong>FULL THICKNESS SKIN GRAFT</strong>",
    "<strong>Imported Customised Ocular Prosthesis</strong>",
    "<strong>INCISION BIOPSY</strong>",
    "<strong>Indian Customised Ocular Porthesis</strong>",
    "<strong>INTRUBRATION DCR/ Revision DCR/ LASER DCR</strong>",
    "<strong>IRISPROLOPSE</strong>",
    "<strong>Inj Botox</strong>",
    "<strong>INJ BOTOX 10U</strong>",
    "<strong>INJ BOTOX 25U</strong>",
    "<strong>INJ BOTOX 40U</strong>",
    "<strong>HOLLOW PROSTHESIS</strong>",
    "<strong>SELF LUBRICATING PROSTHESIS</strong>",
    "<strong>IRIS PAINTED CONFORMER</strong>",
    "<strong>TEMPORARY PROSTHESIS</strong>",
    "<strong>SCLERAL SHELL</strong>",
]

    return render_template('service_details.html',heading=heading,side_heading=side_heading,description=description,why_choose_us=why_choose_us,services=services,count=len(services))

@app.route('/retina_injection')
def retina_injection():
    heading="Precision Care for Your Retina"
    side_heading="Discover Our Specialized Retina Injection Services"
    
    description="""
    <p>SitapurNethralaya is your premier destination for specialized Retina Injection services, where our expert team is dedicated to delivering precise and targeted injections for specific retinal conditions. With a focus on expertise, our specialists bring advanced knowledge to ensure the highest standard of care for your retinal health.<br><br>
    Our commitment extends to providing tailored injection therapies designed for various retinal disorders, including diabetic retinopathy and macular degeneration. Each injection is carefully crafted to address your unique condition, reflecting our dedication to personalized treatment.<br><br>
    Utilizing cutting-edge technology, we administer injections with utmost precision, delivering medications directly to affected retinal areas for optimal therapeutic benefits. Before any injection therapy, our experienced team conducts thorough evaluations, ensuring an accurate diagnosis and a treatment plan tailored to your individual needs.<br><br>
    At SitapurNethralaya, our patient-centric approach ensures not only top-notch medical care but also a supportive and empathetic environment throughout your Retina Injection journey. Trust us for expert care, where precision meets personalized treatment, guiding you towards optimal retinal wellness.</p>
    """
    
    why_choose_us = [
    "<b><strong>Expert Specialists:</strong></b> Our dedicated team of specialists brings extensive experience to Retina Injection services, ensuring your retinal health is in skilled and proven hands.",
    "<b><strong>Personalized Treatment:</strong></b> Tailoring each injection therapy to your unique retinal condition, we provide precision-focused treatments crafted for maximum effectiveness.",
    "<b><strong>Cutting-Edge Technology:</strong></b> With state-of-the-art equipment, SitapurNethralaya delivers Retina Injections with unparalleled precision, staying at the forefront of technological advancements.",
    "<b><strong>Comprehensive Evaluations:</strong></b> Thorough assessments before treatment allow for accurate diagnoses, ensuring targeted and effective Retina Injection therapies.",
    "<b><strong>Patient-Centric Care:</strong></b> Beyond medical expertise, our patient-centric approach prioritizes your comfort and well-being throughout the entire Retina Injection journey."
]
    
    services = [
    "<strong>Inj. Lucentis</strong>",
    "<strong>Razumab Inj</strong>",
    "<strong>ozurdex Inj</strong>",
    "<strong>I.V.T.A.</strong>",
    "<strong>INJ (AVASTIN)</strong>",
    "<strong>RETINA+CATARACT</strong>",
    "<strong>VITRECTOMY+BB+EL+SOI+PHACO FOLDABLE LENS</strong>",
    "<strong>VITRECTOMY+BB+EL+SOI+SICS+GOVT. IOL</strong>",
    "<strong>VITRECTOMY+ILM PEELING+GAS+PHACO FOLDABLE LENS</strong>",
    "<strong>VITRECTOMY+MP+EL+SOI+PHACO FOLDABLE LENS</strong>",
    "<strong>PHACO FOLDABLE LENS+SOR</strong>",
    "<strong>SICS + FOREIGN LENS +IVTA</strong>",
    "<strong>FOREIGN BODY REMOVAL (MICROSCOPE)</strong>",
    "<strong>Resuturing</strong>",
    "<strong>AC WASH</strong>",
    "<strong>INTRAOCULAR FB REMOVAL (ANT.SEGME)</strong>",
    "<strong>POST OPERATIVE REPAIR OR WASH</strong>",
    "<strong>G.A.</strong>",
    "<strong>EXTENDED GA</strong>",
    "<strong>G.A.</strong>",
    "<strong>I.V. GA</strong>",
    "<strong>Stand by GA</strong>",
    "<strong>Short GA</strong>",
    "<strong>E.U.A.</strong>",
]
    return render_template('service_details.html',heading=heading,side_heading=side_heading,description=description,why_choose_us=why_choose_us,services=services,count=len(services))



    
    

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
