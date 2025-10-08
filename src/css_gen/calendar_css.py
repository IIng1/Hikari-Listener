def calendar_base_css(colors, cls):
    return f"""
    <style>
      .{cls} {{
        --c0:{colors[0]}; --c1:{colors[1]}; --c2:{colors[2]};
        --c3:{colors[3]}; --c4:{colors[4]}; --c5:{colors[5]};
        --cell:12px; --gap:3px; --font:12px;
      }}
      .mhm{{font-family: ui-sans-serif,system-ui,Segoe UI,Helvetica,Arial,sans-serif;}}
      .wrap{{display:flex;gap:12px;align-items:flex-start}}
      .grid{{display:grid;grid-auto-flow:column;grid-auto-columns:max-content;grid-template-rows:repeat(7,var(--cell));gap:var(--gap)}}
      .day{{width:var(--cell);height:var(--cell);border-radius:3px;background:var(--c0);transition:background 0.2s}}
      .l1{{background:var(--c1)}} 
      .l2{{background:var(--c2)}} 
      .l3{{background:var(--c3)}} 
      .l4{{background:var(--c4)}} 
      .l5{{background:var(--c5)}}
      .day:hover{{outline:1px solid #999; cursor:pointer}}
      .labels{{display:grid;grid-template-rows:repeat(7,var(--cell));gap:var(--gap);font-size:var(--font);color:#777}}
      .legend{{display:flex;align-items:center;gap:6px;font-size:var(--font);color:#555;margin-top:8px}}
      .swatch{{width:var(--cell);height:var(--cell);border-radius:3px}}
    </style>
    """

def calendar_legend_css(colors, vmax):
    return (
      "<div class='legend'>0 "
      f"<span class='swatch' style='background:{colors[0]}'></span>"
      f"<span class='swatch' style='background:{colors[1]}'></span>"
      f"<span class='swatch' style='background:{colors[2]}'></span>"
      f"<span class='swatch' style='background:{colors[3]}'></span>"
      f"<span class='swatch' style='background:{colors[4]}'></span>"
      f"<span class='swatch' style='background:{colors[5]}'></span> {vmax}</div>"
    )