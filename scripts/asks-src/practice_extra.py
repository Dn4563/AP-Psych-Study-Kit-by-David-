# Extra practice sets written by us (not from Phineas's kit). Writes content/<unit>/practice-extra.json,
# which scripts/import-phineas.mjs merges into practice.json. Run: python3 scripts/asks-src/practice_extra.py
import json, os, random

root = os.path.join(os.path.dirname(__file__), "..", "..")

# (topic, stem, right, [(wrong, why) x3], explanation)
TREATMENT_EXAM = [
("Treatment", "A man with schizophrenia starts a drug that quiets his hallucinations. Months later he develops repetitive, involuntary lip-smacking. Which drug type and side effect fit?",
 "An antipsychotic; tardive dyskinesia",
 [("An antidepressant (SSRI); tardive dyskinesia", "Tardive dyskinesia comes from antipsychotics, and SSRIs don't treat hallucinations."), ("A mood stabilizer; catatonic stupor", "Catatonic stupor is a negative symptom of schizophrenia, not a drug side effect."), ("An anti-anxiety drug; dependency and drowsiness", "Benzodiazepines can cause dependency, but they don't reduce hallucinations.")],
 "Antipsychotics block dopamine to reduce positive symptoms; tardive dyskinesia is their movement side effect."),
("Treatment", "A patient is diagnosed with bipolar disorder. Which medication is the classic treatment on your slides?",
 "Lithium, a mood stabilizer",
 [("Prozac, an SSRI that blocks serotonin reuptake", "SSRIs are antidepressants; the bipolar example is lithium."), ("Xanax, a benzodiazepine that boosts GABA", "That is an anti-anxiety drug."), ("Antabuse, which makes alcohol cause sickness", "Antabuse is used in aversion therapy for alcoholism.")],
 "Mood stabilizers like lithium treat bipolar disorder."),
("Treatment", "A doctor prescribes a drug that depresses the central nervous system and increases the effects of GABA to calm a patient's constant tension. Which side effects should the patient watch for?",
 "Drowsiness and dependency",
 [("Tardive dyskinesia and weight gain", "Those are antipsychotic side effects."), ("Memory loss and a 40% relapse rate", "Those are ECT drawbacks."), ("Fatigue, forgetfulness and insomnia", "Those are listed for antidepressants (SSRIs).")],
 "Anti-anxiety medications (benzodiazepines) can cause drowsiness and dependency."),
("Treatment", "A patient with chronic depression wants a brain-stimulation treatment where she stays awake, has no seizure, and has no memory loss. Which fits?",
 "rTMS",
 [("Electroconvulsive therapy (ECT)", "ECT causes a seizure and can cause memory loss."), ("A lobotomy", "That is psychosurgery and is rarely used today."), ("Biofeedback", "Biofeedback trains control of body responses; it doesn't stimulate the brain.")],
 "rTMS uses magnetic pulses: no seizures, no memory loss, person awake."),
("Treatment", "A family is considering ECT for their son's severe depression. Which concern is supported by your slides?",
 "About 40% relapse within 6 months",
 [("It cuts the main connections to the frontal lobe", "That describes a lobotomy."), ("It only reduces the positive symptoms of schizophrenia", "ECT is used for extreme depression."), ("It is mainly used for mild, everyday anxiety", "ECT is for extreme depression.")],
 "ECT drawbacks: memory loss, about 40% relapse within 6 months, and no one knows why it works."),
("Treatment", "During a session, a client says he plans to seriously hurt his roommate tonight. What should the therapist do?",
 "Break confidentiality to protect the roommate",
 [("Keep it private, because confidentiality has no exceptions at all", "The exception is danger to self or others."), ("Wait until the next session to discuss it further", "The danger is immediate."), ("Switch the client to group therapy", "That doesn't address the danger.")],
 "Confidentiality is the cardinal rule unless the client is a danger to themselves or others."),
("Treatment", "A therapist tells a client a treatment is proven to work, even though she knows it isn't. Which ethics principle is she violating?",
 "Integrity",
 [("Justice", "Justice is about fairness and equal access."), ("Beneficence and nonmaleficence", "That is about weighing harm; the problem here is lying."), ("Respect for rights and dignity", "That is about privacy and self-determination.")],
 "Integrity: honesty, accuracy and transparency. No lying to the client."),
("Personality", "A man cons elderly people out of their savings, lies constantly, and shows no guilt. Which disorder and cluster fit best?",
 "Antisocial, Cluster B",
 [("Narcissistic, Cluster A", "Narcissism is in Cluster B, and its core is self-importance, not violating others' rights."), ("Paranoid, Cluster A", "Paranoid personality disorder is distrust of others."), ("Schizotypal, Cluster C", "Schizotypal is Cluster A and involves odd thinking.")],
 "Antisocial personality disorder: disregard for others' rights, no remorse. Cluster B."),
("Treatment", "A therapist mostly listens, restates the client's feelings (\"It sounds like you feel unseen\"), and never tells him what to do. Which therapy and technique are these?",
 "Person-centered therapy, active listening",
 [("Psychodynamic therapy, using free association and dream interpretation", "The therapist isn't interpreting the unconscious."), ("CBT, using cognitive restructuring", "CBT actively challenges thoughts."), ("REBT, confronting irrational beliefs", "REBT is confrontational, not non-directive.")],
 "Rogers' person-centered therapy uses active listening: echo, restate, clarify."),
("Treatment", "A therapist bluntly tells an anxious client, \"It's irrational to believe everyone must like you,\" then has him replace that belief. Which therapy is this?",
 "REBT",
 [("Person-centered therapy", "That is non-directive and accepting, not confrontational."), ("Systematic desensitization", "That uses relaxation and a fear hierarchy."), ("Psychodynamic therapy", "That explores the unconscious.")],
 "REBT (Ellis) confronts irrational beliefs: identify, challenge, replace."),
("Treatment", "A client afraid of flying learns deep breathing, then imagines each step from booking a ticket to takeoff while staying calm. Which therapy is this?",
 "Systematic desensitization",
 [("Aversion therapy", "Aversion pairs an unwanted behavior with something unpleasant."), ("A token economy", "That rewards behavior with tokens."), ("Rational emotive behavior therapy (REBT)", "REBT confronts beliefs; this uses relaxation and a fear hierarchy.")],
 "Systematic desensitization: a fear hierarchy plus relaxation."),
("Treatment", "To stop drinking, a man takes a pill that makes him sick whenever he drinks alcohol. Which therapy is this, and how does it work?",
 "Aversion therapy: drinking is paired with feeling ill",
 [("Systematic desensitization: drinking is paired with relaxation", "That reduces fear; it doesn't make drinking unpleasant."), ("Token economy: he earns rewards for staying sober", "No rewards are involved."), ("Biofeedback: sensors show his body's reaction", "No sensors or feedback are involved.")],
 "Antabuse pairs a negative outcome with a previously pleasant stimulus."),
("Treatment", "On a psychiatric ward, patients earn points for showering and making their beds and trade them for TV time. Which principle is at work?",
 "Operant conditioning (a token economy)",
 [("Counterconditioning (aversion therapy)", "No unpleasant state is paired with a behavior."), ("Unconditional positive regard", "That is a humanistic attitude, not a reward system."), ("Free association", "That is a psychodynamic technique.")],
 "A token economy rewards desired behavior with tokens."),
("Treatment", "A woman with tension headaches watches a screen that shows her muscle tension and gradually learns to lower it on purpose. Which therapy is this?",
 "Biofeedback",
 [("rTMS", "rTMS stimulates neurons with magnets."), ("Hypnosis", "Hypnosis induces relaxation but doesn't use sensor feedback."), ("Exposure therapy", "Exposure is facing what you avoid.")],
 "Biofeedback: sensors feed body data back so you learn to control it."),
("Treatment", "A client with borderline personality disorder learns mindfulness, distress tolerance, emotion regulation and interpersonal effectiveness. Which therapy is this?",
 "DBT",
 [("REBT", "REBT confronts irrational beliefs."), ("Psychoanalysis", "That explores the unconscious."), ("Aversion therapy", "That pairs a behavior with discomfort.")],
 "DBT, a modified CBT, was originally developed for borderline personality disorder."),
("Treatment", "During free association, a patient goes blank every time her mother comes up. What would a psychodynamic therapist call this?",
 "Resistance",
 [("Flat affect", "Flat affect is a lack of emotional expression in schizophrenia."), ("Unconditional positive regard", "That is the therapist's accepting attitude."), ("Catatonic stupor", "That is a lack of movement.")],
 "Resistance is a mental block during free association."),
("Treatment", "A client says, \"I'm a failure, nobody cares about me, and it will never get better.\" Which theory explains this pattern, and what is it called?",
 "Beck's negative cognitive triad",
 [("Rogers' unconditional positive regard", "That is a therapist's accepting attitude."), ("Eysenck's finding that therapy doesn't work", "Eysenck studied therapy outcomes, not thought patterns."), ("Freud's interpretation of dreams", "That is psychodynamic.")],
 "Beck: negative thoughts about me, the world and the future."),
("Treatment", "A student cites a 1950s study claiming therapy is no better than no treatment. Which reply best fits current evidence?",
 "Meta-analyses show it works, especially with medication",
 [("The study proved that only psychoanalysis is effective for most people", "Eysenck found psychoanalysis no better than nothing."), ("Modern research shows therapy works only without medication", "It works best with medication."), ("Therapy works best when there is no therapeutic alliance", "A strong alliance helps therapy work.")],
 "Eysenck's 1950s claim has been answered by meta-analyses showing therapy is effective."),
("Treatment", "A psychologist teaches a client relaxation, challenges his negative thoughts, and refers him for medication. Which approach is this?",
 "The eclectic approach",
 [("Non-directive therapy", "She is actively directing treatment."), ("Psychodynamic therapy", "She isn't exploring the unconscious."), ("Deinstitutionalization", "That is the historical closing of asylums.")],
 "Eclectic = combining methods that fit the client."),
("Treatment", "A clinical psychologist believes her client needs an antidepressant. What should happen?",
 "A doctor or psychiatrist prescribes it",
 [("The psychologist prescribes it herself after a full evaluation", "Only doctors and psychiatrists can prescribe."), ("The client buys it without a prescription", "It needs a doctor or psychiatrist."), ("The psychologist uses hypnosis instead", "Hypnosis doesn't replace medication.")],
 "Medications can only be prescribed by a doctor or psychiatrist."),
("Treatment", "Which is an advantage of group therapy over individual therapy, according to your slides?",
 "It's cheaper and eases isolation",
 [("It's more personalized and more private than individual sessions", "That describes individual therapy."), ("It has more flexible scheduling", "That is individual therapy."), ("It works for every disorder", "Some disorders need individual therapy.")],
 "Group: cheaper, shows you aren't alone, coping skills together, relieves isolation."),
("Personality", "Ben has no friends and says he doesn't want any; praise and criticism leave him unmoved. Ana has no friends but badly wants them and fears rejection. Which disorders fit?",
 "Ben schizoid; Ana avoidant",
 [("Ben avoidant; Ana schizoid", "This swaps them: avoidant people want relationships but fear rejection."), ("Ben schizotypal; Ana dependent", "Ben shows no magical thinking, and Ana isn't clingy for decisions."), ("Both have dependent personality disorder", "Neither relies on others to make decisions.")],
 "Schizoid = no interest in relationships; avoidant = wants them but fears rejection."),
("Personality", "In the order listed, which clusters do paranoid, histrionic and dependent personality disorders belong to?",
 "A, B, C",
 [("B, A, C", "Paranoid is Cluster A, histrionic is Cluster B."), ("A, C, B", "Histrionic is B and dependent is C."), ("C, B, A", "Paranoid is A and dependent is C.")],
 "A = odd (paranoid), B = dramatic (histrionic), C = anxious (dependent)."),
("Personality", "Kara has unstable moods, a shifting self-image, and intense, stormy relationships. Which disorder fits, and which therapy was first developed for it?",
 "Borderline; DBT",
 [("Bipolar I; lithium", "Bipolar centers on mood episodes, not unstable relationships and self-image."), ("Histrionic; REBT", "Histrionic is attention-seeking; REBT is mainly for anxiety."), ("Narcissistic; psychoanalysis", "Narcissism is grandiosity and entitlement.")],
 "Borderline: instability in mood, self-image and relationships. DBT was developed for it."),
("Personality", "Mark redoes all group work himself because no one else will do it right and keeps strict rules for everything, but he has no intrusive thoughts or rituals. Which fits best?",
 "Obsessive-compulsive personality disorder",
 [("Obsessive-compulsive disorder (OCD) with obsessions and compulsions", "He has no intrusive thoughts or rituals."), ("Dependent personality disorder", "He takes control instead of relying on others."), ("Paranoid personality disorder", "His issue is perfectionism, not distrust.")],
 "OCPD: perfectionism, rigidity, need for control, can't delegate."),
]

def build(items, seed):
    rnd = random.Random(seed)
    slots = [i % 4 for i in range(len(items))]
    rnd.shuffle(slots)
    qs, bad = [], []
    for i, (topic, stem, right, wrongs, exp) in enumerate(items):
        if len(right) > max(len(w[0]) for w in wrongs):
            bad.append("%d: right answer is the longest: %s" % (i + 1, right))
        opts = [w[0] for w in wrongs]; why = [w[1] for w in wrongs]
        opts.insert(slots[i], right); why.insert(slots[i], "")
        if len(set(opts)) != 4: bad.append("%d: repeated choice" % (i + 1))
        qs.append({"id": "TP%d" % (i + 1), "type": "mcq", "topic": topic, "stem": stem, "options": opts, "ans": slots[i], "exp": exp, "why": why})
    return qs, bad

qs, bad = build(TREATMENT_EXAM, 511)
assert len(qs) == 25, len(qs)
for b in bad: print("  " + b)
letters = "".join("ABCD"[q["ans"]] for q in qs)
print("Treatment & Personality exam:", len(qs), "questions", letters, {c: letters.count(c) for c in "ABCD"})
if not bad:
    sec = {"name": "Practice exam: Treatment & Personality", "mode": "exam", "exam": "Treatment & Personality exam",
           "examTips": ["Like your test: 25 multiple-choice questions, mostly applied. Turn the Timer on and don't look anything up.", "About 1 minute per question. Flag hard ones and come back."],
           "tips": ["Every question gives a situation; name the treatment, drug, side effect, ethics principle or disorder that fits.", "Wrong choices are close mix-ups (CBT vs. REBT, desensitization vs. aversion, schizoid vs. avoidant). Cross out what doesn't fit the details."],
           "questions": qs}
    json.dump({"sections": [sec]}, open(os.path.join(root, "content", "unit-05", "practice-extra.json"), "w"), indent=1, ensure_ascii=False)
    print("written")
