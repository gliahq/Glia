import sys

from PyQt5 import Qsci
from PyQt5.Qsci import QsciScintilla
from PyQt5.QtGui import QColor, QFontMetrics

from glia.widgets.editor.lexer import ViewLexer
from resources.themes.dracula.pygments import EXTRA_STYLES


class Editor(Qsci.QsciScintilla):
    """
    Provides access to methods of editor.
    """
    def __init__(self, parent=None):
        """
        Loads default configuration for code_editor including
        the lexer depending on the kernel.
        """
        super(Editor, self).__init__(parent)

        # Scrollbar
        self.SendScintilla(
            self.SCI_SETHSCROLLBAR,
            0
        )

        # Configurations
        self.setBraceMatching(QsciScintilla.SloppyBraceMatch)
        self.setIndentationsUseTabs(False)
        self.setIndentationGuides(True)
        self.setAutoIndent(True)
        self.setTabIndents(True)
        self.setUtf8(True)

        # Margin
        self.setMarginType(0, QsciScintilla.NumberMargin)
        self.setMarginWidth(0, "00")

        # Platform Specific
        if sys.platform.startswith("linux"):
            self.setEolMode(QsciScintilla.EolUnix)
        elif sys.platform.startswith("win32"):
            self.setEolMode(QsciScintilla.EolWindows)
        elif sys.platform.startswith("darwin"):
            self.setEolMode(QsciScintilla.EolMac)

        # Lexer
        self.lexer = ViewLexer("python", "dracula")
        self.setLexer(self.lexer)

        # Configs
        self.text_size = 1

        # Configs - Indentation
        self.setIndentationWidth(4)
        self.setIndentationsUseTabs(False)
        self.setTabIndents(True)
        self.setAutoIndent(True)
        self.setBackspaceUnindents(True)
        self.setIndentationGuides(True)

        # Configs - Caret
        self.setCaretLineVisible(True)
        self.setCaretWidth(4)

        # Config - Edge Marker
        self.setEdgeMode(Qsci.QsciScintilla.EdgeBackground)
        self.setEdgeColumn(80)

        # Config - Font
        font_metrics = QFontMetrics(self.lexer.font)
        self.setMinimumSize(
            int(font_metrics.width("0" * 80)),
            0
        )

        # Multi-selection
        self.SendScintilla(self.SCI_SETMULTIPLESELECTION, True)
        self.SendScintilla(self.SCI_SETMULTIPASTE, 1)
        self.SendScintilla(self.SCI_SETADDITIONALSELECTIONTYPING, True)

        # Slots
        self.linesChanged.connect(self.update_margin)

        # Extras
        self.set_extra_settings(EXTRA_STYLES)

    def update_margin(self):
        """
        Adjust margin width to accommodate the number lines numbers.
        """
        lines = self.lines()
        self.setMarginWidth(0, "0" * (len(str(lines)) + 1))

    def set_extra_settings(self, dct):
        self.setIndentationGuidesBackgroundColor(QColor(0, 0, 255, 0))
        self.setIndentationGuidesForegroundColor(QColor(0, 255, 0, 0))

        if "caret" in dct:
            self.setCaretForegroundColor(QColor(dct["caret"]))

        if "line_highlight" in dct:
            self.setCaretLineBackgroundColor(QColor(dct["line_highlight"]))

        if "edge_color" in dct:
            self.setEdgeColor(QColor(dct["edge_color"]))

        if "brackets_background" in dct:
            self.setMatchedBraceBackgroundColor(
                QColor(dct["brackets_background"])
            )

        if "brackets_foreground" in dct:
            self.setMatchedBraceForegroundColor(
                QColor(dct["brackets_foreground"])
            )

        if "selection" in dct:
            self.setSelectionBackgroundColor(QColor(dct["selection"]))

        if "background" in dct:
            c = QColor(dct["background"])
            self.resetFoldMarginColors()
            self.setFoldMarginColors(c, c)
