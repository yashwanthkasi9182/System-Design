# Tiny Systems

A mobile-first, local-first system design habit: six small cards, three questions, and a little win. Built with native JavaScript modules, HTML, and CSS. No framework, build step, npm packages, account, API, or database.

## Run locally

From this directory, run:

```sh
python3 -m http.server 5173
```

Open http://localhost:5173 in your browser. `npm run dev` is an optional alias for the same command and also requires Python 3. No `npm install` is necessary. Use HTTP rather than opening `index.html` directly: module imports and curriculum fetching need a web origin.

## Deploy to Vercel

1. Push this directory to a Git repository and import it in Vercel.
2. Set the framework preset to **Other**, leave the build command empty, and use `.` as the output directory. The included `vercel.json` supplies these static-site settings.
3. Deploy. There are no environment variables or backend resources to configure.

Alternatively, with the Vercel CLI installed, run `vercel` in this folder, then `vercel --prod` when ready to publish. This implementation has not been deployed. Localhost and deployment URLs have separate browser storage.

## Learning experience

- Home surfaces the first unfinished lesson, current streak, XP, recent seven-day activity, and course progress.
- Swipe left to advance and right to go back. Buttons and left/right arrow keys are also available. Escape exits a lesson.
- Lessons unlock sequentially after completion. You can continue beyond one lesson per day; there is no artificial date lock.
- Complete all three quiz questions to finish. Feedback explains each answer immediately. Wrong answers still allow completion.
- A first completion earns 100 XP plus 10 per correct answer. Replays do not award more XP or extend the streak. This avoids XP farming.
- A streak counts consecutive local calendar dates with a newly completed lesson. Yesterday's streak remains visible until today ends. Multiple lessons on one date count as one active day.
- Badges recognize the first lesson, a historical three-day streak, ten completed lessons in the selected course, and course completion.
- Preview sessions never award XP, unlock lessons, or change activity.

## Content and authoring

`public/system-design.json` is both the default curriculum and a complete sample import: 90 lessons, 540 cards, 270 questions. Days 1–30 build foundations; days 31–90 form a 20-case interview lab with three lessons per case. `public/course.schema.json` documents the portable v1 format. `src/course.js` supplies dependency-free runtime validation, including unique lesson IDs and valid answer indexes.

### Interview practice: days 31–90

The next 60 lessons cover URL shortening, distributed rate limiting, product caching, social feeds, chat, notifications, file storage, video, search, ride matching, ticket booking, payments, analytics, background jobs, monitoring, checkout, collaborative editing, crawling, ML inference, and retrieval-augmented assistants.

Each lesson includes:

- Six cards with four short, newline-separated explanation points each.
- A realistic interview prompt and explicitly stated exercise assumptions.
- A concrete design choice, request walkthrough, and JSON-driven diagram.
- A four-part spoken answer to rehearse in your own words.
- An interviewer follow-up that explores a limitation or failure case.
- Three scenario questions with explanations, rather than only vocabulary recall.

These are original interview-style practice scenarios, not claims about any named company's production system or exact interview questions. Estimated duration is five minutes; practicing aloud may take longer. Four explanation blocks will naturally wrap to more physical lines on a narrow screen.

Use **Open interview track** on the System Design home page to start case studies immediately. This adds a standalone 60-lesson course with independent progress and preserves your foundation course. The original main course still has all 90 days and sequential unlocks. The selected course is remembered on this device. The standalone course is also available as `public/system-design-interview-lab.json` for ordinary import/export workflows.

See `CURRICULUM.md` for the day-by-day outline. Edit `content/interview-lessons.txt` and run `python3 content/build_interview_curriculum.py` to regenerate both course files and the outline. This content compiler is not an application build or a test runner. If you edit generated JSON directly, do not rerun the compiler unless you intend to regenerate the interview section from its authoring source.

### Existing learners and curriculum updates

On reload, the app requests the current bundled curriculum with cache revalidation. `src/curriculum.js` appends lessons introduced after the locally stored `contentRevision`, preserving existing lesson content, stable IDs, completed lessons, XP, and streak dates. It does not overwrite an authoring draft. Already-present new lesson IDs are not duplicated. Previously removed foundation lessons are not resurrected by this release. A customized course too close to the 365-lesson limit is left unchanged with guidance to open the standalone track.

When the update cannot be fetched, an existing saved course still opens and a notice explains the issue. New installations need the bundled JSON to be available. To edit all 90 lessons in the studio, export any draft you want to keep, then choose **Edit active course** after selecting the main course. Publishing an older draft retains the existing course-replacement semantics; a later reload can append the newer bundled release again if its revision was older.

Course Studio supports:

1. **New course** for DSA, Python, AI Engineering, or another subject. The renderer is course-agnostic.
2. Editing course title, stable ID, description, lesson title, category, duration, summary, card copy, diagram type/nodes/caption, quiz options, correct answers, and explanations.
3. Adding and deleting lessons. New lessons include a complete six-card structure and three editable questions.
4. Automatic local draft saving on input. One draft is retained at a time. Export a draft before starting a new course, importing another course, or choosing “Edit active course,” as those actions replace the working draft.
5. **Preview lesson** using the same learning and quiz renderer. The entire draft must be valid before preview or publication.
6. **Publish locally** to add or replace a course on this device. Published content is a separate snapshot; editing the draft does not change it.
7. **Import JSON** to load a validated course as a draft; publication is an explicit separate step. **Export draft** exports even an incomplete draft so unfinished work can be retained; an incomplete export must be repaired before re-importing.
8. **Export progress backup** and **Restore backup** to move all courses, draft, XP, and progress between browsers. Restore asks before replacing local data. Restore expects schema-valid content; finish or publish a valid draft before exporting a backup intended for restoration.

The form editor keeps the existing card count and option count. To author alternative supported counts (5–7 cards, 2–4 answer options) or change card roles, edit the JSON and import it. New lessons use the recommended six-card pattern.

### Content format

```json
{
  "schemaVersion": 1,
  "id": "my-course",
  "title": "My course",
  "description": "One small idea at a time.",
  "lessons": []
}
```

This is a structural illustration; a valid import needs at least one complete lesson. Copy a lesson from `public/system-design.json` for a working starting point. Each lesson has `id`, `title`, `summary`, `category`, `minutes`, `cards`, and `quiz`. Each card has `type`, `title`, `body`, and an optional diagram. An optional `label` changes the visible card label. Newlines in `body` create separated explanation points. Optional lesson `interview` metadata contains `caseStudy`, `focus`, `context`, `part`, and `parts`; it enables the compact case-study layout and can be edited in Course Studio. Optional `contentRevision` on courses and `introducedInRevision` on lessons support additive bundled updates without changing `schemaVersion: 1`. The six supported card roles are `hook`, `problem`, `explanation`, `visual`, `application`, and `takeaway`.

Diagrams are reusable data:

```json
{"type":"flow","nodes":["Client","API","Database"],"caption":"Follow one request."}
```

`flow` draws a sequence, `fanout` connects the first node to the remaining nodes, and `compare` lays out alternatives. Diagram labels and captions come from JSON. Course and lesson text is escaped before display. Optional `icon` and `color` are preserved metadata; the UI currently uses one shared visual theme.

Quiz questions use `question`, `options`, `correctIndex` (zero-based), and `explanation`. Array order determines lesson order; category changes create journey chapter headings. IDs must be stable lowercase slugs, unique within their scope. Publishing the same course ID replaces its content while preserving progress for matching lesson IDs. Use a new course ID for an independent course edition. Removed lesson records remain in historical progress, but no longer count toward the selected course's progress.

## Source map

- `index.html` — entry point and metadata
- `src/app.js` — navigation, learning, quizzes, gamification, studio and imports
- `src/style.css` — responsive design, illustrations, animations, reduced-motion support
- `src/course.js` — course validation and new-lesson factory
- `src/curriculum.js` — additive bundled curriculum upgrades that preserve progress
- `src/storage.js` — persistence, local calendar dates, streaks and JSON export
- `public/system-design.json` — complete authored curriculum and example course
- `public/system-design-interview-lab.json` — standalone 60-lesson interview course
- `content/interview-lessons.txt` — editable interview curriculum source
- `content/build_interview_curriculum.py` — content-to-JSON compiler
- `CURRICULUM.md` — full days 31–90 learning outline
- `public/course.schema.json` — extensible content contract
- `vercel.json` — static hosting configuration

## Persistence and accessibility

Everything is stored under `tiny-systems-v1` in localStorage. There is no cross-device sync. Clearing site data removes progress and imported courses; backups are recommended. Quota/private-mode failures show a notice and leave the current session usable, but cannot promise persistence. Import size is capped at 5 MB. The app needs HTTP to initially load files; it is not a service-worker offline PWA. Google Fonts are optional network resources and system fonts provide a fallback.

The UI includes native buttons and controls, visible keyboard focus, labeled fields, textual diagram alternatives, reduced-motion support, responsive layouts, safe-area spacing, and swipe alternatives. Quiz correctness is communicated with both text/icons and color.

## Delivery status

Implemented without running tests, builds, a development server, browser checks, or automated verification, as requested. Runtime behavior and deployment are ready for your own review, but have not been independently verified.
