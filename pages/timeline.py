import flet as ft

# ── Shared dark palette ───────────────────────────────────────────────────────
BG       = "#0D1117"
SURFACE  = "#161B22"
SURFACE2 = "#1C2128"
BORDER   = "#30363D"
TEXT_PRI = "#E6EDF3"
TEXT_SEC = "#8B949E"
ACCENT   = "#3FB950"
ACCENT_B = "#238636"
AMBER    = "#D29922"
BLUE     = "#58A6FF"


def _hoverable(container: ft.Container, accent_color: str) -> ft.Container:
    container.animate = 200

    def on_hover(e, c=container, col=accent_color):
        if e.data == "true":
            c.bgcolor = SURFACE2
            c.border  = ft.Border.all(1, col)
            c.shadow  = ft.BoxShadow(
                spread_radius=0,
                blur_radius=18,
                color=col + "33",
                offset=ft.Offset(0, 4),
            )
        else:
            c.bgcolor = SURFACE
            c.border  = ft.Border.all(1, BORDER)
            c.shadow  = None
        c.update()

    container.on_hover = on_hover
    return container


class TimelinePage:
    ENTRIES = [
        {
            "week": "Week 1", "dates": "02–06 March 2026",
            "task": "Project Formulation & Problem Brainstorming",
            "contribution": "I participated in the formation of Group 13 and contributed to brainstorming ideas for the mobile application. I helped the team discuss real-world infrastructure problems affecting Ongwediva residents and suggested features that could improve communication between residents and the town council..",
            "status": "Done", "icon": ft.Icons.ROCKET_LAUNCH, "tags": ["Git", "Setup"],
        },
        {
            "week": "Week 2", "dates": "09–13 March 2026",
            "task": "Environment Setup & Repository Initialization",
            "contribution": "I assisted in setting up the development environment using Expo, React Native, and Firebase. I also helped create and organize the GitHub repository structure and tested Expo Go on my mobile device to ensure the application could run correctly.",
            "status": "Done", "icon": ft.Icons.BUILD, "tags": ["Python", "UI"],
        },
        {
            "week": "Week 3", "dates": "16–20 March 2026",
            "task": "Pitch Preparation & Technical Ideation",
            "contribution": "I contributed during Pitch Week by helping prepare the presentation of our three proposed app ideas. I explained possible app features and gave input on how Firebase could be used for storing reports and user information.",
            "status": "Done", "icon": ft.Icons.CALCULATE, "tags": ["Python", "Maths"],
        },
        {
            "week": "Week 4", "dates": "23–27 March 2026",
            "task": "Scope Refinement & Feature Definition",
            "contribution": "After our app idea was approved, I participated in refining the project scope and discussing the final feature list for the Fix-Flow application. I also helped clarify user requirements and possible report categories.",
            "status": "Done", "icon": ft.Icons.TABLE_CHART, "tags": ["Python", "UI"],
        },
        {
            "week": "Week 5", "dates": "30 March–03 April 2026",
            "task": "SRS Initiation & Workflow Design",
            "contribution": "I contributed to the beginning of the System Requirements Specification (SRS) document by helping define the project scope, target users, and overall system workflow. I also shared coding ideas for implementing authentication and reporting features.",
            "status": "Done", "icon": ft.Icons.RATE_REVIEW, "tags": ["Git", "Collaboration"],
        },
        {
            "week": "Week 6", "dates": "06–10 April 2026",
            "task": "Database Schema & Functional Requirements",
            "contribution": "I worked with other coders to discuss Firebase Firestore collections and how reports, comments, and announcements would be stored in the database. I also reviewed functional requirements related to user registration and report submission.",
            "status": "Done", "icon": ft.Icons.WEB, "tags": ["Python", "UI"],
        },
        {
            "week": "Week 7", "dates": "13–17 April 2026",
            "task": "Non-Functional Requirements & Security Planning",
            "contribution": "I assisted with reviewing the non-functional requirements and use case discussions. I contributed technical suggestions on app performance, security, and reliability, especially concerning Firebase Authentication and Firestore rules.",
            "status": "Done", "icon": ft.Icons.LOCK, "tags": ["Python", "Backend"],
        },
        {
            "week": "Week 8", "dates": "20–25 April 2026",
            "task": "SRS Finalization & Quality Review",
            "contribution": "I helped finalize and review the SRS document before submission. I checked that the listed functional requirements matched the intended app functionality and supported the documentation team with corrections and formatting.",
            "status": "Done", "icon": ft.Icons.LOCK, "tags": ["Python", "Backend"],
        },
        {
            "week": "Week 9", "dates": "27 April–01 May 2026",
            "task": "UI/UX Architecture & Navigation Planning",
            "contribution": "I participated in the UI/UX planning phase by discussing screen layouts and navigation flow with the design team. I provided suggestions on how the home screen and report submission forms should function within React Native.",
            "status": "Done", "icon": ft.Icons.LOCK, "tags": ["Python", "Backend"],
        },
        {
            "week": "Week 10", "dates": "04–08 May 2026",
            "task": "Frontend Implementation & Layout Testing",
            "contribution": "I started implementing some React Native screens and assisted with integrating navigation between screens. I also tested form layouts and discussed how users would upload images and report infrastructure issues.",
            "status": "Done", "icon": ft.Icons.LOCK, "tags": ["Python", "Backend"],
        },
        {
            "week": "Week 11", "dates": "11–15 May 2026",
            "task": "Firebase Integration & Workflow Verification",
            "contribution": "I worked on improving app functionality by assisting with Firebase integration and helping connect frontend components to Firestore. I also tested user login and report submission workflows.",
            "status": "Done", "icon": ft.Icons.LOCK, "tags": ["Python", "Backend"],
        },
        {
            "week": "Week 12", "dates": "18–30 May 2026",
            "task": "Prototype Testing & UI Optimization",
            "contribution": "I helped review the prototype and tested navigation flows and screen responsiveness. I contributed to fixing UI issues and ensured some screens aligned with the approved design prototype.",
            "status": "Done", "icon": ft.Icons.LOCK, "tags": ["Python", "Backend"],
        },
        {
            "week": "Week 13", "dates": "01–06 June 2026",
            "task": "Demo Preparation & Milestone Verification",
            "contribution": "I participated in preparing the progress demonstration for Mr. Abisai. I assisted in testing the Expo application, checking authentication features, and verifying Firestore read/write operations before the live demo.",
            "status": "Done", "icon": ft.Icons.LOCK, "tags": ["Python", "Backend"],
        },
        {
            "week": "Week 14", "dates": "08–13 June 2026",
            "task": "Final Sprint, Bug Fixing & APK Build",
            "contribution": "I contributed during the final sprint by helping fix bugs, improving app stability, and testing the final APK build. I also assisted the group in preparing the final submission package and reviewing implemented features against the SRS requirements.",
            "status": "Done", "icon": ft.Icons.LOCK, "tags": ["Python", "Backend"],
        },

        
    ]

    STATUS_STYLES = {
        "Done":        (ACCENT_B + "33", ACCENT, ACCENT),
        "In Progress": (AMBER + "33",    AMBER,  AMBER),
        "Done":     ("#6E40C933",     "#A371F7", "#A371F7"),
    }

    def _tag_chip(self, label):
        return ft.Container(
            content=ft.Text(label, size=10, color=BLUE),
            bgcolor=BLUE + "22",
            padding=ft.Padding(left=8, right=8, top=3, bottom=3),
            border_radius=20,
            border=ft.Border.all(1, BLUE + "44"),
        )

    def _build_entry(self, entry, index, is_last):
        bg, fg, dot_color = self.STATUS_STYLES.get(entry["status"], (SURFACE2, TEXT_SEC, TEXT_SEC))
        is_done     = entry["status"] == "Done"
        is_progress = entry["status"] == "In Progress"

        dot = ft.Container(
            width=44, height=44, border_radius=22,
            bgcolor=SURFACE2,
            content=ft.Icon(entry["icon"], color=dot_color, size=20),
            alignment=ft.Alignment(0, 0),
            border=ft.Border.all(2, dot_color),
        )

        week_badge = ft.Container(
            content=ft.Text(entry["week"], size=11, weight=ft.FontWeight.W_700, color=dot_color),
            bgcolor=bg,
            padding=ft.Padding(left=10, right=10, top=3, bottom=3),
            border_radius=20,
            border=ft.Border.all(1, dot_color + "55"),
        )

        status_icon = (ft.Icons.CHECK_CIRCLE if is_done else ft.Icons.PENDING if is_progress else ft.Icons.CIRCLE)
        status_badge = ft.Container(
            content=ft.Row(controls=[
                ft.Icon(status_icon, size=12, color=fg),
                ft.Text(entry["status"], size=11, weight=ft.FontWeight.W_600, color=fg),
            ], spacing=4),
            bgcolor=bg,
            padding=ft.Padding(left=10, right=10, top=4, bottom=4),
            border_radius=20,
        )

        card = _hoverable(
            ft.Container(
                content=ft.Column(
                    controls=[
                        ft.Row(controls=[
                            week_badge,
                            ft.Text(entry["dates"], size=11, color=TEXT_SEC),
                            ft.Container(expand=True),
                            status_badge,
                        ], spacing=8),
                        ft.Text(entry["task"], size=14, weight=ft.FontWeight.W_700, color=TEXT_PRI),
                        ft.Text(entry["contribution"], size=13, color=TEXT_SEC, no_wrap=False),
                        ft.Row(controls=[self._tag_chip(t) for t in entry.get("tags", [])], spacing=6, wrap=True),
                    ],
                    spacing=8,
                ),
                bgcolor=SURFACE, border_radius=12,
                padding=ft.Padding(left=16, right=16, top=16, bottom=16),
                border=ft.Border.all(1, BORDER),
                expand=True,
            ),
            dot_color,
        )

        connector = ft.Container(
            width=2, height=20,
            bgcolor=dot_color if is_done else BORDER,
            margin=ft.Margin(left=21, right=21, top=0, bottom=0),
        )

        left_col = ft.Column(
            controls=[dot] + ([] if is_last else [connector]),
            spacing=0,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            width=44,
        )

        return ft.Container(
            content=ft.Row(controls=[left_col, card], spacing=16,
                           vertical_alignment=ft.CrossAxisAlignment.START),
            margin=ft.Margin(left=0, right=0, top=0, bottom=12),
        )

    def build(self):
        done_count = sum(1 for e in self.ENTRIES if e["status"] == "Done")
        total      = len(self.ENTRIES)
        progress   = done_count / total

        hero = _hoverable(
            ft.Container(
                content=ft.Column(
                    controls=[
                        ft.Row(controls=[
                            ft.Icon(ft.Icons.TODAY, color=TEXT_PRI, size=28),
                            ft.Text("Project Timeline", size=24, weight=ft.FontWeight.W_700, color=TEXT_PRI),
                        ], spacing=10),
                        ft.Text("Weekly log of my individual contributions to the group project.", size=13, color=TEXT_SEC),
                        ft.Divider(height=8, color="transparent"),
                        ft.Row(controls=[
                            ft.Text(f"{done_count} of {total} weeks completed", size=12, color=TEXT_SEC),
                            ft.Container(expand=True),
                            ft.Text(f"{int(progress * 100)}%", size=12, weight=ft.FontWeight.W_700, color=ACCENT),
                        ]),
                        ft.ProgressBar(value=progress, bgcolor=BORDER, color=ACCENT, height=6, border_radius=4),
                    ],
                    spacing=6,
                ),
                bgcolor=SURFACE, border_radius=16,
                padding=ft.Padding(left=24, right=24, top=24, bottom=24),
                margin=ft.Margin(left=0, right=0, top=0, bottom=24),
                border=ft.Border.all(1, BORDER),
            ),
            ACCENT,
        )

        def stat_card(value, label, color):
            return _hoverable(
                ft.Container(
                    content=ft.Column(
                        controls=[
                            ft.Text(value, size=22, weight=ft.FontWeight.W_700, color=color),
                            ft.Text(label, size=11, color=TEXT_SEC),
                        ],
                        spacing=2,
                        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    ),
                    bgcolor=SURFACE, border_radius=12,
                    padding=ft.Padding(left=20, right=20, top=14, bottom=14),
                    border=ft.Border.all(1, BORDER),
                    expand=True,
                    alignment=ft.Alignment(0, 0),
                ),
                color,
            )

        stats = ft.Row(controls=[
            stat_card(str(total), "Total Weeks", TEXT_PRI),
            stat_card(str(done_count), "Completed", ACCENT),
            stat_card(str(sum(1 for e in self.ENTRIES if e["status"] == "In Progress")), "In Progress", AMBER),
        ], spacing=12)

        entries = [self._build_entry(e, i, i == len(self.ENTRIES) - 1) for i, e in enumerate(self.ENTRIES)]

        return ft.Column(
            controls=[
                hero, stats,
                ft.Divider(height=24, color="transparent"),
                ft.Text("Weekly Contributions", size=16, weight=ft.FontWeight.W_700, color=TEXT_PRI),
                ft.Divider(height=8, color="transparent"),
                *entries,
            ],
            spacing=4,
            scroll=ft.ScrollMode.AUTO,
        )