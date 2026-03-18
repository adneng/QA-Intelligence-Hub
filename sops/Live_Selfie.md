#🔍 Issue 1: Face Not Detected
Possible Causes:
Low lighting / overexposed environment


Face not centered or partially visible


Camera blocked / dirty lens


Camera permission disabled


Resolution:
Ensure proper lighting (front-facing, no backlight)


Align face within frame (full face visible)


Clean camera lens


Enable Camera Permission in app settings



🔍 Issue 2: eKYC Process Suddenly Stops / Exits
Possible Causes:
App moved to background (user switched apps)


Screen timeout / phone locked


Device-specific behavior (e.g. Samsung pause issue)


Resolution:
Keep app in foreground during entire process


Disable screen timeout temporarily


Advise user: do not pause or stop mid-process


Retry from start (non-resumable process)



🔍 Issue 3: Stuck / Loading / Not Submitting
Possible Causes:
Unstable internet connection


API timeout / slow response


Network switching (WiFi → Data)


Resolution:
Switch to stable connection (WiFi or strong data)


Retry after a few minutes


Avoid switching networks during process



🔍 Issue 4: Repeated Failure (Multiple Attempts)
Possible Causes:
Device compatibility issue


Low device performance (camera/processing limits)


App version outdated


Resolution:
Update app to latest version


Restart device


Try on a different device (isolate issue)



🔍 Issue 5: Immediate Failure After Capture
Possible Causes:
Backend validation failure


Image quality not meeting requirements


Face mismatch / detection inconsistency


Resolution:
Retry with better lighting and steady position


Ensure no obstruction (mask, cap, glasses if needed remove)


If persistent → escalate



⚙️ Standard Checks (Always Perform)
Camera Permission = Enabled


Stable Internet Connection


App is Updated


App stays in Foreground


No interruptions during capture



🚨 Escalation Criteria
Escalate to Dev/DNI Team if:
Issue persists after all troubleshooting steps


Same issue reported by multiple users (pattern)


Failure occurs across multiple devices


Possible backend/API issue (loading, submission errors)



📌 Important Notes
eKYC is non-resumable → any interruption = restart


Requires real-time capture (no pauses allowed)

