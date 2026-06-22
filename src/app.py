"""NEET nonprofit volunteer scheduling API."""

from fastapi import FastAPI, HTTPException
from fastapi.staticfiles import StaticFiles
from fastapi.responses import RedirectResponse
from fastapi.middleware.cors import CORSMiddleware
import os
import logging
from pathlib import Path

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI(
    title="NEET Coaching Volunteer Scheduler",
    description="Scheduling and teacher resource API for a nonprofit serving 11th and 12th standard NEET students",
)

# Add CORS middleware for production readiness
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Mount the static files directory
current_dir = Path(__file__).parent
app.mount("/static", StaticFiles(directory=os.path.join(Path(__file__).parent,
          "static")), name="static")

teacher_resources = {
    "11th Standard": {
        "focus": "NCERT mastery with concept-building for Physics, Chemistry, and Biology",
        "subjects": ["Physics", "Chemistry", "Biology"],
        "goals": [
            "Strengthen foundational concepts",
            "Build disciplined problem-solving habits",
            "Introduce NEET-style MCQ reasoning early",
        ],
    },
    "12th Standard": {
        "focus": "Board alignment plus NEET revision depth, timed practice, and error correction",
        "subjects": ["Physics", "Chemistry", "Biology"],
        "goals": [
            "Finish syllabus with revision blocks",
            "Practice mixed NEET sets under time pressure",
            "Track mistakes and recovery plans",
        ],
    },
}

weekly_slots = {
    "Monday": [
        {
            "slot_id": "mon-1",
            "time": "4:00 PM - 4:45 PM",
            "grade": "11th Standard",
            "subject": "Physics",
            "topic": "Units, dimensions, and motion graphs",
            "max_volunteers": 1,
            "volunteers": [],
            "lesson_plan": {
                "course_structure": [
                    "10 min: Units, dimensions, and common conversion traps",
                    "20 min: Reading displacement-time and velocity-time graphs",
                    "10 min: Guided MCQs with reasoning",
                    "5 min: Reflection and recap",
                ],
                "homework": [
                    "Solve 10 motion graph questions",
                    "Write one-page summary of dimension analysis shortcuts",
                ],
                "life_skill_focus": "Teach students to break large problems into smaller checkpoints before panic builds.",
            },
        },
        {
            "slot_id": "mon-2",
            "time": "5:00 PM - 5:45 PM",
            "grade": "12th Standard",
            "subject": "Chemistry",
            "topic": "Electrochemistry basics and galvanic cells",
            "max_volunteers": 1,
            "volunteers": [],
            "lesson_plan": {
                "course_structure": [
                    "15 min: Cell notation and redox recap",
                    "15 min: E cell and spontaneity",
                    "10 min: Two exam-style examples",
                    "5 min: Recap",
                ],
                "homework": [
                    "Practice 8 electrochemistry MCQs",
                    "Create a formula card for electrode potential relations",
                ],
                "life_skill_focus": "Model a calm checklist approach: identify data, formula, substitution, and unit check.",
            },
        },
        {
            "slot_id": "mon-3",
            "time": "6:00 PM - 6:45 PM",
            "grade": "11th Standard",
            "subject": "Biology",
            "topic": "Cell structure and biomolecules",
            "max_volunteers": 1,
            "volunteers": [],
            "lesson_plan": {
                "course_structure": [
                    "15 min: Cell organelle functions",
                    "15 min: Biomolecule classification",
                    "10 min: NEET assertion-reason discussion",
                    "5 min: Recall drill",
                ],
                "homework": [
                    "Label a cell diagram from memory",
                    "Revise biomolecule examples with flashcards",
                ],
                "life_skill_focus": "Encourage active recall instead of passive rereading for retention.",
            },
        },
    ],
    "Tuesday": [
        {
            "slot_id": "tue-1",
            "time": "4:00 PM - 4:45 PM",
            "grade": "12th Standard",
            "subject": "Physics",
            "topic": "Current electricity and circuits",
            "max_volunteers": 1,
            "volunteers": [],
            "lesson_plan": {
                "course_structure": [
                    "10 min: Ohm's law recap",
                    "20 min: Series-parallel reasoning",
                    "10 min: Circuit-based MCQs",
                    "5 min: Wrap-up",
                ],
                "homework": [
                    "Solve 12 current electricity numericals",
                    "Summarize Kirchhoff rules with one example",
                ],
                "life_skill_focus": "Show how drawing neat diagrams first reduces avoidable mistakes.",
            },
        },
        {
            "slot_id": "tue-2",
            "time": "5:00 PM - 5:45 PM",
            "grade": "11th Standard",
            "subject": "Chemistry",
            "topic": "Atomic structure and quantum numbers",
            "max_volunteers": 1,
            "volunteers": [],
            "lesson_plan": {
                "course_structure": [
                    "15 min: Atomic models overview",
                    "15 min: Quantum numbers and orbitals",
                    "10 min: Short MCQ drill",
                    "5 min: Recap",
                ],
                "homework": [
                    "Attempt 10 questions on quantum numbers",
                    "Prepare a comparison table of atomic models",
                ],
                "life_skill_focus": "Help learners build a revision sheet habit after each class.",
            },
        },
        {
            "slot_id": "tue-3",
            "time": "6:00 PM - 6:45 PM",
            "grade": "12th Standard",
            "subject": "Biology",
            "topic": "Genetics and inheritance patterns",
            "max_volunteers": 1,
            "volunteers": [],
            "lesson_plan": {
                "course_structure": [
                    "15 min: Mendelian laws refresher",
                    "15 min: Pedigree interpretation",
                    "10 min: NEET genetics MCQs",
                    "5 min: Summary",
                ],
                "homework": [
                    "Solve 8 pedigree-based questions",
                    "Make a chart of dominant versus recessive examples",
                ],
                "life_skill_focus": "Reinforce patience with multi-step reasoning instead of rushing to answers.",
            },
        },
    ],
    "Wednesday": [
        {
            "slot_id": "wed-1",
            "time": "4:00 PM - 4:45 PM",
            "grade": "11th Standard",
            "subject": "Physics",
            "topic": "Work, energy, and power",
            "max_volunteers": 1,
            "volunteers": [],
            "lesson_plan": {
                "course_structure": [
                    "15 min: Work-energy theorem",
                    "15 min: Conservation examples",
                    "10 min: Mixed MCQ practice",
                    "5 min: Wrap-up",
                ],
                "homework": [
                    "Solve 10 work-energy numericals",
                    "Write three situations showing energy conversion",
                ],
                "life_skill_focus": "Discuss how consistent short practice beats last-minute cramming.",
            },
        },
        {
            "slot_id": "wed-2",
            "time": "5:00 PM - 5:45 PM",
            "grade": "12th Standard",
            "subject": "Chemistry",
            "topic": "Chemical kinetics and rate laws",
            "max_volunteers": 1,
            "volunteers": [],
            "lesson_plan": {
                "course_structure": [
                    "10 min: Rate concepts",
                    "20 min: Order and molecularity",
                    "10 min: Graph interpretation MCQs",
                    "5 min: Recap",
                ],
                "homework": [
                    "Practice 10 rate-law questions",
                    "Prepare a note on first-order reaction features",
                ],
                "life_skill_focus": "Teach students to annotate question stems before solving.",
            },
        },
        {
            "slot_id": "wed-3",
            "time": "6:00 PM - 6:45 PM",
            "grade": "11th Standard",
            "subject": "Biology",
            "topic": "Plant tissues and morphology",
            "max_volunteers": 1,
            "volunteers": [],
            "lesson_plan": {
                "course_structure": [
                    "15 min: Tissue types overview",
                    "15 min: Morphology examples",
                    "10 min: Diagram-based MCQs",
                    "5 min: Recall drill",
                ],
                "homework": [
                    "Draw and label root, stem, and leaf modifications",
                    "Revise tissue functions using flashcards",
                ],
                "life_skill_focus": "Encourage memory anchoring through diagrams and self-quizzing.",
            },
        },
    ],
    "Thursday": [
        {
            "slot_id": "thu-1",
            "time": "4:00 PM - 4:45 PM",
            "grade": "12th Standard",
            "subject": "Physics",
            "topic": "Ray optics and image formation",
            "max_volunteers": 1,
            "volunteers": [],
            "lesson_plan": {
                "course_structure": [
                    "15 min: Mirror and lens sign conventions",
                    "15 min: Image tracing practice",
                    "10 min: Exam-style numericals",
                    "5 min: Recap",
                ],
                "homework": [
                    "Solve 8 ray optics problems",
                    "Make a formula sheet for mirrors and lenses",
                ],
                "life_skill_focus": "Explain why careful sign conventions save time and confidence.",
            },
        },
        {
            "slot_id": "thu-2",
            "time": "5:00 PM - 5:45 PM",
            "grade": "11th Standard",
            "subject": "Chemistry",
            "topic": "Periodic trends and chemical bonding intro",
            "max_volunteers": 1,
            "volunteers": [],
            "lesson_plan": {
                "course_structure": [
                    "15 min: Periodic trends logic",
                    "15 min: Bond formation basics",
                    "10 min: Trend-based MCQs",
                    "5 min: Summary",
                ],
                "homework": [
                    "Answer 12 periodicity questions",
                    "Write one-page notes on ionic versus covalent bonding",
                ],
                "life_skill_focus": "Connect good note-making to faster revision later.",
            },
        },
        {
            "slot_id": "thu-3",
            "time": "6:00 PM - 6:45 PM",
            "grade": "12th Standard",
            "subject": "Biology",
            "topic": "Human reproduction and reproductive health",
            "max_volunteers": 1,
            "volunteers": [],
            "lesson_plan": {
                "course_structure": [
                    "15 min: Human reproductive system overview",
                    "15 min: Hormonal regulation and health topics",
                    "10 min: NEET conceptual questions",
                    "5 min: Wrap-up",
                ],
                "homework": [
                    "Revise labeled diagrams from NCERT",
                    "Solve 8 reproductive health MCQs",
                ],
                "life_skill_focus": "Model respectful, clear communication around sensitive topics.",
            },
        },
    ],
    "Friday": [
        {
            "slot_id": "fri-1",
            "time": "4:00 PM - 4:45 PM",
            "grade": "11th Standard",
            "subject": "Physics",
            "topic": "Rotational motion essentials",
            "max_volunteers": 1,
            "volunteers": [],
            "lesson_plan": {
                "course_structure": [
                    "15 min: Torque and moment of inertia",
                    "15 min: Rolling motion basics",
                    "10 min: Short MCQ set",
                    "5 min: Summary",
                ],
                "homework": [
                    "Solve 8 rotational motion questions",
                    "Prepare a concept map for torque applications",
                ],
                "life_skill_focus": "Show how concept maps make hard chapters less overwhelming.",
            },
        },
        {
            "slot_id": "fri-2",
            "time": "5:00 PM - 5:45 PM",
            "grade": "12th Standard",
            "subject": "Chemistry",
            "topic": "Coordination compounds naming and isomerism",
            "max_volunteers": 1,
            "volunteers": [],
            "lesson_plan": {
                "course_structure": [
                    "15 min: Coordination entity basics",
                    "15 min: Nomenclature and isomerism",
                    "10 min: NEET-style practice",
                    "5 min: Recap",
                ],
                "homework": [
                    "Name 10 coordination compounds",
                    "List isomerism types with one example each",
                ],
                "life_skill_focus": "Teach students to convert confusing facts into small recall lists.",
            },
        },
        {
            "slot_id": "fri-3",
            "time": "6:00 PM - 6:45 PM",
            "grade": "11th Standard",
            "subject": "Biology",
            "topic": "Photosynthesis strategy and key reactions",
            "max_volunteers": 1,
            "volunteers": [],
            "lesson_plan": {
                "course_structure": [
                    "15 min: Light reaction overview",
                    "15 min: Calvin cycle essentials",
                    "10 min: Flowchart-based revision",
                    "5 min: Wrap-up",
                ],
                "homework": [
                    "Draw the photosynthesis flow from memory",
                    "Practice 10 photosynthesis MCQs",
                ],
                "life_skill_focus": "Highlight the value of visual revision for long biology processes.",
            },
        },
    ],
    "Saturday": [
        {
            "slot_id": "sat-1",
            "time": "9:00 AM - 9:45 AM",
            "grade": "12th Standard",
            "subject": "Physics",
            "topic": "Modern physics rapid revision",
            "max_volunteers": 1,
            "volunteers": [],
            "lesson_plan": {
                "course_structure": [
                    "10 min: Photoelectric effect refresher",
                    "15 min: Atoms and nuclei shortcuts",
                    "15 min: Timed MCQs",
                    "5 min: Takeaways",
                ],
                "homework": [
                    "Finish a 15-question modern physics worksheet",
                    "Mark three recurring mistakes in a notebook",
                ],
                "life_skill_focus": "Normalize mistake tracking as a growth tool, not a failure signal.",
            },
        },
        {
            "slot_id": "sat-2",
            "time": "10:00 AM - 10:45 AM",
            "grade": "11th Standard",
            "subject": "Chemistry",
            "topic": "Thermodynamics and enthalpy",
            "max_volunteers": 1,
            "volunteers": [],
            "lesson_plan": {
                "course_structure": [
                    "15 min: System, surroundings, and state functions",
                    "15 min: Enthalpy and Hess law",
                    "10 min: Sample problems",
                    "5 min: Recap",
                ],
                "homework": [
                    "Solve 8 enthalpy problems",
                    "Write a short note on exothermic versus endothermic processes",
                ],
                "life_skill_focus": "Show students how comparison tables can reduce confusion.",
            },
        },
        {
            "slot_id": "sat-3",
            "time": "11:00 AM - 11:45 AM",
            "grade": "12th Standard",
            "subject": "Biology",
            "topic": "Evolution and evidence overview",
            "max_volunteers": 1,
            "volunteers": [],
            "lesson_plan": {
                "course_structure": [
                    "15 min: Evolution theories snapshot",
                    "15 min: Evidence and examples",
                    "10 min: NEET mixed MCQs",
                    "5 min: Summary",
                ],
                "homework": [
                    "Prepare a chart of evidences for evolution",
                    "Solve 10 evolution questions",
                ],
                "life_skill_focus": "Encourage linking facts into stories for better long-term recall.",
            },
        },
        {
            "slot_id": "sat-4",
            "time": "2:00 PM - 2:45 PM",
            "grade": "11th Standard",
            "subject": "Physics",
            "topic": "Gravitation and satellite basics",
            "max_volunteers": 1,
            "volunteers": [],
            "lesson_plan": {
                "course_structure": [
                    "15 min: Gravitational law and field",
                    "15 min: Satellite motion ideas",
                    "10 min: Numericals",
                    "5 min: Wrap-up",
                ],
                "homework": [
                    "Attempt 8 gravitation problems",
                    "List key orbital velocity formulas",
                ],
                "life_skill_focus": "Demonstrate how formula clustering speeds revision.",
            },
        },
        {
            "slot_id": "sat-5",
            "time": "3:00 PM - 3:45 PM",
            "grade": "12th Standard",
            "subject": "Chemistry",
            "topic": "Aldehydes, ketones, and carboxylic acids",
            "max_volunteers": 1,
            "volunteers": [],
            "lesson_plan": {
                "course_structure": [
                    "15 min: Functional group overview",
                    "15 min: Important reactions",
                    "10 min: Conversion-based MCQs",
                    "5 min: Recap",
                ],
                "homework": [
                    "Practice 10 reaction conversion questions",
                    "Create a reaction summary sheet",
                ],
                "life_skill_focus": "Promote spaced revision instead of single-session memorization.",
            },
        },
    ],
    "Sunday": [
        {
            "slot_id": "sun-1",
            "time": "9:00 AM - 9:45 AM",
            "grade": "11th Standard",
            "subject": "Biology",
            "topic": "Digestive system and human physiology",
            "max_volunteers": 1,
            "volunteers": [],
            "lesson_plan": {
                "course_structure": [
                    "15 min: Organ overview",
                    "15 min: Enzymes and functions",
                    "10 min: Conceptual MCQs",
                    "5 min: Summary",
                ],
                "homework": [
                    "Label the digestive system diagram",
                    "Solve 8 physiology questions",
                ],
                "life_skill_focus": "Tie disciplined routines to better cognitive energy for study.",
            },
        },
        {
            "slot_id": "sun-2",
            "time": "10:00 AM - 10:45 AM",
            "grade": "12th Standard",
            "subject": "Physics",
            "topic": "Alternating current essentials",
            "max_volunteers": 1,
            "volunteers": [],
            "lesson_plan": {
                "course_structure": [
                    "15 min: AC terms and waveform basics",
                    "15 min: RMS values and reactance",
                    "10 min: Quick numericals",
                    "5 min: Recap",
                ],
                "homework": [
                    "Solve 8 AC numericals",
                    "Summarize RMS and peak relations",
                ],
                "life_skill_focus": "Show how repeated summary-writing improves confidence before exams.",
            },
        },
        {
            "slot_id": "sun-3",
            "time": "11:00 AM - 11:45 AM",
            "grade": "11th Standard",
            "subject": "Chemistry",
            "topic": "Equilibrium and Le Chatelier principle",
            "max_volunteers": 1,
            "volunteers": [],
            "lesson_plan": {
                "course_structure": [
                    "15 min: Dynamic equilibrium basics",
                    "15 min: Le Chatelier applications",
                    "10 min: MCQ walkthrough",
                    "5 min: Wrap-up",
                ],
                "homework": [
                    "Practice 10 equilibrium problems",
                    "Write three real examples of shifting equilibrium",
                ],
                "life_skill_focus": "Help students connect abstract concepts to real examples.",
            },
        },
        {
            "slot_id": "sun-4",
            "time": "2:00 PM - 2:45 PM",
            "grade": "12th Standard",
            "subject": "Biology",
            "topic": "Ecology and ecosystem flow",
            "max_volunteers": 1,
            "volunteers": [],
            "lesson_plan": {
                "course_structure": [
                    "15 min: Ecosystem components",
                    "15 min: Energy flow and pyramids",
                    "10 min: Ecology MCQs",
                    "5 min: Recap",
                ],
                "homework": [
                    "Make a food chain and food web example chart",
                    "Solve 10 ecology MCQs",
                ],
                "life_skill_focus": "Encourage students to review mistakes without self-criticism.",
            },
        },
        {
            "slot_id": "sun-5",
            "time": "3:00 PM - 3:45 PM",
            "grade": "12th Standard",
            "subject": "Chemistry",
            "topic": "Biomolecules and rapid organic revision",
            "max_volunteers": 1,
            "volunteers": [],
            "lesson_plan": {
                "course_structure": [
                    "15 min: Biomolecule classification",
                    "15 min: Important reactions and memory triggers",
                    "10 min: Quick revision quiz",
                    "5 min: Summary",
                ],
                "homework": [
                    "Revise NCERT biomolecule tables",
                    "Create five memory triggers for difficult facts",
                ],
                "life_skill_focus": "Teach retrieval cues as a practical memory strategy.",
            },
        },
    ],
}


@app.get("/")
def root():
    return RedirectResponse(url="/static/index.html")


@app.get("/health")
def health_check():
    return {"status": "ok"}


@app.get("/api/resources")
def get_teacher_resources():
    logger.info("Fetching teacher resources")
    return teacher_resources


@app.get("/api/schedule")
def get_schedule():
    logger.info("Fetching weekly class schedule")
    return weekly_slots


@app.post("/api/schedule/{slot_id}/signup")
def signup_for_slot(slot_id: str, email: str, name: str):
    """Allow a volunteer to opt into a teaching slot and receive the lesson handbook."""
    for day, slots in weekly_slots.items():
        for slot in slots:
            if slot["slot_id"] != slot_id:
                continue

            volunteer_emails = [volunteer["email"] for volunteer in slot["volunteers"]]
            if email in volunteer_emails:
                logger.warning("Duplicate signup attempt: %s for %s", email, slot_id)
                raise HTTPException(status_code=400, detail=f"{email} is already assigned to this slot")

            if len(slot["volunteers"]) >= slot["max_volunteers"]:
                logger.warning("Signup rejected - slot full: %s", slot_id)
                raise HTTPException(status_code=400, detail="This teaching slot is already assigned")

            slot["volunteers"].append({"name": name, "email": email})
            logger.info("Volunteer %s signed up for %s", email, slot_id)
            return {
                "message": f"{name} is scheduled for {day} {slot['time']}.",
                "slot": {
                    "day": day,
                    "time": slot["time"],
                    "grade": slot["grade"],
                    "subject": slot["subject"],
                    "topic": slot["topic"],
                },
                "handbook": slot["lesson_plan"],
            }

    logger.warning("Signup attempt for unknown slot: %s", slot_id)
    raise HTTPException(status_code=404, detail="Teaching slot not found")
