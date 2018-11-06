import json 

results = [
  {
    "brochure_id": "488",
    "title": "Biocompatibility Testing of Adhesives",
    "description": "Biocompatibility testing of adhesives is used to determine how compatible a material is within a biological environment. It is also used to predict any potentially harmful effects on the human body. The testing for this falls either under ISO 10993 or USP Class VI.",
    "thumbnail_link": "http://www.epotek.com/site/images/SAS_Biocomp_Image.jpg",
    "thumbnail": "SAS_Biocomp_Image.jpg",
    "pdf_link": "http://www.epotek.com/site/files/brochures/pdfs/SAS_Biocompatibility_Testing_of_Adhesives_2018.pdf",
    "pdf": "SAS_Biocompatibility_Testing_of_Adhesives_2018.pdf"
  },
  {
    "brochure_id": "446",
    "title": "Cryogenic Temperatures and Epoxies",
    "description": "Epoxy Technology provides optical",
    "thumbnail_link": " thermally conductive and electrically conductive adhesives for a variety of cryogenic applications. This piece discusses what happens to epoxies at these temperatures and which EPO-TEK products are best suited for this environment.",
    "thumbnail": "http://www.epotek.com/site/images/SAS_Cryo_thumbnail.jpg",
    "pdf_link": "SAS_Cryo_thumbnail.jpg",
    "pdf": "http://www.epotek.com/site/files/brochures/pdfs/SAS-_Cryogenic_Temperature_and_Epoxies.6low.pdf"
  },
  {
    "brochure_id": "371",
    "title": "Cure Matters",
    "description": "After selecting the appropriate adhesive",
    "thumbnail_link": " determining the proper cure schedule is a very important aspect to achieving optimal adhesive performance for your specific application.",
    "thumbnail": "http://www.epotek.com/site/images/Cure Matters.JPG",
    "pdf_link": "Cure Matters.JPG",
    "pdf": "http://www.epotek.com/site/files/brochures/pdfs/Cure_Matters_Final.pdf"
  },
  {
    "brochure_id": "253",
    "title": "Custom Formulation Services",
    "description": "Epoxy Technology provides custom formulating services to our customers. Leveraging our over 50+ years of specialty adhesive formulating expertise for your unique application to ensure that we meet your specific formulation requirements.",
    "thumbnail_link": "http://www.epotek.com/site/images/Custom_Formulation.jpg",
    "thumbnail": "Custom_Formulation.jpg",
    "pdf_link": "http://www.epotek.com/site/files/brochures/pdfs/Custom_Formulation_Services_2018.pdf",
    "pdf": "Custom_Formulation_Services_2018.pdf"
  },
  {
    "brochure_id": "429",
    "title": "Down-Hole Application Guide",
    "description": "Epoxy Technology presents various high temperature epoxies suited for down-hole applications that include die attach",
    "thumbnail_link": " heat sinking",
    "thumbnail": " capacitor attach",
    "pdf_link": " potting",
    "pdf": " fiber optics & sensors."
  },
  {
    "brochure_id": "258",
    "title": "EK2000 Announcement",
    "description": "Epoxy Technology announces EPO-TEK® EK1000 & EPO-TEK® EK2000. These new silver filled adhesives exhibit exceptional thermal & electrical conductivity and are now available in either a single or two component format.",
    "thumbnail_link": "http://www.epotek.com/site/images/brochures/thumbnails/ek2000_announcement.jpg",
    "thumbnail": "ek2000_announcement.jpg",
    "pdf_link": "http://www.epotek.com/site/files/brochures/pdfs/ek2000_announcement.pdf",
    "pdf": "ek2000_announcement.pdf"
  },
  {
    "brochure_id": "462",
    "title": "Electrically Conductive Adhesives with Enhanced Dispense Properties",
    "description": "Epoxy Technology presents New Electrically Conductive Adhesives with Enhanced Dispensed Properties. These materials increase the reliability of high volume dispense applications by minimizing the potential for skips or misses in the dispense process",
    "thumbnail_link": " while allowing for smaller and more accurate dot sizes.",
    "thumbnail": "http://www.epotek.com/site/images/brochures/thumbnails/ECA_with_enhanced_dispense.jpg",
    "pdf_link": "ECA_with_enhanced_dispense.jpg",
    "pdf": "http://www.epotek.com/site/files/brochures/pdfs/ECA_with_enhanced_dispense.lowres.pdf"
  },
  {
    "brochure_id": "410",
    "title": "EPO-TEK® 353ND Family of Products for Fiber Optics",
    "description": "Epoxy Technology's optical line of adhesives are used for bonding and protective coatings in various fiber optic applications. Our epoxy adhesives are frequently used to bundle optical fibers and bond components in optoelectronic devices. ",
    "thumbnail_link": "http://www.epotek.com/site/images/brochures/thumbnails/353ND_Cover.JPG",
    "thumbnail": "353ND_Cover.JPG",
    "pdf_link": "http://www.epotek.com/site/files/brochures/pdfs/fiber_9-1.pdf",
    "pdf": "fiber_9-1.pdf"
  },
  {
    "brochure_id": "444",
    "title": "EPO-TEK® 353ND Family of Products Selector Guide",
    "description": "Epoxy Technology presents a new comparative piece focused on the industry standard",
    "thumbnail_link": " EPO-TEK® 353ND",
    "thumbnail": " and it's related family of products used in semiconductor",
    "pdf_link": " hybrid",
    "pdf": " fiber optic and medical applications. This is a visual and informative piece showing where each product falls based on a variety of physical properties. "
  },
  {
    "brochure_id": "374",
    "title": "EPO-TEK® Adhesives for Concentrated Photo Voltaic (CPV)",
    "description": "Epoxy Technology offers a variety of specialty adhesives for your Concentrated Photo Voltaic (CPV) applications.",
    "thumbnail_link": "http://www.epotek.com/site/images/CPV Ann 1.JPG",
    "thumbnail": "CPV Ann 1.JPG",
    "pdf_link": "http://www.epotek.com/site/files/brochures/pdfs/CPV_flyer.pdf",
    "pdf": "CPV_flyer.pdf"
  },
  {
    "brochure_id": "373",
    "title": "EPO-TEK® Adhesives for Solar Applications",
    "description": "Epoxy Technology announces an expanded line of solar adhesive products for thin film panel assembly.",
    "thumbnail_link": "http://www.epotek.com/site/images/New Solar Products.JPG",
    "thumbnail": "New Solar Products.JPG",
    "pdf_link": "http://www.epotek.com/site/files/brochures/pdfs/New_Solar_Products.pdf",
    "pdf": "New_Solar_Products.pdf"
  },
  {
    "brochure_id": "367",
    "title": "EPO-TEK® Epoxies for Haptic Applications",
    "description": "From front end assembly to back end display manufacturing",
    "thumbnail_link": " Epoxy Technology provides specialized epoxy adhesives for touch applications including: touch",
    "thumbnail": " gesture & motion",
    "pdf_link": " multi-touch & haptic display markets. These products are formulated for exceptional quality and reliability.",
    "pdf": "http://www.epotek.com/site/images/New Haptic cover 2015.jpg"
  },
  {
    "brochure_id": "210",
    "title": "EPO-TEK® Selector Guide",
    "description": "Epoxy Technology&rsquo;s newest version of our Product Selector Guide. This piece supplies detailed product information on our full range of electrically & thermally conductive",
    "thumbnail_link": " thermally conductive/electrically insulating",
    "thumbnail": " optical/fiber optic",
    "pdf_link": " UV curing and UV hybrid epoxy adhesives. The guide allows users to easily select the optimal adhesive for their specific application; based on the best combination of physical",
    "pdf": " electrical and mechanical characteristics."
  },
  {
    "brochure_id": "490",
    "title": "EPO-TEK® Specialty Adhesives for Sensor Applications",
    "description": "Epoxy Technology Inc. has an extensive offering of specialty adhesives for SensorApplications: from Electrically Conductive",
    "thumbnail_link": " to Thermally Conductive",
    "thumbnail": " to Optical GradeAdhesives",
    "pdf_link": " as well as UV Epoxy and UV Hybrid Adhesives. Our EPO-TEK® brand adhesivesare globally recognized for quality",
    "pdf": " performance and reliability."
  },
  {
    "brochure_id": "451",
    "title": "Hybrid Chemistry Adhesives For Optoelectronics",
    "description": "UV Hybrid Adhesive Performancefrom EPO-TEK® \"Fiber-Optic Industry Standard\" EPO-TEK® 353ND Now Available with Enhanced Levels of Performance",
    "thumbnail_link": "http://www.epotek.com/site/images/brochures/thumbnails/UV_hybrid_cover2.jpg",
    "thumbnail": "UV_hybrid_cover2.jpg",
    "pdf_link": "http://www.epotek.com/site/files/brochures/pdfs/UV_Hybrid_Adhesive_tri-fold.pdf",
    "pdf": "UV_Hybrid_Adhesive_tri-fold.pdf"
  },
  {
    "brochure_id": "479",
    "title": "Epoxies in Preservation and Restoration",
    "description": "Epoxy Technology offers specialty adhesive epoxies well suited for use in Preservation and Restoration Projects.",
    "thumbnail_link": "http://www.epotek.com/site/images/SAS_Restoration_thumbnail.jpg",
    "thumbnail": "SAS_Restoration_thumbnail.jpg",
    "pdf_link": "http://www.epotek.com/site/files/SAS_Preservation_and_Restoration.pdf",
    "pdf": "SAS_Preservation_and_Restoration.pdf"
  },
  {
    "brochure_id": "248",
    "title": "Epoxy Adhesive Application Guide",
    "description": "Epoxy Technology offers our newest educational tool designed to assist adhesive users in gaining a more thorough understanding of adhesive properties and testing. The information contained within this guide is useful and invaluable for choosing the best adhesive in your specific application.",
    "thumbnail_link": "http://www.epotek.com/site/images/brochures/thumbnails/adhesive_application_guide.jpg",
    "thumbnail": "adhesive_application_guide.jpg",
    "pdf_link": "http://www.epotek.com/site/files/brochures/pdfs/adhesive_application_guide.pdf",
    "pdf": "adhesive_application_guide.pdf"
  },
  {
    "brochure_id": "483",
    "title": "Fast Curing Electrically Conductive Adhesives (ECAs)",
    "description": "Epoxy Technology",
    "thumbnail_link": " Inc. (EPO-TEK®) offers an expanded line of Fast Curing Electrically Conductive Adhesives (ECAs). These ECAs are ideal for low temperature cure capability allowing use with temperature sensitive substrates such as copper and plastics. Fast Curing ECAs are an optimal choice for manufacturing processes with high volume/high throughput.",
    "thumbnail": "http://www.epotek.com/site/images/Fast_Cure_ECA_Products_Rev_1.jpg",
    "pdf_link": "Fast_Cure_ECA_Products_Rev_1.jpg",
    "pdf": "http://www.epotek.com/site/files/brochures/pdfs/Whats_New_RD_-_Fast_Curing_ECAs.pdf"
  },
  {
    "brochure_id": "425",
    "title": "Fiber to Ferrule Bonding Guide",
    "description": "Epoxy Technology offers several optical adhesives for fiber to ferrule bonding. These products range from high to low viscosity and are grouped by the following cure types: room temperature",
    "thumbnail_link": " thermal and UV. ",
    "thumbnail": "http://www.epotek.com/site/images/brochures/thumbnails/Fiber_to_Ferrule.JPG",
    "pdf_link": "Fiber_to_Ferrule.JPG",
    "pdf": "http://www.epotek.com/site/files/brochures/pdfs/Fiber_to_Ferrule_SAS(1).pdf"
  },
  {
    "brochure_id": "461",
    "title": "Flexible Electrically Conductive Adhesives",
    "description": "Epoxy Technology presents New Flexible Electrically Conductive Adhesives. These materials are ideal for stress relief for large components or CTE mismatch parts. They also can enhance mechanical performance in thermal cycling.",
    "thumbnail_link": "http://www.epotek.com/site/images/brochures/thumbnails/Flexible_enhanced_low.jpg",
    "thumbnail": "Flexible_enhanced_low.jpg",
    "pdf_link": "http://www.epotek.com/site/files/brochures/pdfs/Flexible_enhanced_low.pdf",
    "pdf": "Flexible_enhanced_low.pdf"
  },
  {
    "brochure_id": "441",
    "title": "Glob Top Application Guide",
    "description": "Epoxy Technology offers a wide selection of optical",
    "thumbnail_link": " thermal and UV epoxies needed for glob top applications. These materials are grouped by the two main types of glob tops: single material hemispherical and two material dam-and-fill.",
    "thumbnail": "http://www.epotek.com/site/images/Glob_Top_SAS.JPG",
    "pdf_link": "Glob_Top_SAS.JPG",
    "pdf": "http://www.epotek.com/site/files/brochures/pdfs/Glob_Top_SAS(1).pdf"
  },
  {
    "brochure_id": "252",
    "title": "Halogen Free Brochure",
    "description": "Epoxy Technology offers several products meeting the stringent halogen free requirements based on IEC 61249-2-21 definition. These epoxies have been formulated to satisfy the new green initiatives in PC manufacturing and many other applications.",
    "thumbnail_link": "http://www.epotek.com/site/images/Halogen Free Piece.JPG",
    "thumbnail": "Halogen Free Piece.JPG",
    "pdf_link": "http://www.epotek.com/site/files/brochures/pdfs/EPO-TEK_Halogen_Free_Brochure.pdf",
    "pdf": "EPO-TEK_Halogen_Free_Brochure.pdf"
  },
  {
    "brochure_id": "445",
    "title": "Halogen Free* Epoxy Adhesives",
    "description": "Epoxy Technology offers New Halogen Free* Epoxy Adhesives. These products conform to environmental regulations and provide corrosion or electromigration resistance for high reliability electronic applications.",
    "thumbnail_link": "http://www.epotek.com/site/images/brochures/thumbnails/RD_Halogen.JPG",
    "thumbnail": "RD_Halogen.JPG",
    "pdf_link": "http://www.epotek.com/site/files/brochures/pdfs/Whats_New_RD_-_Halogen_Free(1).pdf",
    "pdf": "Whats_New_RD_-_Halogen_Free(1).pdf"
  },
  {
    "brochure_id": "428",
    "title": "Hard Disk Drive Application Guide",
    "description": "Epoxy Technology specializes in a large selection of epoxies (including low halogen materials) used in many coating",
    "thumbnail_link": " sealing and bonding applications required in hard disk drives. ",
    "thumbnail": "http://www.epotek.com/site/images/brochures/thumbnails/HDD_SAS.JPG",
    "pdf_link": "HDD_SAS.JPG",
    "pdf": "http://www.epotek.com/site/files/brochures/pdfs/HDD_SAS(1).pdf"
  },
  {
    "brochure_id": "372",
    "title": "How to Interpret a Datasheet",
    "description": "When selecting an EPO-TEK® product for any application",
    "thumbnail_link": " the datasheet provides excellent information",
    "thumbnail": " and is a useful first reference guide. It is therefore important that the datasheet be correctly interpreted in order to achieve the expected properties and to avoid problems with any given product.",
    "pdf_link": "http://www.epotek.com/site/images/How to Interpret Cover.JPG",
    "pdf": "How to Interpret Cover.JPG"
  },
  {
    "brochure_id": "255",
    "title": "How To Work Properly With Epoxies - Step by Step Sheet",
    "description": "Epoxy Technology announces its new instructional sheet on how to work properly with epoxies from initial receipt of the material",
    "thumbnail_link": " appropriate storage & handling",
    "thumbnail": " surface preparation",
    "pdf_link": " mixing",
    "pdf": " applying as well as choosing the most applicable cure profile."
  },
  {
    "brochure_id": "470",
    "title": "Jewelry and Watches",
    "description": "Epoxy Technology offers adhesives forjewelry and watch applications. The high-performing mechanical and physical strength properties of epoxies make them the ideal choice.",
    "thumbnail_link": "http://www.epotek.com/site/images/jewelry_US_9_2-1.jpg",
    "thumbnail": "jewelry_US_9_2-1.jpg",
    "pdf_link": "http://www.epotek.com/site/files/brochures/pdfs/jewelry_US_9.2.pdf",
    "pdf": "jewelry_US_9.2.pdf"
  },
  {
    "brochure_id": "257",
    "title": "LED Adhesive Selection",
    "description": "Epoxy Technology showcases their extensive line of LED adhesives for both Low Power (LP) and High Power (HP) LED systems. These products include electrically conductive",
    "thumbnail_link": " thermally conductive and electrically & thermally conductive materials.",
    "thumbnail": "http://www.epotek.com/site/images/brochures/thumbnails/led_flyer.jpg",
    "pdf_link": "led_flyer.jpg",
    "pdf": "http://www.epotek.com/site/files/LED_Flyer.pdf"
  },
  {
    "brochure_id": "256",
    "title": "Low Outgassing Brochure",
    "description": "Epoxy Technology announces its newly updated Low Outgassing Adhesives brochure which includes several products that now meet the NASA ASTM E595",
    "thumbnail_link": " MIL-STD 883/5011 and Telcordia GR-1221 Standards. This brochure allows users to select the most appropriate EPO-TEK material; meeting the most stringent requirements necessary in critical designs.",
    "thumbnail": "http://www.epotek.com/site/images/brochures/thumbnails/low_outgassing.jpg",
    "pdf_link": "low_outgassing.jpg",
    "pdf": "http://www.epotek.com/site/files/brochures/pdfs/low_outgassing_brochure.pdf"
  },
  {
    "brochure_id": "485",
    "title": "Medical Brochure",
    "description": "Epoxy Technology",
    "thumbnail_link": " Inc. announces its newly developed EPO-TEK® Biocompatible Medical Device Grade Products Brochure. The EPO-TEK® MED products have undergone additional specialized ISO 10933 testing from an independent outside testing laboratory. The Medical Brochure provides epoxy information and recommendations for many medical applications including: sensors",
    "thumbnail": " instruments",
    "pdf_link": " hearing aids",
    "pdf": " dental equipment"
  },
  {
    "brochure_id": "409",
    "title": "Next Generation Hybrid Adhesives",
    "description": "Epoxy Technology",
    "thumbnail_link": " Inc. presents our new Epoxy/UV Hybrid Adhesives for Optoelectronics based on the \"Industry Standard\" EPO-TEK® 353ND. This piece highlights three new hybrid products that allow initial UV tacking",
    "thumbnail": " followed by a thermal cure for overall process improvement",
    "pdf_link": " ease of handling and higher thru-put.",
    "pdf": "http://www.epotek.com/site/images/brochures/thumbnails/Hybrid_Cover.JPG"
  },
  {
    "brochure_id": "254",
    "title": "PCB Applications Guide",
    "description": "Epoxy Technology announces its latest offering for epoxy adhesive selection",
    "thumbnail_link": " our PCB Applications Guide. Applications include: IC Packaging",
    "thumbnail": " Ferrite Cores & Magnets",
    "pdf_link": " Flex PCB",
    "pdf": " Flip Chip"
  },
  {
    "brochure_id": "416",
    "title": "Room Temperature Curing ECAs",
    "description": "Epoxy Technology",
    "thumbnail_link": " Inc. (EPO-TEK®) offers an expanded line of Room Temperature Curing Electrically Conductive Adhesives (ECAs). These ECAs are ideal for temperature sensitive substrates",
    "thumbnail": " allowing for a lower stress cure",
    "pdf_link": " best for large parts as well as high stress",
    "pdf": " temperature cycled parts. These epoxies require no oven curing; reducing capital costs and giving greater flexibility for bonding various part sizes.EPO-TEK® EJ2189"
  },
  {
    "brochure_id": "424",
    "title": "Room Temperature Curing Optical Adhesives",
    "description": "Epoxy Technology presents New Room Temperature Curing Electrically Conductive Optical Adhesives. These materials are ideal for temperature sensitive substrates",
    "thumbnail_link": " no need for an oven to accomodate large parts",
    "thumbnail": " and the lowest stress cure for large parts or high stress temperature cycling.",
    "pdf_link": "http://www.epotek.com/site/images/RT_Optical_New_Color.JPG",
    "pdf": "RT_Optical_New_Color.JPG"
  },
  {
    "brochure_id": "251",
    "title": "Solar Review - Epoxy Selection",
    "description": "Epoxy Technology products have been selected by top solar panel manufacturers due their well documented and extensive use in thermal management applications and proven reliable over many years of service.",
    "thumbnail_link": "http://www.epotek.com/site/images/brochures/thumbnails/solar_flyer.jpg",
    "thumbnail": "solar_flyer.jpg",
    "pdf_link": "http://www.epotek.com/site/files/brochures/pdfs/solar_flyer.pdf",
    "pdf": "solar_flyer.pdf"
  },
  {
    "brochure_id": "474",
    "title": "Solar Ribbon Stringing with Epoxies",
    "description": "Solar ribbons can be attached with Silver-filled epoxy",
    "thumbnail_link": " often referred to as Electrically Conductive Adhesives (ECAs)",
    "thumbnail": " as well asother conductive joining materials including",
    "pdf_link": " solder and Pressure Sensitive Adhesives (PSA )tapes. Solder joining ribbons to TCO/PV layers is the mainstream process used with crystalline Si wafer cells.",
    "pdf": "http://www.epotek.com/site/images/brochures/thumbnails/SAS_Solar_Ribbon.jpg"
  },
  {
    "brochure_id": "459",
    "title": "Syringe Packaging",
    "description": "Epoxy Technology announces our worldwide syringe packaging capabilities with certified laboratories in North America",
    "thumbnail_link": " Europe and Asia. All locations utilize our specialized packaging equipment. With extensive experience in epoxy formulation and handling",
    "thumbnail": " we are able to best package EPO-TEK® materials for optimal performance.",
    "pdf_link": "http://www.epotek.com/site/images/brochures/thumbnails/syringePackaging.jpg",
    "pdf": "syringePackaging.jpg"
  },
  {
    "brochure_id": "458",
    "title": "Thermal Management Brochure",
    "description": "Epoxy Technology presents a comprehensive overview of thermal conductivity & management using EPO-TEK® products. It highlights our most advanced products: EPO-TEK EK1000",
    "thumbnail_link": " EK1000-1 & EK2000. These cutting-edge",
    "thumbnail": " silver-filled adhesives exhibit exceptional thermal/electrical coductivity and provide superior performance in high reliability applications.",
    "pdf_link": "http://www.epotek.com/site/images/brochures/thumbnails/ThK_New_front_2.jpg",
    "pdf": "ThK_New_front_2.jpg"
  },
  {
    "brochure_id": "430",
    "title": "Ultrasonic Application Guide",
    "description": "Epoxy Technology provides optical",
    "thumbnail_link": " thermally conductive and electrically conductive adhesives for ultrasound technology in the medical/heathcare",
    "thumbnail": " electronics",
    "pdf_link": " oil & gas and non destructive testing fields.",
    "pdf": "http://www.epotek.com/site/images/brochures/thumbnails/Ultrasound_SAS.JPG"
  },
  {
    "brochure_id": "375",
    "title": "Underfill Guide",
    "description": "Epoxy Technology manufactures a variety of underfills for several applications",
    "thumbnail_link": " with a key distinction being cure temperature.",
    "thumbnail": "http://www.epotek.com/site/images/SAS Underfills.JPG",
    "pdf_link": "SAS Underfills.JPG",
    "pdf": "http://www.epotek.com/site/files/brochures/pdfs/Underfill_SAS_Sheet(1).pdf"
  },
  {
    "brochure_id": "247",
    "title": "Specialty UV Curing Selector Guide",
    "description": "Epoxy Technology",
    "thumbnail_link": " Inc. offers a complete line of high performance Ultraviolet (UV) cure adhesives ranging in viscosity",
    "thumbnail": " flexibility",
    "pdf_link": " refractive index and light transmission.",
    "pdf": "http://www.epotek.com/site/images/brochures/thumbnails/uvcure_brochure_22.jpg"
  }
]

i = 0
for item in results[0].items():
	print(results[i]['title'])
	print(results[i]['description'])
	print(results[i]['thumbnail'])
	print('----------------------')
	i+=1