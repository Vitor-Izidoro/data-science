# data-science
# Student Dropout and Academic Success Dataset

## Overview
This dataset contains comprehensive information about students enrolled in higher education, including demographic data, socio-economic factors, academic performance across two semesters, and macroeconomic indicators at the time of enrollment. 

The primary objective of this dataset is to predict student outcomes at the end of the normal duration of their course, formulated as a three-category classification task.

* **Total Features:** 34
* **Target Variable:** 1 (`Target`)
* **Missing Values:** None (0 missing values across all columns)

---

## Target Variable

| Variable Name | Role | Type | Description |
| :--- | :--- | :--- | :--- |
| **Target** | Target | Categorical | The academic outcome of the student: **Dropout**, **Enrolled**, or **Graduate**. |

---

## Data Dictionary

### 1. Demographic & Socio-Economic Features
| Variable Name | Type | Description |
| :--- | :--- | :--- |
| **Marital Status** | Integer | The marital status of the student. *(See Encodings)* |
| **Nacionality** | Integer | The nationality of the student. *(See Encodings)* |
| **Gender** | Integer | 1 = Male; 0 = Female |
| **Age at enrollment** | Integer | Age of the student at the time of enrollment. |
| **Displaced** | Integer | 1 = Yes; 0 = No |
| **Educational special needs** | Integer | 1 = Yes; 0 = No |
| **Debtor** | Integer | 1 = Yes; 0 = No |
| **Tuition fees up to date** | Integer | 1 = Yes; 0 = No |
| **Scholarship holder** | Integer | 1 = Yes; 0 = No |
| **International** | Integer | 1 = Yes; 0 = No |
| **Mother's qualification** | Integer | Education level of the student's mother. *(See Encodings)* |
| **Father's qualification** | Integer | Education level of the student's father. *(See Encodings)* |
| **Mother's occupation** | Integer | Occupation of the student's mother. *(See Encodings)* |
| **Father's occupation** | Integer | Occupation of the student's father. *(See Encodings)* |

### 2. Academic Enrollment Features
| Variable Name | Type | Description |
| :--- | :--- | :--- |
| **Application mode** | Integer | The method of application to the course. *(See Encodings)* |
| **Application order** | Integer | Application order choice (between 0 - first choice; and 9 - last choice). |
| **Course** | Integer | The specific course the student enrolled in. *(See Encodings)* |
| **Daytime/evening attendance** | Integer | 1 = Daytime; 0 = Evening |
| **Previous qualification** | Integer | Highest education level achieved prior to enrollment. *(See Encodings)* |
| **Previous qualification (grade)** | Continuous | Grade of previous qualification (between 0 and 200). |
| **Admission grade** | Continuous | Admission grade (between 0 and 200). |

### 3. Academic Performance (1st & 2nd Semesters)
*Note: All grade averages are scaled between 0 and 20.*

| Variable Name | Type | Description |
| :--- | :--- | :--- |
| **Curricular units 1st/2nd sem (credited)** | Integer | Number of curricular units credited in the respective semester. |
| **Curricular units 1st/2nd sem (enrolled)** | Integer | Number of curricular units enrolled in the respective semester. |
| **Curricular units 1st/2nd sem (evaluations)** | Integer | Number of evaluations to curricular units in the respective semester. |
| **Curricular units 1st/2nd sem (approved)** | Integer | Number of curricular units approved in the respective semester. |
| **Curricular units 1st/2nd sem (grade)** | Continuous | Grade average in the respective semester. |
| **Curricular units 1st/2nd sem (without evaluations)** | Integer | Number of curricular units without evaluations in the respective semester. |

### 4. Macroeconomic Indicators
| Variable Name | Type | Description |
| :--- | :--- | :--- |
| **Unemployment rate** | Continuous | Unemployment rate (%) at the time. |
| **Inflation rate** | Continuous | Inflation rate (%) at the time. |
| **GDP** | Continuous | Gross Domestic Product index. |

---

## Categorical Encodings Reference

### Marital Status
* `1` - Single
* `2` - Married
* `3` - Widower
* `4` - Divorced
* `5` - Facto union
* `6` - Legally separated

### Course
* `33` - Biofuel Production Technologies
* `171` - Animation and Multimedia Design
* `8014` - Social Service (evening attendance)
* `9003` - Agronomy
* `9070` - Communication Design
* `9085` - Veterinary Nursing
* `9119` - Informatics Engineering
* `9130` - Equinculture
* `9147` - Management
* `9238` - Social Service
* `9254` - Tourism
* `9500` - Nursing
* `9556` - Oral Hygiene
* `9670` - Advertising and Marketing Management
* `9773` - Journalism and Communication
* `9853` - Basic Education
* `9991` - Management (evening attendance)

<details>
<summary><b>Click to expand: Application Mode</b></summary>

* `1` - 1st phase - general contingent
* `2` - Ordinance No. 612/93
* `5` - 1st phase - special contingent (Azores Island)
* `7` - Holders of other higher courses
* `10` - Ordinance No. 854-B/99
* `15` - International student (bachelor)
* `16` - 1st phase - special contingent (Madeira Island)
* `17` - 2nd phase - general contingent
* `18` - 3rd phase - general contingent
* `26` - Ordinance No. 533-A/99, item b2) (Different Plan)
* `27` - Ordinance No. 533-A/99, item b3 (Other Institution)
* `39` - Over 23 years old
* `42` - Transfer
* `43` - Change of course
* `44` - Technological specialization diploma holders
* `51` - Change of institution/course
* `53` - Short cycle diploma holders
* `57` - Change of institution/course (International)
</details>

<details>
<summary><b>Click to expand: Previous, Mother's, and Father's Qualifications</b></summary>

*Includes varying intersections of the following common codes:*
* `1` - Secondary education / 12th Year
* `2` - Higher education - bachelor's degree
* `3` - Higher education - degree
* `4` - Higher education - master's
* `5` - Higher education - doctorate
* `6` - Frequency of higher education
* `9` - 12th year of schooling - not completed
* `10` - 11th year of schooling - not completed
* `11` - 7th Year (Old)
* `12` - Other - 11th year of schooling
* `14` - 10th year of schooling
* `19` - Basic education 3rd cycle (9th/10th/11th year)
* `34` - Unknown
* `35` - Can't read or write
* `37` - Basic education 1st cycle (4th/5th year)
* `38` - Basic education 2nd cycle (6th/7th/8th year)
* `39` - Technological specialization course
* `40` - Higher education - degree (1st cycle)
* `42` - Professional higher technical course
* `43` - Higher education - master (2nd cycle)
*(Note: Refer to raw data for exhaustive distinct mappings for Mother vs. Father specific historical courses like "General commerce course" etc.)*
</details>

<details>
<summary><b>Click to expand: Nationality</b></summary>

* `1` - Portuguese
* `2` - German
* `6` - Spanish
* `11` - Italian
* `13` - Dutch
* `14` - English
* `17` - Lithuanian
* `21` - Angolan
* `22` - Cape Verdean
* `24` - Guinean
* `25` - Mozambican
* `26` - Santomean
* `32` - Turkish
* `41` - Brazilian
* `62` - Romanian
* `100` - Moldova (Republic of)
* `101` - Mexican
* `103` - Ukrainian
* `105` - Russian
* `108` - Cuban
* `109` - Colombian
</details>

<details>
<summary><b>Click to expand: Occupations (Mother & Father)</b></summary>

* `0` - Student
* `1` - Representatives of the Legislative Power and Executive Bodies, Directors...
* `2` - Specialists in Intellectual and Scientific Activities
* `3` - Intermediate Level Technicians and Professions
* `4` - Administrative staff
* `5` - Personal Services, Security and Safety Workers and Sellers
* `6` - Farmers and Skilled Workers in Agriculture...
* `7` - Skilled Workers in Industry, Construction and Craftsmen
* `8` - Installation and Machine Operators and Assembly Workers
* `9` - Unskilled Workers
* `10` - Armed Forces Professions
* `90` - Other Situation
* `99` - (blank)
*(Additional specialized codes 101-195 represent granular breakdowns of these macro categories).*
</details>
