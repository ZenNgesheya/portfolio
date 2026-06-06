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
BLUE     = "#58A6FF"
AMBER    = "#D29922"
PURPLE   = "#A371F7"
RED      = "#F85149"


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


class GithubPage:
    COMMITS = [
        {"hash": "9ba816e", "message": "chore: update gitignore configuration",                   "date": "6 Jun 2026", "branch": "feature/verify-location-screen"},
        {"hash": "5242bc9", "message": "chore: update app.json configuration",                    "date": "6 Jun 2026", "branch": "feature/verify-location-screen"},
        {"hash": "2805f05", "message": "feat: add VerifyLocationScreen base structure and imports","date": "6 Jun 2026", "branch": "feature/verify-location-screen"},
        {"hash": "5d85ae3", "message": "feat: add location verification logic with error handling","date": "6 Jun 2026", "branch": "feature/verify-location-screen"},
        {"hash": "dcf8737", "message": "feat: add loading and success UI states",                  "date": "6 Jun 2026", "branch": "feature/verify-location-screen"},
        {"hash": "c6270c2", "message": "feat: add error UI state with retry button",               "date": "6 Jun 2026", "branch": "feature/verify-location-screen"},
        {"hash": "e969bc3", "message": "style: add complete stylesheet for VerifyLocationScreen",  "date": "6 Jun 2026", "branch": "feature/verify-location-screen"},
        {"hash": "169a0d6", "message": "fix: resolve merge conflict in gitignore",                 "date": "6 Jun 2026", "branch": "feature/verify-location-screen"},
        {"hash": "bafb226", "message": "chore: update app name and slug to Fix-Flow",              "date": "6 Jun 2026", "branch": "feature/app-config"},
        {"hash": "68af86a", "message": "chore: update splash color and UI interface style",        "date": "6 Jun 2026", "branch": "feature/app-config"},
        {"hash": "2bf0371", "message": "chore: add iOS bundle identifier and tablet support",      "date": "6 Jun 2026", "branch": "feature/app-config"},
        {"hash": "0891f33", "message": "chore: add VIBRATE and RECEIVE_BOOT_COMPLETED permissions","date": "6 Jun 2026", "branch": "feature/app-config"},
        {"hash": "06903ae", "message": "chore: add app description to config",                    "date": "6 Jun 2026", "branch": "feature/app-config"},
        {"hash": "16fcc09", "message": "chore: add owner and primary color to app config",         "date": "6 Jun 2026", "branch": "feature/app-config"},
        {"hash": "98fdf13", "message": "chore: add Android versionCode and SDK target versions",   "date": "6 Jun 2026", "branch": "feature/app-config"},
        {"hash": "2ad48c8", "message": "chore: add deep link scheme and background color",         "date": "6 Jun 2026", "branch": "feature/app-config"},
        {"hash": "e2c0ff7", "message": "chore: add EAS project configuration",                    "date": "6 Jun 2026", "branch": "feature/app-config"},
        {"hash": "12365cd", "message": "chore: add Google Services file reference for Firebase",   "date": "6 Jun 2026", "branch": "feature/app-config"},
        {"hash": "b79cf83", "message": "chore: merge PR #15 feature/app-config into main",         "date": "6 Jun 2026", "branch": "feature/app-config"},
    ]

    PULL_REQUESTS = [
        {"pr_number": "#14", "title": "Feature/verify location screen", "status": "Merged",
         "commits": 8, "reviews": "Reviewed by: @git-user01nf",
         "description": "Added the full VerifyLocationScreen component with GPS-based location verification, loading/success/error UI states, auto-redirect on success, and retry functionality for users outside the Ongwediva service area."},
        {"pr_number": "#15", "title": "Feature/app config", "status": "Merged",
         "commits": 11, "reviews": "Reviewed by: @git-user01nf",
         "description": "Complete app.json configuration for Fix-Flow including app name, slug, iOS/Android settings, permissions, EAS config, deep link scheme, and Google Services file reference."},
    ]

    WEEKLY_COMMITS = [
        {"week": "20 Jan", "count": 0},
        {"week": "27 Jan", "count": 0},
        {"week": "3 Feb",  "count": 0},
        {"week": "10 Feb", "count": 0},
        {"week": "1 Jun",  "count": 0},
        {"week": "6 Jun",  "count": 19},
    ]

    IMPACT_SUMMARY = (
        "My contributions to the FixFlow group project covered two key areas:\n\n"
        "**1. VerifyLocationScreen (PR #14 — 8 commits)**\n"
        "Built the GPS-based location gate that restricts app access to users within Ongwediva. "
        "Implemented loading, success, and error UI states with auto-redirect and retry functionality.\n\n"
        "**2. App Configuration (PR #15 — 11 commits)**\n"
        "Configured the complete app.json for Fix-Flow including iOS/Android settings, "
        "permissions, deep link scheme, EAS project config, and Google Services integration.\n\n"
        "This work is critical to the Civil engineering module — the location gate ensures "
        "only verified on-site users can submit water leak reports, maintaining data integrity.\n\n"
        "**Total: 19 commits · 2 PRs opened · 2 PRs merged**"
    )

    STATUS_STYLE = {
        "Merged": (ACCENT_B + "33", ACCENT, ACCENT_B),
        "Closed": (RED + "22",      RED,    RED + "55"),
        "Open":   (BLUE + "22",     BLUE,   BLUE + "44"),
    }

    BRANCH_COLORS = {
        "feature/verify-location-screen": (PURPLE + "22", PURPLE),
        "dev":                            (ACCENT_B+"22", ACCENT),
    }

    def _stat_card(self, icon, value, label, color):
        return _hoverable(
            ft.Container(
                content=ft.Column(controls=[
                    ft.Icon(icon, color=color, size=24),
                    ft.Text(value, size=22, weight=ft.FontWeight.W_700, color=TEXT_PRI),
                    ft.Text(label, size=12, color=TEXT_SEC),
                ], spacing=4, horizontal_alignment=ft.CrossAxisAlignment.CENTER),
                bgcolor=SURFACE, border_radius=12,
                padding=ft.Padding(left=16, right=16, top=16, bottom=16),
                border=ft.Border.all(1, BORDER),
                expand=True, alignment=ft.Alignment(0, 0),
            ),
            color,
        )

    def _build_contribution_graph(self):
        max_count = max(w["count"] for w in self.WEEKLY_COMMITS) or 1
        bars = []
        for w in self.WEEKLY_COMMITS:
            height = max(4, int((w["count"] / max_count) * 80))
            bars.append(ft.Column(controls=[
                ft.Text(str(w["count"]), size=11, color=TEXT_SEC, text_align=ft.TextAlign.CENTER),
                ft.Container(width=36, height=height,
                             bgcolor=ACCENT if w["count"] > 0 else BORDER,
                             border_radius=ft.BorderRadius(4, 4, 0, 0)),
                ft.Text(w["week"], size=10, color=TEXT_SEC, text_align=ft.TextAlign.CENTER),
            ], horizontal_alignment=ft.CrossAxisAlignment.CENTER, spacing=4))

        return _hoverable(
            ft.Container(
                content=ft.Column(controls=[
                    ft.Text("Contribution Activity", size=14, weight=ft.FontWeight.W_600, color=TEXT_PRI),
                    ft.Text("Commits per week — ZenNgesheya", size=12, color=TEXT_SEC),
                    ft.Container(
                        content=ft.Row(controls=bars,
                                       alignment=ft.MainAxisAlignment.SPACE_AROUND,
                                       vertical_alignment=ft.CrossAxisAlignment.END),
                        padding=ft.Padding(left=0, right=0, top=8, bottom=4),
                    ),
                ], spacing=6),
                bgcolor=SURFACE, border_radius=12,
                padding=ft.Padding(left=16, right=16, top=16, bottom=16),
                border=ft.Border.all(1, BORDER),
            ),
            ACCENT,
        )

    def _commit_row(self, c):
        bg, fg = self.BRANCH_COLORS.get(c["branch"], (SURFACE2, TEXT_SEC))
        return ft.Container(
            content=ft.Row(controls=[
                ft.Icon(ft.Icons.COMMIT, size=14, color=BLUE),
                ft.Text(c["hash"], size=12, color=BLUE, font_family="monospace", width=70),
                ft.Text(c["message"], size=13, color=TEXT_PRI, expand=True),
                ft.Text(c["date"], size=11, color=TEXT_SEC, width=90),
                ft.Container(
                    content=ft.Text(c["branch"], size=10, color=fg),
                    bgcolor=bg,
                    padding=ft.Padding(left=8, right=8, top=3, bottom=3),
                    border_radius=20,
                    border=ft.Border.all(1, fg + "55"),
                ),
            ], spacing=10),
            padding=ft.Padding(left=12, right=12, top=10, bottom=10),
            border=ft.Border(bottom=ft.BorderSide(1, BORDER)),
        )

    def _pr_card(self, pr):
        bg, fg, border_c = self.STATUS_STYLE.get(pr["status"], (SURFACE2, TEXT_SEC, BORDER))
        icon = (ft.Icons.MERGE if pr["status"] == "Merged"
                else ft.Icons.CLOSE if pr["status"] == "Closed"
                else ft.Icons.CALL_SPLIT)
        return _hoverable(
            ft.Container(
                content=ft.Column(controls=[
                    ft.Row(controls=[
                        ft.Icon(icon, color=fg, size=16),
                        ft.Text(pr["pr_number"], size=13, color=TEXT_SEC, width=36),
                        ft.Text(pr["title"], size=14, weight=ft.FontWeight.W_600,
                                color=TEXT_PRI, expand=True),
                        ft.Container(
                            content=ft.Text(pr["status"], size=11,
                                            weight=ft.FontWeight.W_600, color=fg),
                            bgcolor=bg,
                            padding=ft.Padding(left=10, right=10, top=4, bottom=4),
                            border_radius=20,
                            border=ft.Border.all(1, border_c),
                        ),
                    ], spacing=8),
                    ft.Text(pr["description"], size=13, color=TEXT_SEC),
                    ft.Row(controls=[
                        ft.Icon(ft.Icons.COMMIT, size=12, color=TEXT_SEC),
                        ft.Text(f"{pr['commits']} commits", size=12, color=TEXT_SEC),
                        ft.Text("·", size=12, color=BORDER),
                        ft.Icon(ft.Icons.PERSON, size=14, color=TEXT_SEC),
                        ft.Text(pr["reviews"], size=12, color=TEXT_SEC),
                    ], spacing=4),
                ], spacing=8),
                bgcolor=SURFACE, border_radius=12,
                padding=ft.Padding(left=16, right=16, top=16, bottom=16),
                border=ft.Border.all(1, BORDER),
                margin=ft.Margin(left=0, right=0, top=0, bottom=10),
            ),
            fg,
        )

    def _screenshot_card(self, title, src):
        return _hoverable(
            ft.Container(
                content=ft.Column(controls=[
                    ft.Text(title, size=13, weight=ft.FontWeight.W_600, color=TEXT_PRI),
                    ft.Container(
                        content=ft.Image(
                            src=src, fit="contain",
                            error_content=ft.Column(controls=[
                                ft.Icon(ft.Icons.IMAGE_NOT_SUPPORTED, color=BORDER, size=32),
                                ft.Text(
                                    "Add screenshot to:\nassets/" + src,
                                    size=11, color=TEXT_SEC,
                                    text_align=ft.TextAlign.CENTER,
                                ),
                            ], horizontal_alignment=ft.CrossAxisAlignment.CENTER, spacing=4),
                        ),
                        bgcolor=SURFACE2, border_radius=8, height=160,
                        border=ft.Border.all(1, BORDER),
                        clip_behavior=ft.ClipBehavior.HARD_EDGE,
                        alignment=ft.Alignment(0, 0),
                    ),
                ], spacing=6),
                bgcolor=SURFACE, border_radius=12,
                padding=ft.Padding(left=12, right=12, top=12, bottom=12),
                border=ft.Border.all(1, BORDER),
                expand=True,
            ),
            BLUE,
        )

    def build(self):
        hero = _hoverable(
            ft.Container(
                content=ft.Column(controls=[
                    ft.Row(controls=[
                        ft.Icon(ft.Icons.FOLDER, color=TEXT_PRI, size=28),
                        ft.Text("GitHub Evidence", size=24, weight=ft.FontWeight.W_700, color=TEXT_PRI),
                    ], spacing=10),
                    ft.Text(
                        "Individual contributions by ZenNgesheya to the UNAM-I3691CP-WaterLeak-Ongwediva repository.",
                        size=13, color=TEXT_SEC,
                    ),
                ], spacing=8),
                bgcolor=SURFACE, border_radius=16,
                padding=ft.Padding(left=24, right=24, top=24, bottom=24),
                margin=ft.Margin(left=0, right=0, top=0, bottom=16),
                border=ft.Border.all(1, BORDER),
            ),
            ACCENT,
        )

        stats = ft.Row(controls=[
            self._stat_card(ft.Icons.COMMIT,      "19", "Commits",     BLUE),
            self._stat_card(ft.Icons.CALL_MERGE,  "2",  "PRs Opened",  ACCENT),
            self._stat_card(ft.Icons.RATE_REVIEW, "2",  "PRs Merged",  PURPLE),
            self._stat_card(ft.Icons.BUG_REPORT,  "1",  "Bugs Fixed",  AMBER),
        ], spacing=12)

        graph       = self._build_contribution_graph()
        commit_rows = [self._commit_row(c) for c in self.COMMITS]

        commits_section = ft.Container(
            content=ft.Column(controls=[
                ft.Text("Commit History", size=16, weight=ft.FontWeight.W_700, color=TEXT_PRI),
                ft.Container(
                    content=ft.Column(controls=commit_rows, spacing=0),
                    bgcolor=SURFACE, border_radius=12,
                    border=ft.Border.all(1, BORDER),
                    clip_behavior=ft.ClipBehavior.HARD_EDGE,
                ),
            ], spacing=10),
        )

        screenshots = ft.Column(controls=[
            ft.Row(controls=[
                self._screenshot_card("Commit History Screenshot", "screenshots/commit_history.png"),
                self._screenshot_card("Pull Requests Overview",    "screenshots/pull_request.png"),
            ], spacing=12),
            ft.Row(controls=[
                self._screenshot_card("PR #14 — Verify Location Screen (Merged)", "screenshots/pr_14.png"),
                self._screenshot_card("PR #15 — App Config (Merged)",             "screenshots/pr_15.png"),
            ], spacing=12),
        ], spacing=12)

        pr_cards   = [self._pr_card(p) for p in self.PULL_REQUESTS]
        pr_section = ft.Column(controls=[
            ft.Text("Pull Request Logs", size=16, weight=ft.FontWeight.W_700, color=TEXT_PRI),
            *pr_cards,
        ], spacing=8)

        impact_section = _hoverable(
            ft.Container(
                content=ft.Column(controls=[
                    ft.Row(controls=[
                        ft.Icon(ft.Icons.STAR, color=AMBER, size=20),
                        ft.Text("Impact Summary", size=16, weight=ft.FontWeight.W_700, color=TEXT_PRI),
                    ], spacing=8),
                    ft.Markdown(self.IMPACT_SUMMARY, selectable=True,
                                extension_set="gitHubFlavored"),
                ], spacing=10),
                bgcolor=SURFACE2, border_radius=12,
                padding=ft.Padding(left=16, right=16, top=16, bottom=16),
                border=ft.Border.all(1, AMBER + "55"),
            ),
            AMBER,
        )

        return ft.Column(controls=[
            hero, stats,
            ft.Divider(height=16, color="transparent"),
            graph,
            ft.Divider(height=16, color="transparent"),
            commits_section,
            ft.Divider(height=12, color="transparent"),
            ft.Text("Screenshots", size=16, weight=ft.FontWeight.W_700, color=TEXT_PRI),
            screenshots,
            ft.Divider(height=16, color="transparent"),
            pr_section,
            ft.Divider(height=16, color="transparent"),
            impact_section,
        ], spacing=4, scroll=ft.ScrollMode.AUTO)