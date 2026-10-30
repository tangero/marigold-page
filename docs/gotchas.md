# Gotchas — nečekané chování a důležité detaily

Nové záznamy přidávej nahoru. Formát: nadpis s datem, **Vzorec** (co se stalo), **Pravidlo** (jak postupovat).

## Nový článek se nevydává bez titulního obrázku a odkazu na zdroj (2026-10-30)

- **Vzorec:** článek o Protonu šel na web s prázdným `thumbnail` (pro sdílení se použil avatar) a se zdrojem bez odkazu. Obojí se doplňovalo dalšími dvěma deployi.
- **Pravidlo:** před vydáním článku zkontroluj `thumbnail` a odkazy na zdroje. Když chybí, vyžádej si je od autora ještě před pushem, ne až po vydání.

## GitHub Pages rozlišuje velikost písmen v názvech souborů, macOS ne (2026-10-28)

- **Vzorec:** 13 obrázků v `content/obrazy/` a jinde odkazovalo na `/assets/obrazy/anderle-jiri-…jpg`, ale soubor se jmenoval `Anderle-jiri-…jpg`. Lokálně (`hugo server`, `os.path.exists` na macOS) vše fungovalo, na webu 404. Kontrolní skript existence souborů to nenašel, protože souborový systém macOS velikost písmen ignoruje.
- **Pravidlo:** existenci souboru ověřuj proti `git ls-files` (přesná shoda řetězce), ne proti disku. Nové soubory pojmenovávej malými písmeny, bez mezer a diakritiky.

## Diakritika v názvu souboru může být v jiné normalizaci než v odkazu (2026-10-28)

- **Vzorec:** článek „Piráti se STANem“ odkazoval na `Sni%CC%81mek-…png` (rozložené „í“ = `i` + kombinující čárka, NFD), v gitu byl soubor jako `Sn%C3%ADmek-…` (NFC). Vizuálně stejné, na GitHub Pages 404.
- **Pravidlo:** u souborů s diakritikou porovnávej bajty (`git -c core.quotepath=false ls-files … | xxd`). Raději soubor přejmenuj na ASCII.

## Velké soubory ve `static/` zpomalují deploy až k limitu GitHub Pages (2026-10-28)

- **Vzorec:** deploy trval 2–10 min, artefakt měl 760 MB (audio 334 MB, nekomprimované obrázky 350 MB, archiv tech-news). Krok `deploy-pages` kolísal 6 s – 8 min. GitHub Pages má limit 1 GB na web a výchozí timeout deploye 10 min.
- **Pravidlo:** audio a video do R2 (`media.vibecoding.cz/marigold/…`), obrázky jako WebP (viz CLAUDE.md). Po větší změně zkontroluj velikost artefaktu: `gh api repos/tangero/marigold-page/actions/runs/<id>/artifacts --jq '.artifacts[].size_in_bytes'`. Dnes ~140 MB.

## Hugo 0.169+ odmítne `content/aiprace.html` (2026-10-28)

- **Vzorec:** lokální Hugo z brew (0.169) skončí chybou `"text/html" is not whitelisted in policy "security.allowContent"`. CI běží na 0.159.1, kde to prochází.
- **Pravidlo:** lokálně builduj s doplňkovým configem `hugo --minify --config hugo.toml,sec.toml`, kde `sec.toml` obsahuje `[security]` / `allowContent = [".*"]`. Při upgradu Huga v CI přidej `security.allowContent` do `hugo.toml`.

## Na obrázky marigoldu odkazuje i vibecoding.cz (2026-10-28)

- **Vzorec:** po převodu obrázků na WebP přestaly fungovat 3 obrázky v článcích na vibecoding.cz, které odkazovaly na `https://www.marigold.cz/assets/*.png`.
- **Pravidlo:** před přejmenováním nebo smazáním souboru ve `static/assets/` hledej odkazy i ve vedlejším repu: `grep -rn "marigold.cz/assets/<soubor>" ~/Github/vibecoding-site/src`. Staré URL po změně vracejí 404 (GitHub Pages neumí přesměrování).

## Kontrola rozbitých odkazů nesmí uříznout dvojitou příponu (2026-10-28)

- **Vzorec:** regex `assets/…?\.(png|jpg|webp)` (líný) zachytil z `/assets/Agent.png.webp` jen `/assets/Agent.png` a hlásil falešně rozbitý odkaz. Soubory typu `*.png.webp` a `*.jpg.webp` ve `static/assets/` existují.
- **Pravidlo:** při hledání odkazů ber cestu až k oddělovači (`"`, `)`, mezera), ne k první příponě.

## Obsah webu je jen v `content/` (2026-07-11, doplněno 2026-10-28)

- **Vzorec:** push notifikace (OneSignal, FCM) hledaly nové články v `_posts/` z doby Jekyllu, které se po přechodu na Hugo neplnily, a proto nefungovaly. Duplicitní Jekyll složky (`_posts/` s ~3000 články a další) se pak držely v repu až do 2026-10-28, kdy byly smazány.
- **Pravidlo:** skripty a workflowy čtou obsah z `content/`. Starší Jekyll verzi článku hledej v historii gitu (`git log --all -- _posts/<rok>-…`).
