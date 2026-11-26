"""EBQ sets 2 to 10 (fictional studies written for this kit). Same format and rules as items.py.
The sources never name the psychology concepts the model answers apply (on the real exam, a concept that
appears in the sources doesn't earn the application point), and every concept used is a card in the kit."""

Q = "Using the sources provided, develop and justify an argument about "

EBQ_MORE = [
    # ------------------------------------------------------------------ 2. school start times
    {
        "id": "starttimes",
        "topic": "Sleep, Circadian rhythm",
        "title": "School Start Times",
        "question": Q + "whether high schools should start later in the morning.",
        "topicWords": ["start", "later", "school", "morning", "sleep"],
        "sources": [
            ("Sleep Before and After a Later Start Time", """## Introduction
In this study, researchers examined whether moving a high school's start time later changes how much students sleep on school nights.

## Participants
Participants were 178 students at two public high schools in Seattle, Washington. Students were recruited through their biology classes and received a $40 gift card for completing both parts of the study. They ranged in age from 14 to 18 years (mean age = 15.8 years). The sample was 56% girls and 44% boys. Researchers did not report race/ethnicity data for the participants.

## Method
Both schools moved their start time from 7:50 a.m. to 8:45 a.m. at the beginning of a new school year. Students in the study were measured in the spring before the change and again in the spring after the change.

Each time, students wore a wrist monitor for two weeks that recorded when they fell asleep and woke up. Students also kept a daily diary of their bedtime, caffeine use, and any naps, and rated how sleepy they felt during their first class from 1 (wide awake) to 5 (struggling to stay awake). The schools provided students' grades in biology for the same semesters, along with attendance records.

The school district made the change after a year of meetings with parents and teachers. Bus schedules were changed so that elementary schools started earlier and high schools later. After-school sports practices were moved 30 minutes later, and the district added lights to two practice fields. Students who changed schools, or who did not wear the monitor for at least 10 school nights each time, were not included; 14 students were removed for these reasons.

## Results and Discussion
After the change, students slept a median of 34 minutes longer on school nights (7 hours 24 minutes compared with 6 hours 50 minutes). Students did not go to bed later after the change: average bedtime moved only 3 minutes later. Instead, students woke up later.

| Measure | Before the change | After the change |
| Sleep on school nights | 6 h 50 min | 7 h 24 min |
| Sleepiness in first class (1 to 5) | 3.6 | 2.9 |
| Biology grade (out of 100) | 77.5 | 81.9 |
| First-period absences per student | 4.1 | 2.7 |

Students' biology grades were significantly higher after the change (p = .01), and first-period absences dropped. Students at one of the two schools reported less use of caffeine after the change, but the difference was not statistically significant."""),
            ("A Survey of Teens' Sleep and School Times", """## Introduction
In this study, researchers examined the relationship between school start times and how much sleep teens get, using a survey of students across several states.

## Participants
The survey was completed by 9,089 students in grades 9 through 12 at 29 high schools in Colorado, Minnesota, and Wyoming. Schools were selected because they started at different times, ranging from 7:30 a.m. to 8:55 a.m. Participants ranged in age from 13 to 19 years. The sample was 51% girls and 49% boys. The race/ethnicity of the participants was 71% White, 14% Hispanic/Latino/a, 6% Black/African American, 4% Asian/Asian American, and 5% other.

## Method
Students completed an online survey during class. The survey asked what time they usually went to bed and woke up on school nights, how often they fell asleep in class, how often they drank caffeinated drinks, and how often they felt sad or hopeless during the past two weeks. It also asked whether they had a job, played sports, or drove to school. Students who drove reported whether they had been in a car crash in the past year.

Each school's principal agreed to take part, and parents were sent a letter that allowed them to keep their child out of the survey. Students could skip any question. The survey took about 30 minutes and was given during the same two months at every school. Answers were anonymous: no names or student ID numbers were collected. Schools received a summary of their own results the following year.

## Results and Discussion
Students at schools that started at 8:30 a.m. or later were significantly more likely to get 8 or more hours of sleep on school nights than students at schools that started before 8:00 a.m. (p < .001).

| School start time | Students getting 8 or more hours of sleep | Students who fell asleep in class at least once a week |
| Before 8:00 a.m. | 34% | 22% |
| 8:00 to 8:29 a.m. | 43% | 18% |
| 8:30 a.m. or later | 60% | 13% |

At every start time, students who slept less were more likely to report feeling sad or hopeless and to drink more caffeinated drinks. Among students who drove to school, those at schools starting before 8:00 a.m. reported more car crashes in the past year. The researchers noted that schools that start later may differ in other ways, such as being in different communities."""),
            ("When Do Teens Feel Most Awake?", """## Introduction
In this study, researchers compared the times of day when teens and adults feel most alert and perform best on a simple attention task.

## Participants
Participants were 60 teens aged 15 to 17 (mean age = 16.1 years) and 60 adults aged 35 to 50 (mean age = 42.3 years) in Providence, Rhode Island. Each teen took part with a parent's written permission. Participants were recruited through flyers and were paid $50. The teen group was 52% female, and the adult group was 55% female. Researchers did not report race/ethnicity data for the participants.

## Method
For one week during the school year, participants received a text message at 7:30 a.m., 10:00 a.m., 1:00 p.m., 4:00 p.m., and 8:00 p.m. each day. At each text, they rated how alert they felt from 1 (very sleepy) to 10 (very alert) and completed a 2-minute attention task on their phones, in which they tapped the screen as quickly as possible whenever a red circle appeared. The researchers counted the number of times a participant missed a circle or tapped too slowly (more than half a second).

Participants also wore a wrist monitor that recorded when they fell asleep and woke up, and on one weekend night they collected a saliva sample every hour from 7:00 p.m. until they went to bed, which was later tested for melatonin. Each participant chose their own bedtime.

## Results and Discussion
Teens rated themselves as least alert at 7:30 a.m., with an average rating of 3.8, and most alert at 8:00 p.m., with an average rating of 7.4. Adults were most alert at 10:00 a.m. (7.6) and least alert at 8:00 p.m. (5.1).

| Time | Teens' missed or slow taps | Adults' missed or slow taps |
| 7:30 a.m. | 9.2 | 4.1 |
| 1:00 p.m. | 5.0 | 3.8 |
| 8:00 p.m. | 3.6 | 5.7 |

Teens' melatonin levels began to rise at an average of 10:40 p.m., compared with 8:50 p.m. for adults (p < .001). On school nights, teens fell asleep at an average of 11:15 p.m. and slept 6 hours 55 minutes."""),
        ],
        "model": {
            "A": "High schools should start later in the morning because later start times help teens get more sleep and do better in school.",
            "Bi": "After two high schools moved their start time from 7:50 to 8:45 a.m., students slept 34 minutes longer on school nights and their biology grades rose from 77.5 to 81.9 (Source 1).",
            "Bii": "This supports my claim because teens' circadian rhythm, the body's 24-hour biological clock, makes most teens evening-energized, so they fall asleep late no matter when school starts. Starting school later lets them wake up later and get the sleep their clock allows, which helps them learn.",
            "Ci": "Teens missed or tapped too slowly 9.2 times on an attention task at 7:30 a.m. but only 3.6 times at 8:00 p.m., and they were least alert in the early morning (Source 3).",
            "Cii": "This supports my claim because sleep loss diminishes attentional focus and memory consolidation, so teens who are short on sleep and tested early in the morning pay attention less well and remember less of what they are taught. A later start time means students are in class when they can focus.",
        },
    },
    # ------------------------------------------------------------------ 3. energy drinks
    {
        "id": "energydrinks",
        "topic": "Drugs, Caffeine",
        "title": "Energy Drinks and Students",
        "question": Q + "whether energy drinks help or harm students.",
        "topicWords": ["energy drink", "student", "help", "harm", "caffeine"],
        "sources": [
            ("Energy Drinks and a Late-Night Study Session", """## Introduction
In this study, researchers tested whether an energy drink helps college students stay focused during a late-night study session.

## Participants
Participants were 90 undergraduate students (49 women, 41 men) at a public university in Georgia who received course credit. They ranged in age from 18 to 24 years (mean age = 19.9 years). Students who reported heart problems or anxiety disorders were not eligible. Researchers did not report race/ethnicity data for the participants.

## Method
Sessions began at 10:00 p.m. in a campus computer lab. Students were randomly assigned to drink either an energy drink containing 160 milligrams of caffeine or a drink that looked and tasted the same but contained no caffeine. Neither the students nor the researcher handing out the drinks knew which drink each student received.

Thirty minutes after drinking, students read a 3,000-word textbook passage about ocean currents for 40 minutes and then took a 20-question multiple-choice quiz on it. They also completed a 10-minute task in which they watched a screen and pressed a key whenever a letter appeared twice in a row. Researchers counted the number of misses. At midnight, students went home. The next morning, each student reported what time they fell asleep and how well they slept.

The study took place on weeknights in October, and each session included 6 to 10 students seated at separate computers with dividers between them. Students were asked not to have any caffeine after noon on the day of their session and not to nap that afternoon. Phones were placed in a basket at the front of the room. Before drinking, students rated how sleepy they felt, and the two groups did not differ.

## Results and Discussion
Students who had the energy drink missed significantly fewer letters on the attention task than students who had the drink with no caffeine (p < .01).

| Measure | Energy drink | No caffeine |
| Missed letters on the attention task | 6.1 | 10.8 |
| Quiz score (out of 20) | 14.2 | 13.6 |
| Time to fall asleep after getting home (minutes) | 71 | 29 |

Quiz scores were not significantly different between the two groups. However, students who had the energy drink took significantly longer to fall asleep that night (p < .001), and 38% rated their sleep as poor, compared with 12% in the no-caffeine group."""),
            ("Daily Energy Drink Use and Headaches", """## Introduction
In this study, researchers followed students who drank energy drinks every day to see what happened when they stopped for several days.

## Participants
Participants were 46 high school seniors (ages 17 to 18) in Ohio who reported drinking at least one energy drink every school day for at least three months. Each student took part with a parent's written permission and received a $30 gift card. The sample was 39% girls and 61% boys. Researchers did not report race/ethnicity data for the participants.

## Method
For one week, students continued to drink energy drinks as usual. Each evening, they reported how many energy drinks they had, how many hours they slept, and whether they had a headache, felt tired, or had trouble concentrating, using a 0 (none) to 4 (severe) scale for each.

Students then agreed to drink no energy drinks or other caffeinated drinks for the next five school days. A researcher checked in by text each day. Students continued the same evening reports. On the first and fifth days without energy drinks, students took a 15-minute math quiz in study hall. Their scores were compared with a math quiz taken during the first week.

Before the study, the researchers met with each student and a parent to explain the schedule, and students practiced filling out the evening report on their phones. Students were allowed to take pain relievers if they had a headache, but they were asked to record it. Students who played a sport during the study continued their usual practices. The math quizzes had different problems each time but were made to be equally difficult.

## Results and Discussion
During the usual week, students drank an average of 1.8 energy drinks a day. Many said they had needed more energy drinks over the past few months to feel the same boost they used to get from one.

| Measure | Usual week | First day without | Fifth day without |
| Headache (0 to 4) | 0.6 | 2.7 | 1.1 |
| Tiredness (0 to 4) | 1.4 | 3.1 | 1.9 |
| Math quiz score (out of 25) | 18.3 | 14.9 | 18.0 |

On the first day without energy drinks, headaches and tiredness were significantly higher than during the usual week (p < .001), and math scores were significantly lower. By the fifth day, scores were close to the usual week. Seven students (15%) drank an energy drink before the five days were over and were not included in the results."""),
            ("Energy Drinks and Heart Rate During Exams", """## Introduction
In this study, researchers measured whether students who drink energy drinks during final exam week have a higher heart rate and feel more nervous.

## Participants
Participants were 214 college students at a private university in New York who answered an email invitation sent to all students. They ranged in age from 18 to 23 years (mean age = 20.2 years). The sample was 58% women and 42% men. Students received $15 for taking part. Researchers did not report race/ethnicity data for the participants.

## Method
During final exam week, students wore a fitness watch that recorded their heart rate every minute. Each evening, they reported how many energy drinks, cups of coffee, and other caffeinated drinks they had that day, and rated how nervous they had felt from 1 (calm) to 7 (extremely nervous). They also reported the number of hours they slept.

Students were sorted into three groups based on their average number of energy drinks per day during the week: none, one, or two or more.

Before exam week, students wore the watch for two days so they could get used to it, and those data were not used. Resting heart rate was the average heart rate during the first 10 minutes after the student woke up each morning, before getting out of bed. Students who reported smoking or vaping were included, and their results were similar to those of other students.

## Results and Discussion
| Energy drinks per day | Number of students | Resting heart rate (beats per minute) | Nervousness (1 to 7) | Hours of sleep |
| None | 118 | 68 | 3.9 | 6.9 |
| One | 61 | 73 | 4.4 | 6.4 |
| Two or more | 35 | 81 | 5.3 | 5.6 |

Students who drank two or more energy drinks a day had significantly higher resting heart rates and higher nervousness ratings than students who drank none (p < .001). They also slept significantly less. Eleven students in the two or more group reported a racing or pounding heartbeat at least once during the week, compared with two students in the none group.

The researchers noted that students who were more stressed about exams may have chosen to drink more energy drinks."""),
        ],
        "model": {
            "A": "Energy drinks harm students more than they help, because the short boost in focus does not improve learning and leads to poor sleep and dependence.",
            "Bi": "Students who drank an energy drink at 10:00 p.m. missed fewer letters on an attention task (6.1 vs. 10.8), but their quiz scores were about the same (14.2 vs. 13.6) and they took 71 minutes to fall asleep compared with 29 minutes (Source 1).",
            "Bii": "This supports my claim because caffeine is a stimulant, a drug that excites the central nervous system. That made students more alert for a short time, but the same stimulant effect kept them awake long after they were done studying, so they lost sleep without learning any more.",
            "Ci": "Seniors who drank about 1.8 energy drinks a day had headaches rated 2.7 and math quiz scores of 14.9 on their first day without them, compared with headaches of 0.6 and scores of 18.3 during a usual week (Source 2).",
            "Cii": "This supports my claim because regular energy drink users developed tolerance, needing more drinks to get the same boost, and showed withdrawal, the discomfort and distress that follow stopping a drug, when they quit. This shows that students can become dependent and do worse in school on days they go without.",
        },
    },
    # ------------------------------------------------------------------ 4. exercise and mood
    {
        "id": "exercisemood",
        "topic": "Depression, Anxiety, Health",
        "title": "Exercise and Mood",
        "question": Q + "whether regular exercise reduces symptoms of depression and anxiety.",
        "topicWords": ["exercise", "depress", "anxi", "symptom", "reduce"],
        "sources": [
            ("A Walking Program for Adults With Depression", """## Introduction
In this study, researchers tested whether a 12-week walking program reduces symptoms of depression in adults diagnosed with major depressive disorder.

## Participants
Participants were 120 adults (74 women, 46 men) aged 25 to 60 years (mean age = 41.6 years) who were patients at three community health clinics in Arizona. All had been diagnosed with major depressive disorder by a doctor. Adults who already exercised more than once a week, or who had a medical condition that made walking unsafe, were not eligible. The race/ethnicity of the participants was 48% White, 33% Hispanic/Latino/a, 10% Native American, 6% Black/African American, and 3% other.

## Method
Participants were randomly assigned to one of two groups. The walking group walked briskly for 40 minutes, three times a week, for 12 weeks, in small groups led by a trainer. The control group received phone calls from a researcher every two weeks and were told they could start the walking program after the study. Participants in both groups continued any treatment they were already receiving.

Before the program and at the end of 12 weeks, a psychologist who did not know which group each participant was in rated each participant's depression using a 17-item interview. Scores range from 0 to 52, with higher scores meaning more severe depression.

The walking sessions took place on indoor tracks at local recreation centers in the morning and evening so that participants could choose a time that fit their work schedules. Each participant wore a step counter, and trainers recorded attendance. Participants in the walking group were asked not to change other parts of their daily routine, such as their diet. The study was approved by the clinics' review board, and every participant signed a consent form.

## Results and Discussion
| Group | Depression score before | Depression score after 12 weeks |
| Walking | 21.4 | 12.6 |
| Control | 20.9 | 18.7 |

Depression scores dropped significantly more in the walking group than in the control group (p < .001). In the walking group, 42% of participants had a score under 8 at the end of the study, compared with 15% of the control group. Participants who attended at least 30 of the 36 walking sessions improved the most. Nine participants in the walking group stopped attending before the end of the program."""),
            ("Exercise and Feeling Calmer the Same Day", """## Introduction
In this study, researchers examined whether college students feel less anxious on days when they exercise.

## Participants
Participants were 88 undergraduate students at a university in Wisconsin who received course credit. They ranged in age from 18 to 22 years (mean age = 19.4 years). The sample was 64% women and 36% men. Researchers did not report race/ethnicity data for the participants.

## Method
For 21 days, students received a text message at 9:00 p.m. with a short survey. Each evening they reported whether they had exercised that day for at least 20 minutes (for example, running, lifting weights, playing a sport, or biking), how many hours they had slept the night before, and how anxious they had felt that day on a scale from 1 (not at all) to 10 (extremely). They also rated how many stressful events they had had that day, such as an exam or an argument with a friend.

Researchers compared each student's anxiety ratings on days when they exercised with their own ratings on days when they did not.

Before the study, students attended a 20-minute meeting where a researcher explained the survey and answered questions. Students who missed more than four of the evening surveys were not included, which removed 7 students. Students were asked to answer each survey on their own phone and were not allowed to fill in missed days later. The study took place during the middle of the fall semester, between the first exams and Thanksgiving break.

## Results and Discussion
Students exercised on an average of 9 of the 21 days. On days when they exercised, students rated their anxiety at an average of 3.9, compared with 5.2 on days when they did not exercise. This difference was statistically significant (p < .001) and appeared even on days with the same number of stressful events.

| Type of day | Average anxiety (1 to 10) |
| Exercised, few stressful events | 3.4 |
| Exercised, many stressful events | 4.7 |
| Did not exercise, few stressful events | 4.6 |
| Did not exercise, many stressful events | 6.3 |

Students who slept more also reported less anxiety the next day. The researchers noted that students chose for themselves which days to exercise, so they may have exercised more on days when they already felt calmer."""),
            ("Fitness and Mood in Older Adults", """## Introduction
In this study, researchers examined whether older adults who are more physically fit report fewer symptoms of depression.

## Participants
Participants were 1,240 adults aged 65 to 84 years (mean age = 72.3 years) living in Maine and Vermont. They were randomly selected from state health records and invited by mail, and 61% of those invited agreed to take part. The sample was 55% women and 45% men. The race/ethnicity of the participants was 94% White, 2% Black/African American, 2% Hispanic/Latino/a, and 2% other.

## Method
Each participant visited a community center for a 90-minute appointment. Fitness was measured as the distance each person could walk in 6 minutes on an indoor track. Participants also completed a 15-item questionnaire about depressive symptoms over the past week, such as feeling that life was empty or that they were not as happy as most people. Scores range from 0 to 15, with higher scores meaning more symptoms. They also reported how often they saw friends or family and whether they had any long-term illnesses.

Trained staff measured the walking distance and gave the same instructions to every participant: walk as far as you comfortably can in 6 minutes, and rest if you need to. A nurse checked each person's blood pressure before the walk, and 23 people did not walk because their blood pressure was too high; they were not included. Appointments were offered on weekdays and Saturdays, and transportation was provided for participants who needed it.

## Results and Discussion
Walking distance was negatively correlated with depressive symptom scores (r = -.31, p < .001). People who walked farther in 6 minutes tended to report fewer symptoms of depression.

| Walking distance in 6 minutes | Mean depressive symptom score (0 to 15) |
| Less than 350 meters | 5.8 |
| 350 to 450 meters | 3.9 |
| More than 450 meters | 2.4 |

The relationship was smaller, but still statistically significant, after the researchers accounted for long-term illnesses and how often people saw friends and family. The researchers noted that people who feel depressed may be less likely to stay active, so the study cannot show which came first."""),
        ],
        "model": {
            "A": "Regular exercise reduces symptoms of depression and anxiety, so people with these symptoms should exercise several times a week.",
            "Bi": "Adults with major depressive disorder who walked for 40 minutes three times a week for 12 weeks saw their depression scores drop from 21.4 to 12.6, while the control group only went from 20.9 to 18.7 (Source 1).",
            "Bii": "This supports my claim because exercise causes the brain to release endorphins, the brain's natural painkillers that relieve pain and stress. Walking regularly gave participants that natural boost to their mood, which helped reduce their depression.",
            "Ci": "Students rated their anxiety 3.9 on days when they exercised for at least 20 minutes, compared with 5.2 on days when they did not exercise (Source 2).",
            "Cii": "This supports my claim because exercise works as emotion-focused coping: it doesn't change the stressor, but it helps people regulate their negative emotions. That is why students felt less anxious on days they exercised even when they had just as many stressful events (4.7 vs. 6.3 on stressful days).",
        },
    },
    # ------------------------------------------------------------------ 5. therapy vs medication
    {
        "id": "therapy",
        "topic": "Treatment, Depression",
        "title": "Talk Therapy and Medication for Depression",
        "question": Q + "whether a therapy that changes how people think is as effective as medication for treating depression.",
        "topicWords": ["therapy", "medication", "effective", "depress", "treat"],
        "sources": [
            ("Therapy Versus Medication for 16 Weeks", """## Introduction
In this study, researchers compared a talk therapy that teaches people to change their thinking with an antidepressant medication for adults with depression.

## Participants
Participants were 240 adults (157 women, 83 men) aged 18 to 65 years (mean age = 39.8 years) who had been diagnosed with major depressive disorder at two university clinics in Pennsylvania. People who had bipolar disorder, who were already in treatment, or who had thoughts of harming themselves that required hospital care were not eligible. The race/ethnicity of the participants was 76% White, 15% Black/African American, 5% Asian/Asian American, and 4% other.

## Method
Participants were randomly assigned to one of three groups for 16 weeks:
1. Therapy group: weekly 50-minute sessions with a therapist. Therapists taught participants to notice their negative ideas about themselves, their lives, and their future, to check whether those ideas were accurate, and to replace them with more balanced ones. Participants also scheduled small enjoyable activities each week.
2. Medication group: a daily antidepressant pill that increases the activity of a mood-related brain chemical, with a doctor's visit every two weeks.
3. Pill group: a daily pill with no active ingredient, with the same doctor's visits. Participants in groups 2 and 3 did not know which pill they were taking.

A psychologist who did not know which group each participant was in rated depression using a 17-item interview. Scores range from 0 to 52.

Therapists had at least five years of experience and followed a written guide for each session, and a supervisor listened to recordings of some sessions to check that the guide was being followed. Participants in all three groups were told that they could leave the study at any time, and anyone whose depression got much worse was referred for other care. Participants were paid $20 for each assessment visit.

## Results and Discussion
| Group | Depression score before | Depression score at 16 weeks | Percent who improved by half or more |
| Therapy | 23.1 | 11.8 | 58% |
| Medication | 23.4 | 11.2 | 58% |
| Inactive pill | 22.9 | 16.7 | 25% |

Both the therapy group and the medication group improved significantly more than the inactive pill group (p < .01). The therapy and medication groups did not differ significantly from each other. Twelve participants in the medication group stopped taking the pill because of side effects, such as nausea or trouble sleeping."""),
            ("What Happened After Treatment Ended", """## Introduction
In this study, researchers followed the participants who had improved in a treatment study to see who stayed well after treatment ended.

## Participants
Participants were 104 adults from the study described in Source 1 whose depression scores had dropped by at least half after 16 weeks of either therapy or medication. Their mean age was 40.6 years, and 68% were women. They continued to receive $25 for each follow-up visit.

## Method
After the 16 weeks, participants in the therapy group stopped attending sessions. Participants in the medication group were randomly split: half continued taking the medication, and half were switched, without being told, to a pill with no active ingredient.

Every two months for one year, a psychologist interviewed each participant. A relapse was counted when a participant's depression score rose above 14 for two visits in a row, or when they needed to start treatment again. Participants were told that they could leave the study at any time and would be helped to find treatment if their depression returned.

The psychologists who did the interviews did not know which group each participant had been in. Participants were asked at each visit whether they had started any new treatment, such as seeing a counselor, and 9 participants said they had; their results were included. Visits lasted about 45 minutes and were held at the same clinics as the original study. Participants who moved away were interviewed by video, and 6 participants could not be reached by the end of the year.

## Results and Discussion
| Group during the follow-up year | Number of participants | Percent who relapsed within one year |
| Had therapy, then stopped | 35 | 31% |
| Kept taking medication | 34 | 47% |
| Stopped medication | 35 | 76% |

Participants who had received therapy were significantly less likely to relapse than those who stopped medication (p < .001), and they relapsed at a similar rate to those who kept taking the medication. Many participants from the therapy group said they still used what they learned, such as checking whether a negative idea was true."""),
            ("Brain Activity Before and After Treatment", """## Introduction
In this study, researchers used brain scans to compare changes in the brain after therapy or medication for depression.

## Participants
Participants were 38 adults with major depressive disorder at a hospital in Toronto, Canada. They ranged in age from 22 to 58 years (mean age = 37.5 years), and 61% were women. Researchers did not report race/ethnicity data for the participants.

## Method
Participants chose whether to receive weekly therapy sessions that focused on changing negative thinking or a daily antidepressant medication. Twenty chose therapy and 18 chose medication. Before treatment and after 15 weeks, each participant had a PET scan, which shows how active different brain areas are. During the scan, participants rested quietly with their eyes closed. They also completed a 21-item depression questionnaire; scores range from 0 to 63.

The medication group took the same type of antidepressant pill as in Source 1, and the therapy group met with one of three therapists for 15 to 20 weekly sessions. PET scans took about one hour and were done at the same time of day before and after treatment. Each participant gave written consent after a doctor explained the small amount of radiation involved in a PET scan. Participants who did not finish treatment, 6 in all, were not included in the results, and every participant was paid $100 for each scan.

## Results and Discussion
| Group | Depression questionnaire before | Depression questionnaire after 15 weeks |
| Therapy | 27.3 | 13.5 |
| Medication | 28.1 | 14.2 |

Both groups improved by about the same amount. However, the brain changes were different. In the therapy group, activity changed most in areas at the front of the brain involved in planning and thinking about oneself. In the medication group, activity changed most in deeper areas of the brain involved in emotion. Within each group, the people whose depression improved the most also showed the largest brain changes. Five participants in the medication group reported side effects such as dry mouth or trouble sleeping, and none in the therapy group did. The researchers noted that participants chose their own treatment, so people who chose therapy may have been different from those who chose medication, and that the study included only 38 people."""),
        ],
        "model": {
            "A": "A therapy that changes how people think is as effective as medication for treating depression and works better at preventing depression from coming back.",
            "Bi": "After 16 weeks, the therapy group's depression scores dropped from 23.1 to 11.8 and the medication group's from 23.4 to 11.2, and 58% of each group improved by half or more (Source 1).",
            "Bii": "This supports my claim because Beck's cognitive theory says depressed people develop a negative cognitive triad: negative thoughts about themselves, their world, and their future. Therapy that teaches people to check and replace those negative ideas fixes the faulty thinking behind depression, so it helped as much as the pill.",
            "Ci": "Only 31% of people who had therapy relapsed within a year after stopping, compared with 76% of people who stopped their medication (Source 2).",
            "Cii": "This supports my claim because an SSRI antidepressant works by blocking reuptake so serotonin stays in the synapse longer, a chemical effect that comes from taking the pill. The results show that its benefit faded for most people once they stopped taking it, while the thinking skills learned in therapy stayed with the person, so fewer of them relapsed.",
        },
    },
    # ------------------------------------------------------------------ 6. ACEs
    {
        "id": "aces",
        "topic": "Health psychology, Adverse childhood experiences",
        "title": "Childhood Adversity and Later Health",
        "question": Q + "whether adverse childhood experiences increase the risk of health problems later in life.",
        "topicWords": ["childhood", "adverse", "aces", "health", "risk"],
        "sources": [
            ("Childhood Experiences and Adult Health", """## Introduction
In this study, researchers examined whether adults who experienced more stressful or traumatic events as children have more health problems as adults.

## Participants
Participants were 8,420 adults who had a routine checkup at a large health clinic in California. They ranged in age from 25 to 79 years (mean age = 56.1 years). The sample was 53% women and 47% men. The race/ethnicity of the participants was 74% White, 11% Hispanic/Latino/a, 8% Asian/Asian American, 5% Black/African American, and 2% other. Participants were not paid.

## Method
After their checkup, adults were mailed a questionnaire that asked whether, before age 18, they had experienced each of 10 kinds of hardship, such as being hit or insulted by a parent, having a parent who abused alcohol or drugs, seeing a parent being hurt, or having a parent go to prison. Each "yes" counted as 1 point, for a total score from 0 to 10. Researchers then checked each participant's medical record for heart disease, diabetes, lung disease, and depression.

The questionnaire was stored separately from participants' names, and only two researchers could match the two records. Participants were told that they could skip any question they did not want to answer, and 7% did not return the questionnaire.

The questionnaire also asked about adults' current habits, such as smoking, drinking alcohol, and exercise, and about their income and education. The clinic's review board approved the study. Participants' answers were not shared with their doctors. Researchers compared the people who returned the questionnaire with those who did not and found that they were similar in age, sex, and the health problems listed in their records.

## Results and Discussion
About two thirds of participants reported at least one hardship, and 13% reported four or more.

| Number of childhood hardships | Percent with heart disease | Percent ever diagnosed with depression |
| 0 | 5% | 14% |
| 1 | 6% | 21% |
| 2 or 3 | 8% | 31% |
| 4 or more | 11% | 49% |

As the number of hardships increased, the percentage of adults with each health problem increased (p < .001 for each). Adults with four or more hardships were also more likely to smoke and to report heavy drinking. The researchers noted that adults reported their childhood experiences many years later, so some may have forgotten or misremembered events."""),
            ("Childhood Hardship and Getting Sick", """## Introduction
In this study, researchers examined whether adults who experienced hardship in childhood are more likely to catch a cold after being exposed to a cold virus.

## Participants
Participants were 152 healthy adults aged 18 to 55 years (mean age = 30.4 years) in Pittsburgh, Pennsylvania, who answered newspaper ads. They were paid $1,000 for staying in a hotel for 6 days. The sample was 46% women and 54% men. Researchers did not report race/ethnicity data for the participants.

## Method
The study was approved by a university review board, and participants were told in detail what would happen before signing a consent form. Before the study, participants completed the same 10-item childhood hardship questionnaire described in Source 1. They also had blood tests to make sure they were not already immune to the virus being used.

Participants stayed in separate hotel rooms. On the first day, a doctor gave each participant nose drops containing a common cold virus. For the next five days, nurses checked participants each morning for cold symptoms and weighed the used tissues they had collected. A participant was counted as having a cold if they had the virus in their nose and also had clear symptoms.

During their stay, participants could watch television, read, and use the internet, but they stayed at least 1 meter away from one another when they met in the hallways. Meals were delivered to their rooms. Each day, participants also rated how stressed they felt and how many hours they had slept the night before. Participants who smoked were asked not to smoke during the study, and the number of smokers was similar across groups.

## Results and Discussion
| Number of childhood hardships | Number of participants | Percent who developed a cold |
| 0 | 68 | 26% |
| 1 or 2 | 54 | 33% |
| 3 or more | 30 | 53% |

Participants with three or more childhood hardships were significantly more likely to develop a cold than participants with none (p = .01). This difference remained after the researchers accounted for age, sex, weight, and how many hours participants slept in the hotel. At the end of the study, every participant received cold medicine and was checked by a doctor before going home."""),
            ("Children's Stress Response After Family Hardship", """## Introduction
In this study, researchers examined how children's bodies react to a stressful task, and whether this is different for children who have lived through serious family hardship.

## Participants
Participants were 96 children aged 9 to 12 years (mean age = 10.7 years) in Minneapolis, Minnesota. Half of the children (48) had been placed in foster care after being neglected or mistreated at home, and half (48) had lived with their parents their whole lives. The two groups were similar in age, sex (54% girls), and family income. Each child took part with written permission from a parent or legal guardian, and the child also agreed. Researchers did not report race/ethnicity data for the participants.

## Method
Each child visited a laboratory with a caregiver. After 20 minutes of quiet play, the child gave a 5-minute speech in front of two adults about why they would be a good friend, and then solved math problems out loud. The adults did not smile or give encouragement.

The child's heart rate was recorded throughout. The child also gave saliva samples before the task, right after it, and 40 minutes later. These were tested for a hormone the body releases in response to stress. Afterward, a researcher praised the child's effort, explained that the adults had been asked not to smile, and let the child pick a small toy.

Sessions were held in the afternoon, and children were asked not to eat for an hour before arriving. Caregivers waited in a nearby room during the speech and math tasks. A child psychologist watched each session from behind a one-way window and was ready to stop the task if a child became very upset; this happened twice, and those children's data were included up to the point the task stopped.

## Results and Discussion
| Group | Heart rate increase during task (beats per minute) | Hormone level 40 minutes after (compared with before) |
| Children in foster care | +21 | 64% higher |
| Children living with parents | +12 | 8% higher |

During the task, both groups showed a rise in heart rate, but the rise was significantly larger for children in foster care (p < .01). Forty minutes after the task, the hormone level of children living with their parents had returned almost to where it started, while children in foster care still had much higher levels (p < .001). Children in foster care also reported more headaches and stomachaches in the past month."""),
        ],
        "model": {
            "A": "Adverse childhood experiences increase the risk of health problems later in life, and the risk grows with the number of experiences.",
            "Bi": "Adults with four or more childhood hardships had heart disease at a rate of 11% and depression at 49%, compared with 5% and 14% for adults with no hardships (Source 1).",
            "Bii": "This supports my claim because of the diathesis-stress model: high levels of stress can trigger a biological predisposition to develop mental illness. Children who went through many hardships lived with high stress, which could trigger depression in people who were already vulnerable, so depression was far more common with more hardships.",
            "Ci": "Adults with three or more childhood hardships developed a cold 53% of the time after being given a cold virus, compared with 26% of adults with no hardships (Source 2).",
            "Cii": "This supports my claim because long-term stress leads to immunosuppression, a weakened immune system. Childhood hardship is a long-lasting stressor, so people who went through more hardship were less able to fight off the virus and got sick more often.",
        },
    },
    # ------------------------------------------------------------------ 7. coping
    {
        "id": "coping",
        "topic": "Health psychology, Coping",
        "title": "How People Cope With Stress",
        "question": Q + "whether the way people cope with stress changes how stress affects them.",
        "topicWords": ["cope", "coping", "stress", "way"],
        "sources": [
            ("Coping With a Hard Class", """## Introduction
In this study, researchers examined how college students handled a difficult chemistry course and whether their approach was related to their stress and their grades.

## Participants
Participants were 233 first-year students taking an introductory chemistry course at a public university in Michigan. They ranged in age from 17 to 20 years (mean age = 18.4 years). The sample was 55% women and 45% men. Students received a small amount of extra credit. Researchers did not report race/ethnicity data for the participants.

## Method
After students received their first exam grade, they completed a questionnaire about what they had done when they felt stressed about the course. One set of items asked about taking direct action, such as "I made a plan for studying," "I went to office hours," or "I joined a study group." Another set asked about avoiding the problem, such as "I tried not to think about the class" or "I watched videos to take my mind off it." Students rated each item from 1 (never) to 4 (a lot).

Students also rated their stress about the course from 1 (none) to 10 (extreme) at the start of the semester, after the first exam, and at the end of the semester. Final course grades were provided by the instructor with students' permission.

The course had about 600 students in three lecture sections taught by the same instructor, and students who dropped the course before the end of the semester, 19 in all, were not included. Students were told that the instructor would not see their questionnaire answers until after final grades were submitted. The questionnaire took about 15 minutes and was completed online.

## Results and Discussion
Students were divided into groups based on whether they scored above or below the middle on each set of items.

| Approach after the first exam | Number of students | Stress at end of semester (1 to 10) | Final grade (out of 100) |
| High direct action, low avoiding | 71 | 4.8 | 81.6 |
| High direct action, high avoiding | 52 | 6.1 | 76.2 |
| Low direct action, low avoiding | 49 | 6.4 | 72.9 |
| Low direct action, high avoiding | 61 | 7.7 | 68.3 |

Students who took more direct action had significantly lower stress at the end of the semester and higher final grades (p < .001). The four groups did not differ in their first exam grades."""),
            ("Coping With a Loved One's Long Illness", """## Introduction
In this study, researchers examined how adults coped with caring for a family member with a serious long-term illness, a situation they could not change.

## Participants
Participants were 140 adults (71% women) aged 30 to 78 years (mean age = 55.2 years) in Massachusetts who were caring for a spouse or parent with advanced cancer or advanced heart failure. They were recruited through two hospitals and received $40. The race/ethnicity of the participants was 81% White, 10% Black/African American, 5% Hispanic/Latino/a, and 4% other.

## Method
Participants completed questionnaires at the start of the study and again 6 months later. They rated how often they tried to change the situation (for example, "I kept looking for a different treatment") and how often they worked on how they felt about it (for example, "I looked for something good in what was happening," "I talked to a friend about how I felt," or "I practiced slow breathing or prayer"). Each item was rated from 1 (never) to 4 (a lot).

Participants also completed a 20-item questionnaire about how often they felt sad, worried, or hopeless, with scores from 0 to 60, and reported how many days in the past month they had a headache or trouble sleeping.

Questionnaires were completed at home and mailed back in a prepaid envelope, or completed by phone with a research assistant. Participants could skip any question. If a participant's distress score was very high, a social worker from the hospital called to offer help. During the 6 months, 18 of the family members being cared for died; their caregivers were offered the chance to stop, and 11 chose to continue.

## Results and Discussion
Caregivers who more often worked on how they felt had significantly lower distress scores 6 months later (r = -.37, p < .001). Caregivers who more often tried to change the situation had higher distress scores 6 months later (r = .22, p = .01).

| Approach | Distress score at 6 months (0 to 60) | Days with headaches in past month |
| Mostly worked on feelings | 17.3 | 3.1 |
| Mostly tried to change the situation | 26.8 | 6.4 |

The researchers suggested that when a problem cannot be solved, trying hard to change it may lead to frustration."""),
            ("Writing About a Stressful Event", """## Introduction
In this study, researchers tested whether a short writing activity changes how stressed students feel before a big test.

## Participants
Participants were 106 ninth-grade students at a public high school in Chicago, Illinois, who were about to take their final biology exam. Each student took part with a parent's written permission. The sample was 52% girls and 48% boys. Researchers did not report race/ethnicity data for the participants.

## Method
Ten minutes before the exam, students were randomly assigned to one of two writing activities. Students in the expressive writing group wrote as openly as possible about their thoughts and feelings about the exam. Students in the control group wrote about what they had done the day before. Teachers did not read what the students wrote.

Before the writing activity and right after it, students rated how nervous they felt from 1 (calm) to 10 (extremely nervous). Their exam scores were provided by the school. Earlier in the year, all students had completed a questionnaire about how much they usually worried about tests, and students were grouped as high or low worriers.

The writing activity took place in students' regular classrooms, and each student wrote on a numbered sheet of paper instead of writing their name. Teachers read the same instructions to every class from a script. Students who were absent on the exam day took the exam later and were not included. After the exam, the researchers met with each class to explain the purpose of the study and to share tips for managing test nerves.

## Results and Discussion
| Group | Nervousness before writing | Nervousness after writing | Exam score (out of 100) |
| Expressive writing, high worriers | 7.9 | 5.4 | 82 |
| Control, high worriers | 7.7 | 7.6 | 76 |
| Expressive writing, low worriers | 4.2 | 3.8 | 85 |
| Control, low worriers | 4.4 | 4.3 | 84 |

High worriers who wrote about their feelings became significantly less nervous and scored significantly higher on the exam than high worriers in the control group (p < .01). For low worriers, the writing activity made little difference. Students in the expressive writing group wrote an average of 182 words, and those who wrote more did not score higher than those who wrote less. The researchers suggested that writing may help most for students who worry a lot, because it gives their worries somewhere to go before the test starts."""),
        ],
        "model": {
            "A": "The way people cope changes how stress affects them: taking direct action reduces stress when a problem can be solved, and managing feelings helps more when it can't.",
            "Bi": "Students who took more direct action after their first chemistry exam had a final stress rating of 4.8 and a grade of 81.6, compared with 7.7 and 68.3 for students who took little direct action and avoided the problem (Source 1).",
            "Bii": "This supports my claim because problem-focused coping deals with the stressor itself by finding solutions and taking action. Students who made study plans and went to office hours fixed the root cause of their stress, so they ended the semester less stressed and with better grades.",
            "Ci": "Caregivers who mostly worked on how they felt had a distress score of 17.3 and 3.1 days with headaches, compared with 26.8 and 6.4 for caregivers who mostly tried to change the situation (Source 2).",
            "Cii": "This supports my claim because emotion-focused coping regulates negative emotions and is used when a stressor can't be changed. Caregivers could not cure their family member's illness, so working on their feelings lowered their distress, while trying to change something they couldn't control made them more upset.",
        },
    },
    # ------------------------------------------------------------------ 8. distraction and pain
    {
        "id": "pain",
        "topic": "Touch and pain",
        "title": "Distraction and Pain",
        "question": Q + "whether distraction reduces the pain people feel.",
        "topicWords": ["distract", "pain", "reduce", "feel"],
        "sources": [
            ("Video Games During Burn Care", """## Introduction
In this study, researchers examined whether playing an immersive video game during painful wound care reduces the pain that burn patients feel.

## Participants
Participants were 54 patients aged 12 to 54 years (mean age = 27.3 years) being treated for burns at a hospital burn center in Washington State. All needed daily wound cleaning and dressing changes, which are usually very painful even with medication. Patients who had burns on their face or head, or who were too sick to answer questions, were not eligible. The sample was 80% male. Researchers did not report race/ethnicity data for the participants.

## Method
Each patient received their usual pain medication before every dressing change. During one dressing change, patients played a video game in which they flew through an icy canyon and threw snowballs at snowmen, using a headset that blocked their view of the room and headphones that played the game's sounds. During another dressing change on a nearby day, they received the usual care with no game. The order of the two conditions was chosen at random for each patient, and the same nurses did both dressing changes.

Right after each dressing change, patients rated their worst pain from 0 (no pain) to 100 (the worst pain possible) and the percentage of time they spent thinking about their pain, also from 0 to 100. They also rated how much fun they had.

The hospital's review board approved the study, and patients (or, for patients under 18, a parent) signed a consent form. Patients were told they could stop playing at any time. Dressing changes lasted an average of 18 minutes. The headset was cleaned between patients, and patients who could not use their hands controlled the game by turning their heads.

## Results and Discussion
| Condition | Worst pain (0 to 100) | Time spent thinking about pain (0 to 100) |
| Video game | 41 | 22 |
| Usual care | 72 | 69 |

Patients reported significantly less worst pain and spent significantly less time thinking about their pain while playing the game (p < .001). Patients who said they felt most "inside" the game reported the biggest drop in pain. Two patients said the game made them feel slightly sick, and both chose to keep playing. The amount of pain medication was the same in both conditions."""),
            ("Counting Backward and Cold Water", """## Introduction
In this study, researchers tested whether doing a mental task while keeping a hand in ice water reduces how much pain people feel and changes how long they can stand it.

## Participants
Participants were 80 undergraduate students (41 women, 39 men) at a university in Ontario, Canada, aged 18 to 26 (mean age = 20.3 years). Students received course credit. Students with heart problems, high blood pressure, or problems with circulation in their hands were not eligible. Researchers did not report race/ethnicity data for the participants.

## Method
Each student placed their left hand in a tank of water kept at 2°C (about 36°F) and was told to keep it there until they wanted to stop, up to a limit of 3 minutes. Students were randomly assigned to one of two conditions. In the distraction condition, students counted backward from 1,000 by 7s out loud while their hand was in the water. In the attention condition, students were told to focus on the feelings in their hand and describe them out loud.

Pain tolerance was measured as the number of seconds the student kept their hand in the water. After removing their hand, students rated the strongest pain they had felt from 0 (no pain) to 10 (the worst pain imaginable).

Before the task, students rated how anxious they felt about it from 0 to 10, and the two groups did not differ. A researcher sat beside each student and reminded them that they could take their hand out at any time. After the task, students warmed their hand in room-temperature water and were given a towel. Each session took about 20 minutes, and all sessions were run by the same researcher in the same room.

## Results and Discussion
| Condition | Seconds hand stayed in water | Strongest pain (0 to 10) |
| Counting backward | 112 | 5.9 |
| Focusing on the hand | 69 | 7.4 |

Students who counted backward kept their hands in the water significantly longer and rated their pain significantly lower than students who focused on their hand (p < .01). Twelve students in the counting condition reached the 3-minute limit, compared with three in the attention condition. Students who made more counting mistakes did not report more pain than students who made fewer mistakes."""),
            ("Expecting the Pain to Be Strong", """## Introduction
In this study, researchers tested whether what people expect about a painful stimulus changes how much pain they feel.

## Participants
Participants were 46 healthy adults (24 women, 22 men) aged 19 to 40 years (mean age = 26.8 years) in Boston, Massachusetts, who answered online ads and were paid $60. Researchers did not report race/ethnicity data for the participants.

## Method
A small heating pad was placed on each participant's forearm. On each trial, a symbol appeared on a screen, followed by a few seconds of heat. Participants first learned that a blue circle came before mild heat and a yellow triangle came before strong heat. After learning, participants were not told that on some trials the heat that followed was always the same medium temperature, no matter which symbol appeared.

After each trial, participants rated the heat from 0 (not painful) to 10 (extremely painful). There were 60 trials over about 40 minutes. Participants were told before the study that the heat could be uncomfortable but would not burn the skin, and that they could stop at any time. At the end, a researcher explained that the medium heat had been the same after both symbols and why participants had not been told.

The temperature of the pad was checked by a computer before each trial and could never go above a safe limit. Participants had a short break halfway through and rated how tired they felt. Two participants stopped early because the heat was too uncomfortable, and their data were not used.

## Results and Discussion
| Symbol shown before the same medium heat | Mean pain rating (0 to 10) |
| Blue circle (expect mild) | 3.6 |
| Yellow triangle (expect strong) | 6.1 |

Participants rated the same medium heat as significantly more painful when it followed the symbol that meant strong heat (p < .001). Participants who said they believed the symbols most strongly showed the biggest difference. The researchers noted that people in real life usually know a lot about what is about to happen to them, such as before a shot."""),
        ],
        "model": {
            "A": "Distraction reduces the pain people feel, so patients going through painful procedures should be given something engaging to focus on.",
            "Bi": "Burn patients rated their worst pain 41 while playing a video game during wound care, compared with 72 during usual care, and spent only 22% of the time thinking about their pain instead of 69% (Source 1).",
            "Bii": "This supports my claim because of gate control theory: the spinal cord has a neurological gate that either blocks pain signals or lets them through to the brain, and distraction can close the gate. The game distracted the patients, so fewer pain signals got through and they felt less pain.",
            "Ci": "Students who counted backward by 7s kept their hand in ice water for 112 seconds and rated their pain 5.9, compared with 69 seconds and 7.4 for students who focused on their hand (Source 2).",
            "Cii": "This supports my claim because selective attention means focusing conscious awareness on one stimulus and not something else. When students focused their attention on counting, they were not focusing on the cold in their hand, so the pain felt weaker and they could stand it longer.",
        },
    },
    # ------------------------------------------------------------------ 9. phobia treatment
    {
        "id": "phobia",
        "topic": "Phobias, Treatment",
        "title": "Treating Phobias",
        "question": Q + "whether facing feared situations step by step is an effective treatment for phobias.",
        "topicWords": ["phobia", "fear", "effective", "treat", "step"],
        "sources": [
            ("Step-by-Step Practice for Fear of Flying", """## Introduction
In this study, researchers tested whether practicing feared parts of flying, one step at a time, helps adults with an intense fear of flying.

## Participants
Participants were 75 adults aged 21 to 66 years (mean age = 41.2 years) in Atlanta, Georgia, who met the criteria for a specific phobia of flying after an interview with a psychologist. Most (68%) had not flown in at least two years. The sample was 72% women and 28% men. Researchers did not report race/ethnicity data for the participants.

## Method
Participants were randomly assigned to one of two groups for 8 weekly sessions. In the step-by-step group, participants first made a list of flying situations from least to most frightening, such as packing a suitcase, driving to the airport, sitting in a parked plane, and hearing the engines start. They learned slow breathing and muscle relaxation, and then, starting with the least frightening item, practiced each situation using a virtual reality headset until they could stay relaxed. In the comparison group, participants met with a therapist to talk about their fear, its history, and how it affected their lives, without practicing any flying situations.

After treatment, all participants were offered a seat on a real 30-minute round-trip flight. Fear was rated by participants from 0 (none) to 100 (extreme) during the flight.

The study was approved by a university review board, and each participant signed a consent form. Sessions lasted 50 minutes and were led by the same three therapists in both groups. Participants paid nothing for treatment, and the flight was paid for by the study. Before treatment, participants also rated how much their fear affected their work and family life, and the two groups did not differ.

## Results and Discussion
| Group | Took the flight | Mean fear during flight (0 to 100) |
| Step-by-step practice | 73% | 38 |
| Talking about the fear | 30% | 64 |

Significantly more participants in the step-by-step group took the flight (p < .001), and those who flew reported significantly less fear. Six months later, 63% of the step-by-step group said they had taken another flight on their own, compared with 19% of the comparison group."""),
            ("Fear Responses in the Brain Before and After Treatment", """## Introduction
In this study, researchers used brain scans to see whether repeated, gradual exposure to spiders changes how the brain responds to spider pictures in people who fear spiders.

## Participants
Participants were 28 adults aged 18 to 35 years (mean age = 24.6 years) in Munich, Germany, who had a specific phobia of spiders, and 14 adults of similar age with no strong fears. The sample was 71% women. Researchers did not report race/ethnicity data for the participants.

## Method
Adults with a spider phobia were randomly assigned either to receive treatment right away or to wait. Treatment was one long session in which participants slowly moved closer to live spiders with a therapist's help, staying with each step until their fear dropped, and then spent a week looking at spider photos at home.

Before and after treatment (or waiting), each participant lay in an fMRI scanner and looked at photos of spiders, mushrooms, and neutral objects. The researchers measured activity in a small area deep in the brain that responds strongly to threats. Participants also rated their fear of each photo from 1 (none) to 9 (extreme) and how much they would avoid a spider if they saw one at home.

Each participant signed a consent form after the scanner's safety rules were explained. Participants with metal in their bodies were not eligible. Scans took about 45 minutes, and participants could press a button to stop at any time. Participants in the waiting group were offered treatment when the study ended.

## Results and Discussion
| Group | Fear rating of spider photos before | Fear rating of spider photos after |
| Treated right away | 7.8 | 3.1 |
| Waited | 7.6 | 7.3 |
| No phobia | 2.2 | 2.0 |

Before treatment, people with a spider phobia showed much more activity in the threat-response area when viewing spiders than people with no phobia. After treatment, activity in this area dropped significantly in the treated group, to a level close to that of people with no phobia (p < .01), but did not change in the group that waited."""),
            ("Avoiding Versus Approaching", """## Introduction
In this study, researchers followed children with a fear of dogs to see whether avoiding dogs or approaching them was related to how their fear changed over a year.

## Participants
Participants were 63 children aged 7 to 12 years (mean age = 9.4 years) in Melbourne, Australia, whose parents said the child had a strong fear of dogs that interfered with daily life, such as refusing to visit friends who owned dogs. The sample was 57% girls and 43% boys. Researchers did not report race/ethnicity data for the participants.

## Method
At the start of the study and again one year later, each child completed a test in which a calm, trained dog sat on a leash at the far end of a room, and the child was asked to come as close as they felt able. The researchers recorded the closest distance in meters. Children also rated their fear from 0 (none) to 8 (very scared).

Every two months during the year, parents completed a short questionnaire about how often their child had avoided dogs, such as crossing the street or refusing to go to a park, and how often the child had approached dogs, such as petting a neighbor's dog with an adult.

Parents signed a consent form, and each child agreed to take part. The dog and its trainer were the same at both tests, and children could leave the room at any time. Families received a $50 gift card at each visit.

## Results and Discussion
Children were grouped based on the parents' reports over the year.

| Group | Closest distance at start (meters) | Closest distance after one year (meters) | Fear rating after one year (0 to 8) |
| Mostly approached dogs | 4.2 | 0.9 | 2.8 |
| Mostly avoided dogs | 4.0 | 3.8 | 6.5 |

Children who mostly approached dogs during the year got significantly closer to the dog and reported significantly less fear after one year than children who mostly avoided dogs (p < .001). The researchers noted that parents chose whether to encourage their children to approach dogs."""),
        ],
        "model": {
            "A": "Facing feared situations step by step is an effective treatment for phobias, so people with phobias should gradually practice what they fear instead of avoiding it.",
            "Bi": "In the step-by-step group, 73% of people with a fear of flying took a real flight and rated their fear 38, compared with 30% and a fear rating of 64 in the group that only talked about their fear (Source 1).",
            "Bii": "This supports my claim because systematic desensitization creates a fear hierarchy from least to most scary and pairs each step with relaxation techniques. The step-by-step group used exactly that kind of hierarchy, from packing a suitcase to hearing the engines, so they learned to stay relaxed and were able to fly.",
            "Ci": "After gradual exposure to spiders, people with a spider phobia rated spider photos 3.1 instead of 7.8, while people who waited stayed at 7.3 (Source 2).",
            "Cii": "This supports my claim because the amygdala processes fear and triggers the fight-or-flight response. After treatment, the threat-response area deep in the brain became much less active when viewing spiders, which shows that facing the fear step by step calmed the brain's fear response, not just people's ratings.",
        },
    },
    # ------------------------------------------------------------------ 10. sleep loss and memory
    {
        "id": "sleepmemory",
        "topic": "Sleep, Memory",
        "title": "Sleep and Memory",
        "question": Q + "whether losing sleep harms students' ability to learn and remember.",
        "topicWords": ["sleep", "learn", "remember", "memory", "student"],
        "sources": [
            ("A Night Without Sleep Before Learning", """## Introduction
In this study, researchers examined whether staying awake all night affects how well people learn new information the next day.

## Participants
Participants were 56 healthy college students (30 women, 26 men) aged 18 to 25 years (mean age = 21.0 years) at a university in California. They were paid $150. Students who worked night shifts or had a sleep disorder were not eligible. Researchers did not report race/ethnicity data for the participants.

## Method
Students were randomly assigned to one of two groups. The sleep loss group stayed awake all night in a laboratory, watched by research assistants. The normal sleep group slept for 8 hours in the same laboratory. Neither group was allowed caffeine.

At noon the next day, both groups looked at 150 photos of scenes, such as a beach or a kitchen, for 2 seconds each and were asked to remember them. Two days later, after both groups had slept normally at home for two nights, students were shown 300 photos: the 150 they had seen and 150 new ones. Memory was measured as the percentage of the original photos that a student correctly recognized.

The study was approved by the university's review board, and students signed consent forms after the procedures were explained. They were told that they could stop at any time and still be paid for the hours completed. Students in the sleep loss group were driven home by taxi after the learning session so that they would not drive while sleepy. During the night, students in the sleep loss group could read, watch movies, and play board games, but they could not lie down.

## Results and Discussion
| Group | Photos correctly recognized two days later | Sleepiness rating at noon (1 to 9) |
| Sleep loss | 58% | 7.1 |
| Normal sleep | 77% | 2.8 |

Students in the sleep loss group recognized significantly fewer photos two days later than students in the normal sleep group (p < .001), even though both groups had slept normally for two nights before the test. Students in the sleep loss group also reported feeling much sleepier while learning."""),
            ("Sleep and Grades in High School", """## Introduction
In this study, researchers examined the relationship between how much high school students sleep on school nights and their grades.

## Participants
Participants were 2,259 students in grades 9 through 12 at eight public high schools in Massachusetts. They ranged in age from 14 to 18 years. The sample was 50% girls and 50% boys. The race/ethnicity of the participants was 62% White, 15% Hispanic/Latino/a, 12% Black/African American, 7% Asian/Asian American, and 4% other.

## Method
Students completed a survey during class asking what time they usually went to bed and woke up on school nights, how many hours of homework they did each night, how many hours they worked at a job, and how often they used their phones after going to bed. They also reported the grades they usually got, from mostly As to mostly Ds and Fs.

Parents received a letter about the study and could choose to keep their child out of it. Students could skip any question, and no names were collected. The survey was given during the same week at all eight schools and took about 20 minutes. Researchers checked students' reported grades against school records for a random sample of 200 students and found that 89% matched.

The survey also asked students how sleepy they usually felt during their first two classes and how often they had fallen asleep while doing homework. Schools were chosen to include cities, suburbs, and small towns, and their start times ranged from 7:20 a.m. to 8:15 a.m. Students in special education classes completed the same survey with help from a teacher's aide if they asked for it.

## Results and Discussion
| Usual sleep on school nights | Percent of students | Percent reporting mostly As and Bs |
| Less than 6 hours | 18% | 41% |
| 6 to 7 hours | 49% | 58% |
| 8 or more hours | 33% | 71% |

Hours of sleep were positively correlated with grades (r = .24, p < .001). Students who slept less also reported more phone use after going to bed and more hours at a job. The researchers noted that students who are struggling in school may stay up later doing homework, so the survey cannot show which came first."""),
            ("Studying Then Sleeping Versus Studying Then Staying Awake", """## Introduction
In this study, researchers tested whether sleeping soon after learning helps people remember what they learned better than staying awake for the same amount of time.

## Participants
Participants were 72 undergraduate students (44 women, 28 men) aged 18 to 24 years (mean age = 19.8 years) at a university in Illinois who received course credit. Researchers did not report race/ethnicity data for the participants.

## Method
Each student learned 40 pairs of unrelated words, such as "candle–river," until they could recall at least 60% of them. Students were randomly assigned to one of two groups. The sleep group learned the pairs at 9:00 p.m., slept at home, and were tested 12 hours later at 9:00 a.m. The wake group learned the pairs at 9:00 a.m., went about their normal day, and were tested 12 hours later at 9:00 p.m. When tested, students saw the first word of each pair and wrote the second word.

Students wore a wrist monitor so that researchers could check how long the sleep group slept. Students in the wake group were asked not to nap, and the monitor confirmed that none did. Each student signed a consent form and was told that they could stop at any time. After the test, students were told what the study was testing. Students in both groups were asked not to practice the word pairs between learning and testing, and 94% said they had not. Before learning, students rated how alert they felt, and the two groups did not differ.

## Results and Discussion
| Group | Word pairs recalled right after learning | Word pairs recalled 12 hours later |
| Sleep | 27.1 | 26.3 |
| Wake | 26.8 | 21.5 |

The two groups recalled about the same number of pairs right after learning. Twelve hours later, the sleep group had forgotten significantly fewer pairs than the wake group (p < .001). Students in the sleep group slept an average of 7 hours 20 minutes. Students in the wake group who said they had a busy day did not forget more than those who said they had a quiet day."""),
        ],
        "model": {
            "A": "Losing sleep harms students' ability to learn and remember, so students should get a full night of sleep instead of staying up late to study.",
            "Bi": "Students who stayed awake all night recognized only 58% of the photos they had studied, compared with 77% for students who slept 8 hours, even after two normal nights of sleep (Source 1).",
            "Bii": "This supports my claim because sleep loss diminishes attentional focus, so it hurts selective attention, the ability to focus conscious awareness on one thing. Students who had not slept rated their sleepiness 7.1 while studying, so they could not focus on the photos and remembered fewer of them days later.",
            "Ci": "Students who slept after learning word pairs still recalled 26.3 pairs 12 hours later, while students who stayed awake for those 12 hours recalled only 21.5 (Source 3).",
            "Cii": "This supports my claim because sleep is needed for memory consolidation, the process of storing new learning so it lasts, and sleep loss diminishes it. Students who slept after learning kept almost all of the word pairs, which shows that skipping sleep after studying means losing more of what you learned.",
        },
    },
]
