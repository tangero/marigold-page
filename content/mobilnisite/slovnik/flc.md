---
slug: "flc"
url: "/mobilnisite/slovnik/flc/"
type: "slovnik"
title: "FLC – Frequency Layer Convergence"
date: 2025-01-01
abbr: "FLC"
fullName: "Frequency Layer Convergence"
category: "Radio Access Network"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/flc/"
summary: "Frequency Layer Convergence je síťově řízený mechanismus mobility v UMTS, který navádí uživatelské zařízení, aby se připojilo k nejvhodnější frekvenční vrstvě (např. 900 MHz vs 2100 MHz) v rámci vícev"
---

FLC je síťově řízený mechanismus mobility v UMTS, který navádí uživatelské zařízení, aby se připojilo k nejvhodnější frekvenční vrstvě v rámci vícevrstvého nasazení, a tím optimalizovalo kapacitu, vyrovnávání zatížení a uživatelský zážitek.

## Popis

Frequency Layer Convergence (FLC) je funkce správy rádiových zdrojů ([RRM](/mobilnisite/slovnik/rrm/)) definovaná ve specifikacích 3GPP pro sítě UMTS ([WCDMA](/mobilnisite/slovnik/wcdma/)), podrobně popsaná v dokumentech TS 25.346 a TS 26.111. Funguje v rámci řadiče rádiové sítě ([RNC](/mobilnisite/slovnik/rnc/)) za účelem řízení distribuce uživatelských zařízení (UE) mezi více nosnými kmitočty neboli 'frekvenčními vrstvami' ve stejné geografické oblasti. Typické nasazení může používat vrstvu 2100 MHz pro kapacitu a vrstvu 900 MHz pro pokrytí; FLC inteligentně přiřazuje UE k nejvhodnější vrstvě. Mechanismus je primárně síťově řízený, spoléhá na měření a explicitní signalizaci z RNC směrem k UE, nikoli na autonomní převýběr buňky ze strany UE.

Proces funguje v několika klíčových krocích. Nejprve síť vysílá na každé buňce systémové informace, které mohou obsahovat parametry související s FLC, jako jsou indikátory priority a prahové hodnoty. RNC, které má celkový přehled o zatížení a podmínkách na všech vrstvách, pak může řídit UE. Pro UE v idle módu se tak děje pomocí dedikované signalizace (např. zpráva [RRC](/mobilnisite/slovnik/rrc/) CONNECTION RELEASE), která obsahuje 'přesměrování' na konkrétní kmitočet a kód přeběhu. Pro UE v connected módu (ve stavech CELL_[FACH](/mobilnisite/slovnik/fach/), CELL_[PCH](/mobilnisite/slovnik/pch-text-pch/) nebo [URA](/mobilnisite/slovnik/ura/)_PCH) může RNC použít zprávu PHYSICAL CHANNEL RECONFIGURATION nebo CELL UPDATE CONFIRM, aby přikázalo UE přesunout se na cílovou frekvenční vrstvu. UE těmto síťovým příkazům vyhoví a provede potřebné procedury k připojení nebo navázání spojení na určené vrstvě.

Mezi klíčové součásti patří RNC, které hostí algoritmus a rozhodovací logiku FLC; UE, které musí podporovat příslušné procedury měření a signalizace; a Node B (základnová stanice), které vysílá potřebné pilotní kanály a bloky systémových informací ([SIB](/mobilnisite/slovnik/sib/)) pro každou vrstvu. Úlohou FLC je optimalizovat celkový výkon sítě. Umožňuje operátorům používat vyšší frekvenční vrstvy (s menšími buňkami) k absorbování uživatelů s vysokým provozem a vysokou přenosovou rychlostí, zatímco uživatele s omezeným pokrytím nebo zaměřené na hlasové služby navádí na nižší frekvenční vrstvy s lepšími šířicími charakteristikami. Toto vyrovnávání zatížení zabraňuje přetížení primární vrstvy, zlepšuje celkovou kapacitu vícevrstvé sítě a zvyšuje uživatelsky vnímanou kvalitu služeb snížením počtu spadlých hovorů a zlepšením datové propustnosti.

## K čemu slouží

FLC bylo vyvinuto k řešení provozních výzev, které přinášejí vícekmitočtová a vícevrstvá nasazení UMTS. S rozšiřováním sítí 3G operátoři často nasazovali další frekvenční vrstvy (např. přidání UMTS na 900 MHz vedle původního nasazení na 2100 MHz), aby zvýšili kapacitu nebo zlepšili pokrytí. Bez inteligentního řízení by se UE typicky připojovala k nejsilnějšímu pilotnímu signálu, což mohlo vést k tomu, že se všichni uživatelé shromáždili na jedné vrstvě, způsobili přetížení a neefektivně využívali celkový rádiový zdroj. Problém byl obzvláště akutní u služeb s různými požadavky; UE zapojené do jednoduchého hlasového hovoru nepotřebuje vysokou kapacitu mikrobunky na 2100 MHz, pokud makrobunka na 900 MHz nabízí dostatečnou službu s nižšími náklady na síťové zdroje.

Tato technologie existuje, aby vyřešila tuto nerovnováhu zatížení a optimalizovala využití zdrojů. Poskytuje síti přímou kontrolu nad distribucí UE, což je schopnost přesahující rámec tradičního převýběru buňky v idle módu, který je z velké části řízen UE a založen na naměřené síle/kvalitě signálu. FLC umožňuje RNC aplikovat provozní politiky – s ohledem na faktory jako aktuální zatížení vrstvy, typ služby (hlas vs. paketová data), schopnosti UE a stav mobility – za účelem učinit optimální rozhodnutí o přiřazení. To vede k lepší distribuci provozu, zvýšené celkové síťové kapacitě a konzistentnějšímu uživatelskému zážitku pro koncové uživatele.

Historicky zavedené v Rel-6 představovalo FLC významné vylepšení síťově řízené mobility pro UMTS. Řešilo omezení mechanismů z dřívějších releasů, kterým chyběla detailní, na službu zaměřená kontrola nad výběrem frekvenční vrstvy. Umožněním dynamického směrování provozu dovolilo operátorům maximalizovat návratnost investic do vícevrstvých kmitočtových aktiv a připravilo cestu pro sofistikovanější koncepty řízení provozu používané v pozdějších technologiích, jako jsou LTE a 5G NR.

## Klíčové vlastnosti

- Síťově řízené přesměrování UE mezi frekvenčními vrstvami UMTS
- Podpora UE v idle módu i v connected módu (CELL_FACH/PCH)
- Využívá signalizaci RRC pro explicitní příkazy k přiřazení vrstvy
- Umožňuje vyrovnávání zatížení a prevenci přetížení mezi vrstvami
- Umožňuje směrování provozu s ohledem na typ služby (např. hlas vs. data)
- Optimalizuje využití kmitočtových aktiv s různými šířicími charakteristikami

## Související pojmy

- [UMTS – Universal Mobile Telecommunications System](/mobilnisite/slovnik/umts/)
- [RNC – Radio Network Controller](/mobilnisite/slovnik/rnc/)
- [WCDMA – Wideband Code Division Multiple Access](/mobilnisite/slovnik/wcdma/)

## Definující specifikace

- **TS 25.346** (Rel-19) — MBMS in UTRA Technical Specification
- **TS 26.111** (Rel-19) — 3G-324M Terminal Specification for CS Multimedia

---

📖 **Anglický originál a plná specifikace:** [FLC na 3GPP Explorer](https://3gpp-explorer.com/glossary/flc/)
