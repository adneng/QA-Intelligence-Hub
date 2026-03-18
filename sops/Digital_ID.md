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
graph LR
    %% Direction changed to LR (Left to Right)
    
    subgraph START_PHASE [Inbound / Verification]
        START([START]) --> Confirm[Confirm Registration]
        START --> PVC[WITH ePhilID OR PVC]
        Confirm --> Question1{Ask if there's<br/>Recent PSA Update}
        PVC --> Question1
    end

    subgraph ANALYSIS [PSA Validation]
        Question1 --> UpdateFound{PSA Update<br/>Found?}
        UpdateFound -- NO --> Log[LOG TO 'NO<br/>CONNECTION FORM']
    end

    subgraph RESOLUTION [Technical Fixes]
        UpdateFound -- YES --> Issued[ISSUED NEW ePhilID]
        Issued --> Delete[DELETE ACCOUNT]
        Delete --> ReVerify[RE-VERIFY WITH<br/>UPDATED INFO]
        ReVerify --> DNIDisplays{DNI<br/>Displays?}
    end

    subgraph ESCALATION [External Handling]
        DNIDisplays -- NO --> Inform[INFORM DNI TEAM]
        Inform --> PSAs[PSA'S HANDLING]
        Log --> PSAs
        PSAs --> Intervention[DNI TEAM INTERVENTION]
    end

    %% Final Exit
    DNIDisplays -- YES --> End([END])
    Intervention --> End

    %% Simplified Styling
    style START fill:#85a828,color:#fff,stroke:#333,stroke-width:2px
    style End fill:#a31d21,color:#fff,stroke:#333,stroke-width:2px
    style UpdateFound fill:#FFD580,stroke:#333,stroke-width:2px
    style DNIDisplays fill:#FFD580,stroke:#333,stroke-width:2px
    
    %% Box (Subgraph) Styling
    style START_PHASE fill:transparent,stroke:#fff,stroke-dasharray: 5 5
    style ANALYSIS fill:transparent,stroke:#fff,stroke-dasharray: 5 5
    style RESOLUTION fill:transparent,stroke:#fff,stroke-dasharray: 5 5
    style ESCALATION fill:transparent,stroke:#fff,stroke-dasharray: 5 5
