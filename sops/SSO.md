
# 🔗 SSO Integration: Troubleshooting Guide

**System:** eGovPH / Single Sign-On | **Category:** Account Linking & Integration

Ang guide na ito ay para sa mga isyu sa pag-access ng Agency Services (hal. GSIS, PAG-IBIG, PhilHealth, etc.) gamit ang eGovPH SSO.

---

### 📋 Requirements for SSO Integration
Bago simulan ang troubleshooting, siguraduhin na ang user ay:
1. **Verified eGovPH App Account** (Dapat may Blue Check).
2. **Matching Details** sa eGovPH app at sa mismong Agency record.
3. **Existing Records** sa agency na sinusubukang i-access.

&nbsp;
&nbsp;

---

### 1️⃣ Confirm Account Matching (MOST COMMON)
I-check kung tugma ang details sa pagitan ng **eGovPH account** vs **Agency account**.

**Ano ang dapat i-verify?**
* **Email Address:** Dapat exact match (walang typos o extra spaces).
* **Mobile Number:** Consistent dapat ang format (may o walang +63).
* **Full Name:** I-check ang middle name, suffix (Jr., III), at tamang spelling.

👉 **If hindi matched:** Ang SSO ay mag-fa-fail o hindi mag-re-redirect nang tama. Sabihan ang user na i-align ang details o gamitin ang tamang account.

&nbsp;

---

### 2️⃣ Existing vs Non-Existing Agency Account
Tanungin ang user: *“May existing account na po ba kayo sa agency na ina-access niyo?”*

**Important Cases:**
* ❌ **No account:** Sa karamihan ng agencies, **hindi** awtomatikong gagawa ng bagong account ang SSO.
* ⚠️ **Pre-registration:** May mga agencies na kailangan munang mag-register sa kanilang website bago gumana ang SSO.

👉 **Action:** Advise the user to register directly sa agency website muna.

&nbsp;

---

### 3️⃣ Wrong Account Linked
Maaaring ang user ay may:
* Multiple emails o mobile numbers.
* Naka-login sa eGovPH gamit ang isang email, pero iba ang email na gamit sa Agency.

👉 **Action:** I-confirm kung aling account ang ginagamit sa magkabilang side. Ipa-login ang user gamit ang tamang matching account.

&nbsp;

---

### 4️⃣ Session / Token Expired
**Symptoms:**
* Walang nangyayari pagkatapos i-click ang service.
* Redirect loop (pabalik-balik).
* Biglang bumabalik sa Home screen.

👉 **Action:** **Log out → Log in** ulit. Force close ang app, i-reopen, at i-retry ang SSO.

&nbsp;

---

### 5️⃣ SSO Redirection Issue (App Behavior)
Kapag nag-ta-tap ng service pero stuck sa loading o walang nangyayari.

👉 **Basic Fixes:**
1. Maghintay ng ilang segundo at i-retry.
2. Mag-switch ng internet (Data to WiFi or vice versa).
3. I-clear ang app cache.

&nbsp;

---

### 6️⃣ Agency System Limitation / Downtime
Tandaan: Ang SSO ay depende sa backend ng Agency.

**Possible Issues:**
* Under maintenance ang agency portal.
* Service unavailable o down ang SSO endpoint.

👉 **Action:** Subukang i-access nang direkta ang website ng agency. Kung down
