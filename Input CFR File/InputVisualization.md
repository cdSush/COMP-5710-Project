# §117.130 Hazard Analysis – Atomic Rule Tree

```mermaid
graph TD
  %% Section (a)
  A[REQ-117.130-001: Requirement for hazard analysis] 
  A1[A: Conduct hazard analysis]
  A2[F: Hazard analysis must be written]
  A --> A1
  A --> A2
  A1 --> B[B: Identify known hazards]
  A1 --> C[C: Identify reasonably foreseeable hazards]
  A1 --> D[D: Evaluate hazards using data, experience, reports]
  A1 --> E[E: Determine hazards requiring preventive controls]

  %% Section (b)
  BSEC[REQ-117.130-002: Hazard identification]
  BSEC1[A: Known or reasonably foreseeable hazards include]
  BSEC2[B: Consider hazards for origin]
  BSEC --> BSEC1
  BSEC --> BSEC2
  BSEC1 --> BA[Biological hazards]
  BSEC1 --> BB[Chemical hazards]
  BSEC1 --> BC[Physical hazards]
  BSEC2 --> BD[Occur naturally]
  BSEC2 --> BE[Unintentionally introduced]
  BSEC2 --> BF[Intentionally introduced for economic gain]

  %% Section (c)
  CSEC[REQ-117.130-003: Hazard evaluation]
  CSEC1[A: Evaluate identified hazards]
  CSEC2[B: Consider effects on safety of finished food]
  CSEC --> CSEC1
  CSEC --> CSEC2
  CSEC1 --> C1[A1: Assess severity and probability]
  CSEC1 --> C2[A2: Evaluate environmental pathogens for ready-to-eat foods]
  CSEC2 --> D1[B1: Formulation of the food]
  CSEC2 --> D2[B2: Facility and equipment condition, function, design]
  CSEC2 --> D3[B3: Raw materials and other ingredients]
  CSEC2 --> D4[B4: Transportation practices]
  CSEC2 --> D5[B5: Manufacturing/processing procedures]
  CSEC2 --> D6[B6: Packaging and labeling activities]
  CSEC2 --> D7[B7: Storage and distribution]
  CSEC2 --> D8[B8: Intended or reasonably foreseeable use]
  CSEC2 --> D9[B9: Sanitation, including employee hygiene]
  CSEC2 --> D10[B10: Any other relevant factors]