import flet as ft
import math

# ── Shared dark palette ───────────────────────────────────────────────────────
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
    words   = len(content.split())
    minutes = max(1, math.ceil(words / 200))
    return f"{minutes} min read"


def _hoverable(container: ft.Container, accent_color: str) -> ft.Container:
    container.animate = 200

    def on_hover(e, c=container, col=accent_color):
        if e.data == "true":
            c.bgcolor = SURFACE2
            c.border  = ft.Border.all(1, col)
            c.shadow  = ft.BoxShadow(spread_radius=0, blur_radius=18,
                                     color=col + "33", offset=ft.Offset(0, 4))
        else:
            c.bgcolor = SURFACE
            c.border  = ft.Border.all(1, BORDER)
            c.shadow  = None
        c.update()

    container.on_hover = on_hover
    return container


def _get_video_id(url: str) -> str:
    if "v=" in url:
        return url.split("v=")[-1].split("&")[0]
    if "youtu.be/" in url:
        return url.split("youtu.be/")[-1].split("?")[0]
    return ""


class BlogPage:
    POSTS = [
        {
            "title": "Understanding the Total Cost Formula",
            "date": "1 June 2026",
            "summary": "A breakdown of how we calculate project costs using summation notation.",
            "content": (
                "## Total Cost Formula\n\n"
                "Total Cost = \u03a3 (Q\u1d62 \u00d7 P\u1d62) + Overheads\n\n"
                "Where:\n"
                "- Q\u1d62 = quantity of material i\n"
                "- P\u1d62 = unit price of material i\n"
                "- Overheads = fixed project overhead costs\n\n"
                "### Python Implementation\n\n"
                "```python\n"
                "def calculate_total_cost(quantities, prices, overheads):\n"
                "    material_cost = sum(q * p for q, p in zip(quantities, prices))\n"
                "    return material_cost + overheads\n"
                "```\n"
            ),
            "video_url": "https://www.youtube.com/watch?v=XJkIaw2e1Pw",
            "video_thumb": "https://img.youtube.com/vi/XJkIaw2e1Pw/hqdefault.jpg",
            "tags": ["Python", "Maths", "Mechanical Engineering"],
        },
        {
            "title": "How Git Branching Saved Our Project",
            "date": "2 June 2026",
            "summary": "Why we used feature branches and how pull requests kept our 20-person team in sync.",
            "content": (
                "## Git Branching Strategy\n\n"
                "1. main - stable, deployable code only\n"
                "2. dev - integration branch for testing\n"
                "3. feature/your-name-feature - individual work branches\n\n"
                "No one broke main accidentally. Every merge required a code review, "
                "catching 3 critical bugs before production.\n"
            ),
            "video_url": "https://www.youtube.com/watch?v=e9lnsKot_SQ",
            "video_thumb": "https://img.youtube.com/vi/e9lnsKot_SQ/hqdefault.jpg",
            "tags": ["Git", "Collaboration", "Best Practices"],
        },
        {
            "title": "Loops and List Comprehensions in Python",
            "date": "3 June 2026",
            "summary": "Exploring the difference between for-loops and list comprehensions.",
            "content": (
                "## For-loops vs List Comprehensions\n\n"
                "```python\n"
                "# Traditional loop\n"
                "costs = []\n"
                "for q, p in zip(quantities, prices):\n"
                "    costs.append(q * p)\n\n"
                "# List comprehension\n"
                "costs = [q * p for q, p in zip(quantities, prices)]\n"
                "```\n\n"
                "The comprehension is faster, more readable, and uses less memory.\n"
            ),
            "video_url": "https://www.youtube.com/watch?v=YlY2g2xrl6Q",
            "video_thumb": "https://img.youtube.com/vi/YlY2g2xrl6Q/hqdefault.jpg",
            "tags": ["Python", "Programming Concepts"],
        },
        {
            "title": "Functions and Modular Code Design",
            "date": "4 June 2026",
            "summary": "How breaking code into functions made our engineering app easier to test and maintain.",
            "content": (
                "## Why Functions Matter\n\n"
                "```python\n"
                "def compute_area(length, width):\n"
                "    return length * width\n\n"
                "def compute_volume(area, depth):\n"
                "    return area * depth\n\n"
                "def compute_cost(volume, unit_price, overheads):\n"
                "    return volume * unit_price + overheads\n"
                "```\n\n"
                "Each function can now be tested independently.\n"
            ),
            "video_url": "https://www.youtube.com/watch?v=89cGQjB5R4M",
            "video_thumb": "https://img.youtube.com/vi/89cGQjB5R4M/hqdefault.jpg",
            "tags": ["Python", "Programming Concepts", "Best Practices"],
        },
        {
            "title": "Introduction to MATLAB Matrices",
            "date": "6 June 2026",
            "summary": "How MATLAB's matrix operations simplified our signal processing calculations.",
            "content": (
                "## Matrices in MATLAB\n\n"
                "```matlab\n"
                "A = [1 2 3; 4 5 6; 7 8 9];\n"
                "B = A';          % Transpose\n"
                "C = A * B;       % Matrix multiplication\n"
                "```\n\n"
                "In signal processing, filters are represented as matrices enabling fast convolution.\n"
            ),
            "video_url": "https://www.youtube.com/watch?v=eilJQja9qLU",
            "video_thumb": "https://img.youtube.com/vi/eilJQja9qLU/hqdefault.jpg",
            "tags": ["MATLAB", "Maths", "Signal Processing"],
        },
        {
            "title": "Version Control Best Practices for Teams",
            "date": "7 June 2026",
            "summary": "Lessons learned from managing a 20-person codebase.",
            "content": (
                "## Version Control in Large Teams\n\n"
                "- feat: add cost calculator module\n"
                "- fix: correct volume formula\n"
                "- docs: update README\n"
                "- refactor: simplify material loop logic\n\n"
                "We merged 47 pull requests with zero broken builds on main.\n"
            ),
            "video_url": "https://www.youtube.com/watch?v=ZBexzpgj1GE",
            "video_thumb": "https://img.youtube.com/vi/ZBexzpgj1GE/hqdefault.jpg",
            "tags": ["Git", "Collaboration", "Best Practices"],
        },
    ]

    ALL_TAGS = sorted({tag for post in POSTS for tag in post["tags"]})

    def __init__(self):
        self._active_tag = None
        self._cards_ref  = ft.Ref[ft.Column]()

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

    def _build_video_section(self, video_url, thumb_url):
        def open_video(e):
            import webbrowser
            webbrowser.open(video_url)

        return ft.Container(
            content=ft.Column(controls=[
                ft.Text("📹 Video Reference", size=13,
                        weight=ft.FontWeight.W_600, color=TEXT_PRI),
                ft.Container(
                    content=ft.Stack(controls=[
                        ft.Image(
                            src=thumb_url,
                            fit="cover",
                            width=float("inf"),
                            height=180,
                        ),
                        ft.Container(
                            content=ft.Icon(ft.Icons.PLAY_CIRCLE_FILLED, color="#FFFFFF", size=56),
                            alignment=ft.Alignment(0, 0),
                            bgcolor="#00000066",
                            expand=True,
                        ),
                    ]),
                    border_radius=8,
                    clip_behavior=ft.ClipBehavior.HARD_EDGE,
                    height=180,
                    on_click=open_video,
                    ink=True,
                ),
                ft.Text("▶ Click the thumbnail to watch on YouTube", size=11, color=ACCENT, italic=True),
            ], spacing=6),
            bgcolor=SURFACE2, border_radius=8,
            padding=ft.Padding(left=12, right=12, top=12, bottom=12),
            margin=ft.Margin(left=0, right=0, top=8, bottom=0),
            border=ft.Border.all(1, BORDER),
        )

    def _build_post_card(self, post):
        read_time   = _estimate_read_time(post["content"])
        content_col = ft.Column(
            controls=[ft.Markdown(post["content"], selectable=True,
                                  extension_set="gitHubFlavored",
                                  code_theme="atom-one-dark")],
            visible=False,
        )
        if post.get("video_url") and post.get("video_thumb"):
            content_col.controls.append(
                self._build_video_section(post["video_url"], post["video_thumb"])
            )

        btn_text   = ft.Text("Read more ▾", color=ACCENT, size=13)
        expand_btn = ft.TextButton(content=btn_text)

        def toggle_expand(e, cc=content_col, bt=btn_text):
            cc.visible = not cc.visible
            bt.value   = "Read less ▴" if cc.visible else "Read more ▾"
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

    def _rebuild_cards(self, page):
        filtered = (self.POSTS if self._active_tag is None
                    else [p for p in self.POSTS if self._active_tag in p["tags"]])
        self._cards_ref.current.controls = [self._build_post_card(p) for p in filtered]
        page.update()

    def _make_filter_row(self, page):
        all_labels = ["All"] + self.ALL_TAGS

        def make_handler(label):
            def handler(e):
                self._active_tag = None if label == "All" else label
                filter_row.controls = [self._filter_chip(l, make_handler(l)) for l in all_labels]
                self._rebuild_cards(page)
            return handler

        filter_row = ft.Row(
            controls=[self._filter_chip(l, make_handler(l)) for l in all_labels],
            spacing=8, wrap=True,
        )
        return filter_row

    def build(self, page=None):
        hero = _hoverable(
            ft.Container(
                content=ft.Column(controls=[
                    ft.Row(controls=[
                        ft.Icon(ft.Icons.ARTICLE, color=TEXT_PRI, size=28),
                        ft.Text("Technical Blog", size=24, weight=ft.FontWeight.W_700, color=TEXT_PRI),
                    ], spacing=10),
                    ft.Text("Confidence in Concepts — written explanations of core programming and engineering topics.",
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

        cards_col  = ft.Column(ref=self._cards_ref,
                               controls=[self._build_post_card(p) for p in self.POSTS],
                               spacing=0)
        filter_row = self._make_filter_row(page) if page else ft.Row(spacing=8)

        return ft.Column(controls=[
            hero,
            ft.Text("Filter by Topic", size=13, weight=ft.FontWeight.W_600, color=TEXT_SEC),
            filter_row,
            ft.Divider(height=16, color="transparent"),
            cards_col,
        ], spacing=8, scroll=ft.ScrollMode.AUTO)