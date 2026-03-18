# 🛡️ Digital National ID: Sync Issues

**System:** eGovPH App / PSA | **Category:** National ID Fetching

Ang guide na ito ay para sa mga user na hindi lumalabas ang Digital ID o hindi nag-si-sync ang data mula sa PSA.

---

### 🚩 Step 1: Pre-Verification (The "Bakit" Check)
Bago mag-proceed sa technical fixes, tanungin muna ang user:

* **Agency Registration:** Nag-register na ba ang user sa PSA (ePhilID/PVC)?
    * *Note: Ang eGov App ay tagafetch lang ng data; dapat existing ang record sa PSA.*
* **Information Changes:** May binago ba sa information kamakailan? (e.g., corrected spelling, change status).
* **Agency Confirmation:** Kinumpirma ba ng PSA na updated na ang record?

---

### 🛠️ Step 2: Technical Fixes (The "Basic" Reset)
Kung confirmed na registered ang user, ipagawa ang mga sumusunod:

1.  **Refresh Session:** Logout at Login ulit sa eGovPH App.
2.  **Clear Storage:** I-clear ang **App Cache** at **Data** sa phone settings.
3.  **Re-sync:** Login muli at i-check ang Digital ID section.

---

### 📉 Step 3: Troubleshooting Flow (The Decision Tree)

Kung hindi pa rin gumagana pagkatapos ng Technical Fixes, sundin ang logic na ito base sa ating official flowchart:

#### **A. Initial Entry Point**
* Simulan sa **Confirm Registration** or check if they have **ePhilID/PVC**.
* **Tanong:** *"May recent PSA Update ba ang user?"*

#### **B. Path: PSA Update Found? (YES)**
1.  **Issued New ePhilID:** Siguraduhing nakuha na ang bagong record.
2.  **Delete Account:** I-delete ang account sa eGovPH app (if necessary/applicable).
3.  **Re-Verify:** Gamitin ang **Updated Information** sa pag-verify.
4.  **Result:**
    * Pag lumabas ang DNI -> **SUCCESS (END)**.
    * Pag ayaw pa rin -> **Inform DNI Team** para sa escalation.

#### **C. Path: PSA Update Found? (NO)**
1.  **Log Concern:** I-record ang issue sa **"No Connection Form"**.
2.  **PSA Handling:** I-forward sa PSA representative for validation.
3.  **Intervention:** Hintayin ang DNI Team intervention para ma-sync ang record.

---

### 📊 Process Map
![Digital ID Flowchart](LINK_NG_IMAGE_MO_DITO)

> **Pro-Tip for Staff:** Laging i-check kung "No Connection" ang error o "Record Not Found." Pag "Record Not Found," madalas ay nasa PSA side ang kulang (Step 1).

---
### 📊 Process Flowchart
![Digital ID Troubleshooting Flow](https://github.com/adneng/QA-Intelligence-Hub/blob/main/sops/DNI%20FLOWCHART.jpg?raw=true)
