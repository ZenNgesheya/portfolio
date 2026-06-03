import flet as ft

# ── Shared colours (mirrors main.py) ─────────────────────────────────────────
BG       = "#0D1117"
SURFACE  = "#161B22"
SURFACE2 = "#1C2128"
BORDER   = "#30363D"
BORDER2  = "#21262D"
TEXT_PRI = "#E6EDF3"
TEXT_SEC = "#8B949E"
TEXT_MUT = "#484F58"
ACCENT   = "#3FB950"
BLUE     = "#58A6FF"
ORANGE   = "#F78166"


def _chip(label: str, color: str = ACCENT) -> ft.Container:
    return ft.Container(
        content=ft.Text(label, size=11, color=color, weight=ft.FontWeight.W_500),
        bgcolor=f"{color}18",
        border=ft.Border(
            top=ft.BorderSide(1, f"{color}35"),
            bottom=ft.BorderSide(1, f"{color}35"),
            left=ft.BorderSide(1, f"{color}35"),
            right=ft.BorderSide(1, f"{color}35"),
        ),
        border_radius=20,
        padding=ft.Padding(left=12, right=12, top=4, bottom=4),
    )


def _section_label(text: str) -> ft.Row:
    return ft.Row(
        controls=[
            ft.Container(width=3, height=16, bgcolor=ACCENT, border_radius=2),
            ft.Text(text, size=13, weight=ft.FontWeight.W_600, color=TEXT_PRI),
            ft.Container(expand=True, height=1, bgcolor=BORDER2),
        ],
        spacing=10,
        vertical_alignment=ft.CrossAxisAlignment.CENTER,
    )


def _stat_card(value: str, label: str, icon, color: str = ACCENT) -> ft.Container:
    return ft.Container(
        content=ft.Column(
            controls=[
                ft.Row(
                    controls=[
                        ft.Icon(icon, size=16, color=color),
                        ft.Container(expand=True),
                        ft.Text(value, size=22, weight=ft.FontWeight.W_700, color=color),
                    ],
                ),
                ft.Text(label, size=11, color=TEXT_SEC),
            ],
            spacing=6,
        ),
        bgcolor=SURFACE,
        border=ft.Border(
            top=ft.BorderSide(1, BORDER),
            bottom=ft.BorderSide(1, BORDER),
            left=ft.BorderSide(1, BORDER),
            right=ft.BorderSide(1, BORDER),
        ),
        border_radius=12,
        padding=ft.Padding(left=16, right=16, top=14, bottom=14),
        expand=True,
    )


def _skill_bar(label: str, pct: int, color: str = ACCENT) -> ft.Column:
    return ft.Column(
        controls=[
            ft.Row(
                controls=[
                    ft.Text(label, size=12, color=TEXT_PRI, expand=True),
                    ft.Text(f"{pct}%", size=11, color=color, weight=ft.FontWeight.W_600),
                ],
            ),
            ft.Stack(
                controls=[
                    ft.Container(height=5, border_radius=4, bgcolor=BORDER2),
                    ft.Container(
                        height=5,
                        border_radius=4,
                        bgcolor=color,
                        width=pct * 2.8,
                        animate=ft.Animation(800, ft.AnimationCurve.EASE_OUT),
                    ),
                ],
                height=5,
            ),
        ],
        spacing=7,
    )


def _project_card(num, title, desc, tags, icon, color=ACCENT):
    c = ft.Container(
        content=ft.Column(
            controls=[
                ft.Row(
                    controls=[
                        ft.Container(
                            content=ft.Icon(icon, size=16, color=color),
                            bgcolor=f"{color}18",
                            border_radius=8,
                            padding=8,
                        ),
                        ft.Container(expand=True),
                        ft.Text(num, size=10, color=TEXT_MUT, font_family="monospace"),
                    ],
                ),
                ft.Text(title, size=14, weight=ft.FontWeight.W_600, color=TEXT_PRI),
                ft.Text(desc, size=12, color=TEXT_SEC, max_lines=3),
                ft.Container(expand=True),
                ft.Row(
                    controls=[_chip(t, color) for t in tags],
                    spacing=6,
                    wrap=True,
                ),
            ],
            spacing=10,
        ),
        bgcolor=SURFACE,
        border=ft.Border(
            top=ft.BorderSide(1, BORDER),
            bottom=ft.BorderSide(1, BORDER),
            left=ft.BorderSide(1, BORDER),
            right=ft.BorderSide(1, BORDER),
        ),
        border_radius=12,
        padding=18,
        expand=True,
    )

    def on_hover(e):
        e.control.bgcolor = SURFACE2 if e.data == "true" else SURFACE
        e.control.update()

    c.on_hover = on_hover
    return c


class HomePage:
    def build(self) -> ft.Column:

        # ── Profile image ─────────────────────────────────────────────────────
        # Place your photo at  assets/profile.png
        profile_image = ft.Stack(
            controls=[
                ft.Container(
                    width=148,
                    height=148,
                    border_radius=74,
                    border=ft.Border(
                        top=ft.BorderSide(2, f"{ACCENT}60"),
                        bottom=ft.BorderSide(2, f"{ACCENT}60"),
                        left=ft.BorderSide(2, f"{ACCENT}60"),
                        right=ft.BorderSide(2, f"{ACCENT}60"),
                    ),
                ),
                ft.Container(
                    content=ft.Image(
                        src="/profile.png",
                        width=136,
                        height=136,
                        fit="cover",
                        border_radius=68,
                        error_content=ft.Container(
                            content=ft.Icon(ft.Icons.PERSON, size=56, color=TEXT_SEC),
                            width=136,
                            height=136,
                            border_radius=68,
                            bgcolor=SURFACE2,
                        ),
                    ),
                    width=136,
                    height=136,
                    border_radius=68,
                    margin=ft.Margin(left=6, top=6, right=0, bottom=0),
                    clip_behavior=ft.ClipBehavior.ANTI_ALIAS,
                ),
                # Green online dot
                ft.Container(
                    width=16,
                    height=16,
                    border_radius=8,
                    bgcolor=ACCENT,
                    border=ft.Border(
                        top=ft.BorderSide(2, BG),
                        bottom=ft.BorderSide(2, BG),
                        left=ft.BorderSide(2, BG),
                        right=ft.BorderSide(2, BG),
                    ),
                    margin=ft.Margin(left=114, top=114, right=0, bottom=0),
                ),
            ],
            width=148,
            height=148,
        )

        # ── Hero card ─────────────────────────────────────────────────────────
        hero = ft.Container(
            content=ft.Row(
                controls=[
                    ft.Column(
                        controls=[
                            ft.Container(
                                content=ft.Row(
                                    controls=[
                                        ft.Icon(ft.Icons.ENGINEERING, size=12, color=ACCENT),
                                        ft.Text(
                                            "MECHANICAL ENGINEERING ",
                                            size=12,
                                            color=ACCENT,
                                            weight=ft.FontWeight.W_500,
                                        ),
                                    ],
                                    spacing=6,
                                    tight=True,
                                ),
                                bgcolor=f"{ACCENT}18",
                                border=ft.Border(
                                    top=ft.BorderSide(1, f"{ACCENT}35"),
                                    bottom=ft.BorderSide(1, f"{ACCENT}35"),
                                    left=ft.BorderSide(1, f"{ACCENT}35"),
                                    right=ft.BorderSide(1, f"{ACCENT}35"),
                                ),
                                border_radius=20,
                                padding=ft.Padding(left=12, right=12, top=5, bottom=5),
                            ),
                            ft.Text(
                                "MICHAEL N NGESHEYA",
                                size=40,
                                weight=ft.FontWeight.W_700,
                                color=TEXT_PRI,
                            ),
                            ft.Row(
                                controls=[
                                    ft.Icon(ft.Icons.SCHOOL_OUTLINED, size=14, color=TEXT_SEC),
                                    ft.Text(
                                        "UNAM JEDS SCHOOL OF ENGINEERING",
                                        size=13,
                                        color=TEXT_SEC,
                                        font_family="monospace",
                                    ),
                                ],
                                spacing=6,
                            ),
                            ft.Container(height=4),
                            ft.Text(
                                "Turning first principles into functional systems — from precise "
                                "CAD models to physical prototypes. Passionate about structural "
                                "analysis, thermodynamics, and mechatronics.",
                                size=13,
                                color=TEXT_SEC,
                                max_lines=4,
                            ),
                            ft.Container(height=10),
                            ft.Row(
                                controls=[
                                    ft.ElevatedButton(
                                        content=ft.Row(
                                            controls=[
                                                ft.Icon(ft.Icons.ROCKET_LAUNCH, size=14, color=BG),
                                                ft.Text("View Projects", size=13, color=BG,
                                                        weight=ft.FontWeight.W_600),
                                            ],
                                            spacing=6, tight=True,
                                        ),
                                        bgcolor=ACCENT,
                                        style=ft.ButtonStyle(
                                            shape=ft.RoundedRectangleBorder(radius=8),
                                            padding=ft.Padding(left=16, right=16, top=10, bottom=10),
                                        ),
                                    ),
                                    ft.OutlinedButton(
                                        content=ft.Row(
                                            controls=[
                                                ft.Icon(ft.Icons.DOWNLOAD_OUTLINED, size=14, color=TEXT_SEC),
                                                ft.Text("Download CV", size=13, color=TEXT_SEC),
                                            ],
                                            spacing=6, tight=True,
                                        ),
                                        style=ft.ButtonStyle(
                                            shape=ft.RoundedRectangleBorder(radius=8),
                                            side=ft.BorderSide(1, BORDER),
                                            padding=ft.Padding(left=16, right=16, top=10, bottom=10),
                                        ),
                                    ),
                                    ft.OutlinedButton(
                                        content=ft.Row(
                                            controls=[
                                                ft.Icon(ft.Icons.MAIL_OUTLINE, size=14, color=TEXT_SEC),
                                                ft.Text("Contact", size=13, color=TEXT_SEC),
                                            ],
                                            spacing=6, tight=True,
                                        ),
                                        style=ft.ButtonStyle(
                                            shape=ft.RoundedRectangleBorder(radius=8),
                                            side=ft.BorderSide(1, BORDER),
                                            padding=ft.Padding(left=16, right=16, top=10, bottom=10),
                                        ),
                                    ),
                                ],
                                spacing=10,
                                wrap=True,
                            ),
                            ft.Container(height=6),
                            ft.Row(
                                controls=[
                                    ft.TextButton(
                                        content=ft.Row(
                                            controls=[
                                                ft.Icon(ft.Icons.FOLDER_OUTLINED, size=13, color=TEXT_MUT),
                                                ft.Text("GitHub", size=12, color=TEXT_MUT),
                                            ],
                                            spacing=5, tight=True,
                                        ),
                                        style=ft.ButtonStyle(padding=ft.Padding(0, 0, 0, 0)),
                                    ),
                                    ft.Text("·", color=TEXT_MUT, size=12),
                                    ft.TextButton(
                                        content=ft.Row(
                                            controls=[
                                                ft.Icon(ft.Icons.LINK, size=13, color=TEXT_MUT),
                                                ft.Text("LinkedIn", size=12, color=TEXT_MUT),
                                            ],
                                            spacing=5, tight=True,
                                        ),
                                        style=ft.ButtonStyle(padding=ft.Padding(0, 0, 0, 0)),
                                    ),
                                    ft.Text("·", color=TEXT_MUT, size=12),
                                    ft.TextButton(
                                        content=ft.Row(
                                            controls=[
                                                ft.Icon(ft.Icons.LOCATION_ON_OUTLINED, size=13, color=TEXT_MUT),
                                                ft.Text("Your City", size=12, color=TEXT_MUT),
                                            ],
                                            spacing=5, tight=True,
                                        ),
                                        style=ft.ButtonStyle(padding=ft.Padding(0, 0, 0, 0)),
                                    ),
                                ],
                                spacing=4,
                            ),
                        ],
                        spacing=10,
                        expand=True,
                    ),
                    ft.Column(
                        controls=[profile_image],
                        horizontal_alignment=ft.CrossAxisAlignment.END,
                    ),
                ],
                alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                vertical_alignment=ft.CrossAxisAlignment.START,
            ),
            bgcolor=SURFACE,
            border=ft.Border(
                top=ft.BorderSide(1, BORDER),
                bottom=ft.BorderSide(1, BORDER),
                left=ft.BorderSide(1, BORDER),
                right=ft.BorderSide(1, BORDER),
            ),
            border_radius=14,
            padding=ft.Padding(left=28, right=28, top=28, bottom=28),
        )

        # ── Stats ─────────────────────────────────────────────────────────────
        stats = ft.Row(
            controls=[
                _stat_card("12+", "Projects Completed", ft.Icons.BUILD_OUTLINED,  ACCENT),
                _stat_card("2nd", "Year of Study",      ft.Icons.SCHOOL_OUTLINED, BLUE),
                _stat_card("3.8", "GPA / 4.0",          ft.Icons.STAR_OUTLINE,    ORANGE),
                _stat_card("2×",  "Internships",        ft.Icons.WORK_OUTLINE,    ACCENT),
            ],
            spacing=12,
        )

        # ── Projects ──────────────────────────────────────────────────────────
        projects_section = ft.Column(
            controls=[
                _section_label("Featured Projects"),
                ft.Row(
                    controls=[
                        _project_card(
                            "01",
                            "Suspension Bracket Redesign",
                            "FEA-driven redesign achieving 22% mass reduction while maintaining fatigue safety factors above 2.5.",
                            ["SolidWorks", "ANSYS", "FEA"],
                            ft.Icons.SETTINGS_OUTLINED,
                            ACCENT,
                        ),
                        _project_card(
                            "02",
                            "Autonomous Line-Following Robot",
                            "Designed chassis & drivetrain; implemented PID control loop for real-time path correction.",
                            ["Arduino", "PID", "3D Print"],
                            ft.Icons.SMART_TOY_OUTLINED,
                            BLUE,
                        ),
                        _project_card(
                            "03",
                            "Heat Exchanger Analysis",
                            "Built & tested shell-and-tube HX; validated empirical data against LMTD and NTU-effectiveness models.",
                            ["MATLAB", "Thermodynamics"],
                            ft.Icons.THERMOSTAT,
                            ORANGE,
                        ),
                    ],
                    spacing=12,
                ),
            ],
            spacing=14,
        )

        # ── Skills ────────────────────────────────────────────────────────────
        skills_section = ft.Column(
            controls=[
                _section_label("Technical Skills"),
                ft.Container(
                    content=ft.Row(
                        controls=[
                            ft.Column(
                                controls=[
                                    _skill_bar("SolidWorks",        90, ACCENT),
                                    _skill_bar("ANSYS / FEA",       70, ACCENT),
                                    _skill_bar("AutoCAD",           75, ACCENT),
                                ],
                                spacing=16,
                                expand=True,
                            ),
                            ft.Container(width=40),
                            ft.Column(
                                controls=[
                                    _skill_bar("MATLAB",            80, BLUE),
                                    _skill_bar("Python",            65, BLUE),
                                    _skill_bar("3D Printing / FDM", 85, BLUE),
                                ],
                                spacing=16,
                                expand=True,
                            ),
                        ],
                    ),
                    bgcolor=SURFACE,
                    border=ft.Border(
                        top=ft.BorderSide(1, BORDER),
                        bottom=ft.BorderSide(1, BORDER),
                        left=ft.BorderSide(1, BORDER),
                        right=ft.BorderSide(1, BORDER),
                    ),
                    border_radius=12,
                    padding=ft.Padding(left=24, right=24, top=20, bottom=20),
                ),
            ],
            spacing=14,
        )

        # ── About ─────────────────────────────────────────────────────────────
        about_section = ft.Column(
            controls=[
                _section_label("About Me"),
                ft.Row(
                    controls=[
                        ft.Container(
                            content=ft.Column(
                                controls=[
                                    ft.Row(
                                        controls=[
                                            ft.Icon(ft.Icons.PERSON_OUTLINE, size=15, color=ACCENT),
                                            ft.Text("Background", size=12, color=TEXT_PRI,
                                                    weight=ft.FontWeight.W_600),
                                        ],
                                        spacing=8,
                                    ),
                                    ft.Text(
                                        "Second-year Mechanical Engineering student focused on design, "
                                        "simulation, and manufacturing. I enjoy bridging theory and the "
                                        "physical world through hands-on projects and prototyping.",
                                        size=13, color=TEXT_SEC,
                                    ),
                                ],
                                spacing=10,
                            ),
                            bgcolor=SURFACE,
                            border=ft.Border(
                                top=ft.BorderSide(1, BORDER),
                                bottom=ft.BorderSide(1, BORDER),
                                left=ft.BorderSide(1, BORDER),
                                right=ft.BorderSide(1, BORDER),
                            ),
                            border_radius=12,
                            padding=18,
                            expand=True,
                        ),
                        ft.Container(
                            content=ft.Column(
                                controls=[
                                    ft.Row(
                                        controls=[
                                            ft.Icon(ft.Icons.LIGHTBULB_OUTLINE, size=15, color=BLUE),
                                            ft.Text("Currently Exploring", size=12, color=TEXT_PRI,
                                                    weight=ft.FontWeight.W_600),
                                        ],
                                        spacing=8,
                                    ),
                                    ft.Row(
                                        controls=[
                                            _chip("Composite Materials",    BLUE),
                                            _chip("Topology Optimisation",  BLUE),
                                            _chip("Embedded Systems",       BLUE),
                                            _chip("Robotics",               BLUE),
                                        ],
                                        wrap=True,
                                        spacing=8,
                                        run_spacing=8,
                                    ),
                                ],
                                spacing=12,
                            ),
                            bgcolor=SURFACE,
                            border=ft.Border(
                                top=ft.BorderSide(1, BORDER),
                                bottom=ft.BorderSide(1, BORDER),
                                left=ft.BorderSide(1, BORDER),
                                right=ft.BorderSide(1, BORDER),
                            ),
                            border_radius=12,
                            padding=18,
                            expand=True,
                        ),
                    ],
                    spacing=12,
                ),
            ],
            spacing=14,
        )

        # ── Contact strip ─────────────────────────────────────────────────────
        contact = ft.Container(
            content=ft.Row(
                controls=[
                    ft.Column(
                        controls=[
                            ft.Text("Open to opportunities", size=16,
                                    weight=ft.FontWeight.W_700, color=TEXT_PRI),
                            ft.Text("Internships · Research · Collaborations",
                                    size=12, color=TEXT_SEC),
                        ],
                        spacing=4,
                        expand=True,
                    ),
                    ft.ElevatedButton(
                        content=ft.Row(
                            controls=[
                                ft.Icon(ft.Icons.MAIL_OUTLINE, size=14, color=BG),
                                ft.Text("Get in touch", size=13, color=BG,
                                        weight=ft.FontWeight.W_600),
                            ],
                            spacing=6, tight=True,
                        ),
                        bgcolor=ACCENT,
                        style=ft.ButtonStyle(
                            shape=ft.RoundedRectangleBorder(radius=8),
                            padding=ft.Padding(left=18, right=18, top=10, bottom=10),
                        ),
                    ),
                ],
                alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                vertical_alignment=ft.CrossAxisAlignment.CENTER,
            ),
            bgcolor=f"{ACCENT}12",
            border=ft.Border(
                top=ft.BorderSide(1, f"{ACCENT}40"),
                bottom=ft.BorderSide(1, f"{ACCENT}40"),
                left=ft.BorderSide(1, f"{ACCENT}40"),
                right=ft.BorderSide(1, f"{ACCENT}40"),
            ),
            border_radius=12,
            padding=ft.Padding(left=24, right=24, top=20, bottom=20),
        )

        return ft.Column(
            controls=[
                hero,
                stats,
                projects_section,
                skills_section,
                about_section,
                contact,
            ],
            spacing=28,
        )