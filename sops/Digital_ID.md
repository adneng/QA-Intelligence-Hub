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

graph TD
    %% Define the distinct START node
    START([START])
    
    %% Connect the two initial nodes to START
    START --> Confirm[Confirm Registration]
    START --> PVC[WITH ePhilID OR PVC]
    
    %% Define the first question/condition
    Question1{Ask if there's<br/>Recent PSA Update}
    
    %% Connect initial nodes to the first question
    Confirm --> Question1
    PVC --> Question1
    
    %% First decision point
    Question1 --> UpdateFound{PSA Update<br/>Found?}
    
    %% YES PATH
    UpdateFound -- YES --> Issued[ISSUED NEW ePhilID]
    Issued --> Delete[DELETE ACCOUNT]
    Delete --> ReVerify[RE-VERIFY USING THE<br/>UPDATED INFORMATION]
    
    %% Second decision point
    ReVerify --> DNIDisplays{DNI DISPLAYS?}
    
    %% Path to END
    DNIDisplays -- YES --> End([END])
    DNIDisplays -- NO --> Inform[INFORM THE DNI TEAM]
    Inform --> PSAs[PSA'S HANDLING]
    PSAs --> Intervention[DNI TEAM INTERVENTION]
    Intervention --> End
    
    %% NO PATH
    UpdateFound -- NO --> Log[LOG CONCERN TO<br/>'NO CONNECTION FORM']
    Log --> PSAs
    
    %% Simplified Styling for High Contrast Black Text
    style START fill:#85a828,color:#fff,stroke:#333,stroke-width:2px
    style End fill:#a31d21,color:#fff,stroke:#333,stroke-width:2px
    style UpdateFound fill:#FFD580,stroke:#333,stroke-width:2px
    style DNIDisplays fill:#FFD580,stroke:#333,stroke-width:2px
    style Question1 fill:#fff,stroke:#333,stroke-width:2px
    style Confirm fill:#f9f9f9,stroke:#333,stroke-width:2px
    style PVC fill:#f9f9f9,stroke:#333,stroke-width:2px
    style Issued fill:#f9f9f9,stroke:#333,stroke-width:2px
    style Delete fill:#f9f9f9,stroke:#333,stroke-width:2px
    style ReVerify fill:#f9f9f9,stroke:#333,stroke-width:2px
    style Inform fill:#f9f9f9,stroke:#333,stroke-width:2px
    style Log fill:#f9f9f9,stroke:#333,stroke-width:2px
    style PSAs fill:#f9f9f9,stroke:#333,stroke-width:2px
    style Intervention fill:#f9f9f9,stroke:#333,stroke-width:2px
