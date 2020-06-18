# Plot / Interval / Polar / Stacked
# No description available.
# ---
from synth import FakeMultiCategoricalSeries
from telesync import Site, data, ui

site = Site()

page = site['/demo']

n = 10
k = 5
f = FakeMultiCategoricalSeries(groups=k)
v = page.add('example', ui.plot_card(
    box='1 1 4 5',
    title='Intervals, polar, stacked',
    data=data('country product price', n * k),
    vis=ui.vis([
        ui.mark(coord='polar', mark='interval', x='=product', y='=price', color='=country', stack='auto', y_min=0)])
))

v.data = [(g, t, x) for x in [f.next() for _ in range(n)] for g, t, x, dx in x]

page.sync()