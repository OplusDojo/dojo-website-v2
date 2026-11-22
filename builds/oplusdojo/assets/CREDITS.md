# Photo credits

All photos are from Unsplash under the Unsplash License (free for commercial use, no attribution required). They were graded to one look with ffmpeg (desaturated, slight cool balance).

| File | Unsplash page | Used in |
|---|---|---|
| city.jpg, city-m.jpg | https://unsplash.com/photos/a-view-of-a-city-skyline-from-a-body-of-water-62UWrTdRq78 | II. The builders (Toronto skyline) |
| first.jpg | https://unsplash.com/photos/two-people-drawing-on-whiteboard-26MJGnCM0Wc | I. You first |
| ops.jpg | https://unsplash.com/photos/modern-data-center-with-rows-of-white-server-cabinets-fImCPTZ026U | IV. Ownership |

None of these photos show O+Dojo staff, and the captions do not claim they do.

## Tech logos
assets/tech/*.svg from Simple Icons v13 (CC0 1.0). Brand marks remain trademarks of their owners; shown to name the tools we work with.

## RaLHF
assets/ralhf/* captured from https://ralhf.ai/ on 2026-10-31 (Bot Food Co, sister company).

## Office network map

Land geometry: Natural Earth, 1:110m physical land, public domain.
https://www.naturalearthdata.com/about/terms-of-use/
Source geometry: https://github.com/nvkelso/natural-earth-vector/blob/master/geojson/ne_110m_land.geojson
Rounded geographic data is stored in `lab/gen/offices-land.json`; `lab/gen/offices.py`
samples it into a dotted SVG map during the existing page build. Office markers
use approximate city centres for the four offices already listed in the footer.
