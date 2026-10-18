# Days 31–90: System design interview lab

Twenty original interview-style case studies, three five-minute lessons each. Scale numbers are practice assumptions, not descriptions of specific companies.

Each lesson has six cards with four short explanation blocks, a diagram, a four-part spoken answer, and three scenario-based questions. Physical line wrapping varies with screen width.

| Day | Case study | Lesson | Focus |
| --- | --- | --- | --- |
| 31 | URL shortener | Short links: frame the design | Requirements & API |
| 32 | URL shortener | Short links: size the read path | Capacity & caching |
| 33 | URL shortener | Short links: hot keys & safe changes | Failure & consistency |
| 34 | API rate limiter | Rate limits: define fairness first | Requirements & algorithm |
| 35 | API rate limiter | Rate limits: make the decision atomic | Distributed coordination |
| 36 | API rate limiter | Rate limits: outages and regional budgets | Degraded operation |
| 37 | Product cache | Product cache: choose what may be stale | Access patterns & freshness |
| 38 | Product cache | Product cache: survive a cold start | Stampedes & capacity |
| 39 | Product cache | Product cache: explain the invalidation race | Versioning & failure |
| 40 | Social news feed | News feed: start with the read model | Requirements & baseline |
| 41 | Social news feed | News feed: choose where fan-out happens | Scaling & skew |
| 42 | Social news feed | News feed: ranking, deletion & late work | Correctness & evolution |
| 43 | Messaging service | Chat: separate send from delivery | API & message lifecycle |
| 44 | Messaging service | Chat: order within a conversation | Partitioning & ordering |
| 45 | Messaging service | Chat: reconnect without losing the thread | Recovery & presence |
| 46 | Notification platform | Notifications: turn events into intent | Preferences & durable work |
| 47 | Notification platform | Notifications: retries without a spam storm | Delivery semantics |
| 48 | Notification platform | Notifications: protect urgent messages | Scheduling & fairness |
| 49 | Cloud file storage | File storage: separate bytes from metadata | Upload protocol |
| 50 | Cloud file storage | File storage: resume, version & sync | Multipart & concurrency |
| 51 | Cloud file storage | File storage: clean up without deleting live files | Lifecycle & recovery |
| 52 | Video streaming | Video: upload once, prepare many renditions | Ingestion pipeline |
| 53 | Video streaming | Video: serve viewers near the edge | CDN & adaptive playback |
| 54 | Video streaming | Video: retry processing without corrupt publication | Idempotent workflows |
| 55 | Search service | Search: build an index for the question | Inverted index & retrieval |
| 56 | Search service | Search: partition, retrieve, then rank | Distributed query planning |
| 57 | Search service | Search: rebuild without stale resurrection | Index lifecycle |
| 58 | Ride dispatch | Ride matching: find nearby candidates | Geospatial discovery |
| 59 | Ride dispatch | Ride matching: reserve one driver once | Assignment invariants |
| 60 | Ride dispatch | Ride matching: hot cities & stale locations | Regional scaling |
| 61 | Ticket booking | Ticket booking: hold the seat, not the page | Inventory invariants |
| 62 | Ticket booking | Ticket booking: survive the opening minute | Admission & hot partitions |
| 63 | Ticket booking | Ticket booking: payment after hold expiry | Cross-system recovery |
| 64 | Payment processing | Payments: model the operation before the button | API & idempotency |
| 65 | Payment processing | Payments: uncertain is a real state | External effects & webhooks |
| 66 | Payment processing | Payments: explain the ledger and reconciliation | Auditability & invariants |
| 67 | Event analytics | Analytics: capture useful events | Event contracts |
| 68 | Event analytics | Analytics: late events change the answer | Windows & deduplication |
| 69 | Event analytics | Analytics: replay without double counting | Recovery & schema evolution |
| 70 | Background job platform | Job scheduler: claim work durably | State & ownership |
| 71 | Background job platform | Job scheduler: retries are additional load | Backoff & fairness |
| 72 | Background job platform | Job scheduler: cancellation is a protocol | Fencing & deadlines |
| 73 | Monitoring platform | Metrics: a time series is a label set | Data model & ingestion |
| 74 | Monitoring platform | Metrics: why you cannot average p99s | Aggregation & retention |
| 75 | Monitoring platform | Metrics: alert on symptoms that matter | SLOs & failure detection |
| 76 | E-commerce checkout | Checkout: an order is a state machine | API & ownership |
| 77 | E-commerce checkout | Checkout: coordinate with a saga | Cross-service consistency |
| 78 | E-commerce checkout | Checkout: prevent overselling at the source | Inventory concurrency |
| 79 | Collaborative editor | Collaborative docs: define the convergence goal | Operations & synchronization |
| 80 | Collaborative editor | Collaborative docs: recover from a long disconnect | Snapshots & operation logs |
| 81 | Collaborative editor | Collaborative docs: separate presence from content | Access & degraded operation |
| 82 | Web crawler | Web crawler: build a polite frontier | Scheduling & scope |
| 83 | Web crawler | Web crawler: deduplicate without pretending certainty | Frontier scale & content identity |
| 84 | Web crawler | Web crawler: freshness under an adversarial web | Recrawl & resource safety |
| 85 | ML inference platform | Inference: define the serving contract | Latency & model lifecycle |
| 86 | ML inference platform | Inference: batch carefully, shed deliberately | Scheduling & capacity |
| 87 | ML inference platform | Inference: release models without guessing | Evaluation & rollout |
| 88 | Retrieval-augmented assistant | RAG: index documents with their permissions | Ingestion & retrieval |
| 89 | Retrieval-augmented assistant | RAG: improve retrieval before buying a bigger model | Quality & latency |
| 90 | Retrieval-augmented assistant | RAG: defend your complete interview answer | Freshness & synthesis |

## How to practice

Read the prompt, then make your own choice before advancing. On the spoken-answer card, say the answer aloud in your own words. Use the follow-up card to practice naming a limitation. Answer the quiz before reviewing its explanation.

The main course preserves the original first 30 days and unlocks lessons sequentially. To start directly with interview practice, choose **Open interview track** on the System Design home page, or import `public/system-design-interview-lab.json` in Course Studio and publish it locally. It has independent progress and starts with the URL-shortener case.

The companion `content/interview-lessons.txt` is the editable authoring source. Each block contains metadata, six cards (four pipe-separated explanation blocks each), diagram data, and three questions. `python3 content/build_interview_curriculum.py` writes the two JSON courses and this outline; it does not launch or test the app.
