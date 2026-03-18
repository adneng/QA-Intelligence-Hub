# 🛡️ eKYC & Face Verification: Troubleshooting Guide

**System:** eGovPH App / eKYC | **Category:** Identity Verification

Ang guide na ito ay para sa mga issues habang nag-su-submit ng face capture o eKYC process.

---

### 🔍 Issue 1: Face Not Detected
*Madalas mangyari kapag hindi ma-identify ng system ang mukha sa frame.*

**Possible Causes:**
* Low lighting o overexposed (masyadong maliwanag) na environment.
* Face is not centered o partially visible lang.
* Camera is blocked o madumi ang lens.
* Camera permission is disabled sa phone settings.

**Resolution:**
1. **Lighting:** Siguraduhing maliwanag ang harap ng mukha at walang "backlight."
2. **Alignment:** I-gitna ang mukha sa frame; dapat buong mukha ang nakikita.
3. **Hardware Check:** Linisin ang camera lens.
4. **Permissions:** I-enable ang *Camera Permission* sa App Settings.

&nbsp;
&nbsp;

---

### 🔍 Issue 2: Process Suddenly Stops / Exits
*Kapag biglang nagsasara ang app o bumabalik sa simula ang process.*

**Possible Causes:**
* App moved to background (lumipat ng ibang app ang user).
* Screen timeout o na-lock ang phone.
* Device-specific behavior (e.g., Samsung "App Pause" issue).

**Resolution:**
1. **Stay Active:** Panatilihing nakabukas ang app sa *foreground* buong process.
2. **Settings:** Pansamantalang i-disable ang screen timeout.
3. **User Advice:** Sabihan ang user: *Do not pause or stop mid-process.*
4. **Retry:** Dahil ito ay *non-resumable*, kailangang ulitin mula sa start.

&nbsp;
&nbsp;

---

### 🔍 Issue 3: Stuck / Loading / Not Submitting
*Ito ay karaniwang network o API-related issue.*

**Possible Causes:**
* Unstable na internet connection.
* API timeout o mabagal na response mula sa server.
* Network switching (halimbawa: biglang lumipat mula WiFi papuntang Data).

**Resolution:**
1. **Connection:** Lumipat sa stable na WiFi o malakas na data signal.
2. **Cooldown:** Subukan ulit pagkalipas ng ilang minuto.
3. **Consistency:** Iwasang magpalit ng network habang ongoing ang capture.

&nbsp;
&nbsp;

---

### 🔍 Issue 4: Repeated Failure (Multiple Attempts)
*Kapag paulit-ulit na nag-e-error kahit sinunod na ang steps.*

**Possible Causes:**
* Device compatibility issues.
* Low device performance (mabagal ang processing ng camera).
* Outdated ang version ng app.

**Resolution:**
1. **Update:** I-update ang eGovPH app sa pinakabagong version.
2. **Restart:** I-restart ang device para ma-clear ang RAM.
3. **Isolate:** Subukan sa ibang device para malaman kung sa phone ba ang issue.

&nbsp;
&nbsp;

---

### 🔍 Issue 5: Immediate Failure After Capture
*Naka-capture na pero nag-e-error agad pagkatapos i-submit.*

**Possible Causes:**
* Backend validation failure.
* Image quality (malabo o pixelated).
* Face mismatch o detection inconsistency.

**Resolution:**
1. **Steady:** Ulitin nang may mas maayos na lighting at hindi gumagalaw.
2. **No Obstruction:** Tanggalin ang mask, cap, o salamin kung kinakailangan.
3. **Escalate:** Kung persistent, i-refer na sa Technical Team.

&nbsp;
&nbsp;

---

### ⚙️ Standard Checks (Always Perform)
Bago mag-escalate, siguraduhing na-check ang **"Big Five"**:
1. [ ] **Camera Permission** = Enabled
2. [ ] **Internet Connection** = Stable
3. [ ] **App Version** = Updated
4. [ ] **App Status** = Stay in Foreground
5. [ ] **Environment** = Proper Lighting

&nbsp;
&nbsp;
