"""
Library Management System — Desktop GUI

This file is ONLY responsible for:
    - drawing widgets
    - reading user input from the form fields
    - calling the appropriate method on Library / Member / Librarian
    - showing the result (or the error message) to the user

No business rules live in this file. Every rule (limits, validation,
availability, borrowing rules, ...) lives inside the model classes
(library.py, member.py, item.py, ...), exactly as it should in an
OOP design.
"""

import tkinter as tk
from tkinter import ttk, messagebox

from library import Library
from member import Member
from librarian import Librarian
from book import Book
from magazine import Magazine


# --------------------------------------------------------------------------
# Palette / fonts — kept in one place so the whole app stays consistent
# --------------------------------------------------------------------------
COLOR_BG = "#F4F6FA"
COLOR_SIDEBAR = "#1B2440"
COLOR_SIDEBAR_ACTIVE = "#2C3B6B"
COLOR_PRIMARY = "#2C3B6B"
COLOR_ACCENT = "#C9A24B"
COLOR_CARD = "#FFFFFF"
COLOR_TEXT = "#1B2440"
COLOR_MUTED = "#6B7280"
COLOR_SUCCESS = "#1E8E5A"
COLOR_DANGER = "#C0392B"
COLOR_BORDER = "#E3E6EE"

FONT_TITLE = ("Segoe UI", 18, "bold")
FONT_SUBTITLE = ("Segoe UI", 11)
FONT_HEADER = ("Segoe UI", 13, "bold")
FONT_BODY = ("Segoe UI", 10)
FONT_BODY_BOLD = ("Segoe UI", 10, "bold")
FONT_SIDEBAR = ("Segoe UI", 11)
FONT_BUTTON = ("Segoe UI", 10, "bold")


class LibraryApp(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Alexandria Library — Management System")
        self.geometry("1080x680")
        self.minsize(960, 600)
        self.configure(bg=COLOR_BG)

        self.library = Library("Alexandria Library", max_items=50)
        self.current_user = None  # Member or Librarian instance

        self._seed_demo_data()
        self._build_style()

        # container that holds whichever screen is active
        self.container = tk.Frame(self, bg=COLOR_BG)
        self.container.pack(fill="both", expand=True)

        self.show_login_screen()

    # ------------------------------------------------------------ helpers

    def _seed_demo_data(self):
        member = Member(1, "Mahmoud", "mahmoud@gmail.com", 101)
        librarian = Librarian(2, "Ahmed", "ahmed@gmail.com", 501)

        self.library.add_member(member)
        self.library.add_librarian(librarian)

        try:
            self.library.add_book(
                "Clean Code",
                "A handbook of agile software craftsmanship.",
                "Robert C. Martin",
            )
            self.library.add_book(
                "1984",
                "A dystopian social science fiction novel.",
                "George Orwell",
            )
            self.library.add_magazine(
                "National Geographic",
                "Science, geography and nature magazine.",
                305,
            )
        except ValueError:
            pass

    def _build_style(self):
        style = ttk.Style(self)
        style.theme_use("clam")

        style.configure("TFrame", background=COLOR_BG)
        style.configure("Card.TFrame", background=COLOR_CARD)

        style.configure(
            "Primary.TButton",
            background=COLOR_PRIMARY,
            foreground="white",
            font=FONT_BUTTON,
            padding=(14, 8),
            borderwidth=0,
        )
        style.map(
            "Primary.TButton",
            background=[("active", "#3A4C8C"), ("disabled", "#9AA3C0")],
        )

        style.configure(
            "Accent.TButton",
            background=COLOR_ACCENT,
            foreground=COLOR_TEXT,
            font=FONT_BUTTON,
            padding=(14, 8),
            borderwidth=0,
        )
        style.map("Accent.TButton", background=[("active", "#D9B968")])

        style.configure(
            "Danger.TButton",
            background=COLOR_DANGER,
            foreground="white",
            font=FONT_BUTTON,
            padding=(10, 6),
            borderwidth=0,
        )
        style.map("Danger.TButton", background=[("active", "#D9645A")])

        style.configure(
            "Ghost.TButton",
            background=COLOR_CARD,
            foreground=COLOR_PRIMARY,
            font=FONT_BUTTON,
            padding=(10, 6),
            borderwidth=1,
        )

        style.configure(
            "Sidebar.TButton",
            background=COLOR_SIDEBAR,
            foreground="white",
            font=FONT_SIDEBAR,
            padding=(16, 12),
            borderwidth=0,
            anchor="w",
        )
        style.map(
            "Sidebar.TButton",
            background=[("active", COLOR_SIDEBAR_ACTIVE)],
        )

        style.configure(
            "Treeview",
            background="white",
            fieldbackground="white",
            rowheight=28,
            font=FONT_BODY,
            borderwidth=0,
        )
        style.configure(
            "Treeview.Heading",
            background=COLOR_PRIMARY,
            foreground="white",
            font=FONT_BODY_BOLD,
            padding=(6, 6),
        )
        style.map("Treeview.Heading", background=[("active", COLOR_PRIMARY)])
        style.map(
            "Treeview",
            background=[("selected", COLOR_ACCENT)],
            foreground=[("selected", COLOR_TEXT)],
        )

        style.configure("TNotebook", background=COLOR_BG, borderwidth=0)
        style.configure(
            "TNotebook.Tab",
            background=COLOR_BORDER,
            foreground=COLOR_TEXT,
            font=FONT_BODY_BOLD,
            padding=(16, 8),
        )
        style.map(
            "TNotebook.Tab",
            background=[("selected", COLOR_CARD)],
            foreground=[("selected", COLOR_PRIMARY)],
        )

        style.configure("TCombobox", padding=4)

    def _clear_container(self):
        for widget in self.container.winfo_children():
            widget.destroy()

    def info(self, message, title="Success"):
        messagebox.showinfo(title, message)

    def error(self, message, title="Error"):
        messagebox.showerror(title, message)

    def confirm(self, message, title="Please confirm"):
        return messagebox.askyesno(title, message)

    @staticmethod
    def _row(parent, **kwargs):
        row = tk.Frame(parent, bg=COLOR_CARD)
        row.pack(fill="x", **kwargs)
        return row

    @staticmethod
    def _labeled_entry(parent, label_text, show=None):
        wrapper = tk.Frame(parent, bg=COLOR_CARD)
        wrapper.pack(fill="x", pady=6)

        label = tk.Label(
            wrapper, text=label_text, font=FONT_BODY_BOLD,
            bg=COLOR_CARD, fg=COLOR_TEXT, anchor="w",
        )
        label.pack(fill="x")

        entry = tk.Entry(
            wrapper, font=FONT_BODY, relief="solid", bd=1,
            highlightthickness=1, highlightbackground=COLOR_BORDER,
            highlightcolor=COLOR_PRIMARY, show=show,
        )
        entry.pack(fill="x", ipady=5, pady=(4, 0))
        entry.label = label  # keep a direct reference so callers can retitle it
        return entry

    # -------------------------------------------------------- login screen

    def show_login_screen(self):
        self._clear_container()
        self.current_user = None

        outer = tk.Frame(self.container, bg=COLOR_BG)
        outer.pack(fill="both", expand=True)

        card = tk.Frame(outer, bg=COLOR_CARD, bd=0, highlightthickness=1,
                         highlightbackground=COLOR_BORDER)
        card.place(relx=0.5, rely=0.5, anchor="center", width=460, height=500)

        tk.Label(
            card, text="📚 " + self.library.name, font=FONT_TITLE,
            bg=COLOR_CARD, fg=COLOR_PRIMARY,
        ).pack(pady=(30, 4))
        tk.Label(
            card, text="Library Management System", font=FONT_SUBTITLE,
            bg=COLOR_CARD, fg=COLOR_MUTED,
        ).pack(pady=(0, 20))

        # ---- Librarian login
        tk.Label(
            card, text="Login as Librarian", font=FONT_BODY_BOLD,
            bg=COLOR_CARD, fg=COLOR_TEXT, anchor="w",
        ).pack(fill="x", padx=40, pady=(10, 4))

        librarian_var = tk.StringVar()
        librarian_box = ttk.Combobox(
            card, textvariable=librarian_var, state="readonly",
            values=[f"{l.employee_id} — {l.name}" for l in self.library.librarians],
            font=FONT_BODY,
        )
        librarian_box.pack(fill="x", padx=40, ipady=4)
        if self.library.librarians:
            librarian_box.current(0)

        def login_as_librarian():
            if not librarian_var.get():
                self.error("Please select a librarian first.")
                return
            index = librarian_box.current()
            self.current_user = self.library.librarians[index]
            self.show_main_screen()

        ttk.Button(
            card, text="Continue as Librarian", style="Primary.TButton",
            command=login_as_librarian,
        ).pack(fill="x", padx=40, pady=(10, 20))

        ttk.Separator(card).pack(fill="x", padx=40)

        # ---- Member login
        tk.Label(
            card, text="Login as Member", font=FONT_BODY_BOLD,
            bg=COLOR_CARD, fg=COLOR_TEXT, anchor="w",
        ).pack(fill="x", padx=40, pady=(20, 4))

        self.member_var = tk.StringVar()
        self.member_box = ttk.Combobox(
            card, textvariable=self.member_var, state="readonly",
            values=[f"{m.member_id} — {m.name}" for m in self.library.members],
            font=FONT_BODY,
        )
        self.member_box.pack(fill="x", padx=40, ipady=4)
        if self.library.members:
            self.member_box.current(0)

        def login_as_member():
            if not self.member_var.get():
                self.error("Please select a member first.")
                return
            index = self.member_box.current()
            self.current_user = self.library.members[index]
            self.show_main_screen()

        ttk.Button(
            card, text="Continue as Member", style="Primary.TButton",
            command=login_as_member,
        ).pack(fill="x", padx=40, pady=(10, 6))

        ttk.Button(
            card, text="+ Register New Member", style="Ghost.TButton",
            command=self._open_register_member_dialog,
        ).pack(fill="x", padx=40, pady=(0, 20))

    def _open_register_member_dialog(self):
        dialog = tk.Toplevel(self)
        dialog.title("Register New Member")
        dialog.configure(bg=COLOR_CARD)
        dialog.geometry("360x260")
        dialog.grab_set()

        tk.Label(
            dialog, text="Register New Member", font=FONT_HEADER,
            bg=COLOR_CARD, fg=COLOR_PRIMARY,
        ).pack(pady=(16, 10))

        form = tk.Frame(dialog, bg=COLOR_CARD)
        form.pack(fill="both", expand=True, padx=24)

        name_entry = self._labeled_entry(form, "Full Name")
        email_entry = self._labeled_entry(form, "Email")

        def submit():
            try:
                member = self.library.register_member(
                    name_entry.get(), email_entry.get()
                )
            except ValueError as exc:
                self.error(str(exc))
                return

            dialog.destroy()
            self.member_box["values"] = [
                f"{m.member_id} — {m.name}" for m in self.library.members
            ]
            self.member_box.set(f"{member.member_id} — {member.name}")
            self.info(f"Member '{member.name}' registered successfully!")

        ttk.Button(
            form, text="Register", style="Primary.TButton", command=submit,
        ).pack(fill="x", pady=16)

    # --------------------------------------------------------- main screen

    TAB_ATTRS = (
        "catalog_tab", "search_tab", "add_tab", "manage_tab",
        "loans_tab", "issue_tab", "my_loans_tab",
    )

    def show_main_screen(self):
        self._clear_container()

        # drop any stale tab references from a previous session (e.g. the
        # user logged out and back in under a different role)
        for attr in self.TAB_ATTRS:
            if hasattr(self, attr):
                delattr(self, attr)

        is_librarian = isinstance(self.current_user, Librarian)

        # ---------------- sidebar ----------------
        sidebar = tk.Frame(self.container, bg=COLOR_SIDEBAR, width=230)
        sidebar.pack(side="left", fill="y")
        sidebar.pack_propagate(False)

        tk.Label(
            sidebar, text="📚 " + self.library.name, font=("Segoe UI", 13, "bold"),
            bg=COLOR_SIDEBAR, fg="white", wraplength=200, justify="left",
        ).pack(fill="x", padx=16, pady=(24, 4))

        role = "Librarian" if is_librarian else "Member"
        tk.Label(
            sidebar, text=f"{role}: {self.current_user.name}",
            font=FONT_BODY, bg=COLOR_SIDEBAR, fg=COLOR_ACCENT,
            wraplength=200, justify="left",
        ).pack(fill="x", padx=16, pady=(0, 20))

        # main content area (tabs live here)
        content = tk.Frame(self.container, bg=COLOR_BG)
        content.pack(side="left", fill="both", expand=True)

        header = tk.Frame(content, bg=COLOR_BG)
        header.pack(fill="x", padx=24, pady=(20, 10))
        tk.Label(
            header, text="Dashboard", font=FONT_TITLE, bg=COLOR_BG, fg=COLOR_TEXT,
        ).pack(side="left")
        ttk.Button(
            header, text="Logout", style="Ghost.TButton",
            command=self.show_login_screen,
        ).pack(side="right")

        notebook = ttk.Notebook(content)
        notebook.pack(fill="both", expand=True, padx=24, pady=(0, 20))

        self.catalog_tab = self._build_catalog_tab(notebook)
        notebook.add(self.catalog_tab, text="📖  Catalog")

        self.search_tab = self._build_search_tab(notebook)
        notebook.add(self.search_tab, text="🔍  Search")

        if is_librarian:
            self.add_tab = self._build_add_item_tab(notebook)
            notebook.add(self.add_tab, text="➕  Add Item")

            self.manage_tab = self._build_manage_tab(notebook)
            notebook.add(self.manage_tab, text="✏️  Manage")

            self.loans_tab = self._build_loans_overview_tab(notebook)
            notebook.add(self.loans_tab, text="📋  All Loans")
        else:
            self.issue_tab = self._build_issue_return_tab(notebook)
            notebook.add(self.issue_tab, text="🔄  Issue / Return")

            self.my_loans_tab = self._build_my_loans_tab(notebook)
            notebook.add(self.my_loans_tab, text="🗂️  My Loans")

        self.refresh_all()

    # ------------------------------------------------------------ catalog

    def _make_items_tree(self, parent):
        columns = ("id", "type", "title", "creator", "status")
        tree = ttk.Treeview(parent, columns=columns, show="headings", height=14)

        headings = {
            "id": ("ID", 50),
            "type": ("Type", 90),
            "title": ("Title", 260),
            "creator": ("Author / Issue #", 200),
            "status": ("Status", 110),
        }
        for col, (text, width) in headings.items():
            tree.heading(col, text=text)
            tree.column(col, width=width, anchor="w")

        tree.tag_configure("available", foreground=COLOR_SUCCESS)
        tree.tag_configure("issued", foreground=COLOR_DANGER)

        return tree

    def _fill_items_tree(self, tree, items):
        tree.delete(*tree.get_children())

        for item in items:
            item_type = "Book" if isinstance(item, Book) else "Magazine"
            creator = item.author if isinstance(item, Book) else f"Issue #{item.issue_number}"
            status = "Available" if item.is_available else "Issued"
            tag = "available" if item.is_available else "issued"

            tree.insert(
                "", "end",
                values=(item.item_id, item_type, item.title, creator, status),
                tags=(tag,),
            )

    def _build_catalog_tab(self, notebook):
        tab = tk.Frame(notebook, bg=COLOR_BG)

        toolbar = tk.Frame(tab, bg=COLOR_BG)
        toolbar.pack(fill="x", pady=(14, 8))

        tk.Label(
            toolbar, text="All items currently in the library",
            font=FONT_BODY, bg=COLOR_BG, fg=COLOR_MUTED,
        ).pack(side="left")

        ttk.Button(
            toolbar, text="⟳ Refresh", style="Ghost.TButton",
            command=self.refresh_all,
        ).pack(side="right")

        tree_frame = tk.Frame(tab, bg=COLOR_CARD, highlightthickness=1,
                               highlightbackground=COLOR_BORDER)
        tree_frame.pack(fill="both", expand=True)

        tab.catalog_tree = self._make_items_tree(tree_frame)
        tab.catalog_tree.pack(fill="both", expand=True, padx=1, pady=1)
        tab.catalog_tree.bind(
            "<Double-1>", lambda e: self._show_item_details(tab.catalog_tree)
        )

        tk.Label(
            tab, text="Double-click a row to see full details.",
            font=("Segoe UI", 9), bg=COLOR_BG, fg=COLOR_MUTED,
        ).pack(anchor="w", pady=(6, 0))

        return tab

    def _show_item_details(self, tree):
        selection = tree.selection()
        if not selection:
            return

        item_id = int(tree.item(selection[0])["values"][0])
        try:
            item = self.library.get_item_by_id(item_id)
        except ValueError as exc:
            self.error(str(exc))
            return

        self.info(item.get_info(), title=f"Item #{item_id}")

    # ------------------------------------------------------------- search

    def _build_search_tab(self, notebook):
        tab = tk.Frame(notebook, bg=COLOR_BG)

        bar = tk.Frame(tab, bg=COLOR_BG)
        bar.pack(fill="x", pady=(14, 10))

        search_var = tk.StringVar()
        entry = tk.Entry(
            bar, textvariable=search_var, font=FONT_BODY, relief="solid", bd=1,
            highlightthickness=1, highlightbackground=COLOR_BORDER,
            highlightcolor=COLOR_PRIMARY,
        )
        entry.pack(side="left", fill="x", expand=True, ipady=6)
        entry.insert(0, "")

        tree_frame = tk.Frame(tab, bg=COLOR_CARD, highlightthickness=1,
                               highlightbackground=COLOR_BORDER)
        tree_frame.pack(fill="both", expand=True)

        tab.search_tree = self._make_items_tree(tree_frame)
        tab.search_tree.pack(fill="both", expand=True, padx=1, pady=1)
        tab.search_tree.bind(
            "<Double-1>", lambda e: self._show_item_details(tab.search_tree)
        )

        def do_search():
            results = self.library.search_items(search_var.get())
            self._fill_items_tree(tab.search_tree, results)

        entry.bind("<Return>", lambda e: do_search())

        ttk.Button(
            bar, text="Search", style="Primary.TButton", command=do_search,
        ).pack(side="left", padx=(8, 0))

        # show everything initially
        self._fill_items_tree(tab.search_tree, self.library.view_all_items())

        return tab

    # --------------------------------------------------------- add item

    def _build_add_item_tab(self, notebook):
        tab = tk.Frame(notebook, bg=COLOR_BG)

        card = tk.Frame(tab, bg=COLOR_CARD, highlightthickness=1,
                         highlightbackground=COLOR_BORDER)
        card.pack(fill="x", pady=16, padx=2)

        inner = tk.Frame(card, bg=COLOR_CARD)
        inner.pack(fill="x", padx=24, pady=20)

        tk.Label(
            inner, text="Add a new item to the catalog", font=FONT_HEADER,
            bg=COLOR_CARD, fg=COLOR_PRIMARY,
        ).pack(anchor="w", pady=(0, 10))

        type_var = tk.StringVar(value="Book")
        type_row = tk.Frame(inner, bg=COLOR_CARD)
        type_row.pack(fill="x", pady=6)
        tk.Label(
            type_row, text="Item Type", font=FONT_BODY_BOLD,
            bg=COLOR_CARD, fg=COLOR_TEXT,
        ).pack(anchor="w")
        type_box = ttk.Combobox(
            type_row, textvariable=type_var, state="readonly",
            values=["Book", "Magazine"], font=FONT_BODY,
        )
        type_box.pack(fill="x", ipady=4, pady=(4, 0))

        title_entry = self._labeled_entry(inner, "Title")
        desc_entry = self._labeled_entry(inner, "Description")
        extra_entry = self._labeled_entry(inner, "Author")

        def on_type_change(event=None):
            if type_var.get() == "Book":
                extra_entry.label["text"] = "Author"
            else:
                extra_entry.label["text"] = "Issue Number"

        type_box.bind("<<ComboboxSelected>>", on_type_change)

        def submit():
            try:
                if type_var.get() == "Book":
                    item = self.library.add_book(
                        title_entry.get(), desc_entry.get(), extra_entry.get()
                    )
                else:
                    issue_raw = extra_entry.get().strip()
                    if not issue_raw.isdigit():
                        raise ValueError("Issue Number must be a whole number.")
                    item = self.library.add_magazine(
                        title_entry.get(), desc_entry.get(), int(issue_raw)
                    )
            except ValueError as exc:
                self.error(str(exc))
                return

            title_entry.delete(0, "end")
            desc_entry.delete(0, "end")
            extra_entry.delete(0, "end")

            self.info(f"'{item.title}' was added with ID {item.item_id}.")
            self.refresh_all()

        ttk.Button(
            inner, text="Add Item", style="Primary.TButton", command=submit,
        ).pack(anchor="w", pady=(14, 0))

        return tab

    # ------------------------------------------------------------- manage

    def _build_manage_tab(self, notebook):
        tab = tk.Frame(notebook, bg=COLOR_BG)

        tree_frame = tk.Frame(tab, bg=COLOR_CARD, highlightthickness=1,
                               highlightbackground=COLOR_BORDER)
        tree_frame.pack(fill="both", expand=True, pady=(14, 10))

        tab.manage_tree = self._make_items_tree(tree_frame)
        tab.manage_tree.pack(fill="both", expand=True, padx=1, pady=1)

        form_card = tk.Frame(tab, bg=COLOR_CARD, highlightthickness=1,
                              highlightbackground=COLOR_BORDER)
        form_card.pack(fill="x")

        inner = tk.Frame(form_card, bg=COLOR_CARD)
        inner.pack(fill="x", padx=24, pady=16)

        tk.Label(
            inner, text="Edit selected item", font=FONT_HEADER,
            bg=COLOR_CARD, fg=COLOR_PRIMARY,
        ).pack(anchor="w", pady=(0, 8))

        title_entry = self._labeled_entry(inner, "New Title (leave blank to keep)")
        desc_entry = self._labeled_entry(inner, "New Description (leave blank to keep)")
        extra_entry = self._labeled_entry(inner, "New Author / Issue Number (leave blank to keep)")

        buttons_row = tk.Frame(inner, bg=COLOR_CARD)
        buttons_row.pack(fill="x", pady=(10, 0))

        def get_selected_id():
            selection = tab.manage_tree.selection()
            if not selection:
                self.error("Please select an item from the list first.")
                return None
            return int(tab.manage_tree.item(selection[0])["values"][0])

        def save_changes():
            item_id = get_selected_id()
            if item_id is None:
                return

            try:
                item = self.library.get_item_by_id(item_id)

                kwargs = {}
                if title_entry.get().strip():
                    kwargs["title"] = title_entry.get()
                if desc_entry.get().strip():
                    kwargs["description"] = desc_entry.get()

                extra = extra_entry.get().strip()
                if extra:
                    if isinstance(item, Book):
                        kwargs["author"] = extra
                    elif isinstance(item, Magazine):
                        if not extra.isdigit():
                            raise ValueError("Issue Number must be a whole number.")
                        kwargs["issue_number"] = int(extra)

                self.library.edit_item(item_id, **kwargs)
            except ValueError as exc:
                self.error(str(exc))
                return

            title_entry.delete(0, "end")
            desc_entry.delete(0, "end")
            extra_entry.delete(0, "end")

            self.info("Item updated successfully.")
            self.refresh_all()

        def delete_selected():
            item_id = get_selected_id()
            if item_id is None:
                return

            if not self.confirm(f"Delete item #{item_id}? This cannot be undone."):
                return

            try:
                self.library.delete_item(item_id)
            except ValueError as exc:
                self.error(str(exc))
                return

            self.info("Item deleted successfully.")
            self.refresh_all()

        ttk.Button(
            buttons_row, text="Save Changes", style="Primary.TButton",
            command=save_changes,
        ).pack(side="left")
        ttk.Button(
            buttons_row, text="Delete Item", style="Danger.TButton",
            command=delete_selected,
        ).pack(side="left", padx=(10, 0))

        return tab

    # -------------------------------------------------------- issue/return

    def _build_issue_return_tab(self, notebook):
        tab = tk.Frame(notebook, bg=COLOR_BG)

        tree_frame = tk.Frame(tab, bg=COLOR_CARD, highlightthickness=1,
                               highlightbackground=COLOR_BORDER)
        tree_frame.pack(fill="both", expand=True, pady=(14, 10))

        tab.issue_tree = self._make_items_tree(tree_frame)
        tab.issue_tree.pack(fill="both", expand=True, padx=1, pady=1)

        actions = tk.Frame(tab, bg=COLOR_BG)
        actions.pack(fill="x")

        tk.Label(
            actions,
            text="Select an item above, then borrow or return it "
                 "(you can hold up to 3 items at once).",
            font=("Segoe UI", 9), bg=COLOR_BG, fg=COLOR_MUTED,
        ).pack(anchor="w", pady=(0, 8))

        def get_selected_id():
            selection = tab.issue_tree.selection()
            if not selection:
                self.error("Please select an item from the list first.")
                return None
            return int(tab.issue_tree.item(selection[0])["values"][0])

        def issue_selected():
            item_id = get_selected_id()
            if item_id is None:
                return

            try:
                loan = self.library.issue_item(self.current_user, item_id)
            except ValueError as exc:
                self.error(str(exc))
                return

            self.info(
                f"'{loan.item.title}' issued to you.\nDue date: {loan.due_date}"
            )
            self.refresh_all()

        def return_selected():
            item_id = get_selected_id()
            if item_id is None:
                return

            try:
                self.library.return_item(self.current_user, item_id)
            except ValueError as exc:
                self.error(str(exc))
                return

            self.info("Item returned successfully. Thank you!")
            self.refresh_all()

        buttons = tk.Frame(tab, bg=COLOR_BG)
        buttons.pack(fill="x")
        ttk.Button(
            buttons, text="Borrow Selected Item", style="Primary.TButton",
            command=issue_selected,
        ).pack(side="left")
        ttk.Button(
            buttons, text="Return Selected Item", style="Accent.TButton",
            command=return_selected,
        ).pack(side="left", padx=(10, 0))

        return tab

    # ----------------------------------------------------------- my loans

    def _make_loans_tree(self, parent, show_member_column):
        columns = ["item", "borrow", "due", "return", "status"]
        headings = {
            "item": ("Item", 260),
            "borrow": ("Borrow Date", 110),
            "due": ("Due Date", 110),
            "return": ("Return Date", 110),
            "status": ("Status", 110),
        }
        if show_member_column:
            columns.insert(0, "member")
            headings["member"] = ("Member", 150)

        tree = ttk.Treeview(parent, columns=columns, show="headings", height=14)
        for col in columns:
            text, width = headings[col]
            tree.heading(col, text=text)
            tree.column(col, width=width, anchor="w")

        tree.tag_configure("overdue", foreground=COLOR_DANGER)
        tree.tag_configure("active", foreground=COLOR_PRIMARY)
        tree.tag_configure("closed", foreground=COLOR_MUTED)

        return tree

    def _fill_loans_tree(self, tree, loans, show_member_column):
        tree.delete(*tree.get_children())

        for loan in loans:
            if loan.return_date:
                status, tag = "Returned", "closed"
            elif loan.is_overdue():
                status, tag = "Overdue", "overdue"
            else:
                status, tag = "Active", "active"

            values = [
                loan.item.title, str(loan.borrow_date),
                str(loan.due_date), str(loan.return_date or "—"), status,
            ]
            if show_member_column:
                values.insert(0, loan.member.name)

            tree.insert("", "end", values=values, tags=(tag,))

    def _build_my_loans_tab(self, notebook):
        tab = tk.Frame(notebook, bg=COLOR_BG)

        tk.Label(
            tab, text="Your borrowing history", font=FONT_BODY,
            bg=COLOR_BG, fg=COLOR_MUTED,
        ).pack(anchor="w", pady=(14, 8))

        tree_frame = tk.Frame(tab, bg=COLOR_CARD, highlightthickness=1,
                               highlightbackground=COLOR_BORDER)
        tree_frame.pack(fill="both", expand=True)

        tab.my_loans_tree = self._make_loans_tree(tree_frame, show_member_column=False)
        tab.my_loans_tree.pack(fill="both", expand=True, padx=1, pady=1)

        return tab

    def _build_loans_overview_tab(self, notebook):
        tab = tk.Frame(notebook, bg=COLOR_BG)

        tk.Label(
            tab, text="All active and past loans across the library",
            font=FONT_BODY, bg=COLOR_BG, fg=COLOR_MUTED,
        ).pack(anchor="w", pady=(14, 8))

        tree_frame = tk.Frame(tab, bg=COLOR_CARD, highlightthickness=1,
                               highlightbackground=COLOR_BORDER)
        tree_frame.pack(fill="both", expand=True)

        tab.loans_tree = self._make_loans_tree(tree_frame, show_member_column=True)
        tab.loans_tree.pack(fill="both", expand=True, padx=1, pady=1)

        return tab

    # --------------------------------------------------------------- sync

    def refresh_all(self):
        """Re-pull data from the model layer into every visible tree."""
        all_items = self.library.view_all_items()

        if hasattr(self, "catalog_tab"):
            self._fill_items_tree(self.catalog_tab.catalog_tree, all_items)

        if hasattr(self, "search_tab"):
            self._fill_items_tree(self.search_tab.search_tree, all_items)

        if hasattr(self, "manage_tab"):
            self._fill_items_tree(self.manage_tab.manage_tree, all_items)

        if hasattr(self, "issue_tab"):
            self._fill_items_tree(self.issue_tab.issue_tree, all_items)

        if hasattr(self, "my_loans_tab") and not isinstance(self.current_user, Librarian):
            my_loans = self.library.all_loans(member=self.current_user)
            self._fill_loans_tree(self.my_loans_tab.my_loans_tree, my_loans, False)

        if hasattr(self, "loans_tab"):
            self._fill_loans_tree(self.loans_tab.loans_tree, self.library.all_loans(), True)


if __name__ == "__main__":
    app = LibraryApp()
    app.mainloop()
