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
    %% START PHASE
    subgraph S1 [Entry Points]
        START([START]) -- 1 --> CR[Confirm Registration]
        START -- 2 --> PVC[WITH ePhilID OR PVC]
    end

    %% ANALYSIS PHASE
    subgraph S2 [PSA Validation]
        CR --> Q1{Ask if there's<br/>Recent PSA Update}
        PVC --> Q2{Ask if there's<br/>Recent PSA Update}
        Q1 --> PUF{PSA UPDATE<br/>FOUND?}
        Q2 --> PUF
    end

    %% RESOLUTION PATH
    subgraph S3 [Technical Fixes]
        PUF -- YES --> ISS[ISSUED NEW ePhilID]
        ISS --> DEL[DELETE ACCOUNT]
        DEL --> RV[RE-VERIFY USING THE<br/>UPDATED INFORMATION]
        RV --> DD{DNI DISPLAYS?}
    end

    %% ESCALATION PATH
    subgraph S4 [Escalation]
        PUF -- NO --> LOG[LOG CONCERN TO<br/>'NO CONNECTION FORM']
        DD -- NO --> INF[INFORM THE DNI TEAM]
        INF --> PSA[PSA'S HANDLING]
        LOG --> PSA
        PSA --> DNI[DNI TEAM INTERVENTION]
    end

    %% EXIT
    DD -- YES --> END([END])
    DNI --> END

    %% --- STYLING (To match your photo) ---
    
    %% Colors
    style START fill:#85a828,color:#fff,stroke:#fff
    style END fill:#a31d21,color:#fff,stroke:#fff
    
    %% Blue Boxes (Steps)
    classDef blueBox fill:#9dc3e6,color:#fff,stroke:#7fa8d1,stroke-width:1px;
    class CR,PVC,Q1,Q2,ISS,DEL,RV blueBox;

    %% Orange Diamonds (Decisions)
    classDef orangeDiamond fill:#ffd966,color:#fff,stroke:#e6b422,stroke-width:1px;
    class PUF,DD orangeDiamond;

    %% Light Orange Boxes (Escalation)
    classDef lightOrange fill:#fce4d6,color:#d28652,stroke:#d28652,stroke-width:1px;
    class LOG,INF,PSA,DNI lightOrange;

    %% Subgraph Styling (Invisible or Light)
    style S1 fill:none,stroke:#ccc,stroke-dasharray: 5 5
    style S2 fill:none,stroke:#ccc,stroke-dasharray: 5 5
    style S3 fill:none,stroke:#ccc,stroke-dasharray: 5 5
    style S4 fill:none,stroke:#ccc,stroke-dasharray: 5 5
    
    %% Box (Subgraph) Styling
    style START_PHASE fill:transparent,stroke:#fff,stroke-dasharray: 5 5
    style ANALYSIS fill:transparent,stroke:#fff,stroke-dasharray: 5 5
    style RESOLUTION fill:transparent,stroke:#fff,stroke-dasharray: 5 5
    style ESCALATION fill:transparent,stroke:#fff,stroke-dasharray: 5 5
