-- MySQL dump 10.13  Distrib 5.1.73, for Win32 (ia32)
--
-- Host: localhost    Database: medic
-- ------------------------------------------------------
-- Server version	5.1.73-community

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `medicine`
--

DROP TABLE IF EXISTS `medicine`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `medicine` (
  `medicine_name` varchar(100) NOT NULL,
  `usage_or_indications` varchar(200) DEFAULT NULL,
  `quantity` int(11) DEFAULT NULL,
  PRIMARY KEY (`medicine_name`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `medicine`
--

LOCK TABLES `medicine` WRITE;
/*!40000 ALTER TABLE `medicine` DISABLE KEYS */;
INSERT INTO `medicine` VALUES ('1.0 Catgut Suture Needles','Suturing',0),('2.0 Catgut Suture Needles ','Suturing',0),('Acne Star Ointment ','Acne',0),('Actowin nasal Drops ','Clear Nasal Pathway',0),('Acyclofenac - P','Ortho And Muscular Pain',0),('Acyclovir Ointment','Herpes Infections',0),('Arm Sling ','Arm Fracture',0),('Asthalin Inhaler ','Bronchial Asthma And Dypnea',0),('Asthalin Respules ','Expectorant',0),('Bactogen Ointment ','Bactericidal Solution',0),('Beclasone C Ointment','Skin Infections',0),('Benzac AC Ointment ','Skin Infections',0),('Betadin Gargle Solution ','Ent Infections',0),('Betadine solution','Bactericidal Solution',0),('Betamethosone Ointment','Skin Infections',0),('Betzee Ointment ','Skin Infections',0),('Budecort Respules','Expectoration Of Sputum',0),('Burn Heal Ointment ','Treament For Burns',0),('Candispan B Cream ','Skin Infections',0),('Cap Amoxilline 200 mg','Respiratory And Skin Infections',0),('Cap Amoxilline 500 mg ','Respiratory And Skin Infections',0),('Cap E - Rich ','Vitamin Deficiencies',0),('Cap Tramacip ','Pain',0),('Cap Vitamin A & D','Visual Defects',0),('Ciclopirox Olamine Cream ','Skin Infections',0),('Ciplox E/E drops or Moxifloxacin','Ear And Eye Infections',0),('Clindamycin Lotion ','Acne',0),('Clindamycin Ointment ','Acne',0),('Clobetasol + Salcilic acid Ointment ','Dermatological Infections',0),('Clotrimoxazole Powder','Antifungal Dusting Powder',0),('Corn Caps ','Corn',0),('Cotton Roll ','Dressing',0),('Cusicrom Eye Drops','Eye Infections',0),('Dermacure Lotion ','Skin Infections',0),('Dewax Ear Drops','Ear Infections',0),('Disposable 10cc syringe','Injecting Medicine',0),('Disposable 2cc syringe','Injecting Medicine',0),('Disposable 5cc syringe','Injecting Medicine',0),('Disposable Gloves ','Asetic Technique',0),('Distilled Water','Dilution Of Medicines',0),('Easy Fix Medium ','Cannula Fixation',0),('Finger Caught ','Fractures Fingers And Toes',0),('First Aid Plasters ','Injuries And Lacerations',0),('Fusidate Sodium Ointment ','Skin Infections',0),('Gentamycin E/E Drops ','Ear And Eye Infections',0),('Glucon D Powder ','Hypoglycemia',0),('Goodnight - Fabric Roll on ','Mosquito Repellent',0),('Hydrogen Peroxide','Injecting Medicine',0),('Inj Ampicilline ','Respiratory Infection',0),('Inj ASV','Snake Bite',0),('Inj Avil ','Emergency Medicine',0),('Inj Buscopan ','Pain Abdomen',0),('Inj Cefataxim 25 mg','Gastrointestinal And Respiratory Infections',0),('Inj Decamycin ','Emergency Medicine',0),('Inj Deriphyllin ','Bronchodilator',0),('Inj Diclofenac ','Pain',0),('Inj Eptoin ','Anti Epileptic Medicine',0),('Inj Gentamycin ','Gastrointestinal And Respiratory Infections',0),('Inj KCL ','Electrolyte Imbalance',0),('Inj Kenocort ','Keloid Treatment',0),('Inj Ondansetron ','Vomitings',0),('Inj Pantoprazole ','Gastric Pain',0),('Inj PCT ','Hyper Pyrexia',0),('Inj Rantidine','H2 Receptor Agonist',0),('Inj TT','Prophylactic Medicine For Tetanus',0),('Inj Xylocaine ','Local Anasthetic Agent',0),('IV Cifran','Gastrointestinal Infections',0),('IV Dextrose','Fliud Therapy',0),('IV Metrogyl','Gastrointestinal Infections',0),('IV NS','Fluid Therapy',0),('IV RL or IV DNS','Fluid Therapy',0),('IV Sets','Fliud Therapy',0),('Ketakonazole Ointment','Dermatological Infections',0),('Ketakonazole Soap ','Demotological Infections',0),('Knee Pads ','Knee Support',0),('Kojitin Gel ','Skin Infections',0),('Lulicanazole Ointment ','Skin  Fungal Infections',0),('Malaria Testing Kits','Testing Malaria',0),('Megaheal Ointment ','Wound Healing ',0),('Melatile Cream ','Skin Infections',0),('Mesome Ointment','Hypopigmentation Of Skin',0),('Miconazole Ointment ','Taenia Infections',0),('Mometasone Ointment ','Skin Infections',0),('Mucopain Gel ','Mouth Lesions And Ulcers',0),('Mupiricin Ointment ','Wound Healing',0),('Needles 26 Guage ','Administering Medicine',0),('Neosporin Ointment ','Bactericidal ',0),('Norbox - TZ','Urinary Tract Infections',0),('Ofloxacin E/E drops ','Ear And Eye Infections',0),('Omnigel Ointment','Topical Pain Reliever',0),('Omnigel Spray','Topical Pain Reliever',0),('ORS Pockets ','Dehydration And Diarrhoel Diseases',0),('Paper Plaster ','Dressing',0),('Permithrin Lotion ','Skin Infections',0),('Povirex Ointment ','Bactericidal ',0),('Prolene 2.0 ','Suturing',0),('Prolene Suturing Material 2.0','Suturing',0),('Ring Guard Ointment ','Taenia Infections',0),('Roller Banadages 10 cm ','Dressing',0),('Roller Banadages 15 cm ','Dressing',0),('Scabiguard Lotion ','Scabies',0),('Smyle Gel','Dental Cleaning Agent',0),('Soft Crape Bandage','Edema And Fracture',0),('Spirit','Bactericidal Solution',0),('Sterile Pads ','Dressing',0),('Sterilium rub handwash ','Hand Steriliser',0),('Sunban Cream ','Sun Sensitivity',0),('Surgirical blades ','For Dressing',0),('Syp Amrox LS','Expectorant',0),('Syp Atarax ','Allergic Conditions',0),('Syp Augumentin ','Respiratory Infections',0),('Syp Calcium ','Calcium Suppliments',0),('Syp Citralka','Urinary Tract Infections',0),('Syp Coldlay Plus ','Upper Respiratory Infections',0),('Syp CPM ','Allergic Conditions And Upper Respiratory Infections',0),('Syp Cremaffin ','Constipation',0),('Syp Dexorange ','Iron And Multivitamin Suppliments',0),('Syp Furajolidine ','Diarrhoea',0),('Syp Gelucil ','Gastric Pain',0),('Syp Ivermectin + Albendazole','Deworming',0),('Syp Levosetride ','Upper Respiratory Infections',0),('Syp Meftal P ','Spasmodic Pain',0),('Syp Metrogyl','Gastrointestinal  Infections',0),('Syp Multivitamin ','Vitamin Deficiencies',0),('Syp Ondonsetron ','Nausea And Vomitings',0),('Syp Paracetimol P125 mg','Fever',0),('Syp Parecetimol P250 mg','Fever',0),('Syp Q - Coril ','Dry Cough',0),('Syp Tusq','Expectorant',0),('Syp Zincovit','Multivitamin Suppliment',0),('Tab Acefexac-SP','Antiinflammatory',0),('Tab Acyclovir ','Herpes Infections',0),('Tab Albendazole','Deworming',0),('Tab Amlodipine','Antihypertensive',0),('Tab Amoxiclav 375 mg ','Respiratory And Skin Infections',0),('Tab Amoxiclav 625 mg','Respiratory And Skin Infections',0),('Tab Atarax ','Allergic Conditions',0),('Tab Atenolol','Cold And Respiratoy Infections',0),('Tab Azax 250 mg ','Respiratory And Skin Infections',0),('Tab Azax 500 mg ','Respiratory And Skin Infections',0),('Tab B - Complex','Vitamin Deficiencies',0),('Tab Calcium','Supplimentation or Orthopedic Problems',0),('Tab Cefixime 100 mg ','Fever And Gastrointestinal Infections',0),('Tab Cefixime 200 mg ','Fever And Gastrointestinal Infections',0),('Tab Chymoral Forte','Ortho And Muscular Pain',0),('Tab Cifran 250 mg','Infections or Wound Healing And Fever',0),('Tab Cifran 500 mg','Infections or Wound Healing And Fever',0),('Tab Clarithromycin','Skin And Respiratory Infections',0),('Tab CPM','Allergic Conditions',0),('Tab CPM+ Paracetimol','Upper Respiratory Infections',0),('Tab Cyclopam','Pain Abdomen',0),('Tab Defnac - P ','Pain And Fever',0),('Tab Demisone','Hypersensitivity',0),('Tab Deriphylline','Dyspnoea',0),('Tab Diclofenac','Pain',0),('Tab Dicyclomine','Pain Abdomen',0),('Tab Dizene','Indigestion',0),('Tab Doxycycline','Fever',0),('Tab Erythromycin','Respiratory And Skin Infections',0),('Tab Glibenclamide ','Diabetis Mellitus',0),('Tab Glimpramide ','Diabetis Mellitus',0),('Tab Iron and Folic Acid','Anemia',0),('Tab Itrakonazole 200 mg ','Tenia Infections',0),('Tab Ivermectin + Albendazole','Deworming',0),('Tab Ivoral Forte','NA',0),('Tab Lariago','Anti Malaria',0),('Tab Levoflaxacin ','NA',0),('Tab Levosetride','Allergic Conditions',0),('Tab Levosetride + Montelukast ','Allergic Cough And Respiratory Infections',0),('Tab Meftalspas','Spasmodic Pain',0),('Tab Metformin 500 mg ','Diabetis Mellitus',0),('Tab Metrozyl','Gastriintestinal Infections',0),('Tab Mulitivitamin ','Vitamin Deficiencies',0),('Tab Omez D ','Gastritis',0),('Tab Omez Insta','Gastric Pain ',0),('Tab Ondiron','Nausea And Vomitings',0),('Tab Onecan 150 mg (Fluconagole)','Antifungal',0),('Tab Ornamac','Fever',0),('Tab Orniazole','Urinary  And Intestinal  Infections',0),('Tab Pantop -D','Gastric Pain',0),('Tab Pantoprazole40 mg ','H2 Receptor Agonist',0),('Tab Paracetimol 500 mg ','Fever And Inflammations',0),('Tab Paracetimol 650 mg','Fever And Inflammations',0),('Tab Polypod 200 mg','Respiratory And Other Infections',0),('Tab Rantac 150 mg ','Gastric Pain ',0),('Tab Reactin 100SR','Severe Pain',0),('Tab Rebagen','Gastic Pain',0),('Tab Sera Peptidose','Edema',0),('Tab Seratio + Acyclo + Paracetimol ','Injuries And Edeme',0),('Tab Sestil AD','Diarrohea And Dycenty',0),('Tab Setride','Cold And Allergies',0),('Tab Sporalac ','Diarrhoeal Diseases',0),('Tab Telna - H','Antihypertensive',0),('Tab Terbinafin ','Tenia Infections',0),('Tab Thyronorm 100 mg ','Hypothyroid Disorders',0),('Tab Ultrabest','Pain ',0),('Tab Vitamin - C ','Wound Healing And Treat Gums Bleeding',0),('Terbinafin Lotion ','Tenia Infections',0),('Thrombopheb Ointment','Local Erythema',0),('Tobest - F Eye Drops ','Eye Injuries/Infections',0),('Tretinoin Cream ','Skin Infections',0),('Typhoid Testing Kits ','Typhoid Testing',0),('Ulciwock Gel','Mouth Lesions And Ulcers',0),('Vicks Inhalers ','Nasal Congestion',0),('White Bamboo plaster ','Dressing or Splinting',0),('Xylocaine Gel ','Local Anasthetic Agent',0),('Zincoderm Ointment ','Skin Infections',0);
/*!40000 ALTER TABLE `medicine` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2020-09-18 16:40:29
