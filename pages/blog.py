import flet as ft
import math
import subprocess
import os

BG       = "#0D1117"
SURFACE  = "#161B22"
SURFACE2 = "#1C2128"
BORDER   = "#30363D"
TEXT_PRI = "#E6EDF3"
TEXT_SEC = "#8B949E"
ACCENT   = "#3FB950"
ACCENT_B = "#238636"
BLUE     = "#58A6FF"

def _estimate_read_time(content: str) -> str:
    words = len(content.split())
    minutes = max(1, math.ceil(words / 200))
    return f"{minutes} min read"

def _hoverable(container: ft.Container, accent_color: str) -> ft.Container:
    container.animate = 200
    def on_hover(e):
        if e.data == "true":
            container.bgcolor = SURFACE2
            container.border = ft.Border.all(1, accent_color)
            container.shadow = ft.BoxShadow(
                spread_radius=0, blur_radius=18,
                color=accent_color + "33", offset=ft.Offset(0, 4)
            )
        else:
            container.bgcolor = SURFACE
            container.border = ft.Border.all(1, BORDER)
            container.shadow = None
        container.update()
    container.on_hover = on_hover
    return container

class BlogPage:
    POSTS = [
        {
            "title": "Understanding the Total Cost Formula",
            "date": "15 Feb 2026",
            "summary": "A breakdown of how we calculate project costs using summation notation and Python.",
            "content": (
                "## Total Cost Formula\n\n"
                "Total Cost = Sum(Qi x Pi) + Overheads\n\n"
                "Where:\n"
                "- Qi = quantity of material i\n"
                "- Pi = unit price of material i\n"
                "- Overheads = fixed project overhead costs\n\n"
                "### Python Implementation\n\n"
                "\`\`\`python\n"
                "def calculate_total_cost(quantities, prices, overheads):\n"
                "    material_cost = sum(q * p for q, p in zip(quantities, prices))\n"
                "    return material_cost + overheads\n"
                "\`\`\`\n"
            ),
            "video_url": "https://www.youtube.com/watch?v=XJkIaw2e1Pw",
            "video_thumb": "https://img.youtube.com/vi/XJkIaw2e1Pw/hqdefault.jpg",
            "local_video": None,
            "tags": ["Python", "Maths", "Civil Engineering"],
        },
        {
            "title": "How Git Branching Saved Our Project",
            "date": "22 Feb 2026",
            "summary": "Why we used feature branches and how pull requests kept our 20-person team in sync.",
            "content": (
                "## Git Branching Strategy\n\n"
                "1. main - stable, deployable code only\n"
                "2. dev - integration branch for testing\n"
                "3. feature/your-name-feature - individual work branches\n\n"
                "No one pushed directly to main. Every merge required a pull request and code review, "
                "which caught 3 critical bugs before they reached production.\n\n"
                "\`\`\`bash\n"
                "git checkout -b feature/admin-panel-screen\n"
                "git commit -m 'feat: add admin panel layout'\n"
                "git push origin feature/admin-panel-screen\n"
                "\`\`\`\n"
            ),
            "video_url": "https://www.youtube.com/watch?v=e2IbNHi4uCI",
            "video_thumb": "https://img.youtube.com/vi/e2IbNHi4uCI/hqdefault.jpg",
            "local_video": None,
            "tags": ["Git", "Collaboration", "Best Practices"],
        },
        {
            "title": "Loops and List Comprehensions in Python",
            "date": "1 Mar 2026",
            "summary": "Exploring the difference between for-loops and list comprehensions.",
            "content": (
                "## For-loops vs List Comprehensions\n\n"
                "\`\`\`python\n"
                "costs = []\n"
                "for q, p in zip(quantities, prices):\n"
                "    costs.append(q * p)\n\n"
                "costs = [q * p for q, p in zip(quantities, prices)]\n"
                "\`\`\`\n\n"
                "List comprehensions are faster, more readable, and use less memory.\n"
            ),
            "video_url": "https://www.youtube.com/watch?v=_f3qQgOU6No",
            "video_thumb": "https://img.youtube.com/vi/_f3qQgOU6No/hqdefault.jpg",
            "local_video": None,
            "tags": ["Python", "Programming Concepts"],
        },
        {
            "title": "Functions and Modular Code Design",
            "date": "8 Mar 2026",
            "summary": "How breaking code into functions made our engineering app easier to test and maintain.",
            "content": (
                "## Why Functions Matter\n\n"
                "\`\`\`python\n"
                "def compute_area(length, width):\n"
                "    return length * width\n\n"
                "def compute_volume(area, depth):\n"
                "    return area * depth\n\n"
                "def compute_cost(volume, unit_price, overheads):\n"
                "    return volume * unit_price + overheads\n"
                "\`\`\`\n\n"
                "Each function does one thing only, making testing and debugging easier.\n"
            ),
            "video_url": "https://www.youtube.com/watch?v=89cGQjB5R4M",
            "video_thumb": "https://img.youtube.com/vi/89cGQjB5R4M/hqdefault.jpg",
            "local_video": None,
            "tags": ["Python", "Programming Concepts", "Best Practices"],
        },
        {
            "title": "Introduction to MATLAB Matrices",
            "date": "15 Mar 2026",
            "summary": "How MATLAB matrix operations simplified our signal processing calculations.",
            "content": (
                "## Matrices in MATLAB\n\n"
                "\`\`\`matlab\n"
                "A = [1 2 3; 4 5 6; 7 8 9];\n"
                "B = A'\n"
                "C = A * B;\n"
                "\`\`\`\n\n"
                "MATLAB makes matrix operations fast and readable for engineering applications.\n"
            ),
            "video_url": "https://www.youtube.com/watch?v=eilJQja9qLU",
            "video_thumb": "https://img.youtube.com/vi/eilJQja9qLU/hqdefault.jpg",
            "local_video": None,
            "tags": ["MATLAB", "Maths", "Signal Processing"],
        },
        {
            "title": "Version Control Best Practices for Teams",
            "date": "22 Mar 2026",
            "summary": "Lessons learned from managing a 20-person codebase with zero broken builds on main.",
            "content": (
                "## Version Control in Large Teams\n\n"
                "\`\`\`text\n"
                "feat: add cost calculator module\n"
                "fix: correct volume formula\n"
                "docs: update README\n"
                "\`\`\`\n\n"
                "We merged 47 pull requests with zero broken builds on main.\n"
            ),
            "video_url": "https://www.youtube.com/watch?v=0vzYWyHmcY8",
            "video_thumb": "https://img.youtube.com/vi/0vzYWyHmcY8/hqdefault.jpg",
            "local_video": None,
            "tags": ["Git", "Collaboration", "Best Practices"],
        },
        {
            "title": "My Role in Building FixFlow",
            "date": "12 Jun 2026",
            "summary": "A walkthrough of my contributions to FixFlow, a React Native water leak reporting app for Ongwediva.",
            "content": (
                "## FixFlow — Water Leak Reporting App\n\n"
                "Built with React Native for the Ongwediva community.\n\n"
                "### My Contributions\n\n"
                "- Built the AdminPanelScreen\n"
                "- 15 commits on feature/admin-panel-screen branch\n"
                "- Submitted PR #21 for team review\n\n"
                "\`\`\`text\n"
                "Frontend:  React Native + Expo\n"
                "Auth:      Firebase Authentication\n"
                "Database:  Firebase Firestore\n"
                "Maps:      Google Maps API\n"
                "\`\`\`\n"
            ),
            "local_video": None,
            "video_url": "https://drive.google.com/file/d/1uEXD0AP0FkDZLDlWFYCt1_Nt5-w4tq1l/view?usp=sharing",
            "video_thumb": "https://drive.google.com/thumbnail?id=1uEXD0AP0FkDZLDlWFYCt1_Nt5-w4tq1l&sz=w480-h270",
            "tags": ["React Native", "FixFlow", "Teamwork", "Git"],
        },
    ]

    ALL_TAGS = sorted({tag for post in POSTS for tag in post["tags"]})

    def __init__(self):
        self._active_tag = None
        self._page = None

    def _tag_chip(self, label):
        return ft.Container(
            content=ft.Text(label, size=11, color=BLUE),
            bgcolor=BLUE + "22",
            padding=ft.Padding(left=10, right=10, top=4, bottom=4),
            border_radius=20,
            border=ft.Border.all(1, BLUE + "44"),
        )

    def _filter_chip(self, label, on_click):
        is_all = label == "All"
        active = (is_all and self._active_tag is None) or (label == self._active_tag)
        return ft.Container(
            content=ft.Text(label, size=12,
                            color=BG if active else TEXT_SEC,
                            weight=ft.FontWeight.W_600 if active else ft.FontWeight.W_400),
            bgcolor=ACCENT if active else SURFACE,
            padding=ft.Padding(left=14, right=14, top=6, bottom=6),
            border_radius=20,
            border=ft.Border.all(1, ACCENT if active else BORDER),
            on_click=on_click,
            ink=True,
        )

    def _build_local_video_section(self, video_path: str):
        full_path = os.path.abspath(video_path)
        def on_play_click(e):
            try:
                subprocess.Popen(["cmd", "/c", "start", "", full_path])
            except Exception:
                pass
        play_btn = ft.Container(
            content=ft.Icon(ft.Icons.PLAY_CIRCLE_FILL, size=56, color="#FFFFFF"),
            alignment=ft.Alignment(0, 0),
            bgcolor="#00000066",
            border_radius=8,
            on_click=on_play_click,
            ink=True,
            expand=True,
        )
        thumb = ft.Container(
            bgcolor="#1C2128",
            border_radius=8,
            height=180,
            expand=True,
            content=ft.Column(
                controls=[
                    ft.Icon(ft.Icons.VIDEOCAM, size=48, color=TEXT_SEC),
                    ft.Text("FixFlow Demo", size=13, color=TEXT_SEC),
                ],
                alignment=ft.MainAxisAlignment.CENTER,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            ),
        )
        video_stack = ft.Stack(controls=[thumb, play_btn], height=180)
        return ft.Container(
            content=ft.Column(controls=[
                ft.Text("Demo Video", size=13, weight=ft.FontWeight.W_600, color=TEXT_PRI),
                video_stack,
                ft.TextButton("Open Demo Video", on_click=on_play_click,
                              style=ft.ButtonStyle(color=ACCENT)),
            ], spacing=6),
            bgcolor=SURFACE2, border_radius=8,
            padding=ft.Padding(left=12, right=12, top=12, bottom=12),
            margin=ft.Margin(left=0, right=0, top=8, bottom=0),
            border=ft.Border.all(1, BORDER),
        )

    def _build_video_section(self, video_url: str, thumb_url: str, page_ref=None):
        def on_play_click(e):
            import asyncio
            async def _open():
                await e.page.launch_url(video_url)
            asyncio.run_coroutine_threadsafe(_open(), e.page.loop)

        # Thumbnail fills the full width, cropped to 180px height
        thumb_img = ft.Container(
            content=ft.Image(
                src=thumb_url,
                fit="cover",
                width=float("inf"),
                height=180,
            ),
            height=180,
            clip_behavior=ft.ClipBehavior.HARD_EDGE,
            border_radius=8,
            expand=True,
        )

        play_overlay = ft.Container(
            content=ft.Icon(ft.Icons.PLAY_CIRCLE_FILL, size=64, color="#FFFFFF"),
            alignment=ft.Alignment(0, 0),
            bgcolor="#00000055",
            border_radius=8,
            on_click=on_play_click,
            ink=True,
            expand=True,
        )

        video_stack = ft.Stack(controls=[thumb_img, play_overlay], height=180)

        return ft.Container(
            content=ft.Column(controls=[
                ft.Text("Video Reference", size=13, weight=ft.FontWeight.W_600, color=TEXT_PRI),
                video_stack,
                ft.TextButton("Click to watch on Google Drive", on_click=on_play_click,
                              style=ft.ButtonStyle(color=ACCENT)),
            ], spacing=6),
            bgcolor=SURFACE2, border_radius=8,
            padding=ft.Padding(left=12, right=12, top=12, bottom=12),
            margin=ft.Margin(left=0, right=0, top=8, bottom=0),
            border=ft.Border.all(1, BORDER),
        )

    def _build_post_card(self, post):
        read_time = _estimate_read_time(post["content"])
        content_col = ft.Column(
            controls=[ft.Markdown(post["content"], selectable=True,
                                  extension_set="gitHubFlavored",
                                  code_theme="atom-one-dark")],
            visible=False,
        )
        if post.get("local_video"):
            content_col.controls.append(self._build_local_video_section(post["local_video"]))
        elif post.get("video_url") and post.get("video_thumb"):
            content_col.controls.append(self._build_video_section(post["video_url"], post["video_thumb"]))

        btn_text = ft.Text("Read more", color=ACCENT, size=13)
        expand_btn = ft.TextButton(content=btn_text)

        def toggle_expand(e, cc=content_col, bt=btn_text):
            cc.visible = not cc.visible
            bt.value = "Read less" if cc.visible else "Read more"
            e.page.update()

        expand_btn.on_click = toggle_expand

        return _hoverable(
            ft.Container(
                content=ft.Column(controls=[
                    ft.Row(controls=[
                        ft.Text(post["title"], size=15, weight=ft.FontWeight.W_700,
                                color=TEXT_PRI, expand=True),
                        ft.Text(post["date"], size=12, color=TEXT_SEC),
                    ]),
                    ft.Row(controls=[
                        ft.Icon(ft.Icons.ACCESS_TIME, size=13, color=TEXT_SEC),
                        ft.Text(read_time, size=12, color=TEXT_SEC),
                    ], spacing=4),
                    ft.Text(post["summary"], size=13, color=TEXT_SEC),
                    ft.Row(controls=[self._tag_chip(t) for t in post["tags"]], spacing=6, wrap=True),
                    content_col,
                    expand_btn,
                ], spacing=8),
                bgcolor=SURFACE, border_radius=12,
                padding=ft.Padding(left=16, right=16, top=16, bottom=16),
                border=ft.Border.all(1, BORDER),
                margin=ft.Margin(left=0, right=0, top=0, bottom=12),
            ),
            BLUE,
        )

    def build(self, page):
        self._page = page
        self._active_tag = None
        all_labels = ["All"] + self.ALL_TAGS
        cards_col = ft.Column(controls=[], spacing=0)

        def rebuild_cards():
            filtered = (self.POSTS if self._active_tag is None
                        else [p for p in self.POSTS if self._active_tag in p["tags"]])
            cards_col.controls = [self._build_post_card(p) for p in filtered]
            page.update()

        def make_handler(label):
            def handler(e):
                self._active_tag = None if label == "All" else label
                filter_row.controls = [self._filter_chip(l, make_handler(l)) for l in all_labels]
                rebuild_cards()
            return handler

        filter_row = ft.Row(
            controls=[self._filter_chip(l, make_handler(l)) for l in all_labels],
            spacing=8, wrap=True,
        )
        rebuild_cards()

        hero = _hoverable(
            ft.Container(
                content=ft.Column(controls=[
                    ft.Row(controls=[
                        ft.Icon(ft.Icons.ARTICLE, color=TEXT_PRI, size=28),
                        ft.Text("Technical Blog", size=24, weight=ft.FontWeight.W_700, color=TEXT_PRI),
                    ], spacing=10),
                    ft.Text("Confidence in Concepts - written explanations of core programming and engineering topics.",
                            size=13, color=TEXT_SEC),
                    ft.Row(controls=[
                        ft.Container(
                            content=ft.Text(f"{len(self.POSTS)} Posts", size=12, color=ACCENT),
                            bgcolor=ACCENT_B + "33",
                            padding=ft.Padding(left=12, right=12, top=4, bottom=4),
                            border_radius=20,
                            border=ft.Border.all(1, ACCENT_B),
                        ),
                        ft.Container(
                            content=ft.Text(f"{len(self.ALL_TAGS)} Topics", size=12, color=BLUE),
                            bgcolor=BLUE + "22",
                            padding=ft.Padding(left=12, right=12, top=4, bottom=4),
                            border_radius=20,
                            border=ft.Border.all(1, BLUE + "44"),
                        ),
                    ], spacing=8),
                ], spacing=8),
                bgcolor=SURFACE, border_radius=16,
                padding=ft.Padding(left=24, right=24, top=24, bottom=24),
                margin=ft.Margin(left=0, right=0, top=0, bottom=16),
                border=ft.Border.all(1, BORDER),
            ),
            ACCENT,
        )

        return ft.Column(controls=[
            hero,
            ft.Text("Filter by Topic", size=13, weight=ft.FontWeight.W_600, color=TEXT_SEC),
            filter_row,
            ft.Divider(height=16, color="transparent"),
            cards_col,
        ], spacing=8, scroll=ft.ScrollMode.AUTO)