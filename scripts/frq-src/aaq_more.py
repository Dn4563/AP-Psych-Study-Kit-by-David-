"""AAQ articles 2 to 10 (fictional studies written for this kit). Same format and rules as items.py.
Every idea a question or model answer relies on is a card in the kit's Psych units."""
from items import AAQ_D, AAQ_E

# Shared checker words for Part E: populations a student might name.
POP = ["college", "student", "teen", "adolescent", "young adult", "older", "adults", "children", "general population", "everyone", "people", "population"]

AAQ_MORE = [
    # ------------------------------------------------------------------ 2. caffeine (experiment)
    {
        "id": "caffeine",
        "topic": "Drugs, Stimulants",
        "title": "Caffeine Dose and Reaction Time",
        "sections": [
            ("Introduction", """This study examined whether the amount of caffeine a person consumes affects how quickly they respond to a simple visual signal."""),
            ("Participants", """Participants were 120 adults recruited through an online ad posted by a university hospital in Ohio. To take part, adults had to drink no more than two caffeinated drinks a day, have no heart problems, and not be pregnant. Of the 151 adults who filled out the online screening form, 31 did not meet these requirements or could not attend a morning session. Participants were paid $30 for one 3-hour session, and parking was provided.

Participants ranged in age from 21 to 45 years (mean age = 29.8 years, standard deviation = 6.2 years). The sample was 54% women and 46% men. The race/ethnicity of the participants was reported as follows: 62% White, 18% Black/African American, 11% Asian/Asian American, 6% Hispanic/Latino/a, and 3% multiracial. About half of the participants (48%) worked full-time, and 31% were students. On the screening form, participants reported drinking an average of 1.2 caffeinated drinks per day, most often coffee."""),
            ("Method", """The hospital's ethics board approved the study before it began. When participants arrived, a nurse checked their blood pressure, and a researcher explained that they would drink a beverage that might contain caffeine and then complete computer tasks. Participants signed a consent form, and they were told that they could end the session at any time and would still be paid.

Participants were asked not to eat or drink anything with caffeine for 24 hours before the session, and all sessions began at 8:00 a.m. Participants were given a plain bagel and water when they arrived so that no one would be tested on an empty stomach. Each participant was randomly assigned to one of three groups:
- No caffeine group: a drink containing 0 milligrams of caffeine.
- Low dose group: a drink containing 100 milligrams of caffeine, about the amount in one cup of coffee.
- High dose group: a drink containing 300 milligrams of caffeine.

All three drinks were 350 milliliters of the same lemon-flavored beverage and looked and tasted the same. Participants were asked to finish the drink within 5 minutes. Neither the participants nor the researcher running the session knew which drink a participant received.

After drinking the beverage, participants waited 45 minutes in a quiet room, where they could read magazines. They then sat at a computer in a small testing room with the lights dimmed and the door closed and completed a 10-minute reaction-time task. Before the real trials began, each participant completed 10 practice trials, which were not counted. A gray square appeared in the center of a computer screen at random intervals, and participants pressed the space bar as quickly as possible each time it appeared. Reaction time was measured as the average number of milliseconds between the square appearing and the key press, across 60 trials. Participants also rated how alert they felt from 1 (very sleepy) to 7 (very alert) and completed a short word puzzle that was not scored for this study.

At the end of the session, the nurse checked blood pressure again, and each participant was told which drink they had received. Participants who had received caffeine were reminded that it could make it harder to fall asleep that night if they drank more later in the day."""),
            ("Results and Discussion", """Three participants in the high dose group stopped the session early because they felt jittery, and their data were not used. The results for the remaining participants are shown in the table.

Table: Mean Results for Each Group
| Measure | No caffeine | Low dose | High dose |
| Reaction time (milliseconds) | 338 | 305 | 301 |
| Alertness rating (1 to 7) | 3.9 | 5.1 | 5.4 |
| Participants who reported feeling jittery | 3% | 10% | 37% |

Both caffeine groups had significantly faster reaction times than the no caffeine group (p < .01). The difference between the low dose and high dose groups was not statistically significant. Both caffeine groups also rated themselves as significantly more alert than the no caffeine group.

Blood pressure rose slightly more in the high dose group than in the other groups, but no participant's blood pressure reached an unsafe level. The researchers noted that the participants were light caffeine users and that the results might differ for people who drink caffeine every day."""),
        ],
        "q": {
            "A": "Identify the research method used in the study.",
            "B": "State the operational definition of reaction time in the study.",
            "C": "Describe what the mean reaction times indicate for the low dose group as compared to the no caffeine group.",
            "D": AAQ_D,
            "E": AAQ_E,
            "F": "Explain how at least one of the research findings supports or refutes the idea that caffeine is a stimulant that increases alertness.",
        },
        "model": {
            "A": "The research method is an experiment.",
            "B": "Reaction time was the average number of milliseconds between the gray square appearing on the screen and the participant pressing the space bar, across 60 trials.",
            "C": "The low dose group responded in 305 milliseconds on average, compared with 338 milliseconds for the no caffeine group, and the difference was statistically significant. This indicates that 100 milligrams of caffeine made people react faster, and the difference was unlikely to be due to chance.",
            "D": "The researchers used informed consent: before the study, a researcher explained that participants would drink a beverage that might contain caffeine and then do computer tasks, and participants signed a consent form and were told they could end the session at any time and still be paid.",
            "E": "The findings may not generalize to people who drink caffeine every day, because all participants were light caffeine users who drank no more than two caffeinated drinks a day, and they were adults aged 21 to 45 from one area of Ohio.",
            "F": "This supports the idea that caffeine is a stimulant that increases alertness. Both caffeine groups reacted significantly faster than the no caffeine group (305 and 301 milliseconds vs. 338) and rated themselves as more alert (5.1 and 5.4 vs. 3.9). Stimulants excite the central nervous system, so caffeine made participants more alert and quicker to respond.",
        },
        "r": {
            "A": {"answer": "experiment", "keys": ["experiment"], "clues": ["random", "assign", "manipulat", "independent variable", "group"],
                  "trap": "correlational study", "trapHint": "The researchers randomly assigned people to a caffeine dose, so they manipulated caffeine: that makes it an experiment."},
            "B": {"groups": [["millisecond", " ms"], ["square", "space bar", "key", "press", "60 trials", "appear"]],
                  "labels": ["Says it was measured in milliseconds", "Gives how this study measured it (time from the square appearing to pressing the space bar, over 60 trials)"]},
            "C": {"nums": ["305", "338", "33 milliseconds", "33 ms"], "meaning": ["react", "respond", "reaction", "faster", "quicker"], "subject": ["low dose", "caffeine", "100"], "speedHint": True},
            "D": {"eth": [
                {"name": "Institutional review", "keys": ["ethics board", "review board", "irb", "institutional review", "ethics committee"], "ev": ["approved", "before", "began"]},
                {"name": "Informed consent", "keys": ["informed consent", "consent"], "ev": ["signed", "form", "explained", "told", "before"]},
                {"name": "Right to withdraw", "keys": ["withdraw", "end the session", "stop at any time", "leave", "quit"], "ev": ["any time", "anytime", "paid", "still"]},
                {"name": "Debriefing", "keys": ["debrief"], "ev": ["told which", "which drink", "end of the session", "after"]},
            ], "notIn": ["confid", "harm"]},
            "E": {"pop": POP + ["daily", "every day", "heavy", "coffee drinker"],
                  "demo": ["21", "45", "29.8", "54%", "46%", "62%", "18%", "11%", "48%", "ohio", "light", "two caffeinated", "no more than two"]},
            "F": {"data": ["305", "301", "338", "5.1", "5.4", "3.9"], "concept": ["stimulant", "alert", "central nervous system", "excite"]},
        },
    },
    # ------------------------------------------------------------------ 3. exercise and depression (correlational; F refutes)
    {
        "id": "exercise",
        "topic": "Depressive disorders, Correlation",
        "title": "Weekly Exercise and Depressive Symptoms in Teens",
        "sections": [
            ("Introduction", """This study examined the relationship between how much high school students exercise and how many symptoms of depression they report."""),
            ("Participants", """Participants were 640 students in grades 9 through 12 at six public high schools in North Carolina. The schools were chosen because their principals agreed to take part. All students in the selected classes were invited, and 71% of those invited took part. Students who were absent on the day of the survey were not given a second chance to take it. Each participant was entered into a drawing for one of twenty $25 gift cards.

Participants ranged in age from 14 to 18 years (mean age = 15.9 years, standard deviation = 1.1 years). The sample was 52% girls, 46% boys, and 2% another gender identity. The race/ethnicity of the participants was reported as follows: 48% White, 27% Black/African American, 15% Hispanic/Latino/a, 5% Asian/Asian American, and 5% multiracial. Thirty-eight percent of participants played on at least one school sports team, and 41% received free or reduced-price school lunch. Two of the six schools were in rural areas, three in suburbs, and one in a city."""),
            ("Method", """The study was approved by a university's institutional review board and by the school district. Parents received a letter describing the study and returned a signed form if they agreed to let their child take part. Students also signed an assent form. Students were told that they could skip any question or stop at any time, and that their teachers would never see their answers. Surveys were labeled with code numbers instead of names.

Students completed the survey on school laptops during a homeroom period, which took about 25 minutes. A research assistant, not the teacher, handed out the laptops and answered questions. Students who did not take part read silently at their desks. Exercise was measured with the question "In the past 7 days, on how many days were you physically active for a total of at least 60 minutes per day?" Answers ranged from 0 to 7 days. Depressive symptoms were measured with a 20-item questionnaire asking how often in the past week students had felt sad, hopeless, tired, or uninterested in things they usually enjoy. Scores ranged from 0 to 60, with higher scores meaning more symptoms.

Before the main study, the researchers tested the exercise question with a separate group of 40 students who also wore step-counting watches for a week; students who reported more active days also took more steps. The survey also asked about hours of sleep on school nights, hours of screen time per day, and how many close friends the student had. It also asked whether the student had a job and how they got to school (walking, biking, bus, or car). Any student whose depression score was 40 or higher received a private message with information about the school counselor and a free support line.

The researchers chose to survey students in late October, after the start of the school year but before winter break, so that holidays and final exams would not affect students' answers. All six schools completed the survey within the same two weeks, and each school received a short report of its overall results, with no information about individual students."""),
            ("Results and Discussion", """Table: Mean Depressive Symptom Score by Days of Exercise per Week
| Days of exercise in the past week | Percent of students | Mean depressive symptom score (0 to 60) |
| 0 to 1 days | 22% | 24.6 |
| 2 to 4 days | 47% | 17.9 |
| 5 to 7 days | 31% | 12.3 |

Days of exercise were negatively correlated with depressive symptom scores (r = -.41, p < .001). Students who exercised on more days tended to report fewer symptoms of depression. Hours of sleep were also negatively correlated with depressive symptoms (r = -.33), and hours of screen time were positively correlated with depressive symptoms (r = .22).

Girls reported slightly higher depressive symptom scores than boys on average (19.4 vs. 16.2), and boys reported more days of exercise. Students who walked or biked to school did not differ from other students in depressive symptoms. The researchers noted that students who play sports may also spend more time with friends and coaches, and that students who feel depressed may have less energy to exercise."""),
        ],
        "q": {
            "A": "Identify the research method used in the study.",
            "B": "State the operational definition of exercise in the study.",
            "C": "Describe what the correlation coefficient of r = -.41 indicates about the relationship between days of exercise and depressive symptom scores.",
            "D": AAQ_D,
            "E": AAQ_E,
            "F": "Explain how at least one of the research findings supports or refutes the idea that exercising more causes teens to have fewer symptoms of depression.",
        },
        "model": {
            "A": "The research method is a correlational study.",
            "B": "Exercise was the number of days in the past 7 days (0 to 7) on which the student was physically active for a total of at least 60 minutes.",
            "C": "The correlation of r = -.41 is a moderate negative correlation: students who exercised on more days tended to have lower depressive symptom scores, and the relationship was statistically significant, so it was unlikely to be due to chance.",
            "D": "The researchers used confidentiality: surveys were labeled with code numbers instead of names, and students were told their teachers would never see their answers.",
            "E": "The findings may not generalize to teens across the United States, because all participants were students aged 14 to 18 from six public high schools in North Carolina, and 48% were White.",
            "F": "The findings do not support the claim that exercise causes fewer symptoms of depression. Days of exercise were negatively correlated with depressive symptoms (r = -.41), but that is not enough because this was a correlational study, and correlation does not equal causation. Students who feel depressed may have less energy to exercise, or a third variable like sleep or time with friends on sports teams could explain both.",
        },
        "r": {
            "A": {"answer": "correlational study", "keys": ["correlation"], "clues": ["relationship", "survey", "no random", "not manipulat", "measured", "r ="],
                  "trap": "experiment", "trapHint": "Nobody was assigned to exercise more or less; the researchers only measured two variables and looked at their relationship, so it is a correlational study."},
            "B": {"groups": [["day"], ["60 minutes", "sixty minutes", "7 days", "seven days", "past week", "0 to 7"]],
                  "labels": ["Says it was counted in days", "Gives how this study measured it (days in the past 7 with at least 60 minutes of activity)"]},
            "C": {"nums": ["-.41", ".41", "-0.41", "0.41"], "meaning": ["depress", "symptom"], "subject": ["exercise", "active"], "kind": "corr"},
            "D": {"eth": [
                {"name": "Institutional review", "keys": ["institutional review", "review board", "irb", "ethics board", "approved by"], "ev": ["approved", "district", "university"]},
                {"name": "Informed consent", "keys": ["informed consent", "consent", "assent", "parent"], "ev": ["signed", "letter", "form", "agreed"]},
                {"name": "Right to withdraw", "keys": ["withdraw", "stop at any time", "skip", "quit"], "ev": ["any time", "anytime", "question", "skip"]},
                {"name": "Confidentiality", "keys": ["confidential", "anonym", "code number", "privacy", "private"], "ev": ["code", "number", "names", "teachers", "never see"]},
                {"name": "Protection from harm", "keys": ["protection from harm", "harm", "counselor", "support line"], "ev": ["40", "counselor", "support line", "message"]},
            ], "notIn": ["debrief"]},
            "E": {"pop": POP + ["high school", "country", "united states", "other states"],
                  "demo": ["14", "18", "15.9", "52%", "46%", "48%", "27%", "15%", "71%", "38%", "north carolina", "six", "public high school"]},
            "F": {"data": ["-.41", ".41", "24.6", "12.3", "17.9", "-.33"], "concept": ["exercis", "depress", "caus"],
                  "stanceWant": "refute", "stanceHint": "This was a correlational study, so it can't show that exercise causes fewer symptoms. Say the finding does not support (or only partly supports) the causal claim, and why."},
        },
    },
    # ------------------------------------------------------------------ 4. exposure therapy (experiment)
    {
        "id": "spiders",
        "topic": "Phobias, Treatment",
        "title": "Exposure Therapy for Fear of Spiders",
        "sections": [
            ("Introduction", """This study tested whether a single long session of exposure therapy reduces fear and avoidance in adults with an intense fear of spiders."""),
            ("Participants", """Participants were recruited through ads on a university website and in local newspapers in Oregon. Adults who responded completed a phone interview with a clinical psychologist, and those who met the criteria for a specific phobia of spiders were invited to take part. People who were receiving other treatment for anxiety, or who had a heart condition, were not eligible. Of the 97 adults who completed the phone interview, 71 met the criteria, and 7 of those decided not to take part.

The final sample was 64 adults aged 19 to 58 years (mean age = 31.4 years, standard deviation = 9.7 years). The sample was 81% women and 19% men. The race/ethnicity of the participants was reported as follows: 77% White, 9% Asian/Asian American, 8% Hispanic/Latino/a, 3% Black/African American, and 3% multiracial. Most participants (72%) said their fear had started before age 10, and many said they checked rooms for spiders before entering them. Participants did not receive payment, but those in the waiting list group were offered free treatment after the study ended."""),
            ("Method", """The university's institutional review board approved the study. At the first visit, a psychologist explained that participants might be asked to be near or touch a live spider, which could cause strong fear. Participants signed a consent form. They were told that they could stop any task, or leave the study, at any time.

Before treatment, each participant completed a behavioral approach test. A live, harmless house spider sat in a covered glass tank at the far end of a 6-meter hallway. Participants were asked to walk toward the tank and do as many of 12 steps as they could, such as standing 1 meter from the tank, removing the lid, and letting the spider walk on a gloved hand. Avoidance was measured as the number of steps completed, from 0 to 12. At each step, participants also rated their fear from 0 (no fear) to 100 (the most fear imaginable), and the highest rating was recorded. They then filled out a questionnaire about their history of other fears and how much the fear affected their daily life, such as avoiding camping or basements. The test took about 15 minutes, and a researcher stood beside the participant the whole time.

Participants who completed all 12 steps before treatment would not have been included, but none did. Participants were then randomly assigned to one of two groups:
1. Exposure group: one 3-hour session with a therapist. The participant gradually moved closer to spiders of increasing size, staying with each step until their fear dropped by about half. The therapist first showed each step, such as holding a spider in a cup, and then helped the participant try it. Sessions took place in a quiet office with a window, and participants could take short breaks for water.
2. Waiting list group: no treatment during the study.

One week later, every participant completed the behavioral approach test again with a different spider of about the same size. Participants in the exposure group were also asked to look at photos of spiders for 10 minutes a day during that week, and most said they had done so on at least 5 days. The researcher who ran the test did not know which group each participant was in. After the test, participants also rated how confident they felt that they could handle seeing a spider at home, from 0 (not at all confident) to 10 (completely confident)."""),
            ("Results and Discussion", """Table: Mean Results Before and One Week After Treatment
| Group | Steps completed before | Steps completed after | Fear rating before (0 to 100) | Fear rating after (0 to 100) |
| Exposure | 3.1 | 10.4 | 86 | 31 |
| Waiting list | 3.3 | 3.8 | 84 | 80 |

One week after treatment, participants in the exposure group completed significantly more steps and reported significantly less fear than participants in the waiting list group (p < .001). Twenty-two of the 32 participants in the exposure group (69%) completed all 12 steps, compared with none in the waiting list group.

Two participants in the exposure group stopped the session early, and their after-treatment scores were included in the analysis. Confidence ratings rose from an average of 2.2 to 7.6 in the exposure group and stayed near 2 in the waiting list group. The researchers noted that the study did not test whether the improvement lasted beyond one week, and that all of the therapists had years of experience treating phobias."""),
        ],
        "q": {
            "A": "Identify the research method used in the study.",
            "B": "State the operational definition of avoidance in the study.",
            "C": "Describe what the mean number of steps completed after treatment indicates for the exposure group as compared to the waiting list group.",
            "D": AAQ_D,
            "E": AAQ_E,
            "F": "Explain how at least one of the research findings supports or refutes the idea that exposure therapy reduces fear in people with a specific phobia.",
        },
        "model": {
            "A": "The research method is an experiment.",
            "B": "Avoidance was the number of steps out of 12 that the participant completed in the behavioral approach test, such as standing 1 meter from the spider tank or letting the spider walk on a gloved hand.",
            "C": "After treatment, the exposure group completed 10.4 steps on average, compared with 3.8 steps for the waiting list group, and the difference was statistically significant. This indicates that people who had exposure therapy avoided the spider much less, and the difference was unlikely to be due to chance.",
            "D": "The researchers used informed consent: a psychologist explained that participants might have to be near or touch a live spider and could feel strong fear, participants signed a consent form, and they were told they could stop any task or leave at any time.",
            "E": "The findings may not generalize to men with spider phobias, because 81% of the participants were women, and 77% were White adults from Oregon.",
            "F": "This supports the idea that exposure therapy reduces fear in people with a specific phobia. The exposure group's fear ratings dropped from 86 to 31, while the waiting list group stayed about the same (84 to 80). This shows that exposure therapy works: it exposes people to what they normally avoid, and after being gradually exposed to spiders, the participants' fear went down and they could approach the spider.",
        },
        "r": {
            "A": {"answer": "experiment", "keys": ["experiment"], "clues": ["random", "assign", "manipulat", "independent variable", "group", "waiting list"],
                  "trap": "case study", "trapHint": "There were 64 participants randomly assigned to exposure or a waiting list, so this is an experiment, not a case study of one person."},
            "B": {"groups": [["step"], ["12", "twelve", "approach test", "tank", "spider", "hallway"]],
                  "labels": ["Says it was the number of steps completed", "Gives how this study measured it (steps out of 12 toward the spider in the approach test)"]},
            "C": {"nums": ["10.4", "3.8", "6.6"], "meaning": ["avoid", "approach", "steps", "closer", "fear"], "subject": ["exposure", "waiting", "treat"]},
            "D": {"eth": [
                {"name": "Institutional review", "keys": ["institutional review", "review board", "irb", "ethics board"], "ev": ["approved", "before", "board"]},
                {"name": "Informed consent", "keys": ["informed consent", "consent"], "ev": ["signed", "form", "explained", "told", "spider", "fear"]},
                {"name": "Right to withdraw", "keys": ["withdraw", "stop any task", "leave the study", "stop at any time", "quit"], "ev": ["any time", "anytime", "stop", "leave"]},
            ], "notIn": ["confid", "debrief"]},
            "E": {"pop": POP + ["men", "male", "women", "other phobia"],
                  "demo": ["81%", "19%", "77%", "19", "58", "31.4", "oregon", "women", "64"]},
            "F": {"data": ["86", "31", "84", "80", "10.4", "3.8", "69%", "3.1"], "concept": ["exposure", "fear", "phobia", "avoid"]},
        },
    },
    # ------------------------------------------------------------------ 5. exam stress and colds (correlational; F refutes)
    {
        "id": "examstress",
        "topic": "Stress, Immune system",
        "title": "Exam Stress and Catching a Cold",
        "sections": [
            ("Introduction", """This study examined whether college students who report more stress during final exams are more likely to report cold symptoms in the weeks around exams."""),
            ("Participants", """Participants were 212 undergraduate students at a private university in Pennsylvania. Students were recruited through an email sent to all students living in campus housing. They received course credit or $20 for taking part. Of the 260 students who replied to the email, 48 were not included because they had a long-term illness, took medication that affects the immune system, or were studying abroad that semester.

Participants ranged in age from 18 to 24 years (mean age = 20.1 years, standard deviation = 1.4 years). The sample was 57% women and 43% men. The race/ethnicity of the participants was reported as follows: 59% White, 16% Asian/Asian American, 12% Hispanic/Latino/a, 9% Black/African American, and 4% multiracial. Eighty-four percent of participants lived in a residence hall with a roommate, and the rest lived alone. About a third of participants (34%) also had a part-time job on campus."""),
            ("Method", """The university's institutional review board approved the study. Students read an online consent page explaining that they would answer short surveys on their phones for four weeks, and they clicked a button to agree. The consent page said that students could stop at any time, and that their answers would be stored without their names.

The study began in late November. Two weeks before final exams, students completed the 10-item Perceived Stress Scale, which asks how often in the past month they felt nervous and stressed or unable to handle everything they had to do. Scores range from 0 to 40, with higher scores meaning more stress. Students also reported how many exams and papers they had due and how many hours per week they usually exercised. These first surveys took about 15 minutes and were completed online.

For the next four weeks, which included the two weeks of final exams, students received a text message each evening with a link to a short checklist. Cold symptoms were measured as the number of days on which a student reported at least two of the following: sneezing, a runny or stuffy nose, a sore throat, or a cough. Students also reported hours of sleep each night and whether they had gotten a flu shot that year. The checklist asked how many cups of coffee or energy drinks the student had that day, but the researchers did not use those answers in this report. A research assistant checked the responses each week and contacted any student who had missed three or more days in a row to ask whether they wanted to continue.

Each checklist took about 1 minute. If a student missed a day, a reminder was sent the next morning, but students could not fill in checklists for earlier days. Students who completed at least 24 of the 28 daily checklists were included in the analysis.

At the end of the four weeks, students answered a few questions about whether they had used any cold medicine and whether anyone they lived with had been sick. Students were then sent a summary explaining what the researchers were studying."""),
            ("Results and Discussion", """Of the 212 students, 188 completed enough checklists to be included. Stress scores were positively correlated with the number of days with cold symptoms (r = .36, p < .001). Students who reported more stress before exams tended to report more days with cold symptoms during the four weeks.

Table: Days with Cold Symptoms by Stress Level
| Stress score group | Number of students | Mean days with cold symptoms (out of 28) |
| Low (0 to 13) | 51 | 2.1 |
| Medium (14 to 26) | 94 | 4.6 |
| High (27 to 40) | 43 | 7.8 |

Average hours of sleep were negatively correlated with days of cold symptoms (r = -.29). Students with higher stress scores also slept fewer hours on average. Getting a flu shot was not related to the number of days with cold symptoms.

Students who said that a roommate had been sick also reported more days with cold symptoms. Exercise hours were not significantly related to days with cold symptoms. The number of exams and papers due was only weakly related to days with cold symptoms (r = .12). The researchers noted that cold symptoms were reported by the students and were not confirmed by a doctor, and that the study took place during winter, when colds are common on campus."""),
        ],
        "q": {
            "A": "Identify the research method used in the study.",
            "B": "State the operational definition of cold symptoms in the study.",
            "C": "Describe what the correlation coefficient of r = .36 indicates about the relationship between stress scores and days with cold symptoms.",
            "D": AAQ_D,
            "E": AAQ_E,
            "F": "Explain how at least one of the research findings supports or refutes the idea that stress causes immunosuppression.",
        },
        "model": {
            "A": "The research method is a correlational study.",
            "B": "Cold symptoms were measured as the number of days, out of 28 daily checklists, on which a student reported at least two of these: sneezing, a runny or stuffy nose, a sore throat, or a cough.",
            "C": "The correlation of r = .36 is a positive correlation: students with higher stress scores tended to report more days with cold symptoms, and it was statistically significant, so the relationship was unlikely to be due to chance.",
            "D": "The researchers used confidentiality: the consent page told students their answers would be stored without their names.",
            "E": "The findings may not generalize to adults who are not in college, because all participants were students aged 18 to 24 living in campus housing at one private university in Pennsylvania, and 84% lived with a roommate.",
            "F": "The findings do not prove that stress causes immunosuppression. Students in the high stress group had 7.8 days with cold symptoms compared with 2.1 for the low stress group (r = .36), but this was a correlational study, so it cannot show cause. A third variable such as sleep could explain it, since stressed students also slept fewer hours, and sleep was related to colds too.",
        },
        "r": {
            "A": {"answer": "correlational study", "keys": ["correlation"], "clues": ["relationship", "survey", "no random", "not manipulat", "measured", "r ="],
                  "trap": "experiment", "trapHint": "The researchers didn't assign anyone to be stressed; they measured stress and colds and looked at the relationship, so it is a correlational study."},
            "B": {"groups": [["day"], ["two of", "2 of", "sneez", "runny", "sore throat", "cough", "checklist"]],
                  "labels": ["Says it was counted in days", "Gives how this study measured it (days with at least two of the listed symptoms on the daily checklist)"]},
            "C": {"nums": [".36", "0.36"], "meaning": ["cold", "symptom", "sick", "ill"], "subject": ["stress"], "kind": "corr"},
            "D": {"eth": [
                {"name": "Institutional review", "keys": ["institutional review", "review board", "irb", "ethics board"], "ev": ["approved", "board"]},
                {"name": "Informed consent", "keys": ["informed consent", "consent"], "ev": ["consent page", "clicked", "agree", "explain", "online"]},
                {"name": "Right to withdraw", "keys": ["withdraw", "stop at any time", "quit", "leave the study"], "ev": ["any time", "anytime", "stop"]},
                {"name": "Confidentiality", "keys": ["confidential", "anonym", "without their names", "privacy", "private"], "ev": ["name", "stored"]},
                {"name": "Debriefing", "keys": ["debrief"], "ev": ["summary", "explain", "end", "after", "studying"]},
            ], "notIn": ["harm"]},
            "E": {"pop": POP + ["not in college", "workers"],
                  "demo": ["18", "24", "20.1", "57%", "43%", "59%", "16%", "84%", "pennsylvania", "one private", "private university", "campus housing", "roommate"]},
            "F": {"data": [".36", "7.8", "2.1", "4.6", "-.29"], "concept": ["immun", "stress", "caus", "sick", "cold"],
                  "stanceWant": "refute", "stanceHint": "This was a correlational study, so it can't prove stress causes immunosuppression. Say the finding does not prove (or only partly supports) the causal claim, and why."},
        },
    },    # ------------------------------------------------------------------ 6. VR and pain (experiment)
    {
        "id": "vrpain",
        "topic": "Touch and pain, Gate control theory",
        "title": "Virtual Reality Distraction During a Needle Procedure",
        "sections": [
            ("Introduction", """This study examined whether playing a virtual reality game during a blood draw changes how much pain children report."""),
            ("Participants", """Participants were 156 children aged 8 to 14 who were having blood drawn for a routine test at an outpatient clinic of a children's hospital in Texas. Families were approached in the waiting room by a research assistant. Children who had a blood draw scheduled for a long-term illness, who had a history of seizures, or who had trouble seeing were not eligible. Of the 203 families approached, 47 declined, most often because they were in a hurry.

The children's mean age was 10.9 years (standard deviation = 1.8 years). The sample was 49% girls and 51% boys. The race/ethnicity of the children was reported by their parents as follows: 46% Hispanic/Latino/a, 28% White, 18% Black/African American, 5% Asian/Asian American, and 3% multiracial. Most children (68%) said they had had blood drawn at least once before. Each family received a $15 gift card."""),
            ("Method", """The hospital's institutional review board approved the study. A research assistant explained the study to each parent, who signed a consent form, and to each child, who agreed in writing on a simple assent form. Families were told that they could stop at any time without any effect on the child's care.

Before the blood draw, each child rated how worried they felt about the needle on a scale from 0 (not worried) to 10 (very worried). Children were then randomly assigned to one of three conditions:
1. Virtual reality condition: the child wore a virtual reality headset and played an underwater game, in which they steered a submarine and collected glowing fish, starting 1 minute before the needle went in.
2. Tablet condition: the child watched a cartoon of their choice on a tablet held by a parent, starting at the same time.
3. Standard care condition: the child received the clinic's usual care, in which the nurse talked with the child and a parent could hold their hand.

Parents in all three conditions could stay in the room. Six nurses with at least 3 years of experience did all of the blood draws, and each nurse worked with children in all three conditions. The blood draws took an average of 4 minutes.

Within 1 minute after the needle was removed, a research assistant who had not been in the room asked the child to point to one of six faces on the Faces Pain Scale, ranging from a smiling face (0, no pain) to a crying face (10, the most pain possible). Pain was measured as the number under the face the child pointed to. Parents also rated how upset their child seemed during the draw, and the nurse recorded whether the needle had to be inserted more than once.

Before the study began, the research team tested the virtual reality game with 12 children who were not in the study to make sure that the headset fit children of different sizes and that the game was easy to learn in under a minute. The headsets were cleaned with wipes after every use. All blood draws took place between 8:00 a.m. and noon in the same two rooms, which had the same chairs, lighting, and pictures on the walls. After the study, each child was allowed to play the virtual reality game for 5 minutes, whatever condition they had been in."""),
            ("Results and Discussion", """Worry ratings before the blood draw did not differ significantly among the three conditions. Pain ratings after the draw are shown in the table.

Table: Mean Ratings for Each Condition
| Condition | Number of children | Worry before (0 to 10) | Pain rating (0 to 10) |
| Virtual reality | 52 | 5.4 | 2.3 |
| Tablet | 53 | 5.2 | 3.9 |
| Standard care | 51 | 5.6 | 5.6 |

Children in the virtual reality condition reported significantly less pain than children in the standard care condition (p < .001) and than children in the tablet condition (p = .01). Children in the tablet condition reported significantly less pain than those in standard care (p = .02). Parents also rated children in the virtual reality condition as less upset.

The needle had to be inserted more than once for 11 children, spread across all three conditions. Four children in the virtual reality condition said the headset made them feel a little dizzy, and one asked to remove it. The researchers noted that the nurses could see which condition each child was in."""),
        ],
        "q": {
            "A": "Identify the research method used in the study.",
            "B": "State the operational definition of pain in the study.",
            "C": "Describe what the mean pain ratings indicate for the virtual reality condition as compared to the standard care condition.",
            "D": AAQ_D,
            "E": AAQ_E,
            "F": "Explain how at least one of the research findings supports or refutes gate control theory.",
        },
        "model": {
            "A": "The research method is an experiment.",
            "B": "Pain was the number (0 to 10) under the face the child pointed to on the Faces Pain Scale within 1 minute after the needle was removed.",
            "C": "Children in the virtual reality condition rated their pain 2.3 on average, compared with 5.6 in standard care, and the difference was statistically significant. This indicates that playing the virtual reality game made the blood draw hurt less, and the difference was unlikely to be due to chance.",
            "D": "The researchers used informed consent: a research assistant explained the study, each parent signed a consent form, each child agreed on an assent form, and families were told they could stop at any time without affecting the child's care.",
            "E": "The findings may not generalize to adults, because all participants were children aged 8 to 14 at one children's hospital in Texas, and 46% were Hispanic/Latino/a.",
            "F": "This supports gate control theory. Children who played the virtual reality game rated their pain 2.3, compared with 5.6 for standard care, and children watching a cartoon were in between (3.9). Gate control theory says the spinal cord has a gate that can block pain signals and that distraction can close the gate, so the more distracting the activity was, the less pain got through.",
        },
        "r": {
            "A": {"answer": "experiment", "keys": ["experiment"], "clues": ["random", "assign", "manipulat", "independent variable", "condition"],
                  "trap": "naturalistic observation", "trapHint": "The researchers randomly assigned children to virtual reality, a tablet, or standard care, so they manipulated the distraction: that makes it an experiment."},
            "B": {"groups": [["face", "0 to 10", "number"], ["faces pain scale", "pointed", "point", "after the needle", "removed"]],
                  "labels": ["Says it was a number on the faces scale", "Gives how this study measured it (the face the child pointed to right after the needle came out)"]},
            "C": {"nums": ["2.3", "5.6", "3.3"], "meaning": ["pain", "hurt"], "subject": ["virtual", "vr", "standard"]},
            "D": {"eth": [
                {"name": "Institutional review", "keys": ["institutional review", "review board", "irb", "ethics board"], "ev": ["approved", "board"]},
                {"name": "Informed consent", "keys": ["informed consent", "consent", "assent"], "ev": ["signed", "form", "explained", "parent", "agreed"]},
                {"name": "Right to withdraw", "keys": ["withdraw", "stop at any time", "quit", "leave the study"], "ev": ["any time", "anytime", "care", "without"]},
            ], "notIn": ["confid", "debrief"]},
            "E": {"pop": POP + ["younger", "infants", "patients"],
                  "demo": ["8", "14", "10.9", "49%", "51%", "46%", "28%", "18%", "68%", "texas", "one children", "children's hospital"]},
            "F": {"data": ["2.3", "5.6", "3.9", "3.3"], "concept": ["gate", "spinal cord", "distract", "pain signal"]},
        },
    },
    # ------------------------------------------------------------------ 7. placebo energy drink (experiment)
    {
        "id": "placebo",
        "topic": "Research methods, Placebo effect",
        "title": "What You Think Is in Your Drink",
        "sections": [
            ("Introduction", """This study examined whether believing you have had an energy drink changes how energetic you feel and how well you do on a timed math task, even when the drink has no caffeine."""),
            ("Participants", """Participants were 105 undergraduate students at a public university in Colorado who signed up through the psychology department's research website. The study was listed as "Drinks and Problem Solving." Students received 1 hour of course credit. Sessions were held between 1:00 and 4:00 p.m., and participants were asked not to have any caffeine after 9:00 a.m. on the day of their session. Six students who said they had had coffee that afternoon were rescheduled.

Participants ranged in age from 18 to 25 years (mean age = 19.7 years, standard deviation = 1.5 years). The sample was 60% women and 40% men. The race/ethnicity of the participants was reported as follows: 65% White, 17% Hispanic/Latino/a, 8% Asian/Asian American, 4% Black/African American, and 6% multiracial. On a screening survey, 44% said they drank an energy drink at least once a week. Students who reported heart problems or a bad reaction to caffeine were not eligible."""),
            ("Method", """The university's institutional review board approved the study, including its use of deception. Participants were told that the study was about how drinks affect problem solving, that they might drink a beverage containing caffeine, and that they could leave at any time and still receive credit. They then signed a consent form.

Participants were randomly assigned to one of three conditions:
1. Energy drink condition: participants were told they were drinking an energy drink and received a drink with 160 milligrams of caffeine.
2. Placebo condition: participants were told they were drinking an energy drink but received the same drink with no caffeine.
3. Water condition: participants were told they were drinking flavored water and received the same drink with no caffeine.

All drinks were 250 milliliters, were the same color, and were served in a plain cup. For the energy drink and placebo conditions, the researcher poured the drink from a can with a well-known energy drink label. For the water condition, the drink was poured from a plain bottle.

After drinking, participants sat for 20 minutes in a small room with a desk and a window and filled out a questionnaire about their study habits, such as how many hours they studied each week and whether they listened to music while studying. The researcher left the room during this time. They then rated how energetic they felt on a scale from 1 (not at all energetic) to 10 (extremely energetic). Next, they had 5 minutes to solve as many two-digit multiplication problems as they could, such as 47 × 26, without a calculator. Math performance was measured as the number of problems answered correctly. Finally, participants guessed whether their drink had contained caffeine and rated how much they liked its taste.

To make sure the drinks tasted the same, the researchers first asked 20 different students to taste the caffeine and no-caffeine versions; they could not tell them apart better than chance. The same researcher, a graduate student, ran every session and read the same instructions from a script.

At the end of the session, the researcher explained the real purpose of the study, told each participant what their drink had actually contained, and explained why the study could not be described fully at the start."""),
            ("Results and Discussion", """Table: Mean Results for Each Condition
| Condition | Energy rating (1 to 10) | Math problems correct | Guessed the drink had caffeine |
| Energy drink | 7.2 | 14.8 | 89% |
| Placebo | 6.6 | 11.9 | 83% |
| Water | 4.3 | 11.4 | 9% |

Participants in the placebo condition rated themselves as significantly more energetic than participants in the water condition (p < .001), and their ratings were not significantly different from those in the energy drink condition. For math performance, the energy drink condition solved significantly more problems than both other conditions (p < .01), but the placebo and water conditions did not differ significantly.

Weekly energy drink users and nonusers showed the same pattern of results. Participants in the two caffeine-free conditions liked the taste of their drink about as much as participants in the energy drink condition. Four participants said during the debriefing that they had suspected the drink might not be what the label said, but their results were similar to everyone else's, so their data were kept. The researchers noted that the math task lasted only 5 minutes and that the energy rating was taken only once."""),
        ],
        "q": {
            "A": "Identify the research method used in the study.",
            "B": "State the operational definition of math performance in the study.",
            "C": "Describe what the mean energy ratings indicate for the placebo condition as compared to the water condition.",
            "D": AAQ_D,
            "E": AAQ_E,
            "F": "Explain how at least one of the research findings supports or refutes the placebo effect.",
        },
        "model": {
            "A": "The research method is an experiment.",
            "B": "Math performance was the number of two-digit multiplication problems the participant answered correctly in 5 minutes without a calculator.",
            "C": "The placebo condition rated their energy 6.6 on average, compared with 4.3 for the water condition, and the difference was statistically significant. This indicates that people who believed they had an energy drink felt more energetic even though their drink had no caffeine, and the difference was unlikely to be due to chance.",
            "D": "The researchers used debriefing: at the end of the session, the researcher explained the real purpose of the study, told each participant what their drink actually contained, and explained why the study could not be fully described at the start.",
            "E": "The findings may not generalize to older adults, because all participants were college students aged 18 to 25 at one public university in Colorado, and 65% were White.",
            "F": "This partially supports the placebo effect. The placebo condition rated their energy 6.6, almost as high as the energy drink condition (7.2) and much higher than the water condition (4.3), even though the placebo drink had no caffeine. That shows expectations alone made people feel more energetic. But the placebo condition solved about the same number of math problems as the water condition (11.9 vs. 11.4), so expectations changed how people felt, not how they performed.",
        },
        "r": {
            "A": {"answer": "experiment", "keys": ["experiment"], "clues": ["random", "assign", "manipulat", "independent variable", "condition", "placebo"],
                  "trap": "correlational study", "trapHint": "Participants were randomly assigned to what they drank and what they were told, so the researchers manipulated it: that makes it an experiment."},
            "B": {"groups": [["number", "how many", "problems"], ["5 minutes", "five minutes", "multiplication", "two-digit", "correct"]],
                  "labels": ["Says it was the number of problems", "Gives how this study measured it (two-digit multiplication problems correct in 5 minutes)"]},
            "C": {"nums": ["6.6", "4.3", "2.3"], "meaning": ["energ"], "subject": ["placebo", "water", "believ", "told"]},
            "D": {"eth": [
                {"name": "Institutional review", "keys": ["institutional review", "review board", "irb", "ethics board"], "ev": ["approved", "deception", "board"]},
                {"name": "Informed consent", "keys": ["informed consent", "consent"], "ev": ["signed", "form", "told", "caffeine", "explained"]},
                {"name": "Right to withdraw", "keys": ["withdraw", "leave at any time", "stop at any time", "quit", "leave"], "ev": ["any time", "anytime", "credit"]},
                {"name": "Debriefing", "keys": ["debrief"], "ev": ["real purpose", "purpose", "explained", "end", "contained", "actually"]},
            ], "notIn": ["confid", "harm"]},
            "E": {"pop": POP + ["non-students", "energy drink users"],
                  "demo": ["18", "25", "19.7", "60%", "40%", "65%", "17%", "44%", "colorado", "one public", "public university"]},
            "F": {"data": ["6.6", "7.2", "4.3", "11.9", "11.4", "14.8"], "concept": ["placebo", "expect", "believ"]},
        },
    },
    # ------------------------------------------------------------------ 8. hippocampus (case study)
    {
        "id": "hippocampus",
        "topic": "The brain, Hippocampus",
        "title": "Memory After Damage to the Hippocampus",
        "sections": [
            ("Introduction", """This report describes the memory of one man, called M.R. in this report, after an illness damaged the hippocampus on both sides of his brain."""),
            ("Participants", """M.R. is a 58-year-old right-handed man from Michigan who worked as an electrician for 31 years. Three years before this study, he developed a viral infection that caused swelling in his brain. Brain scans taken after he recovered showed damage to the hippocampus on both sides of his brain, with little damage to other areas. He has 12 years of education and lives with his wife, who helps him keep a daily calendar. Before his illness, he coached his grandson's baseball team and enjoyed fishing. Since the illness, he has not been able to return to work, and his wife reports that he often asks the same question several times in an hour. His speech, his vision, and his ability to walk were not affected, and his score on a standard intelligence test was in the average range.

For comparison, the researchers also tested 10 men with no history of brain injury who were similar to M.R. in age (mean age = 57.2 years, range = 52 to 63), years of education, and type of work. Comparison participants were recruited through a community center and were paid $50. M.R. was not paid, but his travel costs were covered."""),
            ("Method", """The hospital's institutional review board approved the study. Because of his memory problems, the study was explained to both M.R. and his wife, and both signed consent forms. The researchers reminded M.R. at the start of each session that he could stop at any time. To protect his privacy, his name and the name of his hometown were not used in this report.

M.R. was tested in six sessions over 2 months, each lasting about 2 hours, in a quiet room at the hospital. The comparison participants each completed one session. Testing included the following tasks:
- Story recall: the researcher read aloud a short story containing 25 details, such as names, places, and events. Participants repeated as much of the story as they could right away (immediate recall) and again 30 minutes later (delayed recall). During the 30 minutes, participants worked on unrelated puzzles. Delayed recall was measured as the number of the 25 story details the participant correctly repeated after 30 minutes.
- Old memories: participants answered questions about events from their own lives before age 40, such as where they went to high school and the name of their first employer. Answers were checked with family members.
- Mirror drawing: participants traced the outline of a star while seeing their hand only in a mirror, for 10 tries each day across 3 days. The number of times they went outside the lines was counted.

The researcher also asked M.R. at each session whether he remembered meeting her before.

Sessions were scheduled in the morning, when M.R.'s wife said he was least tired, and he was offered a break every 30 minutes. A different story was used in each of the six sessions so that M.R. could not improve just from hearing the same story again. The comparison participants heard the first of the six stories."""),
            ("Results and Discussion", """Table: Story Recall Scores (details correctly repeated, out of 25)
| Participant | Immediate recall | Delayed recall (30 minutes) |
| M.R. (average of 6 sessions) | 17 | 1 |
| Comparison group (mean) | 18 | 15 |

M.R.'s immediate recall was close to that of the comparison group, but his delayed recall was far lower than every comparison participant's. In every session, he said he did not remember meeting the researcher, and he did not remember having heard the story before.

M.R. answered 92% of the questions about his life before age 40 correctly, similar to the comparison group (95%). On the mirror drawing task, his errors dropped from 31 on the first day to 9 on the third day, a similar improvement to the comparison group's, even though he said each day that he had never done the task.

When the researcher showed M.R. a photo of herself at the last session and asked who it was, he guessed that she might be a nurse. The researchers noted that M.R. is one person and that his brain damage may not be exactly like damage that happens in other ways, such as from Alzheimer's disease."""),
        ],
        "q": {
            "A": "Identify the research method used in the study.",
            "B": "State the operational definition of delayed recall in the study.",
            "C": "Describe what M.R.'s delayed recall score indicates as compared to the comparison group's mean delayed recall score.",
            "D": AAQ_D,
            "E": AAQ_E,
            "F": "Explain how at least one of the research findings supports or refutes the idea that the hippocampus helps store information into long-term memory.",
        },
        "model": {
            "A": "The research method is a case study.",
            "B": "Delayed recall was the number of the 25 story details that the participant correctly repeated 30 minutes after hearing the story.",
            "C": "M.R. remembered only 1 of the 25 details after 30 minutes, while the comparison group remembered 15 on average. This indicates that M.R. could not hold on to new information over time the way people without brain damage can.",
            "D": "The researchers used informed consent: the study was explained to both M.R. and his wife, both signed consent forms, and M.R. was reminded at each session that he could stop at any time.",
            "E": "The findings may not generalize to other people with memory problems, because the study is about only one person, M.R., a 58-year-old man from Michigan whose damage came from a viral infection, which may differ from damage caused by Alzheimer's disease.",
            "F": "This supports the idea that the hippocampus helps store information into long-term memory. After damage to his hippocampus, M.R. could repeat 17 story details right away but only 1 after 30 minutes, compared with 15 for the comparison group. This shows he could take in new information but could not store it into long-term memory, while his memories from before age 40 (92% correct) were still there.",
        },
        "r": {
            "A": {"answer": "case study", "keys": ["case study"], "clues": ["one", "single", "individual", "in depth", "m.r.", "one man"],
                  "trap": "experiment", "trapHint": "The researchers studied one man in depth and did not assign anyone to conditions; comparing him with 10 other men doesn't make it an experiment. It is a case study."},
            "B": {"groups": [["number", "how many", "details"], ["25", "30 minutes", "thirty minutes", "story"]],
                  "labels": ["Says it was the number of story details", "Gives how this study measured it (details out of 25 repeated 30 minutes later)"]},
            "C": {"nums": ["1 of", "only 1", "15", "1 detail", "one detail", "14"], "meaning": ["remember", "recall", "memory", "store", "hold"], "subject": ["m.r", "comparison", "he "]},
            "D": {"eth": [
                {"name": "Institutional review", "keys": ["institutional review", "review board", "irb", "ethics board"], "ev": ["approved", "board"]},
                {"name": "Informed consent", "keys": ["informed consent", "consent"], "ev": ["signed", "wife", "explained", "form"]},
                {"name": "Right to withdraw", "keys": ["withdraw", "stop at any time", "quit", "leave"], "ev": ["any time", "anytime", "reminded", "session"]},
                {"name": "Confidentiality", "keys": ["confidential", "anonym", "privacy", "name was not", "names were not", "initials", "m.r."], "ev": ["name", "hometown", "m.r.", "not used"]},
            ], "notIn": ["debrief", "harm"]},
            "E": {"pop": POP + ["other patients", "alzheimer", "other people", "women"],
                  "demo": ["58", "one person", "one man", "only one", "single", "michigan", "electrician", "viral", "infection"]},
            "F": {"data": ["17", " 1 ", "only 1", "15", "92%", "1 after", "1 detail"], "concept": ["hippocampus", "long-term", "stor", "memor"]},
        },
    },
    # ------------------------------------------------------------------ 9. phones and noticing (naturalistic observation)
    {
        "id": "phones",
        "topic": "Perception, Attention",
        "title": "Phone Use and Noticing a Street Performer",
        "sections": [
            ("Introduction", """This study observed people walking through a busy downtown square to see whether the way they were using their phones was related to whether they noticed something unusual nearby."""),
            ("Participants", """The researchers observed 412 adults who walked across a large public square in downtown Chicago, Illinois, on weekday afternoons in May. People who appeared to be under 18, people walking in groups of three or more, and people who were running or riding a bike were not counted. Researchers did not record any information that could identify the people they observed.

Based on the 352 people who agreed to answer questions afterward, the sample was 51% women and 49% men, and their reported ages ranged from 18 to 74 years (mean age = 36.5 years). Most (79%) said they walked through the square at least once a week. Researchers did not collect race/ethnicity data. Of those who answered, 64% said they were on their way to or from work, and 22% said they were tourists or visiting the city."""),
            ("Method", """The study was approved by a university's institutional review board. No one was told ahead of time that they were being observed.

During the study, a street performer who regularly worked in the square juggled while riding a unicycle near the center of the square. The performer was not part of the research team, and the researchers did not ask him to do anything differently. He wore a bright red jacket and could be seen from every path across the square.

Two trained observers sat on benches at the edge of the square and chose a person to observe each time someone entered from the north end. For each person, the observers recorded how they were using their phone while crossing:
- Texting or scrolling: looking at a phone screen.
- Talking: talking on a phone, held to the ear or on speaker.
- Music: wearing earbuds but not looking at or talking on a phone.
- No phone: not using a phone at all.

Observations took place on 9 weekday afternoons between 12:00 and 3:00 p.m., only on days with no rain. Before the study, the two observers practiced together for two afternoons until they agreed on nearly every person. The two observers agreed on the category for 96% of people. The observers also recorded how long each person took to cross the square, how many times they changed direction, and whether they bumped into or nearly bumped into another person.

When each person reached the far side of the square, a third researcher stopped them, said she was doing a short university study, and asked whether they would answer two questions. If they agreed, she asked, "Did you see anything unusual while you were walking across the square?" If they said no, she asked, "Did you see the unicycle?" A person was counted as noticing the performer if they said yes to either question. People could say no to the questions or walk away at any time. Those who answered were also asked their age and how often they walked through the square, and they were given a small card thanking them and explaining what the study was about.

The square is about 120 meters across, and people took an average of 1.5 minutes to cross it. The performer stayed in the same part of the square for the whole study and performed for about 2 hours each afternoon, so every person observed walked past while he was riding."""),
            ("Results and Discussion", """Of the 412 people observed, 352 (85%) agreed to answer the questions. The results for these 352 people are shown in the table.

Table: Percentage of People Who Noticed the Performer
| Phone use while crossing | Number of people | Noticed the performer |
| Texting or scrolling | 96 | 31% |
| Talking | 58 | 45% |
| Music | 64 | 61% |
| No phone | 134 | 72% |

People who were texting or scrolling were significantly less likely to notice the performer than people who were not using a phone (p < .001). People who were texting or scrolling also took longer to cross the square and were more likely to nearly bump into someone.

The researchers noted that people who chose to text while walking may differ in other ways from people who did not, such as being in more of a hurry, and that they could not observe people's attention directly."""),
        ],
        "q": {
            "A": "Identify the research method used in the study.",
            "B": "State the operational definition of noticing the performer in the study.",
            "C": "Describe what the percentages of people who noticed the performer indicate for people who were texting or scrolling as compared to people who were not using a phone.",
            "D": AAQ_D,
            "E": AAQ_E,
            "F": "Explain how at least one of the research findings supports or refutes the idea of inattentional blindness.",
        },
        "model": {
            "A": "The research method is naturalistic observation.",
            "B": "A person was counted as noticing the performer if they said yes when asked, at the far side of the square, whether they saw anything unusual or whether they saw the unicycle.",
            "C": "Only 31% of people who were texting or scrolling noticed the performer, compared with 72% of people who were not using a phone, and the difference was statistically significant. This indicates that people looking at their phones were much less likely to notice the unicycle, and the difference was unlikely to be due to chance.",
            "D": "The researchers used confidentiality: the observers did not record any information that could identify the people they observed.",
            "E": "The findings may not generalize to people in small towns or quieter places, because everyone was observed in one busy square in downtown Chicago, and 79% walked through the square at least once a week.",
            "F": "This supports the idea of inattentional blindness. Only 31% of people who were texting or scrolling noticed the performer on a unicycle, compared with 72% of people with no phone, even though he could be seen from every path. This shows that when people's attention was directed at their phones, they failed to see a visible object that was right there.",
        },
        "r": {
            "A": {"answer": "naturalistic observation", "keys": ["naturalistic"], "clues": ["observ", "natural", "public", "not manipulat", "recorded"],
                  "trap": "experiment", "trapHint": "The researchers didn't assign anyone to use a phone or set up the performer; they observed people in a natural setting, so it is naturalistic observation."},
            "B": {"groups": [["said yes", "yes", "answered", "asked"], ["unusual", "unicycle", "far side", "question"]],
                  "labels": ["Says it was based on the person saying yes", "Gives how this study measured it (yes to seeing anything unusual or the unicycle when asked afterward)"]},
            "C": {"nums": ["31%", "72%", "41"], "meaning": ["notic", "see", "saw", "aware", "attention"], "subject": ["text", "scroll", "phone"]},
            "D": {"eth": [
                {"name": "Institutional review", "keys": ["institutional review", "review board", "irb", "ethics board"], "ev": ["approved", "board", "university"]},
                {"name": "Confidentiality", "keys": ["confidential", "anonym", "identify", "privacy", "private", "no names"], "ev": ["identify", "record", "information", "not record", "did not record"]},
                {"name": "Informed consent", "keys": ["informed consent", "consent", "agreed", "asked whether"], "ev": ["agree", "asked", "say no", "questions"]},
                {"name": "Right to withdraw", "keys": ["withdraw", "walk away", "say no", "decline", "refuse"], "ev": ["any time", "anytime", "walk away", "no"]},
            ], "notIn": ["debrief", "harm"]},
            "E": {"pop": POP + ["small town", "rural", "quieter", "other cities", "children"],
                  "demo": ["chicago", "downtown", "one square", "79%", "51%", "49%", "18", "74", "36.5", "85%", "illinois", "weekday"]},
            "F": {"data": ["31%", "72%", "45%", "61%"], "concept": ["inattentional", "attention", "notic", "visible", "fail"]},
        },
    },
    # ------------------------------------------------------------------ 10. nose clip and flavor (experiment, within-subjects)
    {
        "id": "noseclip",
        "topic": "Smell and taste, Sensory interaction",
        "title": "Holding Your Nose and Naming Flavors",
        "sections": [
            ("Introduction", """This study examined whether blocking the sense of smell changes how well people can identify the flavors of foods they are tasting."""),
            ("Participants", """Participants were 48 students at a community college in Washington State who signed up after a short presentation in their introductory psychology classes. Students received extra credit for taking part. The study took place in the spring semester, in a small room in the science building. Students with food allergies, a cold or stuffy nose on the day of testing, or a known loss of smell or taste were not eligible, and 6 students who signed up were turned away for these reasons.

Participants ranged in age from 18 to 41 years (mean age = 22.6 years, standard deviation = 5.3 years). The sample was 63% women and 37% men. The race/ethnicity of the participants was reported as follows: 52% White, 19% Asian/Asian American, 15% Hispanic/Latino/a, 8% Black/African American, and 6% multiracial. Nine participants (19%) said they smoked or vaped. Participants also reported how often they ate jelly beans; most (71%) said less than once a month."""),
            ("Method", """The college's institutional review board approved the study. Students were told that they would taste small candies, some of which might be unfamiliar flavors, and that they could spit out any candy or stop at any time without losing the extra credit. Every student signed a consent form. Each participant was given a code number, which was used on all score sheets.

Each participant tasted 20 jelly beans, one at a time, while wearing a blindfold. There were 10 flavors: cherry, lemon, grape, orange, watermelon, cinnamon, coconut, licorice, root beer, and buttered popcorn. Each participant tasted each flavor twice: once while wearing a soft foam nose clip that blocked air from passing through the nose, and once without the clip. This is called a "within-subjects" design: every participant was tested in both conditions, so each person was compared with themselves. Half of the participants did the nose clip trials first, and half did them second, chosen at random. The flavors were given in a random order within each set of 10.

For each jelly bean, participants chewed for 10 seconds and then named the flavor out loud. Flavor identification was measured as the number of the 10 flavors a participant named correctly in each condition. Answers such as "lime" for lemon were counted as wrong. Participants also rated how sweet each jelly bean tasted from 1 (not sweet) to 9 (extremely sweet). A research assistant wrote down each answer, and a second assistant later checked the score sheets against audio recordings of the session. Between jelly beans, participants rinsed their mouths with water, and there was a 5-minute break between the two sets, during which participants filled out a short questionnaire about their favorite foods.

Before the study, the researchers asked a separate group of 15 students to name the 10 flavors from their labels to make sure that all 10 were familiar; every flavor was recognized by at least 13 of the 15 students. All jelly beans came from the same bag, and the testing room was kept free of food smells. Sessions lasted about 40 minutes."""),
            ("Results and Discussion", """Table: Mean Results With and Without the Nose Clip
| Measure | Without nose clip | With nose clip |
| Flavors correctly named (out of 10) | 8.1 | 3.4 |
| Sweetness rating (1 to 9) | 6.2 | 6.0 |

Participants correctly named significantly fewer flavors while wearing the nose clip than without it (p < .001). With the clip, many participants said that the jelly beans tasted "just sweet." Sweetness ratings did not differ significantly between the two conditions.

Cinnamon and licorice were the flavors most often named correctly with the nose clip. Participants who smoked or vaped named slightly fewer flavors in both conditions, but the difference was not statistically significant. Whether participants did the nose clip trials first or second did not change the results. When participants were wrong without the nose clip, they usually named a similar flavor, such as orange for lemon. When they were wrong with the nose clip, they most often said "I don't know" or named a flavor that was not on the list. Women and men named about the same number of flavors in each condition. The researchers noted that jelly beans have strong artificial flavors and that results might differ with everyday foods."""),
        ],
        "q": {
            "A": "Identify the research method used in the study.",
            "B": "State the operational definition of flavor identification in the study.",
            "C": "Describe what the mean number of flavors correctly named indicates for the nose clip condition as compared to the no nose clip condition.",
            "D": AAQ_D,
            "E": AAQ_E,
            "F": "Explain how at least one of the research findings supports or refutes the idea of sensory interaction.",
        },
        "model": {
            "A": "The research method is an experiment.",
            "B": "Flavor identification was the number of the 10 jelly bean flavors that a participant named correctly, after chewing each one for 10 seconds while blindfolded.",
            "C": "With the nose clip, participants correctly named 3.4 flavors on average, compared with 8.1 without it, and the difference was statistically significant. This indicates that people could identify far fewer flavors when their sense of smell was blocked, and the difference was unlikely to be due to chance.",
            "D": "The researchers used confidentiality: each participant was given a code number, which was used on all score sheets instead of their name.",
            "E": "The findings may not generalize to all adults, because all participants were 48 community college students in Washington State aged 18 to 41, and 63% were women.",
            "F": "This supports the idea of sensory interaction. Participants named 8.1 flavors without the nose clip but only 3.4 with it, while sweetness ratings stayed about the same (6.2 vs. 6.0). This shows that blocking smell did not stop the tongue from tasting sweetness, but it made it much harder to tell flavors apart, because smell influences taste.",
        },
        "r": {
            "A": {"answer": "experiment", "keys": ["experiment"], "clues": ["within-subjects", "within subjects", "both conditions", "manipulat", "independent variable", "nose clip", "random"],
                  "trap": "case study", "trapHint": "The researchers manipulated whether the nose was blocked and compared each person with themselves (a within-subjects design), so it is an experiment."},
            "B": {"groups": [["number", "how many"], ["10 flavors", "ten flavors", "of the 10", "out of 10", "named correctly", "correctly named", "jelly bean"]],
                  "labels": ["Says it was the number of flavors", "Gives how this study measured it (how many of the 10 jelly bean flavors were named correctly)"]},
            "C": {"nums": ["3.4", "8.1", "4.7"], "meaning": ["flavor", "identif", "name", "smell"], "subject": ["nose clip", "clip", "blocked"]},
            "D": {"eth": [
                {"name": "Institutional review", "keys": ["institutional review", "review board", "irb", "ethics board"], "ev": ["approved", "board"]},
                {"name": "Informed consent", "keys": ["informed consent", "consent"], "ev": ["signed", "form", "told", "candies", "explained"]},
                {"name": "Right to withdraw", "keys": ["withdraw", "stop at any time", "spit out", "quit", "leave"], "ev": ["any time", "anytime", "extra credit", "without losing"]},
                {"name": "Confidentiality", "keys": ["confidential", "anonym", "code number", "privacy", "private"], "ev": ["code", "number", "score sheet", "name"]},
            ], "notIn": ["debrief", "harm"]},
            "E": {"pop": POP + ["smokers", "children"],
                  "demo": ["48", "18", "41", "22.6", "63%", "37%", "52%", "19%", "washington", "community college"]},
            "F": {"data": ["8.1", "3.4", "6.2", "6.0", "4.7"], "concept": ["sensory interaction", "smell", "taste", "sense"]},
        },
    },
]
