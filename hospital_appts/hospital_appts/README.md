# Hospital Outpatient Appointment System — Code Implementation

Implements the **Revised Final Class Model** and **Revised Final State Model** from the 10/29 activity.
Every file is a stub: the class and method names come from the UML, and each body says `TODO` / `NotImplementedError`. **The team writes all the logic.** Use AI only to explain concepts, review code you wrote, or explain error messages. Don't paste in AI-generated code.

## Who owns what (one person per file = no merge conflicts)

| Person | Files | Classes / responsibility |
|---|---|---|
| **Aiden** | `users.py`, `session.py`, `main.py` | User, Patient, Administrator; navigation states (Signed In → Appt Manager → Viewer); integration + demo |
| **Anika** | `appointment.py` | Appointment and its full lifecycle (Scheduled / Cancelled / No Show / Checked In / Services Provided / Checked Out) |
| **Jacob** | `staff.py` | Staff, Doctor, Nurse, DeskAssistant (they call Appointment methods) |
| **Yutaro** | `notifications.py`, `billing.py`, `department.py` | Notifications, Bill branch (Issued / Declined loop / Received / Reviewed), Department |
| **Everyone** | `states.py` | Shared enums + `InvalidTransition`. Change only after telling the group |

## Rules for working in parallel
1. **Edit only your own files.** If you need something from someone else's file, ask them. Don't edit it yourself.
2. **Method signatures are the contract.** Call other people's methods by their stub names even before they're written. Don't rename a method without telling the group.
3. Every illegal state change → `raise InvalidTransition("...")`. Every guard in the diagram (`[DayIsFree]`, `[ApptScheduled]`, `[NotCheckedIn]`, `[UserIsStaff]`, `[PaymentApproved/Declined]`) becomes an `if` check.
4. Test your own file with its `if __name__ == "__main__":` block before you push.
5. Commit/push small and often (see below).

## Setup (first 5 min)
**Option A — GitHub (recommended):**
- Aiden creates the repo, pushes this template, and adds the others as collaborators.
- Everyone: `git clone <url>` → work on `main`. Because nobody shares files, `git pull --rebase` then `git push` works without conflicts.

**Option B — fastest, no git:** VS Code **Live Share** (Aiden hosts) or a shared **Replit**. Everyone edits live in their own file.

Run from the project root: `python main.py` (or `python -m hospital.appointment` to test one module).

## Hour plan
| Time | What |
|---|---|
| 0–5 | Set up the repo/Live Share. Read `states.py` together and agree on the names |
| 5–15 | Constructors + attributes in every file (unblocks everyone else) |
| 15–40 | Methods + guards + `InvalidTransition`; self-test your file |
| 40–50 | Aiden fills in `main.py` scenarios; others fix what breaks |
| 50–60 | Run all scenarios; write down the model gaps found (below) |

## Model gaps to discuss (the code exposes these; they're good material for the write-up)
- **No Bill class** in the class model, but the state model has 3 billing states.
- State model needs `markNoShow`, `completeVisit`, `checkOut`, and an `isStaff` guard, but none of them are in the class model.
- `Appointment.Date: int`: a `datetime` is more realistic.
- `Doctor` and `Nurse` both have `enterPatientVitals`. Should it move up to `Staff`?
- `Staff.updatePatientHistory` / `updatePatientHealth` have no patient parameter.
- `createAppt(int ApptID)` appears on Patient, Staff, *and* DeskAssistant. Who should really create appointments?
- Is "User Notified" a real state, or just the effect of sending a notification?
- Typos in the UML: `mamangeApptTypes`, `DatTime`.
