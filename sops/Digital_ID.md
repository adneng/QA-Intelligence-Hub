# 🛡️ Digital National ID: Sync Issues

**System:** eGovPH App / PSA | **Category:** National ID Fetching

Ang guide na ito ay para sa mga user na hindi lumalabas ang Digital ID o hindi nag-si-sync ang data mula sa PSA.

---

### 🚩 Step 1: Pre-Verification (The "Bakit" Check)
Bago mag-proceed sa technical fixes, tanungin muna ang user:

* **Agency Registration:** Nag-register na ba ang user sa PSA (ePhilID/PVC)?
    * *Note: Ang eGov App ay tagafetch lang ng data; dapat existing ang record sa PSA.*
      
* **Information Changes:** May binago ba sa information kamakailan? (e.g., corrected spelling, change status).
  
* **Agency Confirmation:** Kinumpirma ba ng PSA na updated na ang record? Confirmed na ang changes kapag na-issuehan na si user ng bagong ePhilID with changes reflecting.

---

### 📉 Step 2: Troubleshooting Flow (The Decision Tree)

#### **Path: PSA Update Found? (YES)**
1.  **Issued New ePhilID:** Siguraduhing nakuha na ang bagong ePhilID at nagrereflect na ang updates na ginawa.

2.  **Delete Account:** I-delete ang account sa eGovPH app.
   
3.  **Re-Verify:** Gamitin ang **Updated Information** sa pag-verify.
   
4.  **Result:**
    * Pag lumabas ang DNI -> **SUCCESS (END)**.
    * Pag ayaw pa rin -> **Inform DNI Team** para sa escalation.

#### **Path: PSA Update Found? (NO)**
1.  **Log Concern:** I-record ang issue sa **"No Connection Form"**.
   
2.  **PSA Handling:** DNI team will forward to PSA Team for validation.
   
3.  **Intervention:** Hintayin ang DNI Team intervention para ma-sync ang record.

4. **DNI Team Confirmation** Kapag nag-confirm na si DNI team na okay na ang DNI, ipa-reverify si user.

---

### 📊 Process Map
![Digital ID Flowchart](https://github.com/adneng/QA-Intelligence-Hub/blob/main/sops/DNI%20FLOWCHART.jpg?raw=true)

> **Pro-Tip for Staff:** Laging i-check kung "No Connection" ang error o "Record Not Found." Pag "Record Not Found," madalas ay nasa PSA side ang kulang (Step 1).

