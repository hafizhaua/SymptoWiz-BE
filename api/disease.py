import pandas as pd


def get_disease_info(name):
    disease_dict = {
        # BAGIAN REI
        "Drug Reaction": {
            "description": "An adverse drug reaction (ADR) is an injury caused by taking medication. ADRs may occur following a single dose or prolonged administration of a drug or result from the combination of two or more drugs.",
            "precautions": [
                "stop irritation",
                "consult nearest hospital",
                "stop taking drug",
                "follow up",
            ],
            "symptoms": [
                "Skin rash",
                "Hives",
                "Shortness of breath",
                "Fever",
                "Seizure",
            ],
            "doctors": [
                {
                    "name": "Allergist",
                    "description": "Allergists are qualified to diagnose and treat conditions like hay fever, food allergies and intolerances, eczema, psoriasis, asthma, and certain types of sinus and ear infections, among others.",
                },
            ],
            "image": "https://www.nejm.org/na101/home/literatum/publisher/mms/journals/content/nejm/2022/nejm_2022.387.issue-2/nejmicm2116076/20220711/images/img_large/nejmicm2116076_f1.jpeg",
        },
        "Malaria": {
            "description": "An infectious disease caused by protozoan parasites from the Plasmodium family that can be transmitted by the bite of the Anopheles mosquito or by a contaminated needle or transfusion. Falciparum malaria is the most deadly type.",
            "precautions": [
                "Consult nearest hospital",
                "avoid oily food",
                "avoid non veg food",
                "keep mosquitos out",
            ],
            "symptoms": [
                "Fever",
                "Chills",
                "General feeling of discomfort",
                "Headache",
                "Nausea and vomiting",
                "Diarrhea",
                "Abdominal pain",
                "Muscle or joint pain",
                "Fatigue",
                "Rapid breathing",
                "Rapid heart rate",
                "Cough",
            ],
            "doctors": [
                {
                    "name": "Infectious Disease Doctor (ID)",
                    "description": "Infectious disease doctors are trained in clinical and laboratory skills to make the right diagnoses and organize the best treatment plans.",
                },
            ],
            "image": "https://post.medicalnewstoday.com/wp-content/uploads/sites/3/2022/01/know_-malaria_GettyImages959911388_Thumb-2.jpg",
        },
        "Allergy": {
            "description": "An allergy is an immune system response to a foreign substance that's not typically harmful to your body.They can include certain foods, pollen, or pet dander. Your immune system's job is to keep you healthy by fighting harmful pathogens.",
            "precautions": [
                "apply calamine",
                "cover area with bandage",
                "use ice to compress itching",
            ],
            "symptoms": [
                "Itchy, watery eyes",
                "Sneezing",
                "Hives (a rash with raised red patches)",
                "Vomiting",
            ],
            "doctors": [
                {
                    "name": "Allergist",
                    "description": "Allergists are qualified to diagnose and treat conditions like hay fever, food allergies and intolerances, eczema, psoriasis, asthma, and certain types of sinus and ear infections, among others.",
                },
                {
                    "name": "Otolaryngologist (ENT)",
                    "description": "The ENT surgeon is therefore a doctor who specializes in evaluating and treating patients with ear, nose (including sinuses) and throat (including voice and speech) disorders. In addition, they also manage patients with head and neck cancers as well as surgical treatment of obstructive sleep apnea.",
                },
            ],
            "image": "https://d3b6u46udi9ohd.cloudfront.net/wp-content/uploads/2022/08/24072619/Food-causing-allergy.jpg",
        },
        "Hypothyroidism": {
            "description": "Hypothyroidism, also called underactive thyroid or low thyroid, is a disorder of the endocrine system in which the thyroid gland does not produce enough thyroid hormone.",
            "precautions": [
                "reduce stress",
                "exercise",
                "eat healthy",
                "get proper sleep",
            ],
            "symptoms": [
                "tiredness",
                "being sensitive to cold",
                "weight gain",
                "constipation",
                "muscle aches and weakness",
                "muscle cramps",
            ],
            "doctors": [
                {
                    "name": "Endocrinologist",
                    "description": "An endocrinologist is particularly knowledgeable about the function of the thyroid gland and the body's other hormone-secreting glands.",
                },
            ],
            "image": "https://www.niddk.nih.gov/-/media/Images/Health-Information/Endocrine-Diseases/ThyroidAnatomy_758x864.jpg",
        },
        "Psoriasis": {
            "description": "Psoriasis is a common skin disorder that forms thick, red, bumpy patches covered with silvery scales. They can pop up anywhere, but most appear on the scalp, elbows, knees, and lower back. Psoriasis can't be passed from person to person. It does sometimes happen in members of the same family.",
            "precautions": [
                "wash hands with warm soapy water",
                "stop bleeding using pressure",
                "consult doctor",
                "salt baths",
            ],
            "symptoms": [
                "Scale (a dry, thin, and silvery-white coating) covers some plaques",
                "Smooth, red patches of skin that look raw",
                "Little, if any, silvery-white coating",
                "Sore or painful skin",
            ],
            "doctors": [
                {
                    "name": "Dermatologist",
                    "description": "A dermatologist is a medical doctor who specializes in conditions that affect the skin, hair, and nails. Whether it's rashes, wrinkles, psoriasis, or melanoma, no one understands your skin, hair, and nails better than a board-certified dermatologist.",
                },
                {
                    "name": "Rheumatologist",
                    "description": "This is a doctor who specializes in treating arthritis and other problems with the joints, muscles, and bones. They can treat any joint pain caused by psoriasis.",
                },
            ],
            "image": "https://post.healthline.com/wp-content/uploads/2022/04/Scalp-psoriasis-1296x728-slide5.jpg",
        },
        "GERD": {
            "description": "Gastroesophageal reflux disease, or GERD, is a digestive disorder that affects the lower esophageal sphincter (LES), the ring of muscle between the esophagus and stomach. Many people, including pregnant women, suffer from heartburn or acid indigestion caused by GERD.",
            "precautions": [
                "avoid fatty spicy food",
                "avoid lying down after eating",
                "maintain healthy weight",
                "exercise",
            ],
            "symptoms": [
                "A burning sensation in your chest (heartburn), usually after eating, which might be worse at night or while lying down",
                "Backwash (regurgitation) of food or sour liquid",
                "Upper abdominal or chest pain",
                "Trouble swallowing (dysphagia)",
                "Sensation of a lump in your throat",
            ],
            "doctors": [
                {
                    "name": "Gastroenterologist ",
                    "description": "A gastroenterologist is a physician with specialized training in managing diseases of the gastrointestinal tract (esophagus, stomach, small intestine, colon and rectum, pancreas, gallbladder, bile ducts and liver).",
                },
                {
                    "name": "Otolaryngologist",
                    "description": "They are also known as an ENT, or ear, nose, and throat specialist. If you have stomach acid that spills into your throat or voice box, you may have laryngopharyngeal reflux (LPR) instead of, or in addition to, GERD. Otolaryngologists have experience diagnosing and treating both conditions.",
                },
            ],
            "image": "https://assets.medpagetoday.net/media/images/90xxx/90511.jpg",
        },
        "Chronic cholestasis": {
            "description": "Chronic cholestatic diseases, whether occurring in infancy, childhood or adulthood, are characterized by defective bile acid transport from the liver to the intestine, which is caused by primary damage to the biliary epithelium in most cases",
            "precautions": [
                "cold baths",
                "anti itch medicine",
                "consult doctor",
                "eat healthy",
            ],
            "symptoms": [
                "jaundice, which is a yellowing of your skin and the white of your eyes",
                "dark urine",
                "light-colored stool",
                "pain in your abdomen",
                "fatigue",
                "nausea",
                "excessive itching",
            ],
            "doctors": [
                {
                    "name": "Gastroenterologist",
                    "description": "A gastroenterologist is a physician with specialized training in managing diseases of the gastrointestinal tract (esophagus, stomach, small intestine, colon and rectum, pancreas, gallbladder, bile ducts and liver).",
                },
                {
                    "name": "Internal Medicine",
                    "description": "nternal medicine or general internal medicine (in Commonwealth nations) is the medical specialty dealing with the prevention, diagnosis, and treatment of internal diseases. Doctors specializing in internal medicine are called internists, or physicians (without a modifier) in Commonwealth nations.",
                },
            ],
            "image": "https://medlineplus.gov/images/PX0001UT_PRESENTATION.jpeg",
        },
        "hepatitis A": {
            "description": "Hepatitis A is a highly contagious liver infection caused by the hepatitis A virus. The virus is one of several types of hepatitis viruses that cause inflammation and affect your liver's ability to function.",
            "precautions": [
                "Consult nearest hospital",
                "wash hands through",
                "avoid fatty spicy food",
                "medication",
            ],
            "symptoms": [
                "Yellow skin or eyes",
                "Not wanting to eat",
                "Upset stomach",
                "Throwing up",
                "Stomach pain",
                "Dark urine or light- colored stools",
            ],
            "doctors": [
                {
                    "name": "Hepatologist",
                    "description": "Hepatologist: A gastroenterologist with extensive training in liver disease is a hepatologist. These physicians are subspecialists with many years of training and are experts in all the diseases that affect the liver, especially hepatitis.",
                },
            ],
            "image": "https://cdn.aarp.net/content/dam/aarp/health/drugs_supplements/2020/10/1140-hepatitis-a.jpg",
        },
        "Osteoarthristis": {
            "description": "Osteoarthritis is the most common form of arthritis, affecting millions of people worldwide. It occurs when the protective cartilage that cushions the ends of your bones wears down over time.",
            "precautions": [
                "acetaminophen",
                "consult nearest hospital",
                "follow up",
                "salt baths",
            ],
            "symptoms": [
                "Pain. Affected joints might hurt during or after movement.",
                "Stiffness. Joint stiffness might be most noticeable upon awakening or after being inactive",
                "Tenderness",
                "Loss of flexibility.",
                "Grating sensation",
                "Bone spurs",
                "Swelling",
            ],
            "doctors": [
                {
                    "name": "Rheumatologists",
                    "description": "heumatologists are specialists in arthritis and diseases that involve bones, muscles and joints. They are trained to make difficult diagnoses and to treat all types of arthritis, especially those requiring complex treatment. You may be referred to an orthopedist if you have a type of degenerative arthritis.",
                },
            ],
            "image": "https://hulc.ca/wp-content/uploads/2019/01/osteo-hands.jpg?w=624",
        },
        # END OF BAGIAN REI
        # START OF BAGIAN TASYA
        "(vertigo) Paroymsal  Positional Vertigo": {
            "description": "Benign paroxysmal positional vertigo (BPPV) is one of the most common causes of vertigo — the sudden sensation that you're spinning or that the inside of your head is spinning. Benign paroxysmal positional vertigo causes brief episodes of mild to intense dizziness.",
            "precautions": [
                "lie down",
                "avoid sudden change in body",
                "avoid abrupt head movment",
                "relax",
                "use pillows for support",
                "be cautious when changing positions",
                "stay hydrated",
                "manage stress",
            ],
            "symptoms": [
                "Brief Episodes of Vertigo",
                "Positional Triggers",
                "Nystagmus",
                "Imbalance and Unsteadiness",
                "Nausea and Vomiting",
            ],
            "doctors": [
                {
                    "name": "Primary Care Physician",
                    "description": "Your primary care physician can be the first point of contact for evaluating your symptoms. They can perform an initial assessment, take your medical history, and refer you to a specialist if necessary.",
                },
                {
                    "name": "Otolaryngologist",
                    "description": "Also known as an ear, nose, and throat (ENT) specialist, an otolaryngologist is a physician who specializes in conditions related to the ear, including vertigo. They have expertise in diagnosing and treating various forms of vertigo, including BPPV.",
                },
                {
                    "name": "Neurologist",
                    "description": "Neurologists are specialists who diagnose and treat disorders of the nervous system, which includes conditions like vertigo. They can help evaluate the underlying causes of vertigo, including BPPV, and provide appropriate management.",
                },
                {
                    "name": "Physical Therapist",
                    "description": "Physical therapists specializing in vestibular rehabilitation can play a crucial role in treating BPPV. They can perform specific maneuvers and exercises to help reposition the displaced crystals in the inner ear, which is often the cause of BPPV. Vestibular rehabilitation can be an effective treatment for managing BPPV symptoms.",
                },
            ],
            "image": "https://my.clevelandclinic.org/-/scassets/Images/org/health/articles/11858-benign-paroxysmal-positional-vertigo",
        },
        "Hypoglycemia": {
            "description": " Hypoglycemia is a condition in which your blood sugar (glucose) level is lower than normal. Glucose is your body's main energy source. Hypoglycemia is often related to diabetes treatment. But other drugs and a variety of conditions — many rare — can cause low blood sugar in people who don't have diabetes.",
            "precautions": [
                "lie down on side",
                "check in pulse",
                "drink sugary drinks",
                "consult doctor",
                "eat regular meals",
            ],
            "symptoms": [
                "Hunger",
                "Shakiness or Trembling",
                "Sweating",
                "Dizziness or lightheadedness",
                "Weakness or Fatigue",
                "Confusion or difficulty concentrating",
                "Irritability",
                "Headache",
                "Blurred Vision",
            ],
            "doctors": [
                {
                    "name": "Primary Care Physician (PCP)",
                    "description": "Your primary care physician can provide initial evaluation, diagnosis, and management of hypoglycemia. They may refer you to a specialist if needed.",
                },
                {
                    "name": "Endocrinologist",
                    "description": "An endocrinologist specializes in diagnosing and treating disorders related to hormones, including diabetes and hypoglycemia. They can offer specialized care and guidance.",
                },
                {
                    "name": "Registered Dietitian",
                    "description": "A registered dietitian can help create a personalized meal plan to maintain stable blood sugar levels and prevent episodes of hypoglycemia.",
                },
                {
                    "name": "Diabetes Educator",
                    "description": "A diabetes educator is trained to provide education and support for managing diabetes and related conditions, including hypoglycemia. They can help you understand your condition and develop self-management skills.",
                },
            ],
            "image": "https://images.everydayhealth.com/images/warning-signs-of-low-blood-sugar-1440x810.jpg?w=1110",
        },
        "Acne": {
            "description": "Acne vulgaris is the formation of comedones, papules, pustules, nodules, and/or cysts as a result of obstruction and inflammation of pilosebaceous units (hair follicles and their accompanying sebaceous gland). Acne develops on the face and upper trunk. It most often affects adolescents.",
            "precautions": [
                "bath twice",
                "avoid fatty spicy food",
                "drink plenty of water",
                "avoid too many products",
                "keep the skin clean",
                "avoid excessive touching or picking",
                "protect your skin from the sun",
            ],
            "symptoms": ["Pimples", "Blackheads", "Whiteheads", "Inflammatory Lesions"],
            "doctors": [
                {
                    "name": "Dermatologist",
                    "description": "A dermatologist is a medical professional specializing in skin health. They can diagnose and treat various skin conditions, including acne. A dermatologist may prescribe medications, recommend skincare routines, and perform procedures like extractions or acne surgeries.",
                },
                {
                    "name": "General Practitioner (GP)",
                    "description": "A general practitioner can provide initial evaluation and basic treatment for mild to moderate cases of acne. They may prescribe topical medications or refer you to a dermatologist for further management if needed.",
                },
                {
                    "name": "Esthetician",
                    "description": "An esthetician is a skincare specialist who can provide advice on skincare routines and recommend non-medical treatments for acne. They may offer facials, exfoliation treatments, and other non-invasive procedures.",
                },
            ],
            "image": "https://assets.nhs.uk/nhsuk-cms/images/S_0917_acne_M1080444.width-1534_d6DPxCE.jpg",
        },
        "Impetigo": {
            "description": "Impetigo (im-puh-TIE-go) is a common and highly contagious skin infection that mainly affects infants and children. Impetigo usually appears as red sores on the face, especially around a child's nose and mouth, and on hands and feet. The sores burst and develop honey-colored crusts.",
            "precautions": [
                "soak affected area in warm water",
                "use antibiotics",
                "remove scabs with wet compressed cloth",
                "consult doctor",
                "practice good hygiene",
                "avoid scratching",
                "maintain cleanliness",
            ],
            "symptoms": [
                "Blisters or sores",
                "Itching",
                "Rash",
                "Pain or tenderness",
                "Enlarged lymph nodes",
            ],
            "doctors": [
                {
                    "name": "Primary Care Physician (PCP)",
                    "description": "Your primary care physician, such as a family doctor, general practitioner, or internist, can diagnose and treat mild cases of impetigo. They have expertise in managing a wide range of medical conditions, including skin infections like impetigo. Your PCP can provide initial treatment and refer you to a specialist if needed.",
                },
                {
                    "name": "Dermatologist",
                    "description": "If the impetigo is severe, widespread, or not responding to initial treatments, you may be referred to a dermatologist. Dermatologists specialize in diagnosing and treating diseases and conditions related to the skin, hair, and nails. They have in-depth knowledge and experience in managing various skin infections, including impetigo.",
                },
                {
                    "name": "Pediatrician",
                    "description": "For children with impetigo, it's advisable to consult a pediatrician. Pediatricians are doctors who specialize in providing medical care for infants, children, and adolescents. They are experienced in managing skin infections specific to pediatric patients, including impetigo.",
                },
                {
                    "name": "Infectious Disease Specialist",
                    "description": "In rare cases where impetigo is severe, recurrent, or complicated, an infectious disease specialist may be involved in your care. These specialists focus on diagnosing and treating infections caused by bacteria, viruses, fungi, or parasites. They can provide expert guidance on managing challenging or atypical cases of impetigo.",
                },
            ],
            "image": "https://www.cdc.gov/groupastrep/images/impetigo-sores.png?_=53265",
        },
        "Peptic ulcer diseae": {
            "description": "Peptic ulcer disease (PUD) is a break in the inner lining of the stomach, the first part of the small intestine, or sometimes the lower esophagus. An ulcer in the stomach is called a gastric ulcer, while one in the first part of the intestines is a duodenal ulcer.",
            "precautions": [
                "avoid fatty spicy food",
                "consume probiotic food",
                "eliminate milk",
                "limit alcohol",
                "avoid irritants",
                "manage stress",
                "follow a balanced diet",
            ],
            "symptoms": [
                "Abdominal pain",
                "Nausea and vomiting",
                "Loss of appetite",
                "Heartburn or acid reflux",
                "Unexplained weight loss",
            ],
            "doctors": [
                {
                    "name": "Gastroenterologist",
                    "description": " A gastroenterologist specializes in the diagnosis and treatment of diseases and disorders of the digestive system, including peptic ulcer disease. They can perform diagnostic tests, such as endoscopy, and provide comprehensive management for your condition.",
                },
                {
                    "name": "Primary Care Physician (PCP)",
                    "description": "Your primary care physician is a good starting point for initial evaluation and management of peptic ulcer disease. They can assess your symptoms, provide guidance, and refer you to a gastroenterologist if necessary.",
                },
            ],
            "image": "https://www.gastro-liver-specialist.co.uk/shared/images/content/bus_54542/thumbnails/gastroenterologist-in-surrey-Peptic-Ulcer-Disease.jpg?cache=45252",
        },
        "Common Cold": {
            "description": "The common cold is a viral infection of your nose and throat (upper respiratory tract). It's usually harmless, although it might not feel that way. Many types of viruses can cause a common cold.",
            "precautions": [
                "drink vitamin c rich drinks",
                "take vapour",
                "avoid cold food",
                "keep fever in check",
                "hand hygiene",
                "avoid close contact",
                "cover your mouth and nose",
            ],
            "symptoms": [
                "Runny or stuffy nose",
                "Sneezing",
                "Sore throat",
                "Cough",
                "Mild headache",
                "Mild body aches",
                "Mild fever",
            ],
            "doctors": [
                {
                    "name": "Primary Care Physician (PCP)",
                    "description": "our primary care physician, such as a family doctor or general practitioner, can provide guidance, evaluate your symptoms, and suggest appropriate over-the-counter medications or treatments for symptom relief.",
                },
                {
                    "name": "Urgent Care Physician",
                    "description": "If your symptoms are severe and you cannot reach your primary care physician, you may visit an urgent care clinic. Urgent care physicians can assess your condition, provide treatment recommendations, and prescribe medications if necessary.",
                },
            ],
            "image": "https://integrisok.com/-/media/misc/woman-sneezing-sneeze-155785803.ashx?as=1&mw=720&revision=92569ed4-e998-4883-843e-21dcf76f2be1&hash=9E689C0948047788236CF4E4D8F8460B",
        },
        "Chicken pox": {
            "description": "Chickenpox is a highly contagious disease caused by the varicella-zoster virus (VZV). It can cause an itchy, blister-like rash. The rash first appears on the chest, back, and face, and then spreads over the entire body, causing between 250 and 500 itchy blisters.",
            "precautions": [
                "use neem in bathing ",
                "consume neem leaves",
                "take vaccine",
                "avoid public places",
                "hygiene practices",
                "covering blisters",
            ],
            "symptoms": [
                "Rash",
                "Fever",
                "Fatigue and malaise",
                "Headache",
                "Loss of appetite",
            ],
            "doctors": [
                {
                    "name": "Primary Care Physician (PCP)",
                    "description": "If you or your child has symptoms of chickenpox, you can start by consulting a primary care physician. They can evaluate the symptoms, confirm the diagnosis, and provide appropriate advice and treatment options.",
                },
                {
                    "name": "Pediatrician",
                    "description": "For children with chickenpox, a pediatrician is specifically trained to manage the health of infants, children, and adolescents. They can provide specialized care, guidance, and treatment tailored to the needs of children.",
                },
            ],
            "image": "https://assets.nhs.uk/nhsuk-cms/images/D2BX3G.278461f6.fill-420x280.jpg",
        },
        "Cervical spondylosis": {
            "description": "Cervical spondylosis is a general term for age-related wear and tear affecting the spinal disks in your neck. As the disks dehydrate and shrink, signs of osteoarthritis develop, including bony projections along the edges of bones (bone spurs).",
            "precautions": [
                "use heating pad or cold pack",
                "exercise",
                "take otc pain reliver",
                "consult doctor",
                "maintain good posture",
                "use a supportive pillow and mattress",
                "avoid excessive strain on the neck",
                "use proper lifting techniques",
            ],
            "symptoms": [
                "Neck pain",
                "Stiffness",
                "Headaches",
                "Numbness and tingling",
                "Muscle weakness",
            ],
            "doctors": [
                {
                    "name": "Primary Care Physician (PCP)",
                    "description": "Start by scheduling an appointment with your primary care physician. They can assess your symptoms, conduct a physical examination, and provide initial management and treatment options for cervical spondylosis.",
                },
                {
                    "name": "Orthopedic Surgeon",
                    "description": "If conservative treatments do not alleviate the symptoms or if there are complications that require surgical intervention, your primary care physician may refer you to an orthopedic surgeon. Orthopedic surgeons specialize in diagnosing and treating musculoskeletal conditions, including cervical spondylosis.",
                },
                {
                    "name": "Physical Therapist",
                    "description": "Physical therapists play a crucial role in managing cervical spondylosis by providing exercises, manual therapy, and other techniques to improve neck strength, flexibility, and overall function.",
                },
            ],
            "image": "https://www.mayoclinic.org/-/media/kcms/gbs/patient-consumer/images/2013/08/26/10/34/ds00697_im02193_mcdc_7_spondylosisthu_jpg.jpg",
        },
        "Hyperthyroidism": {
            "description": "Hyperthyroidism (overactive thyroid) occurs when your thyroid gland produces too much of the hormone thyroxine. Hyperthyroidism can accelerate your body's metabolism, causing unintentional weight loss and a rapid or irregular heartbeat.",
            "precautions": [
                "eat healthy",
                "massage",
                "use lemon balm",
                "take radioactive iodine treatment",
                "take prescribed medication",
                "manage stress",
            ],
            "symptoms": [
                "Weight loss",
                "Rapid heart rate",
                "Nervousness and irritability",
                "Heat intolerance",
                "Tremors",
                "Fatigue and weakness",
                "Changes in menstrual cycle",
            ],
            "doctors": [
                {
                    "name": "Endocrinologist",
                    "description": "An endocrinologist is a specialist who focuses on diagnosing and treating hormonal disorders, including thyroid disorders like hyperthyroidism. They can conduct comprehensive evaluations, interpret thyroid function tests, and develop personalized treatment plans.",
                },
                {
                    "name": "Primary Care Physician (PCP)",
                    "description": "Initially, you can consult with a primary care physician who can evaluate your symptoms, order thyroid function tests, and provide initial management for hyperthyroidism. They may refer you to an endocrinologist for specialized care if needed.",
                },
            ],
            "image": "https://cdnrmi-19948.kxcdn.com/cdn/ff/UokCSvf1p7VH8u4qmAWFJ7FOLTe_ERzZKR5K4qGM2HA/1592999743/public/Disease-2020-06/hyperthyroidism_2.jpg",
        },
        # END OF BAGIAN TASYA
        # START OF BAGIAN RICHARD
        "Urinary tract infection": {
            "description": "Urinary tract infection: An infection of the kidney, ureter, bladder, or urethra. Abbreviated UTI. Not everyone with a UTI has symptoms, but common symptoms include a frequent urge to urinate and pain or burning when urinating.",
            "precautions": [
                "drink plenty of water",
                "increase vitamin c intake",
                "drink cranberry juice",
                "take probiotics",
            ],
            "symptoms": [
                "Frequent urination",
                "Urgency",
                "Pain or burning sensation",
                "Blood in the urine",
                "Cloudy or strong-smelling urine",
                "Fatigue",
            ],
            "doctors": [
                {
                    "name": "Urologist",
                    "description": "A urologist specializes in the urinary tract and can diagnose and treat complex or recurrent UTIs.",
                },
                {
                    "name": "Gynecologist",
                    "description": "Women who frequently experience UTIs may consult with a gynecologist for evaluation and treatment.",
                },
                {
                    "name": "Primary care physician (PCP)",
                    "description": "Your regular doctor can diagnose and treat most uncomplicated UTIs. They may prescribe antibiotics to clear the infection.",
                },
            ],
            "image": "https://northeasternurology.com.au/wp-content/uploads/2018/12/urinary-tract-infections-1.jpg",
        },
        "Varicose veins": {
            "description": "A vein that has enlarged and twisted, often appearing as a bulging, blue blood vessel that is clearly visible through the skin. Varicose veins are most common in older adults, particularly women, and occur especially on the legs.",
            "precautions": [
                "lie down flat and raise the leg high",
                "use oinments",
                "use vein compression",
                "dont stand still for long",
            ],
            "symptoms": [
                "Visible veins",
                "Blue or purple veins",
                "Vein pain or aching",
                "Swelling",
                "Muscle cramps",
                "Itching",
                "Skin irritation",
                "Heaviness or fatigue in the legs",
            ],
            "doctors": [
                {
                    "name": "Vascular surgeon",
                    "description": " Vascular surgeons specialize in diagnosing and treating conditions affecting the blood vessels, including varicose veins.",
                },
                {
                    "name": "Phlebologist",
                    "description": "Phlebologists are physicians who specialize in the diagnosis and treatment of vein disorders, including varicose veins.",
                },
                {
                    "name": "Dermatologist",
                    "description": " Dermatologists may also be involved in the diagnosis and treatment of varicose veins, particularly if there are skin complications or concerns.",
                },
            ],
            "image": "https://veincenterofflorida.com/wp-content/uploads/2022/01/varicose-veins-vs-spider-veins-1024x683.jpg",
        },
        "AIDS": {
            "description": "Acquired immunodeficiency syndrome (AIDS) is a chronic, potentially life-threatening condition caused by the human immunodeficiency virus (HIV). By damaging your immune system, HIV interferes with your body's ability to fight infection and disease.",
            "precautions": [
                "avoid open cuts",
                "wear ppe if possible",
                "consult doctor",
                "follow up",
            ],
            "symptoms": [
                "Fatigue",
                "Rapid weight loss",
                "Recurring fever",
                "Night sweat",
                "Thrush",
                "Swollen lymph nodes",
                "Persistent diarrhea",
                "Skin rash",
            ],
            "doctors": [
                {
                    "name": "Infectious disease specialist",
                    "description": "These doctors specialize in the diagnosis and treatment of infectious diseases, including HIV/AIDS.",
                },
                {
                    "name": "HIV/AIDS specialist",
                    "description": "Some healthcare providers specialize specifically in HIV/AIDS care and have extensive experience in managing the condition.",
                },
            ],
            "image": "https://redlineindonesia.org/wp-content/uploads/2021/01/what-is-HIV.png",
        },
        "Paralysis (brain hemorrhage)": {
            "description": "Intracerebral hemorrhage (ICH) is when blood suddenly bursts into brain tissue, causing damage to your brain. Symptoms usually appear suddenly during ICH. They include headache, weakness, confusion, and paralysis, particularly on one side of your body.",
            "precautions": ["massage", "eat healthy", "exercise", "consult doctor"],
            "symptoms": [
                "Loss of muscle strength",
                "Numbness",
                "Difficulty with coordination adn balance",
                "Impaired speech",
                "Vision problems",
                "Seizures",
            ],
            "doctors": [
                {
                    "name": "Neurologist",
                    "description": " Neurologists specialize in conditions affecting the nervous system, including brain hemorrhages and their neurological consequences.",
                },
                {
                    "name": "Neurosurgeon",
                    "description": "Neurosurgeons are trained in surgical interventions for brain hemorrhages when necessary.",
                },
                {
                    "name": "Physiatrist",
                    "description": "These specialists focus on restoring function and mobility in individuals with paralysis through physical therapy, occupational therapy, and other rehabilitation methods.",
                },
            ],
            "image": "https://www.clevelandclinic.org/healthinfo/ShowImage.ashx?PIC=4514&width=420",
        },
        "Typhoid": {
            "description": "An acute illness characterized by fever caused by infection with the bacterium Salmonella typhi. Typhoid fever has an insidious onset, with fever, headache, constipation, malaise, chills, and muscle pain. Diarrhea is uncommon, and vomiting is not usually severe.",
            "precautions": [
                "eat high calorie vegitables",
                "antiboitic therapy",
                "consult doctor",
                "medication",
            ],
            "symptoms": [
                "Prolonged high fever",
                "Weakness",
                "Fatigue",
                "Abdominal pain",
                "Headache",
                "Loss of appetite",
                "Muscle pain",
                "Diarrhea",
                "Constipation",
            ],
            "doctors": [
                {
                    "name": "Infectious disease specialist",
                    "description": " These doctors specialize in the diagnosis and treatment of infectious diseases and can provide expert care for typhoid fever.",
                },
                {
                    "name": "Internal medicine physician",
                    "description": "Internal medicine doctors can diagnose and manage various medical conditions, including typhoid fever.",
                },
                {
                    "name": "Gastroenterologist",
                    "description": "If complications related to the gastrointestinal system arise, a gastroenterologist may be involved in your care.",
                },
            ],
            "image": "https://homeodoctor.co.in/wp-content/uploads/2019/04/symptoms_of_typhoid_fever.jpg",
        },
        "Hepatitis B": {
            "description": "Hepatitis B is an infection of your liver. It can cause scarring of the organ, liver failure, and cancer. It can be fatal if it isn't treated. It's spread when people come in contact with the blood, open sores, or body fluids of someone who has the hepatitis B virus.",
            "precautions": [
                "consult nearest hospital",
                "vaccination",
                "eat healthy",
                "medication",
            ],
            "symptoms": [
                "Fatigue",
                "Jaundice",
                "Joint pain",
                "Muscle pain",
                "Fever",
                "Nausea",
                "Vomiting",
                "Abdominal pain",
            ],
            "doctors": [
                {
                    "name": "Hepatologist",
                    "description": "Hepatologists are specialists in liver diseases and are the most appropriate healthcare professionals to manage hepatitis B.",
                },
                {
                    "name": "Gastroenterologist",
                    "description": "Gastroenterologists focus on the digestive system, including liver diseases such as hepatitis B.",
                },
                {
                    "name": "Infectious disease specialist",
                    "description": "These doctors specialize in the diagnosis and treatment of infectious diseases, including hepatitis B.",
                },
            ],
            "image": "https://i0.wp.com/rsud.tulungagung.go.id/wp-content/uploads/2021/07/news_20210730-1.jpg?fit=1280%2C720&ssl=1",
        },
        "Fungal infection": {
            "description": "In humans, fungal infections occur when an invading fungus takes over an area of the body and is too much for the immune system to handle. Fungi can live in the air, soil, water, and plants. There are also some fungi that live naturally in the human body. Like many microbes, there are helpful fungi and harmful fungi.",
            "precautions": [
                "bath twice",
                "use detol or neem in bathing water",
                "keep infected area dry",
                "use clean cloths",
            ],
            "symptoms": [
                "Skin rash",
                "Itching",
                "Redness",
                "Inflammation",
                "Peeling skin",
                "Flaking skin",
                "Groin discomfort",
                "Genital area discomfort",
                "White patches in the mouth",
            ],
            "doctors": [
                {
                    "name": "Dermatologist",
                    "description": "Dermatologists specialize in diagnosing and treating conditions affecting the skin, hair, and nails, including fungal infections.",
                },
                {
                    "name": "Gynecologist",
                    "description": "Women with suspected vaginal yeast infections or other fungal infections in the genital area may consult with a gynecologist.",
                },
                {
                    "name": "Dentist or oral specialist",
                    "description": "If you have symptoms of oral thrush or other fungal infections in the mouth, a dentist or oral medicine specialist can provide appropriate treatment.",
                },
            ],
            "image": "data:image/jpeg;base64,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",
        },
        "Hepatitis C": {
            "description": "Inflammation of the liver due to the hepatitis C virus (HCV), which is usually spread via blood transfusion (rare), hemodialysis, and needle sticks. The damage hepatitis C does to the liver can lead to cirrhosis and its complications as well as cancer.",
            "precautions": [
                "Consult nearest hospital",
                "vaccination",
                "eat healthy",
                "medication",
            ],
            "symptoms": [
                "Fatigue",
                "Jaundice",
                "Abdominal pain",
                "Loss of appetite",
                "Nausea",
                "Vomiting",
                "Muscle pain",
                "Joint pain",
                "Itching",
                "Easy bruising",
                "Easy bleeding",
            ],
            "doctors": [
                {
                    "name": "Hepatologist",
                    "description": "Hepatologists specialize in liver diseases and are the most appropriate healthcare professionals to manage hepatitis C.",
                },
                {
                    "name": "Gastroenterologist",
                    "description": "Gastroenterologists focus on the digestive system, including liver diseases such as hepatitis C.",
                },
            ],
            "image": "https://rsudkotabogor.org/wp-content/uploads/2022/07/hepatitis-c.jpg",
        },
        "Migraine": {
            "description": "A migraine can cause severe throbbing pain or a pulsing sensation, usually on one side of the head. It's often accompanied by nausea, vomiting, and extreme sensitivity to light and sound. Migraine attacks can last for hours to days, and the pain can be so severe that it interferes with your daily activities.",
            "precautions": [
                "meditation",
                "reduce stress",
                "use poloroid glasses in sun",
                "consult doctor",
            ],
            "symptoms": [
                "Headache",
                "Sensitivity to light",
                "Sensitivity to sound",
                "Nausea",
                "Vomiting",
                "Dizziness",
                "Sensory changes",
                "Vosual disturbances",
            ],
            "doctors": [
                {
                    "name": "Neurologist",
                    "description": "Neurologists specialize in disorders of the nervous system, including migraines. They can provide comprehensive evaluation, diagnosis, and treatment options for migraines.",
                },
                {
                    "name": "Headache specialist",
                    "description": "Some doctors specialize specifically in the diagnosis and treatment of headaches, including migraines.",
                },
            ],
            "image": "https://www.drswetech.com/wp-content/uploads/2020/08/chronicmigraineheadaches.jpg",
        },
        # END OF BAGIAN RICHARD
        # START OF BAGIAN HAFI
        "Bronchial Asthma": {
            "description": "Bronchial asthma is a medical condition which causes the airway path of the lungs to swell and narrow. Due to this swelling, the air path produces excess mucus making it hard to breathe, which results in coughing, short breath, and wheezing. The disease is chronic and interferes with daily working.",
            "precautions": [
                "switch to loose cloothing",
                "take deep breaths",
                "get away from trigger",
                "seek help",
            ],
            "symptoms": [
                "wheezing",
                "coughing",
                "shortness of breath",
                "chest tightness",
                "difficulty sleeping",
                "rapid breathing",
                "increased mucus production",
                "anxiety",
                "panic",
            ],
            "doctors": [
                {
                    "name": "Primary Care Physician",
                    "description": "Your primary care physician, such as a family doctor or internist, is often the first point of contact for healthcare. They can evaluate your symptoms, perform a physical examination, and provide initial diagnosis and treatment for asthma. They may also refer you to a specialist for further evaluation if necessary.",
                },
                {
                    "name": "Pulmonologist",
                    "description": "A pulmonologist is a medical specialist who focuses on diagnosing and treating diseases of the respiratory system, including asthma. If your primary care physician suspects or confirms asthma, they may refer you to a pulmonologist for a more detailed evaluation, specialized testing (such as lung function tests), and to develop an optimal treatment plan.",
                },
                {
                    "name": "Allergist",
                    "description": "Allergists or immunologists specialize in identifying and managing allergies, including allergic asthma. They can help determine the specific triggers that worsen your asthma symptoms through allergy testing and provide guidance on allergen avoidance strategies. They may also offer immunotherapy (allergy shots) to desensitize your immune system to specific allergens.",
                },
                {
                    "name": "Pediatrician",
                    "description": "If a child is experiencing symptoms of asthma, a pediatrician should be consulted. They are trained to diagnose and manage asthma in children and can coordinate care with other specialists if necessary",
                },
            ],
            "image": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRwypHNFHHlwwEmQvkbyjKBnbmEsWqM5kzgfA&usqp=CAU",
        },
        "Alcoholic hepatitis": {
            "description": "Alcoholic hepatitis is a diseased, inflammatory condition of the liver caused by heavy alcohol consumption over an extended period of time. It's also aggravated by binge drinking and ongoing alcohol use. If you develop this condition, you must stop drinking alcohol",
            "precautions": [
                "stop alcohol consumption",
                "consult doctor",
                "medication",
                "follow up",
            ],
            "symptoms": [
                "abdominal pain",
                "jaundice",
                "fatigue",
                "loss of appetite",
                "nausea",
                "vomiting",
                "fever",
                "ascites",
                "spider angiomas",
                "mental confusion",
            ],
            "doctors": [
                {
                    "name": "Gastroenterologist",
                    "description": "A gastroenterologist specializes in the diagnosis and treatment of diseases related to the digestive system, including the liver. They play a key role in diagnosing alcoholic hepatitis, assessing the severity of liver damage, and developing a treatment plan.",
                },
                {
                    "name": "Hepatologist",
                    "description": "A hepatologist is a specialist specifically focused on diseases of the liver. They have advanced training and expertise in managing liver diseases, including alcoholic hepatitis. In cases of severe or complicated alcoholic hepatitis, a hepatologist may be consulted for specialized care.",
                },
                {
                    "name": "Addiction Specialist",
                    "description": "As alcohol abuse is the underlying cause of alcoholic hepatitis, an addiction specialist or substance abuse counselor may be involved in your care. They can provide support, counseling, and resources to address alcohol addiction and help you achieve long-term sobriety.",
                },
                {
                    "name": "Nutritionist",
                    "description": "A nutritionist or dietitian can play a vital role in managing alcoholic hepatitis. They can provide dietary guidance, develop a nutrition plan, and ensure you receive adequate nutrients to support liver health and recovery.",
                },
                {
                    "name": "Mental Health Professional",
                    "description": "Alcohol addiction and liver disease can have a significant impact on mental health. A mental health professional, such as a psychologist or psychiatrist, may be involved in your care to address any co-occurring mental health concerns, provide counseling, and support your overall well-being.",
                },
            ],
            "image": "https://www.aafp.org/content/dam/brand/aafp/pubs/afp/issues/2022/0400/p412-f1.jpg",
        },
        "Jaundice": {
            "description": 'Yellow staining of the skin and sclerae (the whites of the eyes) by abnormally high blood levels of the bile pigment bilirubin. The yellowing extends to other tissues and body fluids. Jaundice was once called the "morbus regius" (the regal disease) in the belief that only the touch of a king could cure it',
            "precautions": [
                "drink plenty of water",
                "consume milk thistle",
                "eat fruits and high fiberous food",
                "medication",
            ],
            "symptoms": [
                "yellow skin",
                "yellow eyes",
                "yellow mucous membranes",
                "dark-colored urine",
                "pale stools",
                "fatigue",
                "abdominal pain or discomfort",
                "loss of appetite",
                "nausea",
                "vomiting",
                "itching",
                "unexplained weight loss",
                "fever",
            ],
            "doctors": [
                {
                    "name": "Gastroenterologist",
                    "description": "Gastroenterologists specialize in diagnosing and treating disorders of the digestive system, including the liver and gallbladder. They can evaluate the underlying causes of jaundice and provide appropriate management.",
                },
                {
                    "name": "Hepatologist",
                    "description": "Hepatologists are medical specialists who focus on liver diseases. They have expertise in diagnosing and managing various liver disorders that can cause jaundice.",
                },
                {
                    "name": "Hematologist",
                    "description": "Hematologists specialize in disorders of the blood and can be involved in the diagnosis and management of jaundice caused by blood-related conditions, such as hemolytic anemia.",
                },
            ],
            "image": "https://upload.wikimedia.org/wikipedia/commons/1/19/Jaundice08.jpg",
        },
        "Hepatitis E": {
            "description": "A rare form of liver inflammation caused by infection with the hepatitis E virus (HEV). It is transmitted via food or drink handled by an infected person or through infected water supplies in areas where fecal matter may get into the water. Hepatitis E does not cause chronic liver disease.",
            "precautions": [
                "stop alcohol consumption",
                "rest",
                "consult doctor",
                "medication",
            ],
            "symptoms": [
                "fatigue",
                "jaundice",
                "dark urine",
                "pale stools",
                "abdominal pain",
                "loss of appetite",
                "nausea",
                "vomiting",
                "low-grade fever",
                "muscle and joint pain",
                "itching",
            ],
            "doctors": [
                {
                    "name": "Gastroenterologist",
                    "description": "Gastroenterologists specialize in diagnosing and treating diseases of the digestive system, including viral hepatitis. They can provide evaluation, monitoring, and management of hepatitis E.",
                },
                {
                    "name": "Hepatologist",
                    "description": "Hepatologists are specialists who focus on diseases of the liver. They may be involved in the management of severe cases of hepatitis E or complications associated with the infection.",
                },
                {
                    "name": "Infectious Disease Specialist",
                    "description": "Infectious disease specialists have expertise in diagnosing and treating various infectious diseases, including viral hepatitis. They may be consulted for the diagnosis and management of hepatitis E.",
                },
            ],
            "image": "https://www.emergency-live.com/wp-content/uploads/2022/11/epatite-e-1.jpg",
        },
        "Dengue": {
            "description": "an acute infectious disease caused by a flavivirus (species Dengue virus of the genus Flavivirus), transmitted by aedes mosquitoes, and characterized by headache, severe joint pain, and a rash. — called also breakbone fever, dengue fever.",
            "precautions": [
                "drink papaya leaf juice",
                "avoid fatty spicy food",
                "keep mosquitos away",
                "keep hydrated",
            ],
            "symptoms": [
                "high fever",
                "severe headache",
                "eye pain",
                "muscle and joint pain",
                "rash",
                "nausea",
                "vomiting",
                "fatigue",
                "mild bleeding",
                "abdominal pain",
                "swollen lymph nodes",
            ],
            "doctors": [
                {
                    "name": "General Practitioner/Family Physician",
                    "description": "Your primary care physician or family doctor is often the first point of contact for initial evaluation and diagnosis of dengue. They can provide supportive care, monitor your symptoms, and manage your condition.",
                },
                {
                    "name": "Infectious Disease Specialist",
                    "description": "Infectious disease specialists specialize in diagnosing and treating various infectious diseases, including dengue. They may be consulted for complicated or severe cases of dengue.",
                },
                {
                    "name": "Pediatrician",
                    "description": "For children with dengue, a pediatrician should be consulted. They have expertise in managing dengue in children and can provide appropriate care.",
                },
                {
                    "name": "Internal Medicine Specialist",
                    "description": "Internal medicine specialists are trained in the diagnosis and treatment of adult diseases. They may be involved in the management of dengue in adults, particularly in severe cases.",
                },
            ],
            "image": "https://upload.wikimedia.org/wikipedia/commons/9/91/Denguerash.JPG",
        },
        "Hepatitis D": {
            "description": "Hepatitis D, also known as the hepatitis delta virus, is an infection that causes the liver to become inflamed. This swelling can impair liver function and cause long-term liver problems, including liver scarring and cancer. The condition is caused by the hepatitis D virus (HDV).",
            "precautions": ["consult doctor", "medication", "eat healthy", "follow up"],
            "symptoms": [
                "fatigue",
                "jaundice",
                "dark urine",
                "pale stools",
                "abdominal pain",
                "loss of appetite",
                "nausea and vomiting",
                "joint pain",
                "rapid progression",
            ],
            "doctors": [
                {
                    "name": "Gastroenterologist",
                    "description": "Gastroenterologists specialize in diagnosing and treating diseases of the digestive system, including viral hepatitis. They can provide evaluation, monitoring, and management of hepatitis D.",
                },
                {
                    "name": "Hepatologist",
                    "description": "Hepatologists are specialists who focus on diseases of the liver. They may be involved in the management of severe cases of hepatitis D or complications associated with the infection.",
                },
                {
                    "name": "Infectious Disease Specialist",
                    "description": "Infectious disease specialists have expertise in diagnosing and treating various infectious diseases, including viral hepatitis. They may be consulted for the diagnosis and management of hepatitis D, especially if there are complexities or if co-infection with other viral strains is suspected.",
                },
            ],
            "image": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRsUJVDDbp-Lgh3UCGFu9DhA8w_MOHgU5k2_DiOgPfcPg4N67iynfIcAkW08FOuRpmwJCA&usqp=CAU",
        },
        "Heart attack": {
            "description": "The death of heart muscle due to the loss of blood supply. The loss of blood supply is usually caused by a complete blockage of a coronary artery, one of the arteries that supplies blood to the heart muscle.",
            "symptoms": [
                "Chest pain or discomfort",
                "Upper body pain",
                "Shortness of breath",
            ],
            "precautions": [
                "call ambulance",
                "chew or swallow aspirin",
                "keep calm",
            ],
            "doctors": [
                {
                    "name": "Primary Care Physician (PCP)",
                    "description": "Your first step is usually to consult with a primary care physician, such as a general practitioner or family doctor. They can assess your symptoms, perform an initial evaluation, and provide basic treatments or recommend lifestyle modifications.",
                },
                {
                    "name": "Neurologist",
                    "description": "If your headaches are severe, recurrent, or accompanied by other neurological symptoms, you may be referred to a neurologist. Neurologists specialize in diagnosing and treating conditions related to the nervous system, including headaches and migraines.",
                },
                {
                    "name": "Otolaryngologist (ENT)",
                    "description": "Occasionally, headaches may be linked to sinus problems, allergies, or other ear, nose, and throat (ENT) issues. In such cases, an otolaryngologist can provide specialized evaluation and treatment.",
                },
                {
                    "name": "Dentist",
                    "description": "If your headaches are suspected to be caused by dental issues, such as temporomandibular joint (TMJ) disorders or teeth grinding (bruxism), a dentist with expertise in this area may be able to help.",
                },
            ],
            "image": "https://plus.unsplash.com/premium_photo-1661780185218-aef1faa97ebc?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=1470&q=80",
        },
        "Pneumonia": {
            "description": "Pneumonia is an infection in one or both lungs. Bacteria, viruses, and fungi cause it. The infection causes inflammation in the air sacs in your lungs, which are called alveoli. The alveoli fill with fluid or pus, making it difficult to breathe.",
            "precautions": ["consult doctor", "medication", "rest", "follow up"],
            "symptoms": [
                "Cough",
                "Fever",
                "Shortness of breath",
                "Chest pain",
                "Rapid or shallow breathing",
                "Fatigue",
                "Loss of appetite",
                "Sweating",
                "Confusion (in older adults)",
            ],
            "doctors": [
                {
                    "name": "Pulmonologist",
                    "description": "A pulmonologist specializes in diagnosing and treating diseases of the respiratory system, including pneumonia. They can evaluate symptoms, order diagnostic tests, prescribe appropriate medications, and provide respiratory support if needed.",
                },
                {
                    "name": "Infectious Disease Specialist",
                    "description": "An infectious disease specialist is trained in the diagnosis and treatment of various infectious diseases, including pneumonia. They can identify the specific cause of pneumonia, determine the most effective treatment approach, and manage complications if present.",
                },
                {
                    "name": "Primary Care Physician/Family Doctor",
                    "description": "Your primary care physician or family doctor is often the first healthcare professional you would consult for symptoms of pneumonia. They can assess your condition, order diagnostic tests, prescribe antibiotics or other medications, and refer you to a specialist if necessary.",
                },
                {
                    "name": "Critical Care Specialist/Intensivist",
                    "description": "In severe cases of pneumonia requiring intensive care, a critical care specialist or intensivist may be involved in the treatment. They have expertise in managing critically ill patients, providing advanced respiratory support, and monitoring for complications.",
                },
            ],
            "image": "https://prod-images-static.radiopaedia.org/images/1371188/0a1f5edc85aa58d5780928cb39b08659c1fc4d6d7c7dce2f8db1d63c7c737234_gallery.jpeg",
        },
        "Arthritis": {
            "description": "Arthritis is the swelling and tenderness of one or more of your joints. The main symptoms of arthritis are joint pain and stiffness, which typically worsen with age. The most common types of arthritis are osteoarthritis and rheumatoid arthritis.",
            "precautions": [
                "exercise",
                "use hot and cold therapy",
                "try acupuncture",
                "massage",
            ],
            "symptoms": [
                "Joint pain",
                "Joint stiffness",
                "Swelling in the joints",
                "Redness or warmth around the joints",
                "Decreased range of motion",
                "Joint deformities",
                "Fatigue",
                "Muscle aches",
                "Joint tenderness",
                "Difficulty performing daily activities",
            ],
            "doctors": [
                {
                    "name": "Rheumatologist",
                    "description": "A rheumatologist is a medical specialist who diagnoses and treats diseases of the joints, muscles, and bones, including arthritis. They are experts in managing various types of arthritis, developing treatment plans, prescribing medications, and providing recommendations for physical therapy or other interventions.",
                },
                {
                    "name": "Orthopedic Surgeon",
                    "description": "An orthopedic surgeon specializes in surgical treatments of musculoskeletal conditions, including severe cases of arthritis that require surgical intervention. They may perform joint replacement surgeries or other procedures to improve joint function and alleviate pain.",
                },
                {
                    "name": "Primary Care Physician/Family Doctor",
                    "description": "Your primary care physician or family doctor is often the initial point of contact for evaluating arthritis symptoms. They can assess your condition, provide initial treatment options such as pain management, prescribe medications, and refer you to a specialist if necessary.",
                },
                {
                    "name": "Physical Therapist",
                    "description": "A physical therapist specializes in the rehabilitation of musculoskeletal conditions, including arthritis. They can provide exercises, stretches, and other physical interventions to improve joint mobility, strengthen muscles, and manage pain associated with arthritis.",
                },
            ],
            "image": "https://nextcare.com/wp-content/uploads/2022/09/Joint-Img-Web.jpg",
        },
        "Gastroenteritis": {
            "description": "Gastroenteritis is an inflammation of the digestive tract, particularly the stomach, and large and small intestines. Viral and bacterial gastroenteritis are intestinal infections associated with symptoms of diarrhea , abdominal cramps, nausea , and vomiting .",
            "precautions": [
                "stop eating solid food for while",
                "try taking small sips of water",
                "rest",
                "ease back into eating",
            ],
            "symptoms": [
                "Nausea",
                "Vomiting",
                "Diarrhea",
                "Abdominal cramps",
                "Stomach pain",
                "Fever",
                "Headache",
                "Loss of appetite",
                "Dehydration",
                "Fatigue",
            ],
            "doctors": [
                {
                    "name": "Gastroenterologist",
                    "description": "A gastroenterologist specializes in diagnosing and treating disorders of the gastrointestinal tract, including gastroenteritis. They can evaluate the severity of symptoms, provide appropriate medications to manage symptoms, address complications such as dehydration, and offer guidance on dietary modifications.",
                },
                {
                    "name": "Primary Care Physician/Family Doctor",
                    "description": "Your primary care physician or family doctor is often the initial point of contact for evaluating and managing gastroenteritis symptoms. They can assess your condition, provide supportive care, prescribe medications if needed, and recommend dietary changes to help manage symptoms.",
                },
                {
                    "name": "Infectious Disease Specialist",
                    "description": "An infectious disease specialist is trained in diagnosing and managing various infectious diseases, including gastroenteritis. They can determine the cause of the infection, provide specific treatment recommendations if necessary, and address any complications or persistent symptoms.",
                },
                {
                    "name": "Pediatrician",
                    "description": "For children with gastroenteritis, a pediatrician should be consulted. They have expertise in managing gastroenteritis in children, providing appropriate treatment and monitoring for any signs of dehydration or complications.",
                },
            ],
            "image": "https://assets.pikiran-rakyat.com/crop/0x0:0x0/x/photo/2022/08/29/1567302384.jpeg",
        },
        "Tuberculosis": {
            "description": "Tuberculosis (TB) is an infectious disease usually caused by Mycobacterium tuberculosis (MTB) bacteria. Tuberculosis generally affects the lungs, but can also affect other parts of the body. Most infections show no symptoms, in which case it is known as latent tuberculosis.",
            "precautions": ["cover mouth", "consult doctor", "medication", "rest"],
            "symptoms": [
                "Persistent cough",
                "Coughing up blood or sputum",
                "Chest pain",
                "Fatigue",
                "Unintentional weight loss",
                "Loss of appetite",
                "Fever",
                "Night sweats",
                "Chills",
                "Shortness of breath",
            ],
            "doctors": [
                {
                    "name": "Pulmonologist",
                    "description": "A pulmonologist specializes in diagnosing and treating diseases of the respiratory system, including tuberculosis. They can evaluate symptoms, order diagnostic tests (such as a chest X-ray or sputum analysis), prescribe appropriate anti-tuberculosis medications, and provide long-term management of the disease.",
                },
                {
                    "name": "Infectious Disease Specialist",
                    "description": "An infectious disease specialist is trained in the diagnosis and treatment of various infectious diseases, including tuberculosis. They can confirm the diagnosis, prescribe appropriate anti-tuberculosis medications, monitor treatment response, and manage any complications or drug-resistant cases.",
                },
                {
                    "name": "Primary Care Physician/Family Doctor",
                    "description": "Your primary care physician or family doctor is often the first healthcare professional you would consult for symptoms of tuberculosis. They can perform initial assessments, order diagnostic tests, refer you to a specialist, prescribe medications, and provide follow-up care throughout the treatment process.",
                },
                {
                    "name": "Public Health Specialist",
                    "description": "Public health specialists may be involved in the management and prevention of tuberculosis, especially in settings where there is a higher risk of transmission. They work on surveillance, contact tracing, and implementation of public health measures to control the spread of the disease.",
                },
            ],
            "image": "https://i0.wp.com/dutable.com/wp-content/uploads/2021/04/000-4.jpg?fit=1200%2C630&ssl=1",
        },
        # END OF BAGIAN HAFI
    }

    return disease_dict[name]


def generate_df(symptoms):
    symptoms_list = [
        "acidity",
        "back_pain",
        "bladder_discomfort",
        "breathlessness",
        "burning_micturition",
        "chest_pain",
        "chills",
        "constipation",
        "continuous_sneezing",
        "cough",
        "cramps",
        "fatigue",
        "headache",
        "high_fever",
        "indigestion",
        "joint_pain",
        "mood_swings",
        "muscle_wasting",
        "muscle_weakness",
        "neck_pain",
        "pain_during_bowel_movements",
        "patches_in_throat",
        "pus_filled_pimples",
        "shivering",
        "skin_rash",
        "stiff_neck",
        "stomach_pain",
        "sunken_eyes",
        "vomiting",
        "weakness_in_limbs",
        "weight_gain",
        "weight_loss",
        "yellowish_skin",
        "itching",
        "abdominal_pain",
        "anxiety",
        "blackheads",
        "blister",
        "bruising",
        "cold_hands_and_feets",
        "dehydration",
        "dizziness",
        "foul_smell_of urine",
        "knee_pain",
        "lethargy",
        "loss_of_appetite",
        "nausea",
        "nodal_skin_eruptions",
        "pain_in_anal_region",
        "restlessness",
        "skin_peeling",
        "sweating",
        "swelling_joints",
        "ulcers_on_tongue",
        "weakness_of_one_body_side",
        "altered_sensorium",
        "bloody_stool",
        "blurred_and_distorted_vision",
        "continuous_feel_of_urine",
        "dark_urine",
        "diarrhoea",
        "dischromic _patches",
        "extra_marital_contacts",
        "hip_joint_pain",
        "loss_of_balance",
        "movement_stiffness",
        "obesity",
        "red_sore_around_nose",
        "scurring",
        "silver_like_dusting",
        "spinning_movements",
        "swelling_of_stomach",
        "watering_from_eyes",
        "distention_of_abdomen",
        "excessive_hunger",
        "family_history",
        "irregular_sugar_level",
        "irritation_in_anus",
        "lack_of_concentration",
        "painful_walking",
        "passage_of_gases",
        "small_dents_in_nails",
        "spotting_ urination",
        "swollen_legs",
        "yellow_crust_ooze",
        "yellowing_of_eyes",
        "history_of_alcohol_consumption",
        "inflammatory_nails",
        "internal_itching",
        "mucoid_sputum",
        "swollen_blood_vessels",
        "unsteadiness",
        "depression",
        "fast_heart_rate",
        "fluid_overload",
        "malaise",
        "prominent_veins_on_calf",
        "puffy_face_and_eyes",
        "swelled_lymph_nodes",
        "enlarged_thyroid",
        "irritability",
        "mild_fever",
        "muscle_pain",
        "phlegm",
        "yellow_urine",
        "brittle_nails",
        "drying_and_tingling_lips",
        "increased_appetite",
        "visual_disturbances",
        "pain_behind_the_eyes",
        "polyuria",
        "slurred_speech",
        "swollen_extremeties",
        "throat_irritation",
        "toxic_look_(typhos)",
        "abnormal_menstruation",
        "acute_liver_failure",
        "belly_pain",
        "receiving_blood_transfusion",
        "red_spots_over_body",
        "redness_of_eyes",
        "rusty_sputum",
        "coma",
        "palpitations",
        "receiving_unsterile_injections",
        "sinus_pressure",
        "runny_nose",
        "stomach_bleeding",
        "congestion",
        "blood_in_sputum",
        "loss_of_smell",
    ]
    pred_data = {}
    for symptom_candidate in symptoms_list:
        pred_data[symptom_candidate] = 1 if symptom_candidate in symptoms else 0

    df = pd.DataFrame(pred_data, index=[""])
    return df
