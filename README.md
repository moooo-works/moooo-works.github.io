# moooo-works.github.io

Tenra landing pages and support documents, published by GitHub Pages from `main`.

## Update the Tenra pages

- `tool/filmstocks.json` holds the public film catalogue. Keep its names, premium flags and four-language personality copy aligned with the app's `assets/filmstocks.json`.
- Edit the four-language copy and shared layout in `tool/gen.py`, then run `python3 tool/gen.py` from the repository root. Commit the generator, catalogue and all four generated `index.html` files together.
- Catalogue counts in page headings and metadata are calculated from the JSON. Do not hardcode a new count in the HTML.
- `tenra-support.md` contains the FAQ and stable `en` / `zh` / `ja` / `ko` anchors.
- 2026-09-13: Pages reflect **1.7.0**: 11 films / 5 free, new free Kentmere PAN 400 and Agfa Vista 400, and a free capture-date back. Volume-button capture has been available since 1.6.1 (Android / iOS 17.2+). Keep the release section, metadata and four-language support FAQ aligned when updating.

Before publishing, regenerate the pages, check all language versions and local asset links, and inspect desktop/mobile layouts. After pushing, verify the GitHub Pages build and live pages.
