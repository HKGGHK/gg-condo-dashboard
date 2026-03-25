GG Framework: Condo Logic Skills



Skill: Calculate\_CAM\_FeesLogic: 

* Area \\times 59$ THB.
* Constraint: Always round up to the nearest Baht.
* Context: The base fee is 45 THB, but the effective rate with annual extras is 59 THB/sqm.



Skill: Generate\_PromptPay\_QR

* Logic: Use the Thai QR Payment Standard (EMVCo).
* Input: amount (from CAM Fee calculation), biller\_id (To be provided by Juristic).
* Requirement: The QR must be generated as a high-resolution SVG for clear scanning on mobile screens.



Skill: Bilingual\_Translation\_Check

* Logic: Cross-reference English labels with Thai equivalents.
* Standard: Use "นิติบุคคล" for "Juristic Office" and "ค่าส่วนกลาง" for "CAM Fees".

