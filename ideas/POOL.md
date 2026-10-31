# Idea pool

All seeds from Phase 3 with their screening status. Seeds cite signal IDs from `research/SIGNALS.md`. Screening applies the red zones and kill criteria in `METHODOLOGY.md`. Competitor names used in kill reasons are known incumbents; where they were not re-searched in this project the reason says so, and every **developed** seed gets a full competition check in Phase 4.

Status legend:
- **developed**: advanced to Phase 4 (concept note below, then a full idea file).
- **merged into X**: folded into a stronger seed as a feature or segment.
- **killed: reason**: fails a red zone or kill criterion (reason given).
- **pending**: waiting for evidence from a running research track (resolved before Phase 4).

## Capability x persona grid
Rows are personas with strong signals; columns are the capability unlocks from `research/LANDSCAPE.md`. Cells name the seed that mines that combination ("." = nothing promising or already a red zone).

| Persona \ capability | Screen overlay | Computer use (no-API portals) | Realtime voice / phone | Long context case file | Cheap batch models | Doc understanding | Video understanding | Deep research / monitoring | MCP / in-assistant |
|---|---|---|---|---|---|---|---|---|---|
| Owner-operator truckers | . | . | S001 broker calls for detention pay | S001 rate con + ELD + emails | . | S001 BOL, rate cons | . | . | . |
| Self-managing landlords | . | . | S003 tenant maintenance line | . | . | . | S033 move-in/out diff | . | . |
| Trades and HVAC techs | . | S010 facility portals | S036 job-walk talk | . | . | . | S036 walkthrough | . | . |
| Remodelers | . | . | S004 client voice notes | S004 contract + texts | . | . | . | . | . |
| Small importers, micro-sellers | . | . | . | S181 entries + invoices | S181 every entry line | S181 duty bills | . | S182 rule changes per product | . |
| Bookkeepers and DIY owners | . | . | . | S131 full ledger review | S106 every transaction | S106 bank statements | . | . | S131 QBO/Xero |
| Benefits navigators, caseworkers | S156 portal guide | S156 assisted fill | . | S156 client file | . | S156 client docs | . | . | . |
| Families of aging parents | . | . | S007 call the company | S006 5-year statements | . | S007 every letter | S034 home contents | . | . |
| Patients | . | . | S009 insurer calls | S009 bills + EOBs | . | S009 EOBs | . | . | . |
| Households after disasters | . | . | . | S032 claim file | . | S032 receipts, orders | S032 room videos | . | . |
| Instructors | . | . | S035 oral defense | S035 submission | . | . | . | . | . |
| Small nonprofits | . | . | . | S005 grant agreements | S005 every expense | S005 invoices | . | . | . |
| SMBs via MSPs | . | . | . | . | S135 every prompt | . | . | . | S135 gateway |
| Legacy-software workers | S157 overlay | S157 record-once | S157 voice queries | . | . | . | . | . | . |
| Reviewers and editors | . | . | . | S132 paper + references | . | S132 PDFs | . | S132 reference lookup | . |
| HSA holders | . | . | . | . | S002 every receipt | S002 receipts, EOBs | . | . | . |
| Public entities (accessibility) | . | . | . | . | S107 every page | S107 PDFs | . | . | . |

## Seeds

Columns: ID / Name / One-liner / Target user / Lens / Signals / Status.

### Lens 1: Pain-first
| ID | Name | One-liner | Target user | Lens | Signals | Status |
|---|---|---|---|---|---|---|
| S001 | Haul Paid | Recovers detention, layover and short-pays owed to small carriers by building evidence packets from rate cons, ELD logs and emails | Owner-operators and 1-10 truck fleets | Pain-first | PRO-029, PRO-030, PRO-026, REV-35 | developed |
| S002 | Shoebox | Captures every medical receipt and EOB for decades and produces audit-ready HSA reimbursement substantiation | HSA holders using the reimburse-later strategy | Pain-first | LIFE-09, LIFE-10, LIFE-11 | developed |
| S003 | Fix Desk | Text-and-voice maintenance line that triages tenant requests, books the landlord's own vendors and logs costs | Self-managing landlords, 2-50 doors | Pain-first | PRO-011, PRO-012, REV-14, REV-15, REV-13 | developed |
| S004 | Scope Guard | Turns client texts and site voice notes into priced change orders signed before the extra work starts | Small remodelers and contractors | Pain-first | PRO-009, PRO-006, RED-39 | developed |
| S005 | Grant Ledger | Tags every expense to the right grant as it happens and drafts funder and board financial reports | Small nonprofits (under $5M budget) | Pain-first | PRO-208, PRO-211, PRO-212, PRO-209 | developed |
| S006 | Medicaid Ready | Builds a long-term-care Medicaid application packet: 5-year statement review, look-back flags, state forms, RFI tracking | Families placing a parent in nursing or memory care | Pain-first | LIFE-17, LIFE-18, LIFE-13, LIFE-16 | developed |
| S007 | Parent Mail Desk | Parent photographs each letter; AI explains it, flags action, and gives the adult child a one-tap way to handle it | Adult children managing aging parents' admin | Pain-first | LIFE-14, LIFE-13, HN-22, HN-28, LIFE-25 | developed |
| S008 | Paper Trail | Decodes IRS, SSA and state notices, drafts and mails responses, tracks deadlines and escalates through the right channel | Individuals and families facing agency notices | Pain-first | LIFE-27, LIFE-29, LIFE-31, LIFE-22, REV-45, REV-47, LIFE-28, LIFE-30 | developed |
| S009 | Bill Detective | Reconciles medical bills against EOBs, finds who really owes what, and runs the calls and letters to fix it | Patients and caregivers with disputed medical bills | Pain-first | LIFE-01, LIFE-02, LIFE-03, LIFE-04, LIFE-05, LIFE-07, HN-18, SVC-47 | developed |
| S010 | Closeout Copilot | Turns a tech's photos and voice note into the exact closeout each facility-management portal demands | Commercial HVAC, plumbing and electrical contractors | Pain-first | PRO-004, REV-11, PRO-014, REV-08 | developed |
| S011 | Gap Filler | Compacts a salon's day by offering clients earlier or later slots and filling cancellations from a waitlist | Salon and spa owners, independent stylists | Pain-first | REV-33, REV-32, REV-34, PRO-229, PRO-226 | developed |
| S012 | Wholesale Desk | Turns wholesale orders arriving by email, PDF or chat into draft orders, invoices and supplier POs | Small Shopify brands selling wholesale on net terms | Pain-first | RED-19, RED-20, RED-06, RED-18 | developed |
| S013 | Receipt Roundup | Chases staff for missing receipts on personal-card spend and posts matched expenses | 5-50 person teams without corporate cards | Pain-first | RED-01, RED-11, RED-12 | killed: crowded (Expensify, Ramp, Brex, Dext, Hubdoc; known incumbents, not re-searched) and corporate cards remove the pain |
| S014 | Nudge Pay | Polite escalating invoice chasing that knows the client relationship | Freelancers and small agencies | Pain-first | HN-08, RED-07, RED-08, PRO-233 | killed: crowded (Chaser, Upflow, Paidnice, built-in QBO/Xero reminders) and native assistant risk (Claude for Small Business thread, HN-02) |
| S015 | Split Run | Automates monthly revenue splits among co-founders, contractors and affiliates | Small online businesses | Pain-first | HN-07 | killed: single signal; payout platforms (Stripe Connect, Tipalti, Trolley) cover most cases |
| S016 | Trust Lite | Produces a credible security packet and questionnaire answers for solo SaaS founders without a $20K audit | Solo B2B SaaS founders | Pain-first | RED-29, RED-30 | killed: crowded (Vanta, Drata, Secureframe, Delve, Comp AI, Oneleet) |
| S017 | Nexus Watch | Tracks state sales-tax nexus for micro SaaS and files registrations | Micro SaaS founders | Pain-first | RED-14 | killed: crowded (Anrok, Numeral, Kintsugi, TaxJar, Avalara) |
| S018 | FBA Clawback | Finds money Amazon owes sellers in returns and reimbursement reports | Amazon FBA sellers | Pain-first | PRO-215, PRO-216, PRO-217 | killed: crowded (GETIDA, Seller Investigators, Carbon6; 25% contingency is the norm per PRO-216) |
| S019 | Delivery Audit | Computes true delivery-platform take rates and disputes wrong charges | Independent restaurants | Pain-first | PRO-222, PRO-224 | killed: crowded (Loop, Voosh; known as of 2025, not re-searched) |
| S020 | Food Cost Buddy | Photographed supplier invoices become line items, recipe costs and price-change alerts | Independent restaurants under $1M revenue | Pain-first | PRO-221, PRO-223, PRO-225, REV-49 | killed: crowded (MarginEdge, xtraCHEF bundled with Toast, Restaurant365, Craftable) |
| S021 | DM Bookings | Reads Instagram, Messenger and WhatsApp bookings into one roster and matches bank transfers | Kids-class and activity businesses | Pain-first | RED-17 | merged into S201 Chat-to-Ledger |
| S022 | IEP Desk | Keeps a special-education caseload compliant: timelines, progress data, accommodation matrices for every teacher and sub | Special-education teachers and case managers | Pain-first | PRO-202, PRO-203, PRO-204, PRO-201 | developed |
| S023 | IEP Ally | Helps parents request evaluations, track legal timelines and prepare for IEP meetings | Parents of children with disabilities | Pain-first | LIFE-51, LIFE-52, REV-38 | developed |
| S024 | Co-Parent Record | Builds neutral timelines and pattern summaries from co-parenting messages for mediators | Separated parents in custody disputes | Pain-first | LIFE-50, LIFE-54, LIFE-53 | killed: court-ordered incumbents (OurFamilyWizard, TalkingParents) and AI entrant BestInterest (known, not re-searched); summary is a feature |
| S025 | Estate Clerk | Drafts county probate forms, inventories and creditor notices and tracks deadlines for small estate practices | Solo and small estate-law firms and their paralegals | Pain-first | PRO-108, LIFE-21, HN-23, LIFE-22 | developed |
| S026 | COI Desk | Answers certificate-of-insurance requests from email and chases submission data for commercial quotes | Independent insurance agencies | Pain-first | PRO-021, PRO-022, PRO-023, PRO-025 | developed |
| S027 | Real Applicant | Screens out AI-mass applications and fake candidates with short role-specific voice prompts and consistency checks | Small employers and staffing agencies | Pain-first | PRO-127, PRO-128, PRO-129, PRO-130, AI2-23, AI2-24, AI2-25 | developed |
| S028 | Bid Builder | Prices commercial cleaning jobs from a walkthrough video and production rates | Commercial cleaning companies | Pain-first | PRO-034, PRO-032 | killed: thin evidence (2 signals) and existing bid calculators |
| S029 | Submission Chaser | Requests loss runs and current policies from clients and prior carriers and fills submission forms | Commercial-lines insurance agents | Pain-first | PRO-023, PRO-024 | merged into S026 COI Desk |
| S030 | Reauth Writer | Drafts insurer reauthorization reports for ABA and therapy practices from session data | ABA and allied-health practices | Pain-first | PRO-126, PRO-124, REV-26 | killed: incumbents (CentralReach, Motivity, Raven Health) ship AI drafting; sits inside the crowded AI-notes space |
| S031 | Data Plate Helper | Voice troubleshooting companion that reads an equipment data plate and pulls the right manual | HVAC and appliance techs | Pain-first | REV-08, PRO-005 | killed: Bluon and XOi already serve techs (known, not re-searched); weak evidence |

### Lens 2: Newly possible
| ID | Name | One-liner | Target user | Lens | Signals | Status |
|---|---|---|---|---|---|---|
| S032 | Contents Claim Builder | Turns old photos, room videos, receipts and order history into an itemized contents claim in the insurer's format | Households after fire, flood or wildfire; public adjusters | Newly possible | LIFE-46, LIFE-47, LIFE-48 | pending (gap-fill topic 1) |
| S033 | Deposit Defense | Move-in and move-out videos become a timestamped condition diff and a state-compliant deduction letter | Tenants and small landlords | Newly possible | PRO-011 | pending (gap-fill topic 2) |
| S034 | Estate Inventory | A walkthrough video of a parent's home becomes an itemized inventory with resale estimates and a disposal plan | Adult children downsizing or settling a parent's home | Newly possible | HN-22 | pending (gap-fill topic 3) |
| S035 | Viva Voce | Realtime voice agent holds a short oral defense with each student about their own submitted work | College instructors and high-school teachers | Newly possible | AI2-52, AI2-47, AI2-50, AI2-54, AI2-48, AI2-49 | developed |
| S036 | Job Walk | Tech talks while walking a job and snaps photos; AI returns good-better-best estimates from the shop's price book plus job notes | Residential HVAC, plumbing and electrical shops | Newly possible | REV-07, REV-08, REV-09, PRO-005, PRO-003 | developed |
| S037 | Hold Line | Waits on insurer and agency hold queues and hands over with the case file when a human answers | Patients and caregivers | Newly possible | LIFE-12, LIFE-03, HN-28, LIFE-48 | merged into S009 Bill Detective (platform risk: Pixel Hold for Me) |
| S038 | Inspector Voice | Home inspector narrates the walkthrough; AI drafts the report with photos placed and defects coded | Home and property inspectors | Newly possible | none yet | pending (gap-fill topic 8) |
| S039 | Spec Answers | Answers subcontractor RFIs from the full spec book and drawings | Small general contractors | Newly possible | PRO-007, REV-37 | killed: Procore AI, Trunk Tools, Document Crunch target this; GC market leans enterprise |
| S040 | Immigration Binder | Long-context case binder for family petitions: every document, version, deadline and RFE response | Families filing family-based immigration petitions | Newly possible | LIFE-36, LIFE-37, LIFE-38, LIFE-39, LIFE-42 | killed: DIY immigration services (Boundless, CitizenPath, SimpleCitizen) plus unauthorized-practice limits |
| S041 | Local Transcribe IRB | On-device interview transcription that satisfies IRB privacy rules | PhD students and qualitative researchers | Newly possible | PRO-239 | killed: crowded local transcription (MacWhisper, OS features); tiny market |
| S042 | Rule Radar | Deep-research agent that watches the rules for your exact products, states and countries and tells you what changed | Micro-businesses selling physical products | Newly possible | HN-13, HN-14, RED-31, RED-32, RED-33 | merged into S182 Product Compliance Desk |
| S043 | Broker Caller | Voice agent phones brokers about unpaid detention and short-pays | Owner-operators | Newly possible | PRO-029, PRO-030 | merged into S001 Haul Paid |
| S044 | QBO Coach | Screen-aware voice coach for QuickBooks beginners | Small-business owners new to QuickBooks | Newly possible | REV-18, REV-21, RED-03 | killed: red zone generic screen overlay; Intuit Assist and OS assistants cover it |
| S045 | Clio MCP | MCP connector exposing Clio practice data to outside assistants | Small law firms | Newly possible | PRO-109 | killed: feature-sized, Clio can ship it, platform dependency |
| S046 | Voice Audition | Candidates answer three short voice prompts about real experience before any human time is spent | Employers hiring hourly roles | Newly possible | PRO-127, PRO-131, AI2-25 | merged into S027 Real Applicant |
| S047 | Trade SOP Video | Turns a phone video of a job into a written SOP | Trades businesses | Newly possible | RED-23 | killed: crowded (Scribe, Tango, Guidde, Trainual AI) |
| S048 | Photo Fraud Check | Flags AI-edited damage photos for small insurers and adjusters | Small carriers and independent adjusters | Newly possible | AI2-22 | killed: carriers buy enterprise fraud tools (enterprise procurement) |
| S049 | Tenant Triage WhatsApp | Multilingual triage of tenant messages across channels for 40-unit managers | Small property-management teams | Newly possible | PRO-012 | merged into S003 Fix Desk |
| S050 | Statement Ledger | Cheap batch model turns years of bank-statement PDFs into a categorized ledger | Owners with bookkeeping backlogs | Newly possible | SVC-09, SVC-12 | merged into S106 Backlog Books |
| S051 | Board Pack | Builds monthly board and funder packs from the general ledger | Small nonprofits | Newly possible | PRO-211 | merged into S005 Grant Ledger |
| S052 | Batch Remediation | Batch-remediates whole PDF libraries for accessibility at cents per page | Public entities and universities | Newly possible | SVC-29, SVC-31 | merged into S107 Remediate |
| S053 | Grant Prospector | Researches funders and deadlines for small nonprofits | Small nonprofits | Newly possible | SVC-48, SVC-49, SVC-52 | killed: crowded (Instrumentl, Candid, Grantable, GrantStation) |
| S054 | Agent Price List | Publishes a trades business's prices in agent-readable form | Trades businesses | Newly possible | none | killed: red zone (GEO / AI visibility) |
| S055 | Policy Decoder | Explains a consumer's insurance policy and coverage for a specific treatment | Patients | Newly possible | LIFE-05, REV-43 | killed: general assistants read a policy PDF well; folded into S009 where case context matters |

### Lens 3: Remix
| ID | Name | One-liner | Target user | Lens | Signals | Status |
|---|---|---|---|---|---|---|
| S061 | Sibling Ledger | Splitwise for caregiving: siblings log care costs with receipts and settle fairly, reimbursed from the estate later (parents: Splitwise, Expensify) | Siblings sharing a parent's care | Remix | LIFE-15, LIFE-16, LIFE-13, HN-22 | merged into S007 Parent Mail Desk (family case log module) |
| S062 | Smart Waitlist | Calendly-style self-rescheduling plus a waitlist for salons (parents: Calendly, OpenTable waitlist) | Salons | Remix | REV-33, PRO-229 | merged into S011 Gap Filler |
| S063 | Literacy Streaks | Duolingo-style AI-literacy micro-lessons with completion records for EU AI Act Article 4 (parents: Duolingo, KnowBe4) | SMB staff | Remix | AI2-56, AI2-59, AI2-58 | merged into S135 AI Governance Kit |
| S064 | Rental Scam Check | Pay-per-check verification that a rental listing and landlord are real (parents: Snappt, Truecaller) | Renters | Remix | none yet | pending (gap-fill topic 5) |
| S065 | Vendor Cancel Desk | Rocket Money plus Resolver for small businesses: cancels and disputes vendor charges (parents: Rocket Money, Resolver) | Small businesses | Remix | LIFE-44, LIFE-45, LIFE-43 | killed: SMB SaaS-management crowded (Cledara, Vendr, Zylo, Spendflo) |
| S066 | Call Coach Trades | Gong for HVAC call centers: call recording and missed-upsell coaching (parents: Gong, CallRail) | HVAC CSRs | Remix | PRO-003 | killed: ServiceTitan, Housecall Pro, Jobber and CallRail ship call AI; sales-call copilot red zone |
| S067 | Freight Snap | Expensify SmartScan for BOLs and lumper receipts feeding invoices and factoring (parents: Expensify, factoring portals) | Owner-operators | Remix | PRO-030, PRO-029, REV-35 | merged into S001 Haul Paid |
| S068 | Sheet Review | GitHub pull-request review for spreadsheet models (parents: GitHub, Excel) | Analysts inheriting models | Remix | HN-31, HN-30, HN-32 | killed: platform risk (Copilot in Excel, Gemini in Sheets); niche |
| S069 | Adjuster Packets | EvenUp-style claim packages for public adjusters (parents: EvenUp, Xactimate) | Public adjusters | Remix | LIFE-47, LIFE-48 | merged into S032 Contents Claim Builder (B2B tier) |
| S070 | Cargo Claims | EvenUp for freight: carrier-liability claim packets with evidence and follow-up (parents: EvenUp, Chargeflow) | Shippers and small freight brokers | Remix | none yet | pending (gap-fill topic 4) |
| S071 | Wedding Multi-Event | One contract and invoice across several wedding events and locations (parents: HoneyBook, Dubsado) | Wedding vendors | Remix | PRO-242, PRO-243 | killed: feature request for HoneyBook and Dubsado; small |
| S072 | Voice Zap | "Tell it once" phone-to-workflow automation for trades (parents: Zapier, voice assistants) | Trades owners | Remix | PRO-006 | killed: red zone generic agents |
| S073 | Host Copilot | Guest messaging plus cleaner coordination for short-term rentals (parents: Hospitable, Slack) | Short-term-rental operators | Remix | SVC-61 | killed: crowded (Hospitable, Hostaway, HostBuddy AI, Jurny) |
| S074 | Quote Second Opinion | Upload 2-3 contractor quotes; get an apples-to-apples comparison, red flags and a fair range (parents: Carfax, Kayak) | Homeowners buying HVAC, roofing, solar | Remix | none yet | pending (gap-fill topic 7) |
| S075 | Transcript Watch | Credit Karma for the IRS: watches account transcripts to predict notices and refund problems (parents: Credit Karma, IRS online account) | Taxpayers | Remix | REV-47, LIFE-28, LIFE-30 | merged into S008 Paper Trail |
| S076 | Vendor Taskers | TaskRabbit-style dispatch of the landlord's vendors (parents: TaskRabbit, Latchel) | Landlords | Remix | PRO-011 | merged into S003 Fix Desk |
| S077 | Admin Calendar | Linear for a micro company's compliance obligations (parents: Linear, Stripe Atlas) | Micro companies | Remix | HN-11, RED-32, RED-33 | killed: crowded (doola, Firstbase, Stripe Atlas plus accountants); mixed willingness to pay |
| S078 | Record Once | Loom-style "show it once" automation for legacy desktop apps (parents: Loom, RPA) | Legacy software users | Remix | HN-33, HN-34 | merged into S157 Legacy App Buddy |
| S079 | Appeal Contingency | AirHelp-style contingency appeals for denied health claims (parents: AirHelp, Claimable) | Patients | Remix | LIFE-08, LIFE-06, HN-19 | merged into S009 Bill Detective |
| S080 | Parts Lens | Shazam for appliance parts: photo to part number and compatible replacements (parents: Shazam, PartSelect) | Homeowners and handymen | Remix | none | killed: Google Lens and parts retailers cover it; no signals |
| S081 | Tax Appeal Bot | TurboTax-style property-tax appeal with comps (parents: TurboTax, Ownwell) | Homeowners | Remix | LIFE-35 | killed: Ownwell and similar contingency services (known, not re-searched); general LLMs draft appeals (LIFE-35) |
| S082 | Certified Mail Case | Lob-style certified mail plus a case file for disputes with institutions (parents: Lob, Resolver) | Consumers in disputes | Remix | LIFE-43, LIFE-27 | merged into S008 Paper Trail |

### Lens 4: Transplant
| ID | Name | One-liner | Target user | Lens | Signals | Status |
|---|---|---|---|---|---|---|
| S086 | Inspector Scribe | Ambient-scribe pattern (medicine) moved to home inspectors | Home inspectors | Transplant | none yet | merged into S038 Inspector Voice |
| S087 | Adjuster Scribe | Ambient-scribe pattern moved to independent insurance adjusters | Independent adjusters | Transplant | none | killed: no signals; carriers buy enterprise tools |
| S088 | Freight EvenUp | EvenUp's demand-package pattern moved to freight claims | Shippers, brokers | Transplant | none yet | merged into S070 Cargo Claims |
| S089 | Service Chargebacks | Chargeflow's evidence-packet pattern (e-commerce) moved to service businesses: signed estimates, job photos, GPS, texts | Salons, trades and studios taking card payments | Transplant | REV-03, REV-31, PRO-218, PRO-219, REV-24 | developed |
| S090 | Benefits Plaid | YC's "Plaid for government benefits" moved to the caseworker's desk | Benefits navigators | Transplant | LIFE-32, LIFE-33, REV-48 | merged into S156 Benefits Portal Pilot |
| S091 | Duty Contingency | Ownwell's contingency model moved to duty and tariff refunds | Small importers | Transplant | HN-15, PRO-213 | merged into S181 Tariff Refund Finder |
| S092 | Landlord Notices | Rocket Lawyer-style document subscription moved to local landlord compliance notices (rent caps, just-cause) | Self-managing landlords | Transplant | PRO-013 | merged into S003 Fix Desk (compliance module) |
| S093 | Shopify A11y Fixes | App-store distribution of real accessibility code fixes (not overlays) for stores selling into the EU | Shopify merchants selling to the EU | Transplant | FORCE-20, FORCE-22, FORCE-23, FORCE-24, SVC-32 | developed |
| S094 | Household Payroll | Gusto pattern moved to families employing nannies and caregivers | Household employers | Transplant | none | killed: crowded (HomePay, GTM Payroll) |
| S095 | City Hall Desk | YC "AI for City Hall": permit intake and 311 triage for small towns | Small municipalities | Transplant | SVC-46 | killed: public-sector procurement is slow (enterprise-procurement kill criterion) |
| S096 | Rate Terminal | Bloomberg-style freight-rate intelligence for owner-operators | Owner-operators | Transplant | PRO-028 | killed: DAT and Truckstop rate tools |
| S097 | Contractor Carfax | Carfax-style history report on a contractor (permits, licenses, reviews) | Homeowners | Transplant | none | killed: BuildZoom exists; data access limits |
| S098 | Vet Scribe | Ambient scribe moved to veterinary clinics | Vets | Transplant | PRO-122 | killed: crowded (ScribbleVet, VetRec, Talkatoo, Scribenote) |
| S099 | Church Reimburse | Ramp-style receipt matching moved to church and nonprofit treasurers | Volunteer treasurers | Transplant | PRO-208 | merged into S005 Grant Ledger |
| S100 | Triage for Support | HackerOne-style triage moved to small SaaS support queues | Small SaaS vendors | Transplant | AI2-02 | merged into S139 Slop Triage |
| S101 | Auto Substantiate | Robo-advisor automation moved to HSA receipt substantiation | HSA holders | Transplant | LIFE-10 | merged into S002 Shoebox |

### Lens 5: Service-to-software
| ID | Name | One-liner | Target user | Lens | Signals | Status |
|---|---|---|---|---|---|---|
| S106 | Backlog Books | Catch-up bookkeeping as a fixed price per month of backlog: bank statements in, accountant-ready ledger and question list out | Owners and bookkeepers facing months or years of backlog | Service-to-software | SVC-07, SVC-08, SVC-09, SVC-11, SVC-12, SVC-15, SVC-19, RED-37, PRO-104 | developed |
| S107 | Remediate | PDF and document accessibility remediation priced per page, AI first with human QA | State and local agencies, universities, EU-facing businesses | Service-to-software | SVC-29, SVC-30, SVC-31, SVC-32, SVC-33 | developed |
| S108 | Medicaid Packet Service | Done-for-you Medicaid LTC packet | Families | Service-to-software | LIFE-18 | merged into S006 Medicaid Ready |
| S109 | Probate Packet | Done-for-you probate filing packet | Executors | Service-to-software | LIFE-21 | merged into S025 Estate Clerk |
| S110 | Permit Packet | Assembles residential permit applications per jurisdiction | Homeowners and remodelers | Service-to-software | SVC-46 | killed: PermitFlow (YC, funded) and human expediters; single signal |
| S111 | Certified Translate | USCIS-ready certified translations with layout preserved and a human signer | Immigration applicants | Service-to-software | SVC-56, SVC-57, SVC-58, LIFE-38, LIFE-41 | killed: cheap human services (RushTranslate, Rev, Translayte) and a human certifier per language keep margins thin |
| S112 | Grant Reports Service | Done-for-you funder financial reports | Nonprofits | Service-to-software | PRO-212 | merged into S005 Grant Ledger |
| S113 | Catalog Upload | Spreadsheet to finished store catalog with specs and tags | Shopify and Amazon sellers | Service-to-software | SVC-39, SVC-40, SVC-41, SVC-42 | killed: bulk-import apps (Matrixify) plus red-zone AI copy generators |
| S114 | Appeal Packets | Amazon account reinstatement and brand-approval packets | Amazon sellers | Service-to-software | SVC-43, SVC-44 | killed: depends on Amazon's opaque, revocable policies; crowded consultants |
| S115 | Chargeback Service | Done-for-you chargeback responses | Merchants | Service-to-software | SVC-45 | merged into S089 Service Chargebacks |
| S116 | PDF to Sheet | Batches of PDFs and scans into standard spreadsheets | Small businesses | Service-to-software | SVC-21, SVC-22, SVC-23, SVC-24, SVC-28 | killed: red zone (OCR/extraction wrappers; Nanonets, Docparser, Reducto, general assistants) |
| S117 | Captions Done | Transcripts and subtitles delivered | Creators, legal | Service-to-software | SVC-34, SVC-35, SVC-36, SVC-37, SVC-38 | killed: red zone (transcription at $0.003/min) |
| S118 | Test Crowd | Pre-launch QA testers as a service | App developers | Service-to-software | SVC-53, SVC-54, SVC-55 | killed: needs real humans and devices; not AI-deliverable |
| S119 | Lead Errands | Verified lead lists per entity | Small businesses | Service-to-software | SVC-50, SVC-51 | killed: red zone (lead gen / AI SDR) |
| S120 | Duty Refund Packets | Done-for-you protest and refund packets | Small importers | Service-to-software | HN-15 | merged into S181 Tariff Refund Finder |
| S121 | Notice Response Service | Done-for-you agency notice responses | Individuals | Service-to-software | LIFE-27 | merged into S008 Paper Trail |
| S122 | Freight Claim Service | Done-for-you cargo claims | Shippers | Service-to-software | none yet | merged into S070 Cargo Claims |
| S123 | Inventory Service | Done-for-you contents inventories | Disaster-affected households | Service-to-software | none yet | merged into S032 Contents Claim Builder |
| S124 | Nonprofit Books | Fund-accounting cleanup for small nonprofits | Nonprofits | Service-to-software | PRO-208, PRO-211 | merged into S005 Grant Ledger |
| S125 | Renewal Remarket | Remarkets small-business insurance renewals | Small businesses | Service-to-software | PRO-023 | killed: requires an insurance producer license |
| S126 | Grant Writing | Done-for-you grant applications | Nonprofits | Service-to-software | SVC-52 | killed: crowded (Grantable, GrantboostAI, Instrumentl) and red zone (AI writing) |
| S127 | SOP Manuals | Done-for-you operations manuals | Small businesses | Service-to-software | RED-23 | killed: red zone (document generators) |
| S128 | Vendor Packets | Collects W-9s and COIs from vendors | GCs and property managers | Service-to-software | PRO-021 | killed: crowded COI tracking (myCOI, TrustLayer, Jones) |
| S129 | Quote Review Service | Expert-reviewed contractor quote comparison | Homeowners | Service-to-software | none yet | merged into S074 Quote Second Opinion |

### Lens 6: Second-order AI
| ID | Name | One-liner | Target user | Lens | Signals | Status |
|---|---|---|---|---|---|---|
| S131 | Books Second Opinion | Audits AI- or human-kept books for misclassifications, missing items and tax flags and writes a CPA-ready memo | Owners doing books with AI; bookkeepers reviewing juniors | Second-order AI | HN-02, PRO-103, REV-18, REV-19, REV-21, SVC-05, SVC-20, PRO-104 | developed |
| S132 | Cite Check | Verifies that every reference in a manuscript exists and actually supports the claim attached to it | Peer reviewers, journal editors, grant reviewers | Second-order AI | PRO-238, AI2-07, AI2-12, AI2-13, AI2-17 | developed |
| S133 | Integrity Case File | Compiles evidence and drafts the integrity report in the institution's format | Instructors | Second-order AI | AI2-47, AI2-50, AI2-54 | merged into S035 Viva Voce (evidence summary module, no detector-only accusations) |
| S135 | AI Governance Kit | MSP-deployed AI gateway with redaction, logging, policy and AI-literacy records for small companies | MSPs serving 10-200 person companies | Second-order AI | AI2-27, AI2-55, AI2-56, AI2-57, AI2-58, AI2-59, RED-36 | developed |
| S136 | Receipt Forensics | Flags AI-generated receipts in small-company expense claims | SMB finance teams | Second-order AI | AI2-20 | killed: Ramp, Expensify and AppZen ship AI-receipt detection |
| S137 | Applicant Doc Check | Detects doctored pay stubs and bank statements for small landlords | Small landlords | Second-order AI | PRO-015, AI2-21 | killed: Snappt (funded) and screening platforms |
| S138 | Human Proof | Certifies human authorship from writing-process records | Writers, students | Second-order AI | AI2-26, AI2-07 | killed: Grammarly Authorship, GPTZero replay, Docs history tools |
| S139 | Slop Triage | Dedupes and verifies AI-generated inbound before a human reads it | Small SaaS support teams, regulators | Second-order AI | AI2-02, AI2-10, AI2-11 | killed: red zone (support bots); helpdesk incumbents add AI triage |
| S140 | Repro Bot | Reproduces incoming security reports in a sandbox before triage | Bug-bounty programs, maintainers | Second-order AI | AI2-01, AI2-04 | killed: HackerOne and Bugcrowd own the channel; maintainers lack budget |
| S141 | Pro Se Triage | Extracts real arguments and checks citations in AI-drafted pro se filings | Small litigation firms | Second-order AI | AI2-05, AI2-06 | killed: crowded legal AI (CoCounsel, Lexis+ AI, Harvey) |
| S142 | Token Meter | Per-customer AI cost metering and caps for micro-SaaS | Micro-SaaS founders | Second-order AI | RED-35, AI2-35, AI2-36, AI2-38 | killed: crowded (Helicone, Langfuse, OpenMeter, Stripe usage billing, Paid) |
| S143 | AI Spend Audit | Finds overspend across AI subscriptions and APIs | Companies | Second-order AI | AI2-33, AI2-34, AI2-37, AI2-40 | killed: crowded (Vantage, CloudZero) and provider dashboards |
| S144 | Agent Sandbox | Permission sandbox for agents run by non-developers | Non-technical teams | Second-order AI | AI2-29, AI2-31, AI2-32 | killed: red zone (developer agent infrastructure) |
| S145 | Payee Shield | Verifies vendor bank-detail changes and urgent payment requests through independent channels | SMB finance and bookkeepers | Second-order AI | AI2-46, AI2-45 | pending (gap-fill topic 9) |
| S146 | Workslop Squeeze | Compresses AI-padded documents to their real content | Knowledge workers | Second-order AI | AI2-14, AI2-15 | killed: summarization is native in every assistant |
| S147 | Report Fact Check | Checks numbers and claims in AI-written client reports | Agencies, consultants | Second-order AI | AI2-14, AI2-19 | killed: weak willingness-to-pay evidence |
| S148 | AI Label Desk | Tracks AI-generated assets and applies EU AI Act Article 50 labels | Small publishers and marketers | Second-order AI | AI2-59, FORCE-53 | killed: thin evidence, AI Act dates moving (FORCE-53), and creation tools embed provenance labels themselves |
| S150 | Scam Call Screen | Screens calls to elderly parents for voice-clone scams | Families of older adults | Second-order AI | AI2-41, AI2-42, AI2-43, AI2-44, HN-29 | killed: platform features (Pixel scam detection, iOS call screening, carrier scam shields) plus Truecaller and Aura |
| S151 | Family Code Word | Family verification phrases and drills | Families | Second-order AI | AI2-43, AI2-44 | killed: feature-sized, low willingness to pay |
| S152 | RFI Deduper | Dedupes AI-generated RFIs and prospect questions | GCs, insurance agents | Second-order AI | PRO-007, PRO-024 | killed: thin; Procore adds AI RFI tools; agency side folded into S026 |
| S153 | Repro Check | Checks reproducibility of AI-written research scripts | Labs | Second-order AI | AI2-16 | killed: niche, low willingness to pay |
| S154 | Voice Feedback Grader | Grading feedback in the teacher's own voice | Teachers | Second-order AI | PRO-206, REV-39 | killed: crowded (MagicSchool, Brisk, CoGrader, EssayGrader) |
| S155 | Homework Origin | Detects AI-made homework for parents and teachers | Parents, teachers | Second-order AI | AI2-51 | killed: low willingness to pay; false-positive harm |

### Lens 7: Interaction shift
| ID | Name | One-liner | Target user | Lens | Signals | Status |
|---|---|---|---|---|---|---|
| S156 | Benefits Portal Pilot | Browser side panel that walks navigators and applicants through state benefits portals page by page, pre-filling from client documents with approval | Benefits navigators at nonprofits, legal aid, hospitals; applicants | Interaction shift | LIFE-32, LIFE-33, REV-48, LIFE-29 | developed |
| S157 | Legacy App Buddy | Overlay for legacy desktop business software: ask in plain language, get guided entry and record-once macros | Staff at small firms on old ERPs, AS/400 and FoxPro apps | Interaction shift | HN-33, HN-34, LAND-04, RED-23 | developed |
| S158 | Hallway Logger | Teacher speaks; behavior logs, parent-contact logs and IEP progress points are filed | Teachers | Interaction shift | PRO-201, PRO-204, PRO-202 | merged into S022 IEP Desk |
| S159 | Cab Voice | Hands-free logging of detention start and stop and rate-con lookups from the cab | Owner-operators | Interaction shift | PRO-029 | merged into S001 Haul Paid |
| S161 | Sheet Sidekick | Screen-aware spreadsheet helper | Analysts | Interaction shift | HN-30 | killed: platform (Copilot in Excel, Gemini in Sheets) |
| S163 | Tenant Text Line | Tenants text one number; maintenance is handled | Tenants and landlords | Interaction shift | PRO-012 | merged into S003 Fix Desk |
| S164 | Letter Camera | Older adult points the phone at a letter and hears what it means | Older adults | Interaction shift | LIFE-14 | merged into S007 Parent Mail Desk |
| S166 | Phone Tree Navigator | Navigates insurer IVRs for caregivers | Caregivers | Interaction shift | LIFE-12 | merged into S009 Bill Detective |
| S169 | Forward-to-Post | Forward a receipt, work order or intake form to an address; it lands correctly in your vertical software and learns your corrections | Owners using Jobber, Buildium, QBO, Vagaro | Interaction shift | REV-17, REV-01, REV-18, REV-30, REV-23 | developed |
| S170 | Chair-side Rescheduler | Stylist speaks mid-service to move appointments and text the client | Stylists | Interaction shift | REV-33 | merged into S011 Gap Filler |
| S173 | Clio Sidebar | Assistant overlay inside practice-management software | Small law firms | Interaction shift | PRO-109 | killed: platform (Clio's own AI) |
| S174 | Deadline Radar | Proactive deadline alerts from scanned mail | Households | Interaction shift | LIFE-27 | merged into S008 Paper Trail |
| S177 | Dispatcher Whisper | Automates check calls for small freight brokers | Small freight brokers | Interaction shift | PRO-026 | killed: crowded with funded players (HappyRobot, Vooma, Parade; known, not re-searched) |
| S178 | Lobby Intake | Waiting-room tablet intake in the patient's language | Clinics | Interaction shift | PRO-115 | killed: crowded (Phreesia, Klara) |
| S179 | Bookkeeper Side-by-Side | Desktop helper that sees QBO and source documents together | Bookkeepers | Interaction shift | RED-15 | merged into S131 Books Second Opinion |
| S180 | Walk-in Count | Voice inventory counts in the kitchen | Restaurants | Interaction shift | PRO-221 | killed: restaurant back office crowded |

### Lens 8: Forcing function
Based on track T8 (14 live forcing functions; 6 dropped or delayed rules are in `research/SIGNALS.md` under "Forcing functions that were dropped or delayed").

| ID | Name | One-liner | Target user | Lens | Signals | Status |
|---|---|---|---|---|---|---|
| S181 | Tariff Refund Finder | Finds IEEPA tariff refunds and overpaid duties a small importer is owed and builds the CAPE refund files and correction packets | Small importers and cross-border e-commerce sellers | Forcing function | FORCE-04, FORCE-05, FORCE-06, HN-15, PRO-213, FORCE-01 | developed |
| S182 | Product Compliance Desk | One product record becomes per-country obligations (EU packaging, WEEE, GPSR, EUR 3 duty; US CPSC eFiling), registrations, labels and report reminders | Micro-makers and small brands selling physical goods cross-border | Forcing function | HN-13, HN-14, FORCE-07, FORCE-08, FORCE-30, FORCE-33, FORCE-35, RED-31, PRO-220 | developed |
| S183 | Micro Customs Desk | Ongoing HTS classification, entry prep and landed-cost checks now that de minimis is gone | Micro-importers | Forcing function | FORCE-01, FORCE-02, FORCE-03, PRO-214 | merged into S181 Tariff Refund Finder (ongoing duty-accuracy module) |
| S184 | Proof of Hours | Collects and submits Medicaid and SNAP work-requirement proofs (pay stubs, gig earnings, exemptions) before each deadline | Medicaid expansion and SNAP enrollees; navigators | Forcing function | FORCE-11, FORCE-12, FORCE-13, FORCE-14, FORCE-15, FORCE-16 | merged into S156 Benefits Portal Pilot (same buyers: navigators and plans) |
| S185 | Pay Range Desk | Checks job postings and pay ranges against EU and US state pay-transparency rules | SMB employers hiring across jurisdictions | Forcing function | FORCE-38, FORCE-39, FORCE-40 | killed: crowded (Syndio, Trusaic, Figures, Ravio, Payscale; known, not re-searched) and enterprise-leaning |
| S186 | E-Invoice Fixer | Validates and repairs KSeF, Factur-X and XRechnung invoices for micro-businesses | EU micro-businesses | Forcing function | FORCE-25, FORCE-26, FORCE-27, FORCE-28, FORCE-29 | killed: accounting and e-invoicing vendors bundle it (FORCE-29 notes vendor panic-selling); crowded |
| S187 | Authority Guard | Keeps a micro-carrier's FMCSA authority alive: Motus migration, insurance-filing mismatches, MCS-150, hijack alerts | Owner-operators and 1-10 truck carriers | Forcing function | FORCE-44, FORCE-42, FORCE-41, PRO-027, FORCE-45 | developed |
| S188 | Roadside English | Voice practice for the roadside English-proficiency check and English-only CDL tests, taught from the driver's native language | Immigrant truck drivers | Forcing function | FORCE-43, FORCE-45 | pending (underserved track T9) |
| S189 | EAD Gap Watch | Plans EAD renewals now that automatic extensions ended and tracks I-9 reverification | EAD holders and their employers | Forcing function | FORCE-46, FORCE-47 | killed: employer I-9 tools (Tracker, Equifax I-9) and immigration case software; consumer side is a reminder feature |
| S190 | Traffic Rescue | Recovers small-site traffic lost to AI Overviews | Independent publishers | Forcing function | FORCE-48, FORCE-49, FORCE-50 | killed: red zone (GEO / AI visibility) |
| S191 | Tips W-2 Fixer | New W-2 tip and overtime codes for small employers | Restaurants and salons | Forcing function | FORCE-09, FORCE-10, PRO-230 | killed: payroll providers (Gusto, ADP, Square, Toast) ship the codes |
| S192 | EU Duty Calculator | Prices the EUR 3 per-item duty and handling fees into landed cost for non-EU sellers | Non-EU micro-sellers | Forcing function | FORCE-36, FORCE-37 | merged into S182 Product Compliance Desk |
| S193 | Prior Auth API | Helps small practices use payers' new prior-authorization APIs | Small practices | Forcing function | FORCE-17, HN-16, PRO-112 | killed: crowded prior-auth automation (Infinitus, Tennr, Silna, Myndshft, Availity) |
| S194 | WISeR Desk | Prior authorization for traditional-Medicare providers in the six WISeR states | Providers in NJ, OH, OK, TX, AZ, WA | Forcing function | FORCE-18 | killed: same crowding as S193; narrow geography |
| S195 | CAPE Files for Brokers | Builds CAPE refund CSVs for small customs brokers | Customs brokers | Forcing function | FORCE-05 | merged into S181 Tariff Refund Finder (broker tier) |
| S196 | Exemption Navigator | Tells chronically ill and disabled enrollees whether and how they are exempt | Medicaid and SNAP enrollees | Forcing function | FORCE-12, FORCE-13, FORCE-16 | merged into S156 Benefits Portal Pilot |
| S197 | Gig Hours Proof | Converts gig-platform earnings into proof of hours | Gig workers on Medicaid | Forcing function | FORCE-15 | merged into S156 Benefits Portal Pilot |
| S198 | EU Rep Finder | Matches micro-sellers with EU authorised representatives | Non-EU micro-sellers | Forcing function | FORCE-31, FORCE-35 | killed: the representative role needs an EU legal entity (license/partnership); matching is a marketplace |
| S199 | GPSR Listing Fixer | Answers Amazon EU GPSR document requests | Amazon sellers expanding to the EU | Forcing function | FORCE-33, FORCE-34, FORCE-35 | merged into S182 Product Compliance Desk |
| S200 | ADA Title II Desk | Remediates state and local government sites and documents before the (delayed) WCAG deadlines | Small public entities | Forcing function | FORCE-21, SVC-32 | merged into S107 Remediate |

### Lens 9: Underserved users
Pending track T9 (underserved users). Seed already identified:

| ID | Name | One-liner | Target user | Lens | Signals | Status |
|---|---|---|---|---|---|---|
| S201 | Chat-to-Ledger | Orders, bookings and payments that arrive in WhatsApp and Instagram chats become a ledger, invoices and matched payments | Chat-first micro-businesses (LatAm, India, activity businesses) | Underserved users | RED-17 | developed |

### Wild ideas
Pending.
