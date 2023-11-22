# Assignment 2 Planning

## General overview

Our assignment is to use **Python** to make one of three projects.

We chose **Connect 4,** using a TUI interface rather than GUI for simplicity's sake.

## UI Mockup

### Game Start

```plaintext
How many rows? (minimum 8, maximum 18)
> 8
How many columns? (minimum 6, maximum 14)
> 6
Selected grid size: (8, 6)
[ ] [ ] [ ] [ ] [ ] [ ]
[ ] [ ] [ ] [ ] [ ] [ ]
[ ] [ ] [ ] [ ] [ ] [ ]
[ ] [ ] [ ] [ ] [ ] [ ]
[ ] [ ] [ ] [ ] [ ] [ ]
[ ] [ ] [ ] [ ] [ ] [ ]
[ ] [ ] [ ] [ ] [ ] [ ]
[ ] [ ] [ ] [ ] [ ] [ ]
```

### Player 1 Turn State

```plaintext
Selected grid size: (8, 6)
Player 1 Turn
[ ] [ ] [ ] [ ] [ ] [ ]
[ ] [ ] [ ] [ ] [ ] [ ]
[ ] [ ] [ ] [ ] [ ] [ ]
[ ] [ ] [ ] [ ] [ ] [ ]
[ ] [ ] [ ] [ ] [ ] [ ]
[ ] [ ] [ ] [ ] [ ] [ ]
[ ] [ ] [ ] [ ] [ ] [ ]
[ ] [ ] [ ] [ ] [ ] [X]
```

### Player 2 Turn State

```plaintext
Selected grid size: (8, 6)
Player 2 Turn
[ ] [ ] [ ] [ ] [ ] [ ]
[ ] [ ] [ ] [ ] [ ] [ ]
[ ] [ ] [ ] [ ] [ ] [ ]
[ ] [ ] [ ] [ ] [ ] [ ]
[ ] [ ] [ ] [ ] [ ] [ ]
[ ] [ ] [ ] [ ] [ ] [ ]
[ ] [ ] [ ] [ ] [ ] [ ]
[ ] [ ] [ ] [ ] [O] [X]
```

Not quite sure how we'll update these boxes to include different tokens, but we'll figure it out, probably, maybe.

## Possible Choices

* **Connect 4** - Multiple players can engage in a simple, GUI-based game of Connect 4. **Requires GUI,** but we can cheat and use a TUI instead.
* **Zork** - Multiple players can play a simple, text-based (with images) adventure game. **Requires GUI.**
* **Text Messaging** - Multiple users can send simple, text messages to each other. **Probably requires networking.**

<!-- So basically these are all horrible -->

## Assignment Brief Excerpt

### Project Requirements

* Platform: Cross Platform (Windows, Mac, Linux)
* Languages: Python 3.x
* Collaboration: GitHub
* Libraries: Probably `prompt_toolkit`, but we'll decide

### Project Activities

1. Review all available projects before deciding which to develop - We chose Connect 4.
2. Consider your primary target audience (see Possible Project Target Demographics)
3. Create an overall specification based on user and system requirements (including HCI, game-rules and the game-mechanics (e.g. what are the rules for the game, how will the game be controlled, how will any non-player characters interact, etc.)
4. Create two different user profiles (based on your selected target type) – these profiles should include basic details regarding individual’s wants and needs associated with the game
5. Determine the project’s high-level ‘functional specifications’ (e.g. what are the hardware requirements, operating system environment, application functions, collisions, AI, scores, timers, etc.)
6. Determine the project’s high-level ‘non-functional’ specifications (aesthetic, usability, ease of use, feedback style, basic needs, etc.) 
7. Create mock-ups for the overall look, user interface design, dialogue windows and input mechanisms, etc
8. Construct basic storyboards associated with the game-play
9. Identify and rank potential risks to the project’s success (such as: technical knowledge, coding, testing, scope, dependencies) – this should not include time management
10. Identify and establish your software development strategy
11. Define an overall test plan (this will be used later and may be repeated several times to ensure the project is successful).


### Activity 2 Group Guidance – Design Analysis Session

Refine and improve your overall specification and ideas by removing inappropriate or out-of-scope elements, simplify requirements, identify opportunities to improve and streamline HCI elements, game-play and game mechanics, etc.)

1. Agree your project’s requirements ensuring you can deliver them successfully.
2. Use basic pseudo code to help define, establish and quickly test high-level in-game functions, actions and logic (depending on your preference you may prefer to complete step 4 before step 3)
3. Use basic UML flowcharts to help plan, design and test game logic, interaction, mechanics and flow
4. Establish game state management (start, win, lose, draw) – confirm how the state could be monitored, detected or changed?

### Activity Group Guidance 3 – Coding

1. Create a Git repository (or similar) to organise your coding strategy
2. Allocate responsibilities
3. Code (regardless of strategy you must continually test).
4. Complete this stage of the application (depending on strategy this may be repeated or be an incremental activity)

### Activity Group Guidance 4 – Testing

1. Conduct end-to-end system testing (as defined in activity 1.11)
2. Identify and log any errors (including code, logic, interaction, state, etc.)
3. Fix and Repeat (depending on strategy this may mean returning to Activity 2 and or 3)
4. Repeat while necessary

### Activity Group Guidance 5 – End of Project Review (Part A: 20%)

* Complete project source code listing (25%)
  * Consistent evidence of good standards (such as: naming, comments, etc.) (25%)
  * Consistent evidence of good structure (such as: indenting, continuity, etc.) (25%)
  * Consistent evidence of good coding practices (such as: modular, defined functions and clear logic) (25%)

### Activity Individual Guidance 6 – Post Project Design Documentation (Part B: 30%)

1. Gather and document evidence from ALL of your project’s activities and outcomes.
2. Combine and compile ALL project evidence into a well-structured, proofread PowerPoint style presentation that:
    1. Identifies and describes the project (5%)
    2. Identifies each member of your group and summarises their contribution to the project. (5%)
    3. Well-annotated screen shots demonstrating and highlighting features and functions of your software (including: segments of source code illustrating how problems were resolved (e.g. NPC, AI and player control) supported by any initial high-level pseudo code, run-time screen captures, errors as well as embedded digital photos of any hand drawn images, diagrams, initial flowcharts or the results of whiteboard brainstorming sessions, etc.) (15%)
3. A summary of the ‘target user’ including an example profile (5%)
4. An organised list of user requirements (based on the target user) (5%)
5. An organised list of system requirements (e.g. the project, the hardware, the software strategy, the game-rules and mechanics, etc.) (10%)
