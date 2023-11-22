# Risk Assessment & Mitigation Plan

Adapted from RiskAssessment&MitigationPlan.png.

This uses nested lists and not tables because Markdown tables are a hell I
don't want to deal with.

## List of Risks

* Technical Knowledge Gaps
  * **Likelihood:** High
  * **Impact:** High
  * **Description:** Team members may lack the necessary Python skills.
  * **Mitigation:** The team has agreed to watch video tutorials as well as being on call to help each other during code sessions, which will additionally help to mitigate the integration conflict.
* Compatibility Issues
  * **Likelihood:** Medium
  * **Impact:** High
  * **Description:** The game might not run equally across different platforms.
  * **Mitigation:** Regular tests on different platforms will be conducted.
* Unforeseen Bugs and/or Glitches
  * **Likelihood:** High
  * **Impact:** Medium
  * **Description:** Logic errors and bugs can lead to invalid output from the game, or it could lead to a crash.
  * **Mitigation:** Implement an extensive test log and ensure each function is thoroughly tested.
* Library Dependencies
  * **Likelihood:** Medium
  * **Impact:** Medium
  * **Description:** Third-party libraries have the capacity to cause compatibility issues. This may not be a risk if the libraries are not used.
  * **Mitigation:** If any libraries are used, maintain a list of all libraries and what versions are being used in the project.
* User Input Validation
  * **Likelihood:** Medium
  * **Impact:** Medium
  * **Description:** The game may not function properly if user input is invalid. Improper handling of user input may lead to glitches and crashes.
  * **Mitigation:** Implement strong input checks. This should also be performed on the test log.
* Code Integration Conflict
  * **Likelihood:** Medium
  * **Impact:** Low
  * **Description:** As we're all working on the code separately and combining our work later, we may deal with conflicts in our code.
  * **Mitigation:** Regularly review each other's code and agree on the naming conventions. Both of these can be done during the sessions at UH.
* Lack of Documentation
  * **Likelihood:** Medium
  * **Impact:** High
  * **Description:** Poor documentation may lead to the team members not fully understanding code written by the others.
  * **Mitigation:** Agree on how to approach the documentation, and ensure that each team member follows this approach.

## In Table Form (AI-generated)

| Risk Category                | Likelihood | Impact | Description                                                         | Mitigation                                                                                                         |
|------------------------------|------------|--------|---------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------|
| Technical Knowledge Gaps     | High       | High   | Team members may lack the necessary Python skills.                 | Team agrees to watch video tutorials and provide mutual support during code sessions.                               |
| Compatibility Issues         | Medium     | High   | The game might not run equally across different platforms.         | Regular tests on various platforms will be conducted.                                                               |
| Unforeseen Bugs and Glitches | High       | Medium | Logic errors and bugs can lead to invalid output or crashes.        | Implement an extensive test log and ensure each function is thoroughly tested.                                       |
| Library Dependencies         | Medium     | Medium | Third-party libraries may cause compatibility issues.              | Maintain a list of used libraries and their versions in the project.                                               |
| User Input Validation        | Medium     | Medium | The game may not function properly if user input is invalid.       | Implement strong input checks and perform validation as part of the test log.                                       |
| Code Integration Conflict     | Medium     | Low    | Conflicts may arise during code integration.                       | Regularly review each other's code, agree on naming conventions, and conduct these activities during UH sessions.   |
| Lack of Documentation         | Medium     | High   | Poor documentation may lead to a lack of understanding among team members. | Agree on a documentation approach, and ensure each team member follows it.                                       |

You see why I did the list approach now?
