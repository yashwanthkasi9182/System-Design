"""Compile the authored interview lessons into distributable course JSON.

This is a content authoring command, not a test runner. Run from any directory:
    python3 content/build_interview_curriculum.py
"""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
source = ROOT / 'content' / 'interview-lessons.txt'
course_path = ROOT / 'public' / 'system-design.json'
course = json.loads(course_path.read_text())
new_lessons = []
roles = ['hook', 'problem', 'explanation', 'visual', 'application', 'takeaway']
headings = ['The interviewer asks…', 'Find the hard part', 'Make a clear design choice', 'Walk through the system', 'Say it in the interview', 'Handle the follow-up']
labels = ['Interview prompt', 'The challenge', 'Design decision', 'Request walkthrough', 'Your spoken answer', 'Interviewer follow-up']
for index, block in enumerate(source.read_text().strip().split('\n\n')):
    lines = block.splitlines()
    title, case, focus = [part.strip() for part in lines[0][2:].split('|')]
    cards = [dict(type=role, title=heading, label=label, body='\n'.join(part.strip() for part in body.split('|')))
             for role, heading, label, body in zip(roles, headings, labels, lines[1:7])]
    diagram_parts = [part.strip() for part in lines[7][2:].split('|')]
    cards[3]['diagram'] = dict(type=diagram_parts[0], nodes=diagram_parts[1:])
    questions = []
    for question_index, line in enumerate(lines[8:]):
        question, correct, distractor_a, distractor_b, explanation = [part.strip() for part in line[2:].split('|')]
        options = [correct, distractor_a, distractor_b]
        rotation = (index + question_index) % 3
        options = options[rotation:] + options[:rotation]
        questions.append(dict(question=question, options=options, correctIndex=options.index(correct), explanation=explanation))
    new_lessons.append(dict(id=f'day-{index+31:02}', title=title,
        summary=f'{case} · Part {index%3+1} of 3: {focus.lower()}.',
        category=f'Interview lab · {case}', minutes=5, introducedInRevision=2,
        interview=dict(caseStudy=case, focus=focus, part=index%3+1, parts=3,
            context='Original interview-style practice. Workload numbers are illustrative assumptions, not claims about any company’s production architecture.'),
        cards=cards, quiz=questions))
# Preserve the original foundation lessons and stable IDs when rerunning this authoring command.
course['lessons'] = course['lessons'][:30] + new_lessons
course['contentRevision'] = 2
course['description'] = '90 days of system design: 30 days of foundations, then 60 days of concise interview case studies.'
course_path.write_text(json.dumps(course, indent=2, ensure_ascii=False) + '\n')
standalone = dict(schemaVersion=1, id='system-design-interview-lab', title='System Design · Interview Lab',
    description='60 interview lessons across 20 case studies. Import this standalone course to begin the interview track immediately.',
    contentRevision=2, lessons=new_lessons)
(ROOT / 'public' / 'system-design-interview-lab.json').write_text(json.dumps(standalone, indent=2, ensure_ascii=False) + '\n')
outline = ['# Days 31–90: System design interview lab', '',
    'Twenty original interview-style case studies, three five-minute lessons each. Scale numbers are practice assumptions, not descriptions of specific companies.', '',
    'Each lesson has six cards with four short explanation blocks, a diagram, a four-part spoken answer, and three scenario-based questions. Physical line wrapping varies with screen width.', '',
    '| Day | Case study | Lesson | Focus |', '| --- | --- | --- | --- |']
for day, lesson in enumerate(new_lessons, start=31):
    interview = lesson['interview']
    outline.append(f"| {day} | {interview['caseStudy']} | {lesson['title']} | {interview['focus']} |")
outline += ['', '## How to practice', '',
    'Read the prompt, then make your own choice before advancing. On the spoken-answer card, say the answer aloud in your own words. Use the follow-up card to practice naming a limitation. Answer the quiz before reviewing its explanation.', '',
    'The main course preserves the original first 30 days and unlocks lessons sequentially. To start directly with interview practice, choose **Open interview track** on the System Design home page, or import `public/system-design-interview-lab.json` in Course Studio and publish it locally. It has independent progress and starts with the URL-shortener case.', '',
    'The companion `content/interview-lessons.txt` is the editable authoring source. Each block contains metadata, six cards (four pipe-separated explanation blocks each), diagram data, and three questions. `python3 content/build_interview_curriculum.py` writes the two JSON courses and this outline; it does not launch or test the app.', '']
(ROOT / 'CURRICULUM.md').write_text('\n'.join(outline))
