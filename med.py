from tkinter import *
from tkinter import Button, FLAT, Entry, Tk
wind = Tk()
wind.title('YOUR MEDICINE')
wind.geometry("800x960")
wind.attributes("-fullscreen", False)
wind.configure(bg='red')

xi = 0
yi = 0



def clear_message():
    global yi
    yi = 0
    chat_text.delete('1.0', END)

def send_message():
    global yi
    u = user_entry.get()
    user = f'{u} <You\n'
    chat_text.insert(END, user)


    if 'hello' in u:
        bot_response = 'Bot> Hello\n'
    elif 'how are you?' in u:
        bot_response = 'Bot> Im fine\n'
    elif 'Fungal infection' in u :
        bot_response = (
            'Bot> Fungal infections are any disease or condition you get from a fungus.\n'
            'They usually affect your skin, hair, nails or mucous membranes but they can also infect your lungs or other parts of your body. '
            'You’re at higher risk for fungal infections if you have a weakened immune system. '
            'Antifungal medications are usually used to treat fungal infections.\n\n'
            'Ayurvedic Treatment and prevention \n\n'
            '1. Turmeric: Curcumin fights infections, soothes itching, reduces inflammation.\n'
            '2. Neem: Powerful antifungal, antibacterial; relieves itching, reduces redness effectively.\n'
            '3. Aloe Vera: Soothing gel, antifungal properties, relieves itching, promotes healing.\n'
            '4. Garlic: Allicin fights infections, alleviates itching, reduces inflammation effectively.\n'
            '5. Tea Tree Oil: Antifungal, antibacterial; inhibits fungal growth, provides relief.\n'
            '6. Tulsi: Holy basil, antifungal, immunomodulatory; fights infection, strengthens immune response.\n'
            '7. Coconut Oil: Lauric acid\'s antifungal, moisturizing properties; soothes and heals.\n'
            '8. Ginger: Antimicrobial, anti-inflammatory; combats infection, relieves itching, promotes healing.\n'
            '9. Liquorice: Antifungal, anti-inflammatory; soothes itching, reduces redness and inflammation.\n'
            '10. Triphala: Three-fruit remedy; supports digestion, boosts immune system, aids elimination.\n'
            '11. Panchakarma: Ayurvedic detox therapy; removes toxins, strengthens immune system, aids treatment.\n'
            '12. Personalized treatments: Massage, herbal steam, specialized diet; combat infections, promote well-being.\n'
        )
    elif 'fungal infection' in u :
        bot_response = (
            'Bot> Fungal infections are any disease or condition you get from a fungus.\n'
            'They usually affect your skin, hair, nails or mucous membranes but they can also infect your lungs or other parts of your body. '
            'You’re at higher risk for fungal infections if you have a weakened immune system. '
            'Antifungal medications are usually used to treat fungal infections.\n\n'
            'Ayurvedic Treatment and prevention \n\n'
            '1. Turmeric: Curcumin fights infections, soothes itching, reduces inflammation.\n'
            '2. Neem: Powerful antifungal, antibacterial; relieves itching, reduces redness effectively.\n'
            '3. Aloe Vera: Soothing gel, antifungal properties, relieves itching, promotes healing.\n'
            '4. Garlic: Allicin fights infections, alleviates itching, reduces inflammation effectively.\n'
            '5. Tea Tree Oil: Antifungal, antibacterial; inhibits fungal growth, provides relief.\n'
            '6. Tulsi: Holy basil, antifungal, immunomodulatory; fights infection, strengthens immune response.\n'
            '7. Coconut Oil: Lauric acid\'s antifungal, moisturizing properties; soothes and heals.\n'
            '8. Ginger: Antimicrobial, anti-inflammatory; combats infection, relieves itching, promotes healing.\n'
            '9. Liquorice: Antifungal, anti-inflammatory; soothes itching, reduces redness and inflammation.\n'
            '10. Triphala: Three-fruit remedy; supports digestion, boosts immune system, aids elimination.\n'
            '11. Panchakarma: Ayurvedic detox therapy; removes toxins, strengthens immune system, aids treatment.\n'
            '12. Personalized treatments: Massage, herbal steam, specialized diet; combat infections, promote well-being.\n'
        )
    elif 'Allergy' in u:
     bot_response = (
        'Bot> Allergies are immune disorders triggered by harmless substances like pollens, dust, pet dander, food, medications, ticks, and insect bites. '
        'Symptoms include watery eyes, runny nose, sinuses, inflamed skin, hay fever, and itchy/red eyes.\n\n'
        'Ayurvedic Treatments:\n'
        '1. Choti Pippal (Long Pepper): Anti-inflammatory, immune-boosting.\n'
        '2. Shudh Gandhak (Purified Sulfur): Anti-inflammatory, antimicrobial.\n'
        '3. Giloy: Supports immune system, reduces inflammation.\n'
        '4. Ashwagandha: Adaptogenic, reduces stress, supports immune system.\n'
        '5. Ginger: Anti-inflammatory, antioxidant; potentially reduces inflammation.\n'
        '6. Brahmi: Adaptogenic, helps reduce stress.\n'
        '7. Manjistha: Anti-inflammatory, antimicrobial; supports the immune system.\n'
        '8. Daruhaldi (Indian Barberry): Bitter herb, reduces inflammation, supports immune system.\n'
    )
    elif 'allergy' in u:
     bot_response = (
        'Bot> Allergies are immune disorders triggered by harmless substances like pollens, dust, pet dander, food, medications, ticks, and insect bites. '
        'Symptoms include watery eyes, runny nose, sinuses, inflamed skin, hay fever, and itchy/red eyes.\n\n'
        'Ayurvedic Treatments:\n'
        '1. Choti Pippal (Long Pepper): Anti-inflammatory, immune-boosting.\n'
        '2. Shudh Gandhak (Purified Sulfur): Anti-inflammatory, antimicrobial.\n'
        '3. Giloy: Supports immune system, reduces inflammation.\n'
        '4. Ashwagandha: Adaptogenic, reduces stress, supports immune system.\n'
        '5. Ginger: Anti-inflammatory, antioxidant; potentially reduces inflammation.\n'
        '6. Brahmi: Adaptogenic, helps reduce stress.\n'
        '7. Manjistha: Anti-inflammatory, antimicrobial; supports the immune system.\n'
        '8. Daruhaldi (Indian Barberry): Bitter herb, reduces inflammation, supports immune system.\n'
    )
    elif 'GERD' in u:
     bot_response = (
        'Bot> Gastroesophageal Reflux Disease (GERD) is a chronic digestive disorder, characterized by stomach acid flowing back into the esophagus, leading to symptoms like heartburn and chest pain.\n'
        'Ayurveda, the ancient Indian system of medicine, takes a holistic approach to manage GERD by addressing root causes and promoting overall digestive health.\n\n'
        'Causes according to Ayurveda:\n'
        '- Agni Mandhya (low digestive fire): Weak digestion leads to toxin accumulation, irritating the esophagus.\n'
        '- Excess Pitta: Imbalance in the fire element can increase acidity and digestive tract irritation.\n'
        '- Vata Imbalance: Air element imbalance may cause constipation, gas, worsening GERD symptoms.\n\n'
        'Ayurvedic Treatment:\n'
        '- Dietary Modifications: Avoid spicy, oily, and acidic foods; eat smaller, more frequent meals; include cooling and soothing foods.\n'
        '- Herbal Remedies:\n'
        '  - Licorice (Yashtimadhu): Soothes the digestive tract, reduces inflammation.\n'
        '  - Guduchi (Tinospora cordifolia): Boosts immunity, aids esophageal healing.\n'
        '  - Amla (Indian gooseberry): Rich in antioxidants, reduces acidity.\n'
        '  - Aloe vera: Soothes the esophagus, promotes healing.\n'
        '  - Turmeric: Anti-inflammatory, reduces acid production.\n\n'
        'These Ayurvedic approaches aim to restore balance, strengthen digestion, and alleviate GERD symptoms.'
    )
    elif 'Chronic cholestasis' in u:
     bot_response = (
        'Bot> Chronic cholestasis is a condition where bile flow from the liver to the intestines is impaired for an extended period. '
        'This can lead to a buildup of bile acids in the bloodstream, causing various symptoms, including:\n'
        'Jaundice (yellowing of the skin and eyes)\nItching\nFatigue\nDark urine\nPale stools\nAbdominal pain\n'
        'There are different causes, such as:\n'
        '1. Primary biliary cholangitis (autoimmune disease)\n'
        '2. Secondary biliary cholangitis (inflammation caused by another condition)\n'
        '3. Sclerosing cholangitis (scarring of bile ducts)\n'
        '4. Liver cirrhosis\n5. Certain medications\n'
        'Ayurvedic treatments for managing symptoms and preventing complications may include:\n'
        '1. Panchakarma: Detoxification process\n'
        '2. Herbal remedies: Turmeric, milk thistle, bhringraja\n'
        '3. Dietary changes: Fruits, vegetables, whole grains; avoid processed foods, sugary drinks, alcohol\n'
        '4. Lifestyle modifications: Regular exercise, stress management, sufficient sleep\n\n'
        'Note: Ayurvedic treatments should complement, not substitute, conventional medical care. Consult a doctor for diagnosis and treatment.'
    )
    elif 'Drug Reaction' in u:
     bot_response = (
        'Bot>Ayurvedic Approach to Drug Reactions: Prevention & Treatment '
    'Prevention:\n'
    '1.Individualized approach: Ayurveda emphasizes Prakriti (unique constitution) and Vikruti (imbalances). Proper diagnosis ensures medicines align with your individual needs, minimizing adverse reactions.\n'
    '2.Quality matters: Opt for certified Ayurvedic products from reputable sources to avoid contamination and harmful additives.\n'
    '3.Dosage and duration: Follow prescribed dosage and duration meticulously. Overconsumption or prolonged use can disrupt your body\'s natural balance.\n'
    'Dietary and lifestyle adjustments: A balanced diet, adequate sleep, and stress management support detoxification and strengthen your immune system, making it more resilient to reactions.\n'
    'Treatment:\n\n'
    '1.Shodhana (purification): Panchakarma therapies like Basti (enemas) and Virechana (purgation) can help eliminate accumulated toxins and drug residues, reducing the reaction\'s severity.\n'
    '2.Srotas (channels) cleansing: Herbs like Amalaki (Indian gooseberry) and Haritaki (Terminalia chebula) promote lymphatic drainage and blood purification, aiding detoxification.\n'
    '3.Rasayana (rejuvenation): Adaptogenic herbs like Ashwagandha and Giloy enhance immunity and protect cells from further damage.\n'
    '4.Specific herbs for symptoms: Depending on the reaction, herbs like Guduchi (Tinospora cordifolia) for allergies, Manjistha (Rubia cordifolia) for skin rashes, or Yashtimadhu (licorice) for digestive discomfort can be used.'
     )
    elif 'Peptic ulcer diseae' in u:
     bot_response = (
    'Bot> Ayurvedic Approach to Peptic Ulcers:\n\n'
    'Prevention:\n'
    '1. Balance your doshas: Reduce pitta (fire) and kapha (earth) through diet and lifestyle. Avoid spicy, oily, acidic foods. Prioritize easily digestible meals, regular exercise, and stress management.\n'
    '2. Nourish the gut lining: Consume ghee, licorice root, amla, and slippery elm for their healing and protective properties.\n'
    '3. Manage stress: Practice yoga, meditation, and pranayama to reduce stress hormones that aggravate ulcers.\n\n'
    'Treatment:\n'
    '1. Panchakarma: Internal cleansing therapies like snehapana (medicated ghee), virechana (purgation), and basti (medicated enema) address the root cause of imbalance and promote healing.\n'
    '2. Herbal remedies: Licorice, yarrow, guduchi, and holy basil possess anti-inflammatory and ulcer-healing properties. Consult an Ayurvedic practitioner for personalized formulations.\n'
    '3. Diet: Follow a bland, easily digestible diet rich in milk, rice, leafy vegetables, and fruits. Avoid spicy, acidic, and processed foods.\n'
    '4. Lifestyle modifications: Ensure adequate sleep, regular exercise, and stress management to support healing and prevent recurrence.'
     )
    elif 'AIDS' in u:
     bot_response = (
    'Bot> While Ayurveda offers holistic approaches to well-being, it\'s crucial to understand that there\'s no known cure for HIV/AIDS within its framework. '
    'HIV/AIDS is a complex medical condition requiring scientifically proven antiretroviral therapy (ART) for effective management and preventing transmission.\n\n'
    'However, Ayurvedic principles can complement ART by potentially:\n'
    'Boosting immunity: Certain herbs like Ashwagandha and Amla may support the immune system, potentially aiding the body\'s fight against infections.\n'
    'Managing side effects: Ayurvedic practices like yoga and meditation can help manage stress and anxiety, common side effects of ART.\n'
    'Promoting overall well-being: Ayurvedic dietary and lifestyle recommendations can contribute to a healthy lifestyle, crucial for managing chronic conditions like HIV/AIDS.\n'
    'Prevention: While Ayurveda doesn\'t offer a cure, its emphasis on healthy practices like safe sex and a balanced lifestyle aligns with HIV/AIDS prevention strategies.\n\n'
    'Remember, ART remains the cornerstone of HIV/AIDS management. If you\'re living with HIV/AIDS, consult a qualified medical professional for proper diagnosis and treatment. '
    'Consider discussing complementary Ayurvedic practices with your doctor for potential benefits alongside conventional therapy.'
    )
    elif 'Diabetes' in u:
     bot_response = (
    'Bot> Ayurveda for Diabetes:\n\n'
    'Prevent:\n'
    '1. Balance doshas: Light diet, exercise, early sleep.\n'
    '2. Stress less: Yoga, meditation, pranayama.\n'
    '3. Healthy fats: Ghee, coconut oil, oily fish.\n'
    '4. Fiber focus: Fenugreek, lentils, greens, whole grains.\n'
    '5. Bitter is better: Bitter melon, neem, turmeric.\n'
    '6. Spices: Cumin, cinnamon, coriander for blood sugar control.\n'
    'Treatment:\n'
    '1. Personalized herbs: Tailored to your dosha and symptoms.\n'
    '2. Panchakarma detox: Virechana, Basti to cleanse and strengthen digestion.\n'
    '3. Yoga & exercise: Improve insulin sensitivity.\n'
    '4. Diet plan: Low-glycemic, controlled portions, mindful eating.\n'
    'Consult an Ayurvedic practitioner alongside conventional treatment.'
     )
    elif 'Gastroenteritis' in u:
     bot_response = (
    'Bot> Gastroenteritis can be uncomfortable, but Ayurveda offers gentle and holistic ways to manage it:\n\n'
    'Prevention:\n'
    '1. Balance your gut: Maintain healthy digestion with light meals, warm water, and probiotics like buttermilk or ghee.\n'
    '2. Cleanse gently: Regularly consume ginger, cumin, and coriander water for their purifying properties.\n'
    '3. Mindful eating: Avoid heavy, oily, and spicy foods, favoring easily digestible grains like rice and barley.\n'
    '4. Stress management: Practice yoga, meditation, or pranayama to manage stress, a risk factor for gut issues.\n'
    'Treatment:\n\n'
    '1. Hydration is key: Sipping warm water with added honey and lemon helps with electrolyte balance and recovery.\n'
    '2. Herbal allies: Consult an Ayurvedic doctor for personalized herbal remedies like ginger, turmeric, and licorice (yashtimadhu) for their anti-inflammatory and soothing properties.\n'
    '3. Soups and broths: Gentle nourishment is crucial. Opt for light vegetable or lentil soups seasoned with cumin and coriander.\n'
    '4. Rest and recuperation: Allow your body ample rest to heal. Avoid strenuous activities and prioritize sleep.\n'
    'Remember, Ayurveda emphasizes individual needs. Consult an experienced Ayurvedic practitioner for tailored advice and herbal formulations.\n'
    'Remember, this information is not a substitute for professional medical advice'
     )
    elif 'Bronchial Asthma' in u:
     bot_response = (
    'Bot> Ayurveda views asthma as an imbalance of Vata and Kapha doshas, leading to airway inflammation'
    'Prevention:\n'
    'Diet: Opt for easily digestible foods like mung dal, barley, and pumpkin. Avoid cold, heavy, and mucus-forming foods like dairy and fried items.\n'
    'Lifestyle: Regular exercise and pranayama (breathing exercises) strengthen lungs and manage stress. Avoid triggers like dust, smoke, and pollution.\n'
    'Natural remedies: Daily ginger with honey, turmeric milk, and licorice powder soothe airways and boost immunity.\n\n'
    'Treatment:\n'
    'Panchakarma: Therapies like Vamana (therapeutic emesis) and Virechana (purgation) help eliminate excess Kapha. Swedana (sudation) opens channels and relieves congestion.\n'
    'Herbal remedies: Vasaka, Tulsi, and Sunthi (ginger) act as bronchodilators. Trikatu (ginger, black pepper, long pepper) and Lavangadi Vati (clove) reduce inflammation.\n'
    'Yoga and Pranayama: Specific postures and breathing practices like Kapalbhati and Anulom Vilom improve lung function and manage stress.'
    )
    elif 'Hypertension' in u:
     bot_response = (
    'Bot> Ayurveda views high blood pressure as an imbalance of doshas, particularly Pitta. Here\'s how to gently guide them back to harmony:\n\n'
    'Prevention:\n'
    '1. Eat cool & calming: Embrace leafy greens, cucumber, and coconut water. Limit salty, oily, and spicy foods.\n'
    '2. De-stress with Vata: Practice yoga, meditation, and pranayama to manage stress, a major culprit.\n'
    '3. Balance Kapha with weight: Maintain a healthy weight through exercise and balanced diet.\n\n'
    'Treatment:\n'
    '1. Cleanse with Panchakarma: This detoxification process helps eliminate toxins that can contribute to hypertension.\n'
    '2. Harness herbal wisdom: Consult an Ayurvedic doctor for personalized herbal formulations like Sarpagandha and Punarnava, known for their blood pressure-lowering properties.\n'
    '3. Embrace healthy habits: Regular exercise, adequate sleep, and avoiding smoking and alcohol are key.\n\n'
    'Remember, Ayurveda complements, not replaces, conventional treatment. Consult your doctor for proper diagnosis and guidance.'
    )
    elif 'Migraine' in u:
     bot_response = (
    'Bot> Ayurveda, the ancient Indian science of healing, offers a natural and holistic approach to managing migraines. '
    'By addressing the root cause and promoting overall balance, you can find relief from those throbbing headaches.\n\n'
    'Prevention:\n'
    '1. Diet: Embrace sattvic foods like fresh fruits, vegetables, and whole grains. Avoid triggers like processed foods, excessive caffeine, and alcohol.\n'
    '2. Lifestyle: Manage stress through yoga, meditation, and pranayama. Ensure adequate sleep and regular exercise.\n'
    '3. Balance your doshas: Consult an Ayurvedic practitioner to determine your predominant dosha (vata, pitta, or kapha) and adopt practices to keep it balanced.\n\n'
    'Treatment:\n'
    '1. Shirodhara: A continuous stream of warm oil poured onto the forehead, promoting deep relaxation and stress relief.\n'
    '2. Nasya: Application of medicated oils or powders through the nose to cleanse and stimulate the sinus cavities.\n'
    '3. Abhyanga: Therapeutic massage with herbal oils to improve circulation, reduce tension, and soothe the nervous system.\n'
    '4. Herbal remedies: Customized formulations like Brahmi, Shankhapushpi, and Vacha can address specific migraine symptoms.'
    )
    elif 'Cervical spondylosis' in u:
     bot_response = (
    'Bot>Ayurveda offers a gentle and effective approach to managing cervical spondylosis, focusing on preventing further degeneration and alleviating pain.\n\n'
    'Prevention:\n'
    '1. Posture matters: Maintain good posture to avoid neck strain.\n'
    '2. Gentle stretches: Practice yoga poses like Cat and Cobra to improve flexibility.\n'
    '3. Warmth works: Keep your neck warm to reduce stiffness.\n'
    '4. Balanced diet: Choose anti-inflammatory foods like fruits, vegetables, and whole grains.\n\n'
    'Treatment:\n'
    '1. Detoxify with Panchakarma: This five-stage cleanse removes toxins and reduces inflammation.\n'
    '2. Soothe with Snehana & Swedana: Oil massage and herbal steam therapy ease muscle tension.\n'
    '3. Nourish with Greeva Basti: Medicated oil pool applied to the neck lubricates joints.\n'
    '4. Harness herbal power: Guggulu, Rasna, and Ashwagandha possess anti-inflammatory properties.\n'
    'Consult an Ayurvedic practitioner for a personalized plan. By embracing these practices, you can find natural relief and long-term neck health.'
    )
    elif 'Paralysis (brain hemorrhage)' in u:
     bot_response = (
    'Bot>While Ayurveda doesn\'t claim to cure brain hemorrhage (stroke) on its own, it offers valuable support for recovery and managing long-term effects. '
    'Remember, immediate medical attention is crucial in such cases.\n\n'
    'Prevention:\n'
    '1. Balance your doshas: Consult an Ayurvedic practitioner to understand your dominant dosha (vata, pitta, or kapha) and adopt practices for balance, like diet, exercise, and stress management.\n'
    '2. Control blood pressure & cholesterol: Manage these risk factors through a healthy diet, regular exercise, and weight management.\n'
    '3. Manage stress: Practice yoga, meditation, and pranayama to reduce stress and promote overall well-being.\n\n'
    'Support for Recovery:\n'
    '1. Panchakarma: This personalized detoxification process can help eliminate toxins and stimulate healing.\n'
    '2. Shirodhara: Warm oil poured onto the forehead promotes deep relaxation, reduces stress, and improves circulation.\n'
    '3. Nasya: Application of medicated oils or powders through the nose helps clear sinuses, improve cognitive function, and reduce headaches.\n'
    '4. Herbal Remedies: Consult an Ayurvedic doctor for customized formulations to address specific symptoms like weakness, paralysis, and speech difficulties.'
    )
    elif 'Jaundice' in u:
     bot_response = (
    'Bot>Jaundice is a condition that causes the skin and whites of the eyes to turn yellow due to a buildup of bilirubin, a yellow pigment produced by the liver. '
    'In Ayurveda, jaundice is seen as an imbalance of the pitta dosha, which is responsible for digestion and metabolism.\n\n'
    'Prevention:\n'
    '1. Maintain a healthy diet: Eat plenty of fruits, vegetables, and whole grains. Avoid oily, spicy, and processed foods.\n'
    '2. Drink plenty of fluids: Staying hydrated helps to flush out toxins and bilirubin.\n'
    '3. Exercise regularly: Exercise helps to improve digestion and liver function.\n'
    '4. Manage stress: Stress can worsen jaundice symptoms. Practice yoga, meditation, or other relaxation techniques.\n\n'
    'Treatment:\n'
    '1. Panchakarma: This five-stage detoxification process can help to cleanse the liver and remove excess bilirubin.\n'
    '2. Snehana and Swedana: Oil massage and herbal steam therapy can help to open up the liver channels and promote bile flow.\n'
    '3. Basti: Enemas with medicated oils or decoctions can help to stimulate the bowels and eliminate toxins.\n'
    '4. Herbal remedies: Ayurvedic herbs like Bhumiamalaki, Guduchi, and Punarnava can help to treat jaundice.'
    )
    elif 'Malaria' in u:
     bot_response = (
    'Bot>While seeking medical attention is essential for malaria, Ayurveda offers some simple practices to help your body fight and recover.\n\n'
    'Prevention:\n'
    '1. Boost immunity: Sip on teas made with Giloy, Amalaki, or Tulsi for their immune-boosting properties.\n'
    '2. Repel the bite: Use mosquito nets, repellents, and wear protective clothing when outdoors.\n'
    '3. Digest easily: Stick to light meals, avoid spices, caffeine, and alcohol to aid digestion.\n\n'
    'Support and Recovery:\n'
    '1. Stay cool: Drink plenty of water, use cool compresses, and enjoy soothing teas like Neem, Tulsi, or Ginger.\n'
    '2. Harness herbal power: Consider Ayurvedic remedies like Ayush-64, Nimbadi Churna, or Guduchi (Tinospora cordifolia) for their supportive properties.\n\n'
    'Remember, Ayurveda works best alongside medical care. Consult your doctor for proper diagnosis and treatment.\n'
    'Stay safe and healthy!'
    )
    elif 'Chicken pox' in u:
     bot_response = (
    'Bot>While medical care remains crucial, Ayurveda offers natural ways to ease chickenpox symptoms:\n\n'
    'Boost Immunity:\n'
    '1. Neem leaves or powder for blood purification and inflammation relief.\n'
    '2. Chyawanprash for general immunity and infection fight.\n'
    '3. Guduchi decoction for immune response and fever reduction.\n\n'
    'Soothe the Itch:\n'
    '1. Sandalwood paste on blisters for cooling and itch relief.\n'
    '2. Aloe vera gel for its natural anti-inflammatory properties.\n'
    '3. Neem bath in lukewarm water to reduce itching and promote healing.\n\n'
    'Diet & Lifestyle:\n'
    '1. Light, easy-to-digest foods like khichdi, soups, and fruits.\n'
    '2. Plenty of water, coconut water, and cooling herbal teas.\n'
    '3. Adequate sleep for healing and fever reduction.\n\n'
    'Consult an Ayurvedic practitioner for personalized herbal formulations based on your doshas and specific needs.\n\n'
    'Embrace these alongside medical care for a gentle and holistic approach to chickenpox recovery.'
    )
    elif 'Dengue' in u:
     bot_response = (
    'Bot>While seeking medical attention is crucial for dengue, Ayurveda offers complementary practices to support your body\'s fight and recovery.\n\n'
    'Prevention:\n\n'
    '1. Mosquito protection: Use nets, repellents, and wear covered clothing to avoid mosquito bites.\n'
    '2. Boost immunity: Consume Tulsi (holy basil) tea, Amla (Indian gooseberry) juice, and Giloy (Tinospora cordifolia) juice to strengthen your immune system.\n'
    '3. Maintain good hygiene: Keep your surroundings clean and avoid stagnant water to discourage mosquito breeding.\n\n'
    'Treatment Support:\n\n'
    '1. Hydration is key: Drink plenty of coconut water, fresh fruit juices, and herbal teas like coriander or fenugreek to avoid dehydration, a vital concern in dengue.\n'
    '2. Papaya power: Consume papaya juice or extract for its platelet-boosting properties to promote faster recovery.\n'
    '3. Neem\'s healing touch: Neem leaves extract or juice acts as a natural blood purifier and fever reducer.\n'
    '4. Soothing baths: Lukewarm baths with Epsom salts or neem leaves can help reduce body aches and muscle pain.\n'
    '5. Herbal remedies: Consult an Ayurvedic practitioner for personalized herbal formulations like Giloy, Punarnava, or Chyawanprash to address specific symptoms and support your recovery.\n\n'
    'Remember, Ayurveda works best alongside conventional treatment. Always consult your doctor for proper diagnosis and management of dengue.\n\n'
    'By incorporating these practices alongside medical care, you can help your body fight dengue and promote a faster, more comfortable recovery.\n\n'
    'Disclaimer: This information is not a substitute for professional medical advice. Always consult your doctor for any medical concerns.'
    )
    elif 'Typhoid' in u:
     bot_response = (
    'Bot>Typhoid fever, caused by the Salmonella Typhi bacteria, can be debilitating. '
    'While immediate medical attention is crucial, Ayurveda offers complementary practices to support recovery and manage symptoms.\n\n'
    'Prevention:\n'
    '1. Safe water and food: Practice hygiene, boil water, and choose well-cooked food to avoid bacterial contamination.\n'
    '2. Boost immunity: Consume immunity-building herbs like Tulsi (Holy Basil), Guduchi (Tinospora cordifolia), and Amla (Indian Gooseberry).\n'
    '3. Maintain healthy gut flora: Include yogurt, buttermilk, and fermented foods in your diet.\n\n'
    'Treatment:\n'
    '1. Panchakarma: This detoxification process helps eliminate toxins and promotes healing.\n'
    '2. Dietary modifications: Consume easily digestible foods like khichdi, soups, and fruits. Avoid spicy, oily, and fried foods.\n'
    '3. Hydration: Drink plenty of water, coconut water, and herbal teas to prevent dehydration.\n'
    '4. Herbal remedies: Consider formulations like Triphala Churna (mixture of three fruits), Guduchi decoction, or Neem leaves for their antibacterial and immune-boosting properties.\n\n'
    'Remember, Ayurveda works best alongside conventional medicine. Consult your doctor and an Ayurvedic practitioner for a personalized treatment plan.'
    )
    elif 'hepatitis A' in u:
     bot_response = (
    'Bot>Managing Hepatitis A: An Ayurvedic Approach alongside Medical Care\n'
    'While conventional medical treatment remains crucial for Hepatitis A, Ayurveda offers complementary approaches to support liver health and recovery. Here\'s a glimpse:\n\n'
    'Liver-Loving Herbs:\n'
    '1. Kutki (Picrorhiza kurroa): Known for its liver-protective and detoxifying properties, Kutki helps reduce inflammation and promote healing.\n'
    '2. Bhumi amla (Phyllanthus niruri): This powerful herb boasts anti-viral and hepatoprotective properties, aiding in liver regeneration.\n'
    '3. Triphala (Combination of three fruits): This versatile trio balances doshas (Ayurvedic humors), improves digestion, and supports detoxification.\n\n'
    'Dietary Modifications:\n'
    '1. Light & Easily Digestible Foods: Prioritize khichdi, soups, and fruits to ease digestive stress and optimize nutrient absorption.\n'
    '2. Hydration is Key: Drink plenty of water, coconut water, and cooling herbal teas to flush toxins and support liver function.\n'
    '3. Minimize Greasy & Spicy Foods: Opt for natural, anti-inflammatory foods like leafy greens and fruits to reduce inflammation and promote healing.\n\n'
    'Rest & Rejuvenation:\n'
    '1. Prioritize Sleep: Adequate rest allows your body to focus on healing and repair.\n'
    '2. Minimize Stress: Practice yoga, meditation, or pranayama to manage stress and promote overall well-being.\n'
    '3. Avoid Strenuous Activity: Give your body time to recover and focus on gentle movement like walking or light yoga.\n\n'
    'Remember:\n'
    '1. Ayurvedic practices work best alongside medical care. Consult your doctor for proper diagnosis and treatment.\n'
    '2. Personalized Ayurvedic recommendations based on your doshas and specific needs can be obtained through consultation with a qualified practitioner.\n'
    '3. By incorporating these Ayurvedic principles alongside your doctor\'s guidance, you can support your body\'s natural healing process and promote optimal liver health during Hepatitis A recovery.'
    )
    elif 'Hepatitis B' in u:
     bot_response = (
    'Bot>Managing Hepatitis A: An Ayurvedic Approach alongside Medical Care\n'
    'While conventional medical treatment remains crucial for Hepatitis A, Ayurveda offers complementary approaches to support liver health and recovery. Here\'s a glimpse:\n\n'
    'Liver-Loving Herbs:\n'
    '1. Kutki (Picrorhiza kurroa): Known for its liver-protective and detoxifying properties, Kutki helps reduce inflammation and promote healing.\n'
    '2. Bhumi amla (Phyllanthus niruri): This powerful herb boasts anti-viral and hepatoprotective properties, aiding in liver regeneration.\n'
    '3. Triphala (Combination of three fruits): This versatile trio balances doshas (Ayurvedic humors), improves digestion, and supports detoxification.\n\n'
    'Dietary Modifications:\n'
    '1. Light & Easily Digestible Foods: Prioritize khichdi, soups, and fruits to ease digestive stress and optimize nutrient absorption.\n'
    '2. Hydration is Key: Drink plenty of water, coconut water, and cooling herbal teas to flush toxins and support liver function.\n'
    '3. Minimize Greasy & Spicy Foods: Opt for natural, anti-inflammatory foods like leafy greens and fruits to reduce inflammation and promote healing.\n\n'
    'Rest & Rejuvenation:\n'
    '1. Prioritize Sleep: Adequate rest allows your body to focus on healing and repair.\n'
    '2. Minimize Stress: Practice yoga, meditation, or pranayama to manage stress and promote overall well-being.\n'
    '3. Avoid Strenuous Activity: Give your body time to recover and focus on gentle movement like walking or light yoga.\n\n'
    'Remember:\n'
    '1. Ayurvedic practices work best alongside medical care. Consult your doctor for proper diagnosis and treatment.\n'
    '2. Personalized Ayurvedic recommendations based on your doshas and specific needs can be obtained through consultation with a qualified practitioner.\n'
    '3. By incorporating these Ayurvedic principles alongside your doctor\'s guidance, you can support your body\'s natural healing process and promote optimal liver health during Hepatitis A recovery.'
    )
    elif 'Hepatitis C' in u:
     bot_response = (
    'Bot>Managing Hepatitis A: An Ayurvedic Approach alongside Medical Care\n'
    'While conventional medical treatment remains crucial for Hepatitis A, Ayurveda offers complementary approaches to support liver health and recovery. Here\'s a glimpse:\n\n'
    'Liver-Loving Herbs:\n'
    '1. Kutki (Picrorhiza kurroa): Known for its liver-protective and detoxifying properties, Kutki helps reduce inflammation and promote healing.\n'
    '2. Bhumi amla (Phyllanthus niruri): This powerful herb boasts anti-viral and hepatoprotective properties, aiding in liver regeneration.\n'
    '3. Triphala (Combination of three fruits): This versatile trio balances doshas (Ayurvedic humors), improves digestion, and supports detoxification.\n\n'
    'Dietary Modifications:\n'
    '1. Light & Easily Digestible Foods: Prioritize khichdi, soups, and fruits to ease digestive stress and optimize nutrient absorption.\n'
    '2. Hydration is Key: Drink plenty of water, coconut water, and cooling herbal teas to flush toxins and support liver function.\n'
    '3. Minimize Greasy & Spicy Foods: Opt for natural, anti-inflammatory foods like leafy greens and fruits to reduce inflammation and promote healing.\n\n'
    'Rest & Rejuvenation:\n'
    '1. Prioritize Sleep: Adequate rest allows your body to focus on healing and repair.\n'
    '2. Minimize Stress: Practice yoga, meditation, or pranayama to manage stress and promote overall well-being.\n'
    '3. Avoid Strenuous Activity: Give your body time to recover and focus on gentle movement like walking or light yoga.\n\n'
    'Remember:\n'
    '1. Ayurvedic practices work best alongside medical care. Consult your doctor for proper diagnosis and treatment.\n'
    '2. Personalized Ayurvedic recommendations based on your doshas and specific needs can be obtained through consultation with a qualified practitioner.\n'
    '3. By incorporating these Ayurvedic principles alongside your doctor\'s guidance, you can support your body\'s natural healing process and promote optimal liver health during Hepatitis A recovery.'
    )
    elif 'Hepatitis D' in u:
     bot_response = (
    'Bot>Managing Hepatitis A: An Ayurvedic Approach alongside Medical Care\n'
    'While conventional medical treatment remains crucial for Hepatitis A, Ayurveda offers complementary approaches to support liver health and recovery. Here\'s a glimpse:\n\n'
    'Liver-Loving Herbs:\n'
    '1. Kutki (Picrorhiza kurroa): Known for its liver-protective and detoxifying properties, Kutki helps reduce inflammation and promote healing.\n'
    '2. Bhumi amla (Phyllanthus niruri): This powerful herb boasts anti-viral and hepatoprotective properties, aiding in liver regeneration.\n'
    '3. Triphala (Combination of three fruits): This versatile trio balances doshas (Ayurvedic humors), improves digestion, and supports detoxification.\n\n'
    'Dietary Modifications:\n'
    '1. Light & Easily Digestible Foods: Prioritize khichdi, soups, and fruits to ease digestive stress and optimize nutrient absorption.\n'
    '2. Hydration is Key: Drink plenty of water, coconut water, and cooling herbal teas to flush toxins and support liver function.\n'
    '3. Minimize Greasy & Spicy Foods: Opt for natural, anti-inflammatory foods like leafy greens and fruits to reduce inflammation and promote healing.\n\n'
    'Rest & Rejuvenation:\n'
    '1. Prioritize Sleep: Adequate rest allows your body to focus on healing and repair.\n'
    '2. Minimize Stress: Practice yoga, meditation, or pranayama to manage stress and promote overall well-being.\n'
    '3. Avoid Strenuous Activity: Give your body time to recover and focus on gentle movement like walking or light yoga.\n\n'
    'Remember:\n'
    '1. Ayurvedic practices work best alongside medical care. Consult your doctor for proper diagnosis and treatment.\n'
    '2. Personalized Ayurvedic recommendations based on your doshas and specific needs can be obtained through consultation with a qualified practitioner.\n'
    '3. By incorporating these Ayurvedic principles alongside your doctor\'s guidance, you can support your body\'s natural healing process and promote optimal liver health during Hepatitis A recovery.'
    )
    elif 'Hepatitis E' in u:
     bot_response = (
    'Bot>Managing Hepatitis A: An Ayurvedic Approach alongside Medical Care\n'
    'While conventional medical treatment remains crucial for Hepatitis A, Ayurveda offers complementary approaches to support liver health and recovery. Here\'s a glimpse:\n\n'
    'Liver-Loving Herbs:\n'
    '1. Kutki (Picrorhiza kurroa): Known for its liver-protective and detoxifying properties, Kutki helps reduce inflammation and promote healing.\n'
    '2. Bhumi amla (Phyllanthus niruri): This powerful herb boasts anti-viral and hepatoprotective properties, aiding in liver regeneration.\n'
    '3. Triphala (Combination of three fruits): This versatile trio balances doshas (Ayurvedic humors), improves digestion, and supports detoxification.\n\n'
    'Dietary Modifications:\n'
    '1. Light & Easily Digestible Foods: Prioritize khichdi, soups, and fruits to ease digestive stress and optimize nutrient absorption.\n'
    '2. Hydration is Key: Drink plenty of water, coconut water, and cooling herbal teas to flush toxins and support liver function.\n'
    '3. Minimize Greasy & Spicy Foods: Opt for natural, anti-inflammatory foods like leafy greens and fruits to reduce inflammation and promote healing.\n\n'
    'Rest & Rejuvenation:\n'
    '1. Prioritize Sleep: Adequate rest allows your body to focus on healing and repair.\n'
    '2. Minimize Stress: Practice yoga, meditation, or pranayama to manage stress and promote overall well-being.\n'
    '3. Avoid Strenuous Activity: Give your body time to recover and focus on gentle movement like walking or light yoga.\n\n'
    'Remember:\n'
    '1. Ayurvedic practices work best alongside medical care. Consult your doctor for proper diagnosis and treatment.\n'
    '2. Personalized Ayurvedic recommendations based on your doshas and specific needs can be obtained through consultation with a qualified practitioner.\n'
    '3. By incorporating these Ayurvedic principles alongside your doctor\'s guidance, you can support your body\'s natural healing process and promote optimal liver health during Hepatitis A recovery.'
    )
    elif 'Alcoholic hepatitis' in u:
     bot_response = (
    'Bot>While Ayurvedic treatments cannot cure alcoholic hepatitis, they can offer valuable support alongside conventional medical care to aid healing and manage symptoms.\n\n'
    'Prevention:\n'
    '1. Complete alcohol cessation: This is the critical first step for healing and preventing further liver damage.\n'
    '2. Dietetic adjustments: Switch to a light, easily digestible vegetarian diet rich in fruits, vegetables, and whole grains to minimize strain on the liver.\n\n'
    'Treatment:\n'
    '1. Detoxification: Consider gentle Ayurvedic therapies like Virechana (therapeutic purgation) and Basti (medicated enemas) to help eliminate toxins and reduce inflammation.\n'
    '2. Liver-supportive herbs: Consult an Ayurvedic practitioner for personalized herbal formulations containing Kutki, Bhumi amla, and Triphala, known for their hepatoprotective properties.\n'
    '3. Lifestyle modifications: Prioritize adequate sleep, manage stress through yoga or meditation, and stay hydrated with water and herbal teas.\n\n'
    'Remember: Individualized care is crucial. Consult a qualified Ayurvedic practitioner for customized dietary and herbal recommendations based on your doshic balance and specific needs.\n\n'
    'By combining conventional treatment with these supportive Ayurvedic practices, you can promote long-term liver health and manage the progression of alcoholic hepatitis.\n\n'
    'Disclaimer: This information is not a substitute for professional medical advice. Always consult your doctor for any medical concerns.'
    )
    elif 'Tuberculosis' in u:
     bot_response = (
    'Bot>While complete reliance on Ayurveda is not recommended for treating tuberculosis (TB), it can offer valuable supportive measures alongside conventional medical treatment. '
    'Remember, seeking proper medical diagnosis and adhering to prescribed medications remain crucial for successful TB management.\n\n'
    'Boosting Immunity:\n'
    '1. Rasayana therapies: Herbal formulations like Chyawanprash and Ashwagandha bolster the immune system, aiding in fighting the infection.\n'
    '2. Dietary Adjustments: Prioritize fresh fruits, vegetables, and whole grains for essential vitamins and minerals to strengthen your body\'s defense mechanisms.\n'
    '3. Yoga & Pranayama: These practices promote respiratory health, improve oxygen intake, and reduce stress, enhancing overall well-being.\n\n'
    'Addressing Symptoms:\n'
    '1. Cough Relief: Ginger tea with honey, Tulsi, or Vasaka (Adhatoda zeylanica) alleviates cough and eases chest congestion.\n'
    '2. Fatigue Management: Shirodhara (medicated oil therapy on the forehead) and Abhyanga (herbal oil massage) promote relaxation and combat fatigue.\n'
    '3. Fever Management: Sandalwood paste application and lukewarm baths help reduce fever and discomfort.\n\n'
    'Disclaimer: Please note that these are general suggestions and individualized Ayurvedic treatment plans must be formulated by a qualified Ayurvedic practitioner considering your specific doshic balance and disease progression.\n\n'
    'Always remember, Ayurveda complements but does not replace conventional medical care for TB. Work closely with your doctor and an Ayurvedic practitioner for a holistic approach to managing your condition.'
    )
    elif 'Common Cold' in u:
     bot_response = (
    'Bot>While seeking medical advice is essential for severe cases, Ayurveda offers natural home remedies to soothe common cold symptoms and boost your body\'s defenses:\n\n'
    
    'Prevention:\n\n'
    '1. Boost immunity: Practice daily yoga, meditation, and deep breathing for stress reduction and overall well-being.\n'
    '2. Nourish with ginger: Include ginger in your diet or drink ginger tea, its warming properties help prevent congestion.\n'
    '3. Spice up your life: Use spices like black pepper, turmeric, and cumin, known for their anti-inflammatory and immune-boosting qualities.\n\n'
    
    'Treatment:\n\n'
    '1. Steam inhalation: Inhale steam infused with eucalyptus or tulsi leaves to loosen mucus and ease congestion.\n'
    '2. Herbal gargle: Make a gargle with warm water, salt, and turmeric powder to soothe a sore throat.\n'
    '3. Warm drink for relief: Enjoy a cup of turmeric milk or tulsi tea, known for their warming and anti-inflammatory properties.\n'
    '4. Dosha-specific approach: Consult an Ayurvedic practitioner for personalized herbal remedies based on your dominant dosha (vata, pitta, or kapha) for targeted relief.\n\n'
    
    'Remember: Stay hydrated, get adequate rest, and eat light, easily digestible foods for faster recovery.\n\n'
    
    'By incorporating these simple Ayurvedic practices alongside healthy habits, you can give your body the natural boost it needs to fight off the common cold and feel better soon.\n\n'
    
    'Disclaimer: This information is not a substitute for professional medical advice. Always consult your doctor for any medical concerns.'
    )
    elif 'Pneumonia' in u:
     bot_response = (
    'Bot>While seeking medical attention is crucial for pneumonia, Ayurveda offers complementary practices to support your recovery and ease symptoms:\n\n'
    'Prevention:\n'
    '1. Boost your Agni (digestive fire): Consume spices like ginger, turmeric, and black pepper to improve digestion and immunity.\n'
    '2. Warm up & hydrate: Avoid cold water and drafts, sip warm ginger tea to keep mucus thin, and drink plenty of water.\n'
    '3. Pranayama power: Practice Kapalbhati pranayama to clear lung congestion and Kapha buildup.\n\n'
    'Treatment:\n'
    '1. Langhana (fasting): Consider a short, supervised fast under an Ayurvedic practitioner\'s guidance to reduce inflammation and Kapha accumulation.\n'
    '2. Herbal expectorants: Take Vasa (Malabar nut), Tulsi (Holy basil), and Pippali (Long pepper) to expel mucus and soothe the respiratory tract.\n'
    '3. Soothing steam therapy: Inhale steam infused with eucalyptus or ajwain seeds to loosen phlegm and ease breathing.\n'
    '4. Dosha-specific approach: Consult an Ayurvedic practitioner for personalized herbal formulations and dietary recommendations based on your dominant dosha for targeted relief.\n\n'
    'Remember: Rest, eat easily digestible foods, and maintain good hygiene to support your body\'s healing process.\n\n'
    'With a combined approach of conventional medicine and Ayurvedic practices, you can find gentle support on your journey to recovery from pneumonia.\n\n'
    'Disclaimer: This information is not a substitute for professional medical advice. Always consult your doctor for any medical concerns.'
    )
    elif 'Dimorphic hemmorhoids(piles)' in u:
     bot_response = (
    'Bot>While seeking medical diagnosis and guidance is essential, Ayurveda offers holistic approaches to manage dimorphic hemorrhoids and promote long-term relief:\n\n'
    'Prevention:\n\n'
    '1. Dosha Balance: Follow an Ayurvedic diet and lifestyle tailored to your dominant dosha (vata, pitta, or kapha) to prevent constipation and maintain digestive health.\n'
    '2. Fiber Power: Increase intake of fruits, vegetables, and whole grains for smooth bowel movements and reduced straining.\n'
    '3. Hydration Matters: Drink plenty of water and herbal teas throughout the day to prevent dehydration and keep stool soft.\n\n'
    'Treatment:\n\n'
    '1. Panchakarma Detox: Consider a personalized Panchakarma therapy plan to cleanse and rejuvenate your system, addressing digestive imbalances that contribute to hemorrhoids.\n'
    '2. Soothing Sitz Baths: Immerse your lower body in warm water with Epsom salts or anti-inflammatory herbs like neem or calendula to reduce pain and inflammation.\n'
    '3. Herbal Remedies: Consult an Ayurvedic practitioner for customized herbal formulations like Triphala, Abhayarishta, or Manibadra Lehya to improve digestion, reduce congestion, and promote healing.\n'
    '4. Kshara Karma: This minimally invasive Ayurvedic procedure uses an herbal paste to cauterize and shrink hemorrhoids, potentially offering long-term relief.\n\n'
    'Lifestyle Modifications:\n\n'
    '1. Regular Exercise: Engage in moderate physical activity like walking or yoga to improve circulation and digestion.\n'
    '2. Stress Management: Practice meditation, yoga, or pranayama to manage stress, a contributing factor to hemorrhoids.\n'
    '3. Avoid Triggers: Limit spicy, processed foods, and alcohol that can irritate the digestive system and worsen hemorrhoids.\n\n'
    'Remember: Consistency is key! By incorporating these Ayurvedic practices into your daily routine alongside medical guidance, you can manage dimorphic hemorrhoids effectively and promote long-term digestive health.\n\n'
    'Disclaimer: This information is not a substitute for professional medical advice. Always consult your doctor for diagnosis and treatment planning.'
    )
    elif 'Heart attack' in u:
     bot_response = (
    'Bot>While immediate medical attention is crucial for a heart attack, Ayurveda offers complementary and preventive approaches for long-term heart health:\n\n'
    'Prevention:\n\n'
    '1. Dietary modifications: Reduce saturated fats, increase fiber and plant-based foods, and choose healthy cooking oils.\n'
    '2. Lifestyle adjustments: Regular exercise, adequate sleep, and stress management practices like yoga and meditation are key.\n'
    '3. Balance your doshas: Consult an Ayurvedic practitioner to understand your dominant dosha (vata, pitta, or kapha) and adopt practices to maintain harmony, like specific diet and exercise routines.\n\n'
    'Ayurvedic Support:\n\n'
    '1. Panchakarma: This detoxification process can help eliminate toxins and improve circulation.\n'
    '2. Herbal Remedies: Arjuna, Guggulu, Ashwagandha, and Triphala are known for their cardioprotective properties. Consult an Ayurvedic doctor for personalized formulations.\n'
    '3. Therapeutic procedures: Shirodhara and Nasya can promote relaxation and relieve stress, contributing to heart health.\n'
    '4. Dietary guidelines: Emphasize easily digestible foods, avoid oily, spicy, and salty meals, and consume plenty of fruits and vegetables.\n\n'
    'Remember: Ayurveda complements, not replaces, conventional medical care. Work closely with your doctor and an Ayurvedic practitioner for a holistic approach to preventing and managing heart health.\n\n'
    'Disclaimer: This information is not a substitute for professional medical advice. Always consult your doctor for any medical concerns.'
    )
    elif 'Varicoseveins' in u:
     bot_response = (
    'Bot>Prevention:\n\n'
    '1. Move it or lose it: Regular exercise, especially walking and swimming, boosts circulation and prevents blood pooling.\n'
    '2. Avoid triggers: Limit tight clothing, high heels, and prolonged sitting or standing.\n'
    '3. Manage weight: Excess weight adds pressure on veins, contributing to varicosities.\n'
    '4. Diet for balance: Prioritize fiber-rich foods, reduce salt and red meat, and embrace anti-inflammatory spices like turmeric and ginger.\n'
    'Treatment:\n\n'
    '1. Internal remedies: Triphala, Guggulu, and Kaishora Guggulu are herbs renowned for improving blood flow, strengthening veins, and reducing inflammation. Consult an Ayurvedic practitioner for personalized formulations.\n'
    '2. External care: Apply herbal pastes containing Gotu Kola, Neem, and Turmeric for topical relief and inflammation reduction.\n'
    '3. Abhyanga (Ayurvedic massage): Regular massage with herbal oils like Sahacharadi improves circulation and soothes discomfort.\n'
    '4. Panchakarma therapies: Vata-pacifying treatments like Virechana and Basti can help detoxify and balance the Doshas, contributing to overall leg health.\n'
    'Remember: Ayurvedic treatment takes time and consistency. Consult a qualified practitioner for a personalized plan based on your condition and Doshic balance.\n\n'
    'By adopting these preventive measures and seeking Ayurvedic support, you can improve your circulation, manage varicose vein symptoms, and promote long-term leg health.\n\n'
    'Disclaimer: This information is not a substitute for professional medical advice. Always consult your doctor for any medical concerns.'
    )
    elif 'Hypothyroidism' in u:
     bot_response = (
    'Bot>While medication remains crucial for managing hypothyroidism, Ayurveda offers complementary practices to nurture your thyroid and feel your best:\n\n'
    
    'Prevention:\n'
    '1. Nourish your Agni (digestive fire): Consume spices like ginger, turmeric, and cumin to improve digestion and nutrient absorption, crucial for thyroid function.\n'
    '2. Embrace mindful eating: Choose wholesome, balanced meals with ample fruits, vegetables, and whole grains. Avoid processed foods and refined sugars.\n'
    '3. Balance your doshas: Consult an Ayurvedic practitioner to understand your dominant dosha (vata, pitta, or kapha) and adopt practices for harmony, like specific diet and exercise routines.\n\n'
    
    'Treatment:\n'
    '1. Herbs for harmony: Ashwagandha, Guggulu, and Punarnavadi Guggulu are known for their thyroid-stimulating properties. Consult an Ayurvedic doctor for personalized formulations.\n'
    '2. Panchakarma Detox: This five-stage process can help eliminate toxins and balance Doshas, supporting overall thyroid health.\n'
    '3. Yoga & Pranayama: Practices like Shirshasana (headstand) and Kapalbhati Pranayama can stimulate the thyroid gland and improve circulation.\n'
    '4. Warmth is key: Avoid cold drafts and wear warm clothing, as Kapha accumulation can worsen hypothyroidism.\n\n'
    
    'Remember: Consistency is key in Ayurveda. Work closely with your doctor and an Ayurvedic practitioner for a safe and effective approach to managing your thyroid condition.\n\n'
    
    'By incorporating these practices alongside your medical care, you can empower your body, find natural relief from hypothyroidism symptoms, and improve your overall well-being.\n\n'
    
    'Disclaimer: This information is not a substitute for professional medical advice. Always consult your doctor for any medical concerns.'
    )
    elif 'Hyperthyroidism' in u:
     bot_response = (
    'Bot>Ayurveda views hyperthyroidism as an imbalance of doshas, focusing on restoring harmony for long-term relief.\n\n'
    'Prevention:\n'
    '1. Manage stress: Practice yoga, meditation, and pranayama to address the Kapha-Vata imbalance triggered by stress.\n'
    '2. Balanced diet: Prioritize cooling foods like leafy greens, coconut water, and ghee. Avoid dairy, processed foods, and excessive caffeine.\n'
    '3. Lifestyle adjustments: Prioritize adequate sleep, maintain a healthy weight, and avoid straining activities.\n\n'
    'Treatment:\n'
    '1. Panchakarma: This detoxification process helps eliminate ama (toxins) from the body, supporting overall balance.\n'
    '2. Shirodhara and Nasya: These therapies soothe the nervous system and reduce Pitta imbalance.\n'
    '3. Herbal remedies: Kanchanar, Guduchi, and Shatavari are known to address hyperthyroid symptoms. Consult an Ayurvedic practitioner for personalized formulations.\n'
    '4. Dietary modifications: Focus on easily digestible meals, reduce salt intake, and include cooling spices like coriander and fennel.\n\n'
    'Remember: Ayurveda works best alongside medical care. Consult your doctor and an Ayurvedic practitioner for a holistic approach to managing hyperthyroidism.\n\n'
    'By incorporating these practices, you can support your body\'s natural ability to regain balance and experience long-term well-being.\n\n'
    'Disclaimer: This information is not a substitute for professional medical advice. Always consult your doctor for any medical concerns'
    )
    elif 'Hypoglycemia' in u:
     bot_response = (
    'Bot>Balancing Your Sugar with Ayurveda: Managing Hypoglycemia.\n\n'
    'Ayurveda sees hypoglycemia as an imbalance of Agni (digestive fire) and the Kapha dosha. By harmonizing these, you can support your body\'s natural blood sugar regulation.\n\n'
    'Prevention:\n'
    '1. Balanced diet: Focus on complex carbohydrates like starchy vegetables, whole grains, and legumes. Include nuts, seeds, and healthy fats for slow energy release.\n'
    '2. Maintain healthy Agni: Consume ginger, turmeric, black pepper, and other digestive spices to improve food breakdown and absorption.\n'
    '3. Manage stress: Practice yoga, meditation, and pranayama to reduce stress-induced blood sugar fluctuations.\n\n'
    'Treatment:\n'
    '1. Panchakarma: This detoxification process can help eliminate impurities that hinder metabolism and energy balance.\n'
    '2. Herbal remedies: Consider Guduchi, Amalaki, and Ashwagandha to support pancreas function and blood sugar stabilization. Consult an Ayurvedic practitioner for personalized formulations.\n'
    '3. Agnideepana therapy: This fire-stokes process with specific herbal preparations and dietary practices boosts Agni for better glucose utilization.\n'
    '4. Regular meals and snacks: Avoid skipping meals and opt for frequent, small, easily digestible meals to maintain stable blood sugar levels.\n\n'
    'Remember: Ayurveda takes time and consistency. Work with a qualified practitioner for a personalized plan based on your unique needs and doshic balance.\n\n'
    'By adopting these holistic strategies, you can empower your body to manage hypoglycemia naturally and experience renewed energy and well-being.\n\n'
    'Disclaimer: This information is not a substitute for professional medical advice. Always consult your doctor for any medical concerns.'
    )
    elif 'Osteoarthristis' in u:
     bot_response = (
    'Bot>Ayurveda views osteoarthritis as a Vata imbalance with weakened cartilage and inflamed joints. '
    'It offers both preventive and therapeutic approaches:\n\n'
    
    'Prevention:\n'
    '1. Diet: Prioritize bone-building foods like sesame seeds, leafy greens, and milk. Avoid inflammatory foods like red meat, fried food, and dairy.\n'
    '2. Lifestyle: Regular exercise with gentle yoga and low-impact activities like swimming helps maintain joint strength and flexibility.\n'
    '3. Manage stress: Practice meditation and pranayama to reduce Vata aggravation and inflammation.\n\n'
    
    'Treatment:\n'
    '1. Panchakarma: This detoxification process eliminates Ama (toxins) and promotes overall joint health.\n'
    '2. Snehana & Swedana: Ayurvedic massage with medicated oils followed by herbal steam therapy improves circulation, reduces stiffness, and relieves pain.\n'
    '3. Basti: Medicated enemas target specific joints, nourishing and lubricating them.\n'
    '4. Herbal remedies: Consult an Ayurvedic doctor for personalized herbal formulations like Guggulu, Rasna, and Ashwagandha to address inflammation and pain.\n\n'
    
    'Remember: Consistency is key in Ayurveda. Work with a qualified practitioner for a customized plan based on your joint condition and doshic balance.\n\n'
    
    'By incorporating these practices alongside medical care, you can manage osteoarthritis, improve joint function, and enjoy a more active life.\n\n'
    
    'Disclaimer: This information is not a substitute for professional medical advice. Always consult your doctor for any medical concerns.'
   )
    elif 'Arthritis' in u:
     bot_response = (
    'Bot>Finding Relief from Arthritis with Ayurveda: Prevention & Treatment Tips\n\n'
    'Ayurveda, the ancient Indian science of healing, offers a holistic approach to managing arthritis, focusing on preventing joint pain and inflammation while promoting overall well-being. Here\'s a quick overview:\n\n'
    'Prevention:\n\n'
    '1. Balance your diet: Emphasize fresh fruits and vegetables, whole grains, and legumes. Minimize processed foods, red meat, and dairy, which can aggravate inflammation.\n'
    '2. Move your body: Regular exercise like yoga, walking, and swimming helps maintain joint flexibility and reduces stiffness.\n'
    '3. Manage stress: Practice meditation, pranayama, and other stress-reduction techniques to keep Vata dosha (responsible for movement) in balance.\n\n'
    'Treatment:\n\n'
    '1. Panchakarma: This five-step detoxification process helps eliminate toxins and reduce inflammation throughout the body.\n'
    '2. Snehana & Swedana: Herbal oil massage (Snehana) followed by steam therapy (Swedana) promotes deep tissue healing and relieves pain.\n'
    '3. Basti: Medicated oil enemas (Basti) target specific joints and alleviate pain and inflammation.\n'
    '4. Herbal remedies: Guggulu, Boswellia, and Ashwagandha possess anti-inflammatory properties and can be customized into personalized formulations by an Ayurvedic practitioner.\n\n'
    'Remember: Ayurveda emphasizes individuality. Consult a qualified practitioner for a personalized plan based on your specific type of arthritis, doshic balance, and overall health.\n\n'
    'Additional tips:\n\n'
    '- Maintain a healthy weight to reduce stress on your joints.\n'
    '- Apply warm compresses or take hot baths for temporary pain relief.\n'
    '- Get enough sleep to give your body time to heal.\n\n'
    'By incorporating these Ayurvedic practices alongside conventional medical care, you can find natural relief from arthritis and improve your quality of life.\n\n'
    'Disclaimer: This information is not a substitute for professional medical advice. Always consult your doctor for any medical concerns.'
    )
    elif 'Acne' in u:
     bot_response = (
    'Bot>Conquering Acne with Ayurveda: A Holistic Approach\n\n'
    'Ayurveda offers a natural and holistic approach to managing acne, focusing on internal balance and detoxification to achieve clear, radiant skin.\n\n'
    'Prevention:\n\n'
    '1. Diet for balance: Emphasize cooling foods like leafy greens, fruits, and cucumber. Minimize oily, spicy, and processed foods, which aggravate Pitta dosha and contribute to acne.\n'
    '2. Digestive harmony: Consume spices like ginger, turmeric, and cumin to improve digestion and prevent ama (toxins) buildup, a factor in acne formation.\n'
    '3. Manage stress: Practice yoga, meditation, and pranayama to reduce stress hormones that aggravate acne.\n\n'
    'Treatment:\n\n'
    '1. Panchakarma: This five-step detoxification process helps eliminate ama and balance doshas, paving the way for clearer skin.\n'
    '2. Face masks: Apply natural masks made with Neem, Tulsi, or Sandalwood paste for their anti-inflammatory and antibacterial properties.\n'
    '3. Blood purification: Consider herbal remedies like Manjistha and Sariba to cleanse the blood and reduce acne flare-ups.\n'
    '4. Lifestyle adjustments: Ensure adequate sleep, regular exercise, and good hygiene to support overall skin health.\n\n'
    'Remember: Ayurveda focuses on long-term balance and individual needs. Consult a qualified Ayurvedic practitioner for personalized recommendations based on your unique doshic constitution and acne type.\n\n'
    'By incorporating these preventive and treatment measures into your routine, you can experience a significant improvement in acne and achieve glowing, healthy skin naturally.\n\n'
    'Disclaimer: This information is not a substitute for professional medical advice. Always consult your doctor for any medical concerns.'
    )
    elif 'Urinary tract infection' in u:
     bot_response = (
    'Bot>Ayurvedic Solutions for Urinary Tract Infections (UTI): Flush and Soothe\n\n'
    'While seeking medical attention for UTIs is essential, Ayurveda offers complementary support to soothe symptoms and prevent recurrences:\n\n'
    
    'Prevention:\n'
    '1. Hydration is key: Drink plenty of water and cooling herbal teas like cranberry or Punarnava to flush out toxins and bacteria.\n'
    '2. Cranberry power: Include fresh cranberries or unsweetened cranberry juice in your diet for their urinary tract-protective properties.\n'
    '3. Wipe wisely: Always wipe front to back after using the toilet to prevent bacteria transfer.\n'
    '4. Manage stress: Practice yoga, meditation, or pranayama to reduce stress hormones that can compromise your immune system.\n\n'

    'Treatment:\n'
    '1. Punarnava: This herb possesses diuretic and antibacterial properties, aiding in flushing out toxins and reducing inflammation.\n'
    '2. Gokshura: This herb supports urinary tract health by promoting healthy urination and reducing burning sensation.\n'
    '3. Shirodhara: This therapy with warm oil poured onto the forehead promotes relaxation and reduces stress, contributing to UTI relief.\n'
    '4. Sitz bath: Soaking in lukewarm water with Epsom salts or herbal decoctions like neem or calendula can provide soothing relief for pain and burning.\n\n'
    
    'Remember: Consult an Ayurvedic practitioner for personalized herbal formulations and dietary recommendations based on your doshic balance and specific needs.\n\n'
    
    'By incorporating these preventive measures and Ayurvedic practices alongside medical advice, you can support your body\'s natural defenses against UTIs and experience faster relief from discomfort.\n\n'
    
    'Disclaimer: This information is not a substitute for professional medical advice. Always consult your doctor for any medical concerns.'
   )
    elif 'Psoriasis' in u:
     bot_response = (
    'Bot>Psoriasis Management with Ayurveda: A Holistic Approach.\n'
    'Psoriasis, an autoimmune skin condition causing itchy, red, scaly patches, can benefit from Ayurveda\'s holistic approach. '
    'While seeking medical advice is crucial, Ayurveda offers complementary practices to manage symptoms and promote inner balance.\n\n'
    'Prevention:\n\n'
    '1. Diet: Prioritize cooling, sattvic foods like leafy greens, fruits, and whole grains. Reduce inflammatory triggers like red meat, dairy, processed foods, and excessive sugar.\n'
    '2. Manage stress: Practice yoga, meditation, and pranayama to address psychological factors that can worsen psoriasis.\n'
    '3. Detoxify: Consider Panchakarma, a personalized Ayurvedic cleansing process, to eliminate toxins and purify the body.\n\n'
    'Treatment:\n\n'
    'Internal remedies: Consult an Ayurvedic practitioner for personalized herbal formulations based on your dosha (vata, pitta, or kapha). Options include neem, turmeric, guduchi, and manjishtha for their anti-inflammatory and blood-purifying properties.\n'
    'Topical applications: Apply cooling pastes containing aloe vera, sandalwood, and neem to soothe itching and reduce inflammation.\n'
    'Abhyanga (Ayurvedic massage): Regular massage with medicated oils like coconut oil or sesame oil improves circulation and promotes relaxation.\n'
    'Shirodhara: This therapy, pouring warm oil onto the forehead, calms the nervous system and reduces stress, which can benefit psoriasis.\n\n'
    'Remember: Ayurvedic treatment is personalized and takes time for effects to manifest. Consult a qualified practitioner for a comprehensive plan and guidance.\n\n'
    'By incorporating these practices alongside medical treatment, you can empower your body to manage psoriasis naturally and experience improved skin health and overall well-being.\n\n'
    'Disclaimer: This information is not a substitute for professional medical advice. Always consult your doctor for any medical concerns.'
    )
    elif 'Impetigo' in u:
     bot_response = (
    'Bot>Impetigo: Ayurvedic Support for Soothing Skin\n'
    'While medical care is key, Ayurveda offers gentle practices to ease impetigo symptoms and promote faster healing:\n\n'
    'Prevention:\n'
    '1. Wash hands often and keep infected areas clean.\n'
    '2. Hydrate dry skin with natural oils like coconut or sesame.\n'
    '3. Protect sores from sun exposure.\n\n'
    'Treatment:\n'
    '1. Apply local honey for its antibacterial properties.\n'
    '2. Use a neem and turmeric paste for their anti-inflammatory and antimicrobial benefits.\n'
    '3. Soothe with warm Epsom salt compresses.\n'
    '4. Boost immunity with vitamin C and zinc-rich foods.\n\n'
    'Remember:\n'
    '1. Consult an Ayurvedic practitioner for personalized herbal remedies.\n'
    '2. Ayurveda complements, not replaces, medical care.\n\n'
    'By gently supporting your skin with these practices alongside medical advice, you can encourage natural healing and prevent impetigo recurrence.\n\n'
    'Disclaimer: This information is not a substitute for professional medical advice. Always consult your doctor for any medical concerns.'
)

    elif u == 'clear':
        clear_message()
        return
    else:
        bot_response = 'Bot> Do not understand you\n'

    chat_text.insert(END, bot_response + '\n')
    yi += 2

    user_entry.delete(0, 'end')

hcb_text = Label(height=2, width=14, bg='#0084ff', text='YOUR MEDICINE', font=('Impact', 20), fg='white')
hcb_text.place(x=200, y=5)

chat_bg = Frame(height=450, width=580, bg='#f5f5f5')
chat_bg.place(x=10, y=80)

chat_text = Text(chat_bg, height=22, width=86, bg='white', fg='black', font=('Helvetica', 12), wrap=WORD)
chat_text.pack(pady=10)

entry_bg = Frame(height=60, width=500, bg='white')
entry_bg.place(x=10, y=520)

sendbtn_bg = Frame(height=60, width=65, bg='white')
sendbtn_bg.place(x=525, y=520)

def on_enter(e):
    user_entry.delete(0, 'end')
    user_entry.config(fg='black')

def on_leave(e):
    n = user_entry.get()
    user_entry.config(fg='#5c5a5a')
    if n == '' or n == ' ':
        user_entry.insert(0, 'Enter message...')
        user_entry.config(fg='#5c5a5a')

user_entry = Entry(entry_bg, width=32, bg='white', font=('Helvetica', 20), relief=FLAT, border=0)
user_entry.place(x=10, y=13)
user_entry.insert(0, 'Enter message...')
user_entry.config(fg='#5c5a5a')
user_entry.bind("<FocusIn>", on_enter)
user_entry.bind("<FocusOut>", on_leave)

send_button = Button(sendbtn_bg, height=1, width=3, bg='#0084ff', text='➤', font=('Helvetica', 20),
                     activeforeground='white', fg='white', relief=FLAT, border=0,
                     activebackground='#0084ff', command=send_message)
send_button.place(x=5, y=4)
wind.bind('<Return>', lambda event: send_button.invoke())


wind.mainloop()
