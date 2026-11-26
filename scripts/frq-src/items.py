"""Our own exam-length AAQ and EBQ questions for the "frq" unit (David's choice: not Phineas's).

Written to match the released 2025 and 2026 AP Psychology free-response questions:
- an AAQ article is about 750 to 900 words, in Introduction, Participants, Method, Results and Discussion,
  with demographics in the text, a results table, and details the questions never ask about;
- an EBQ has three sources of about 350 to 700 words each, each with the same four sections.
The studies are fictional. The psychology they ask about comes from the kit's Psych units.
make_frq.py checks these and writes content/frq/fr.json.

Article text format (read by the site): blank line = new paragraph; "- " bullet; "1. " numbered step;
"| a | b |" table rows with an optional "Table: title" line above; "## " a subheading (EBQ sources).
"""

AAQ_LABEL = "Written for this kit: a fictional study in the style of the real exam."
EBQ_LABEL = "Written for this kit: fictional studies in the style of the real exam."

# Part wording from the 2026 AP Psychology exam (A, B, C and F name this article's variable, statistic and idea).
AAQ_D = "Identify one ethical guideline described in the study. Describe one way the researchers in the study applied this ethical guideline."
AAQ_E = "Explain the extent to which the research findings may or may not be generalizable using specific and relevant evidence from the study."
EBQ_PARTS = [
    ("A", "Propose a specific and defensible claim based in psychological science that responds to the question.", 1),
    ("Bi", "Support your claim using at least one piece of specific and relevant evidence from one of the sources.", 1),
    ("Bii", "Explain how the evidence from Part B (i) supports your claim using a psychological perspective, theory, concept, or research finding learned in AP Psychology.", 2),
    ("Ci", "Support your claim using an additional piece of specific and relevant evidence from a different source than the one that was used in Part B (i).", 1),
    ("Cii", "Explain how the evidence from Part C (i) supports your claim using a different psychological perspective, theory, concept, or research finding learned in AP Psychology than the one that was used in Part B (ii).", 2),
]

AAQ = [
    {
        "id": "screenlight",
        "topic": "Sleep, Circadian rhythm",
        "title": "Evening Screen Light and Falling Asleep",
        "sections": [
            ("Introduction", """This study examined whether the brightness and color of a tablet screen used in the evening affect how long it takes people to fall asleep that night."""),
            ("Participants", """Ninety-six students from two community colleges in Arizona were recruited through flyers posted on campus and a message sent to students who had signed up for a research email list. Students were not eligible if they had been diagnosed with a sleep disorder, took any medication to help them sleep, or had worked a night shift in the past month. Of the 117 students who completed the online screening survey, 21 were not eligible or could not attend all four nights. Each participant received a $40 gift card after the final night of the study.

Participants ranged in age from 18 to 26 years (mean age = 20.4 years, standard deviation = 1.9 years). The sample was 58% women, 41% men, and 1% nonbinary. The race/ethnicity of the participants was reported as follows: 44% Hispanic/Latino/a, 31% White, 12% Black/African American, 8% Asian/Asian American, and 5% multiracial. Most participants (71%) also held a part-time job. For one week before the study, each participant kept a written sleep diary; the average bedtime they reported was 12:10 a.m."""),
            ("Method", """Before any data were collected, the study plan was reviewed and approved by the colleges' institutional review board. At an orientation session, a researcher explained the procedures, including that participants would spend four nights in a sleep laboratory and would wear a wrist monitor while they slept. Each participant then read and signed a consent form. Participants were told that they could stop taking part at any time and would still receive the gift card. Each participant was given an ID number, and only ID numbers appeared on the data files, which were stored on a password-protected computer.

Participants were randomly assigned to one of two conditions:
- Bright screen condition: participants read on a tablet set to full brightness with the standard white display.
- Dim screen condition: participants read on the same model of tablet set to its lowest brightness with a warm, amber-colored filter turned on.

The first night in the laboratory was an adjustment night, and no data from it were used. On each of the next three nights, participants arrived at 8:30 p.m. and completed a 10-minute questionnaire about their caffeine use and activities that day. From 9:00 p.m. to 11:00 p.m., each participant sat alone in a private bedroom and read the same novel on their assigned tablet. Phones were collected at the door. The overhead lights in each room were kept dim and were the same in both conditions, and each room was kept at 68°F. A research assistant checked on each participant through an intercom at 10:00 p.m. The novel was chosen because none of the participants had read it before and its plot had nothing to do with sleep.

At 10:45 p.m., participants gave a small saliva sample, which was later tested for melatonin. Lights went out at 11:00 p.m. Sleep onset latency was measured as the number of minutes between lights-out and the first time the wrist monitor recorded 10 minutes in a row of sleep. The monitor also recorded total sleep time. Participants were woken at 7:00 a.m. and completed a 5-minute reaction-time test on a computer, pressing a key as soon as a dot appeared on the screen."""),
            ("Results and Discussion", """Two participants in the bright screen condition left the study after the adjustment night for reasons unrelated to the study, and their data were not used. For each remaining participant, the researchers averaged the measures across the three study nights. The mean results for each condition are shown in the table.

Table: Mean Results for Each Screen Condition
| Measure | Bright screen | Dim screen |
| Sleep onset latency (minutes) | 31.6 | 18.2 |
| Melatonin at 10:45 p.m. (picograms per milliliter) | 9.4 | 15.1 |
| Total sleep time (hours and minutes) | 6 h 41 min | 7 h 02 min |
| Morning reaction time (milliseconds) | 312 | 305 |

Participants in the bright screen condition took significantly longer to fall asleep than participants in the dim screen condition (p < .001). Their melatonin levels before lights-out were also significantly lower (p = .002). The differences in total sleep time and in morning reaction time were not statistically significant.

Participants' answers on the caffeine questionnaire did not differ between the two conditions. The researchers noted that the study lasted only three nights and took place in a laboratory, where participants could not use their phones or follow their usual bedtime routines."""),
        ],
        "q": {
            "A": "Identify the research method used in the study.",
            "B": "State the operational definition of sleep onset latency in the study.",
            "C": "Describe what the difference in mean sleep onset latency indicates for the bright screen group as compared to the dim screen group.",
            "D": AAQ_D,
            "E": AAQ_E,
            "F": "Explain how at least one of the research findings supports or refutes the idea that artificial light at night interferes with the circadian rhythm.",
        },
        "model": {
            "A": "The research method is an experiment.",
            "B": "Sleep onset latency was the number of minutes between lights-out and the first time the wrist monitor recorded 10 minutes in a row of sleep.",
            "C": "The bright screen group took 31.6 minutes to fall asleep on average, compared with 18.2 minutes for the dim screen group, and the difference was statistically significant. This indicates that reading on a bright white screen made people take longer to fall asleep, and the difference was unlikely to be due to chance.",
            "D": "The researchers used informed consent: before the study, a researcher explained the procedures, including the four nights in the sleep lab, and each participant signed a consent form and was told they could stop at any time and still get the gift card.",
            "E": "The findings may not generalize to older adults, because all the participants were community college students aged 18 to 26 (mean age 20.4) from two colleges in Arizona.",
            "F": "This supports the idea that artificial light at night interferes with the circadian rhythm. Participants who read on a bright screen had lower melatonin before lights-out (9.4 vs. 15.1) and took longer to fall asleep (31.6 vs. 18.2 minutes). Melatonin is released in response to darkness and helps you sleep, so bright light kept the body from preparing for sleep on its usual schedule.",
        },
        # What the key-word checker looks for in each part (92-frqcheck.js).
        "r": {
            "A": {"answer": "experiment", "keys": ["experiment"], "clues": ["random", "assign", "manipulat", "independent variable", "condition"],
                  "trap": "correlational study", "trapHint": "Participants were randomly assigned to the bright or dim screen, so the researchers manipulated the light: that makes it an experiment."},
            "B": {"groups": [["minute", " min"], ["lights-out", "lights out", "lights went out", "wrist", "monitor", "10 minutes", "ten minutes"]],
                  "labels": ["Says it was measured in minutes", "Gives how this study measured it (from lights-out until the wrist monitor recorded 10 minutes in a row of sleep)"]},
            "C": {"nums": ["31.6", "18.2", "13.4", "13 minutes"], "meaning": ["fall asleep", "fell asleep", "asleep", "sleep onset", "sleep"], "subject": ["bright", "dim"], "speedHint": True},
            "D": {"eth": [
                {"name": "Institutional review", "keys": ["institutional review", "review board", "irb", "ethics board", "ethics committee"], "ev": ["approved", "before", "plan", "review"]},
                {"name": "Informed consent", "keys": ["informed consent", "consent"], "ev": ["signed", "form", "explained", "told", "procedures", "before"]},
                {"name": "Right to withdraw", "keys": ["withdraw", "stop taking part", "stop at any time", "leave the study", "quit"], "ev": ["any time", "anytime", "gift card", "still"]},
                {"name": "Confidentiality", "keys": ["confidential", "anonym", "id number", "privacy", "private"], "ev": ["id number", "number", "password", "names", "stored"]},
            ], "notIn": ["debrief", "harm"]},
            "E": {"pop": ["college", "student", "young adult", "teen", "older", "adults", "children", "general population", "everyone", "people"],
                  "demo": ["18", "26", "20.4", "58%", "41%", "44%", "31%", "12%", "8%", "71%", "arizona", "community college"]},
            "F": {"data": ["31.6", "18.2", "13.4", "9.4", "15.1", "13 minutes"], "concept": ["circadian", "biological clock", "melatonin", "light", "sleep-wake", "body clock"]},
        },
    },
]

EBQ = [
    {
        "id": "support",
        "topic": "Health psychology, Stress",
        "title": "Social Support and Stress",
        "question": "Using the sources provided, develop and justify an argument about whether social support reduces the harmful effects of stress.",
        "topicWords": ["social support", "support", "stress", "friend", "sick"],
        "sources": [
            ("Having a Friend in the Room During a Stressful Task", """## Introduction
In this study, researchers examined whether having a friend present changes how strongly the body reacts while a person completes a stressful task.

## Participants
Eighty-four undergraduate students (52 women, 32 men) at a public university in the Midwestern United States took part in exchange for course credit. Participants ranged in age from 18 to 23 years (mean age = 19.3 years). Each participant was asked to bring a same-gender friend they had known for at least six months. Researchers did not report race/ethnicity data for the participants.

## Method
Participants were randomly assigned to one of three conditions:
1. Friend condition: the participant's friend sat beside them for the whole task and was told to be encouraging (for example, "You've got this").
2. Stranger condition: a research assistant the participant had never met sat beside them and was told to be encouraging in the same way.
3. Alone condition: the participant completed the task alone. In this condition, the friend waited in another room.

Each participant first sat quietly for 10 minutes while a cuff on their arm measured blood pressure and a sensor on their finger measured heart rate. Participants were then told they had 5 minutes to prepare a speech about why they would be a good fit for a job and would deliver it to two judges, who would rate it on video. After preparing, participants gave the speech for 5 minutes and then counted backward from 1,022 by 13s for 3 minutes, starting over each time they made a mistake. The judges kept neutral faces and did not smile or nod.

Heart rate and blood pressure were recorded every minute. After the task, participants rated how stressed they felt on a scale from 1 (not at all stressed) to 10 (extremely stressed). At the end of the session, participants were told that the speeches had not actually been recorded or rated.

## Results and Discussion
The researchers compared each participant's average heart rate and blood pressure during the task with their measures during the quiet period.

Table: Mean Increase from the Quiet Period to the Task
| Condition | Heart rate (beats per minute) | Systolic blood pressure (mm Hg) | Stress rating (1 to 10) |
| Friend | +9 | +11 | 5.8 |
| Stranger | +16 | +19 | 6.9 |
| Alone | +18 | +21 | 7.1 |

Participants in the friend condition showed significantly smaller increases in heart rate and blood pressure than participants in the alone condition (p < .01). The stranger and alone conditions did not differ significantly on any measure. Participants in all three conditions rated the task as stressful, and the differences in stress ratings were not statistically significant."""),
            ("Support and Illness Among Family Caregivers", """## Introduction
Caring for a family member with a long-term illness is a common source of ongoing stress. In this study, researchers examined whether caregivers who have more support from other people get sick less often.

## Participants
The study included 412 adults (68% women, 32% men) in Ohio who were the main caregiver for a parent or spouse with dementia. Participants were recruited through support organizations and doctors' offices. They ranged in age from 34 to 81 years (mean age = 58.7 years) and had been caregivers for an average of 3.4 years. The race/ethnicity of the participants was 71% White, 19% Black/African American, 6% Hispanic/Latino/a, and 4% other.

## Method
At the start of the study, participants completed a 12-item questionnaire measuring perceived social support, which asked how much they agreed with statements such as "There is someone I can turn to when I need help" and "I have people who will listen when I need to talk." Scores ranged from 12 to 84, with higher scores meaning more support. Participants also reported how many hours per week they spent caregiving.

For the next six months, participants filled out a short health diary each week. The diary asked how many days that week they had been sick enough to miss work or other activities, and whether they had a cold or the flu. Participants were paid $10 for each month of completed diaries.

## Results and Discussion
Participants' social support scores were negatively correlated with the number of sick days they reported over the six months (r = -.38, p < .001). Caregivers in the top quarter of support scores reported an average of 4.1 sick days, while caregivers in the bottom quarter reported an average of 11.6 sick days. Support scores were also negatively correlated with the number of colds or cases of the flu reported (r = -.29, p < .001).

Hours spent caregiving were positively correlated with sick days (r = .21). The relationship between support and sick days remained statistically significant when the researchers accounted for hours spent caregiving, age, and income.

The researchers noted that the study relied on caregivers' own reports of illness rather than medical records."""),
            ("A Peer Support Group for First-Year College Students", """## Introduction
Starting college brings many new demands. In this study, researchers tested whether a weekly peer support group lowers stress during students' first semester.

## Participants
Participants were 180 first-year students at a large university in Georgia who responded to an email invitation sent to all first-year students. Participants ranged in age from 17 to 20 years (mean age = 18.2 years). The sample was 61% women and 39% men, and 34% were the first in their family to attend college. Participants received a $25 campus bookstore card for completing the final survey.

## Method
At the start of the semester, participants completed the 10-item Perceived Stress Scale, which asks how often in the past month they felt "unable to control the important things in your life" and similar statements. Scores range from 0 to 40, with higher scores meaning more stress. Participants also listed the major stressors they expected that semester (for example, money, homework load, or being far from home).

Participants were then randomly assigned either to join a peer support group or to a waitlist group. Support groups of 8 to 10 students met for one hour each week for eight weeks, led by a trained junior or senior student. In each meeting, students talked about what was going on in their lives and helped one another think through problems. Students on the waitlist were offered a place in a group the following semester. At the end of the semester, all participants completed the Perceived Stress Scale again.

## Results and Discussion
Students in the support group condition showed a significantly larger drop in stress scores from the start to the end of the semester than students in the waitlist condition (p = .01).

Table: Mean Perceived Stress Scale Scores (0 to 40)
| Group | Start of semester | End of semester |
| Support group, attended 5 or more meetings | 21.4 | 16.9 |
| Support group, attended fewer than 5 meetings | 21.1 | 20.3 |
| Waitlist | 21.6 | 21.8 |

The drop in stress appeared only among students who attended at least five of the eight meetings. Among students who had listed few expected stressors at the start of the semester, there was no significant difference between the support group and the waitlist. The researchers suggested that the group helped most for students who were facing many stressors."""),
        ],
        "model": {
            "A": "Social support from people a person knows reduces the harmful effects of stress on the body, especially for people facing a lot of stress.",
            "Bi": "Participants who gave a stressful speech with a friend beside them had a heart rate increase of only 9 beats per minute, compared with 18 for participants who were alone (Source 1).",
            "Bii": "This supports my claim because stress activates the sympathetic nervous system, the body's fight-or-flight response, which raises heart rate and blood pressure. Having a friend present made that sympathetic response smaller, so the support reduced the body's stress reaction.",
            "Ci": "Caregivers with the most social support reported an average of 4.1 sick days over six months, compared with 11.6 sick days for caregivers with the least support, and support was negatively correlated with sick days (r = -.38) (Source 2).",
            "Cii": "This supports my claim because long-term stress causes immunosuppression: stress hormones like cortisol weaken the immune system, so stressed people get sick more often. Caregivers with more support got sick less, which suggests support protected them from stress weakening their immune systems.",
        },
    },
]

GUIDE = {
    "aaq": [
        {"p": "The AAQ is Question 1 of Section II. You get <b>one summarized study</b> (Introduction, Participants, Method, Results and Discussion, usually with a table or graph) and answer <b>six parts, A to F, for 7 points</b>. College Board suggests about <b>25 minutes</b>: the first 10 reading the article, the rest writing."},
        {"h": "What earns each point"},
        {"rows": [
            ["A. Research method (1)", "Name the method the study used: experiment, correlational study, case study, naturalistic observation, or meta-analysis. Naming two methods loses the point."],
            ["B. Operational definition (1)", "Say how <b>this study</b> measured or manipulated the variable, with something you could count or score (for example \"the number of minutes until…\"). A textbook definition earns 0."],
            ["C. Statistic (1)", "Say what the statistic shows <b>for these groups</b>: which group was higher or lower and what that means. Just repeating the numbers, or only defining the statistic, earns 0."],
            ["D. Ethical guideline (1)", "Name a guideline <b>the article describes</b> (informed consent, right to withdraw, debriefing, confidentiality, review board approval) and say how the researchers carried it out. A guideline the article doesn't mention earns 0."],
            ["E. Generalizability (1)", "Make a claim that the findings do or don't apply to a <b>specific population</b>, using participant details from the article (ages, percentages, location). Sample size alone doesn't count."],
            ["F. Support or refute (2)", "One point for using a specific result. The second point for accurately explaining how that result supports or refutes the idea in the question. Don't say a correlation proves a cause."],
        ]},
        {"h": "Tips"},
        {"p": "Read the six questions <b>before</b> the article so you know what to look for. Real articles include details no question asks about: skim those."},
        {"p": "Write in complete sentences, and always tie your answer to this study. Spelling doesn't cost points if the reader can tell the word."},
        {"p": "Source: the 2025 and 2026 AP Psychology free-response questions and scoring guidelines from College Board."},
    ],
    "ebq": [
        {"p": "The EBQ is Question 2 of Section II. You get <b>three summarized studies</b> on one topic and build an argument in <b>three parts, A to C, for 7 points</b>. College Board suggests about <b>45 minutes</b>: the first 15 reading the sources, the rest writing."},
        {"h": "What earns each point"},
        {"rows": [
            ["A. Claim (1)", "A specific claim that answers the question, such as an effect or a recommendation. Restating the question or saying something too simple (\"It is important to study hard\") earns 0."],
            ["B(i). Evidence (1)", "Specific, accurate evidence from one source, with a citation: \"(Source 1)\" or \"According to Source 1…\". No citation, the wrong source number, or a vague summary earns 0."],
            ["B(ii). Explain and apply (2)", "One point for explaining how the evidence supports your claim. The second for doing it <b>with a psychology concept, theory, perspective or research finding</b> from the course. A definition alone doesn't count."],
            ["C(i). Evidence (1)", "Like B(i), but from a <b>different source</b> than B(i)."],
            ["C(ii). Explain and apply (2)", "Like B(ii), but with a <b>different concept</b> than the one you used in B(ii)."],
        ]},
        {"h": "Tips"},
        {"p": "Words that come from the sources themselves, like \"mean\" or \"statistical significance,\" don't count as your psychology concept. Bring in something you learned in class."},
        {"p": "Keep it consistent: your evidence in B and C has to support the claim you made in A."},
        {"p": "Source: the 2025 and 2026 AP Psychology free-response questions and scoring guidelines from College Board."},
    ],
}

LINKS = {
    "short": {"label": "Phineas's AP Psych kit", "url": "https://ichbleibhier.github.io/Psych-Unit-1/Psych%20Unit%201%20Study%20Kit.html"},
    "past": [
        {"label": "2026 free-response questions", "url": "https://apcentral.collegeboard.org/media/pdf/ap26-frq-psychology.pdf"},
        {"label": "2026 scoring guidelines", "url": "https://apcentral.collegeboard.org/media/pdf/ap26-sg-psychology.pdf"},
        {"label": "2025 free-response questions, set 1", "url": "https://apcentral.collegeboard.org/media/pdf/ap25-frq-psychology-set-1.pdf"},
        {"label": "2025 free-response questions, set 2", "url": "https://apcentral.collegeboard.org/media/pdf/ap25-frq-psychology-set-2.pdf"},
    ],
}
