import math
from datetime import date, timedelta
from html import escape
from src.p_data import CALENDAR_LABELS as labels, CALENDAR_PALETTES as palettes
from src.css_gen.calendar_css import calendar_base_css, calendar_legend_css

K_SHOW_DAYS = 90
K_START_MONDAY = True

def prepare_sequence():
    today = date.today()
    start = today - timedelta(days=K_SHOW_DAYS-1)
    sequence = [start + timedelta(days=i) for i in range(K_SHOW_DAYS)]
    return sequence

def add_pad(sequence):
    pad = sequence[0].weekday() if K_START_MONDAY else (sequence[0].weekday() + 1) % 7
    cells = [None] * pad + sequence[:]
    return cells

def valuesNNvmax(sequence, counts, is_rate):
    global values
    global vmax
    values = [counts.get(d.isoformat(), 0) for d in sequence]
    if is_rate:
        vmax = 5
    else:
        vmax = max(values) if values and max(values) > 5 else 5

def saturation_levels(v: int) -> int:
        if v <= 0 or vmax == 0: return 0
        bucket = math.ceil(v * 5 / vmax)
        return max(1, min(5, bucket))

def building_columns(cells):
    weeks = math.ceil(len(cells) / 7)
    columns = []
    for w in range(weeks):
        col = cells[w*7:(w+1)*7]
        while len(col) < 7: col.append(None)
        columns.append(col)
    return columns

def columns_html(counts, columns):
    cols_html = []
    for col in columns:
        for d in col:
            if d is None:
                cols_html.append("<div class='day' title=''></div>")
            else:
                v = counts.get(d.isoformat(), 0)
                lvl = saturation_levels(v)
                tip = f"{d.isoformat()} • {v}"
                cols_html.append(f"<div class='day l{lvl}' title='{escape(tip)}'></div>")
    grid = "<div class='grid'>" + "".join(cols_html) + "</div>"
    return grid

def html(counts: dict[str, int], title, is_rate=False) -> str:
    # counts: {"YYYY-MM-DD": int}
    # int — activity (number of answers per day) or rate.
    color = "green" if is_rate else "blue"

    sequence = prepare_sequence()
    cells = add_pad(sequence)
    valuesNNvmax(sequence, counts, is_rate)
    columns = building_columns(cells)
    css = calendar_base_css(palettes[color], cls=f"calendar-{color}")
    legend = calendar_legend_css(palettes[color], vmax)
    grid = columns_html(counts, columns)

    heading = f"<h3 class='mhm'>{escape(title)}</h3>"
    return css + f"<div class='calendar-{color}'>" + heading + "<div class='wrap'>" + labels + grid + "</div>" + legend