# 🛡️ Digital National ID: Sync Issues
**System:** eGovPH / PSA 
**Category:** Data Fetching

### 🚩 Pre-Verification Steps
* **Agency Registration:** Did the user register with the concerned agency (PSA, Philhealth)? 
> **NOTE:** eGov App cannot register information for you; we only fetch data from the agency.
* **Information Changes:** Did you make any changes to your information lately?
* **Agency Confirmation:** Did the agency confirm the update?

### 🛠️ Technical Fixes
If the steps above are confirmed, perform the following in order:
1. **Refresh Session:** Logout and login again in the eGovPH App.
2. **Clear Storage:** Clear App Cache and Data in phone settings.
3. **Re-sync:** Login again and check the Digital ID section.

```mermaid
graph TD
    Start([START]) --> Confirm[Confirm Registration]
    Confirm --> Recent{Ask if there's<br/>Recent PSA Update}
    
    PVC[WITH ePhilID OR PVC] --> Recent
    
    Recent --> UpdateFound{PSA Update<br/>Found?}
    
    %% YES PATH
    UpdateFound -- YES --> Issued[ISSUED NEW ePhilID]
    Issued --> Delete[DELETE ACCOUNT]
    Delete --> ReVerify[RE-VERIFY USING THE<br/>UPDATED INFORMATION]
    ReVerify --> DNIDisplays{DNI<br/>Displays?}
    
    DNIDisplays -- YES --> End([END])
    DNIDisplays -- NO --> Inform[INFORM THE DNI TEAM]
    
    %% NO PATH
    UpdateFound -- NO --> Log[LOG CONCERN TO<br/>'NO CONNECTION FORM']
    Log --> PSAs[PSA'S HANDLING]
    PSAs --> Intervention[DNI TEAM INTERVENTION]
    Intervention --> End
    
    Inform --> PSAs
    
    %% Styling
    style Start fill:#85a828,color:#fff
    style End fill:#a31d21,color:#fff
    style UpdateFound fill:#ffcc80
    style DNIDisplays fill:#ffcc80
