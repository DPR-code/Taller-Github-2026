"""Utilidades del portapapeles. Separadas de la interfaz para poder testearlas sin pantalla."""


def copy_to_clipboard(widget, text):
    """Sustituye el contenido del portapapeles por `text` usando cualquier widget de Tk."""
    widget.clipboard_clear()
    widget.clipboard_append(text)
    # Procesa los eventos pendientes para que el portapapeles quede realmente asignado.
    widget.update()

