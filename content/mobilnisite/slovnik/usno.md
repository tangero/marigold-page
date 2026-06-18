---
slug: "usno"
url: "/mobilnisite/slovnik/usno/"
type: "slovnik"
title: "USNO – US Naval Observatory"
date: 2025-01-01
abbr: "USNO"
fullName: "US Naval Observatory"
category: "Other"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/usno/"
summary: "V kontextu 3GPP je čas americké námořní observatoře (US Naval Observatory, USNO) vysoce přesným externím časovým zdrojem používaným pro synchronizaci, zejména ve službách určování polohy (LCS) a v asi"
---

USNO je americká námořní observatoř (US Naval Observatory), vysoce přesný externí časový zdroj používaný v 3GPP pro synchronizaci v rámci služeb určování polohy (Location Services) a pro zarovnání síťového časování.

## Popis

Ve specifikacích 3GPP je americká námořní observatoř (USNO) uvedena jako zdroj přesných časových informací, konkrétně koordinovaného světového času ([UTC](/mobilnisite/slovnik/utc/)). Tento externí časový zdroj využívají síťové i uživatelským zařízením (UE) založené metody určování polohy k dosažení vysoké přesnosti. Hlavní uplatnění nachází v rámci asistovaného globálního družicového navigačního systému ([A-GNSS](/mobilnisite/slovnik/a-gnss/)), kde síť poskytuje asistenční data uživatelskému zařízení (UE) pro urychlení zachycení satelitů a zlepšení přesnosti určení polohy.

Z architektonického hlediska může síťový server určování polohy, jako je Enhanced Serving Mobile Location Centre ([E-SMLC](/mobilnisite/slovnik/e-smlc/)) nebo Location Management Function ([LMF](/mobilnisite/slovnik/lmf/)) v 5G, získat přesný čas ze serveru času USNO prostřednictvím protokolu Network Time Protocol ([NTP](/mobilnisite/slovnik/ntp/)) nebo podobných mechanismů. Tyto časové informace jsou následně naformátovány a doručeny UE jako součást asistenčních dat v rámci zpráv protokolu LTE Positioning Protocol ([LPP](/mobilnisite/slovnik/lpp/)) nebo NR Positioning Protocol (NRPPa). Asistenční data mohou zahrnovat parametry jako referenční čas [GNSS](/mobilnisite/slovnik/gnss/), efemeridy satelitů a korekce hodin, které jsou často vztaženy k přesnému časovému zdroji, jako je USNO.

Když UE tato asistenční data obdrží, použije přesný časový referenční zdroj ke kalibraci svých lokálních hodin a k přesnějšímu výpočtu doby letu signálů z více družic GNSS (např. [GPS](/mobilnisite/slovnik/gps/), Galileo). Protože určování polohy pomocí trilaterace vyžaduje extrémně přesná časová měření (chyby v řádu nanosekund mohou vést k chybám polohy v řádu metrů), je existence společného referenčního zdroje s vysokou přesností, jako je čas USNO, klíčová. Umožňuje UE korigovat posun hodin a zarovnat svá měření s globální časovou stupnicí používanou družicovými konstelacemi.

Mimo A-GNSS jsou přesné externí časové zdroje, jako je USNO, důležité také pro požadavky na synchronizaci sítě, například v systémech s časovým duplexem (TDD) nebo pro koordinaci funkcí jako Coordinated Multipoint (CoMP). Přestože USNO není síťový prvek definovaný 3GPP, jeho zahrnutí do specifikací jako je 3GPP TS 36.355 (LPP) podtrhuje význam spolupráce s globálními časovými infrastrukturami pro splnění přísných požadavků na přesnost určení polohy pro tísňové služby, navigaci a další polohově závislé aplikace.

## K čemu slouží

Odkaz na americkou námořní observatoř (USNO) ve standardech 3GPP řeší potřebu vysoce přesného, stabilního a všeobecně uznávaného časového zdroje pro umožnění přesných polohových služeb. Rané služby určování polohy v celulárních sítích, jako Cell-ID, poskytovaly velmi hrubou přesnost. Zavedení A-GNSS v 3GPP si vyžádalo metodu pro poskytování přesných časových dat UE za účelem zkrácení doby do prvního určení polohy (TTFF) a zlepšení přesnosti lokalizace, zejména v náročných podmínkách příjmu signálu.

Použití externího autoritativního zdroje, jako je USNO, řeší problém zarovnání časové reference mezi celulární sítí, uživatelským zařízením (UE) a globálními družicovými konstelacemi. Bez společného přesného časového referenčního zdroje by asistenční data poskytovaná sítí byla méně účinná, protože jakákoli chyba v čase sítě by byla přenesena na UE, což by degradovalo výkon určování polohy. USNO jako primární časový standard pro Spojené státy a přispěvatel ke koordinovanému světovému času (UTC) poskytuje potřebnou úroveň přesnosti a spolehlivosti.

Tato integrace umožňuje systémům 3GPP splnit regulatorní požadavky na lokalizaci tísňových volání (např. E911 v USA) a umožňuje komerční polohově závislé služby s vysokou přesností. Představuje konvergenci telekomunikací s globálními navigačními a časovými infrastrukturami a zajišťuje, že celulární sítě mohou fungovat jako spolehlivá platforma pro přesné určování polohy díky využití etablovaných a důvěryhodných časových autorit.

## Klíčové vlastnosti

- Poskytuje autoritativní referenční zdroj koordinovaného světového času (UTC)
- Používá se k vytváření přesných časových asistenčních dat pro GNSS
- Umožňuje zkrácení doby do prvního určení polohy (TTFF) uživatelského zařízení (UE)
- Zlepšuje přesnost výpočtů polohy založených na družicích
- Slouží jako společný časový zdroj pro synchronizaci sítě
- Je uvedeno v normalizovaných polohových protokolech (LPP)

## Související pojmy

- [A-GNSS – Assisted Global Navigation Satellite Systems](/mobilnisite/slovnik/a-gnss/)
- [E-SMLC – Enhanced Serving Mobile Location Centre](/mobilnisite/slovnik/e-smlc/)

## Definující specifikace

- **TS 36.355** (Rel-19) — LTE Positioning Protocol (LPP)
- **TS 37.355** (Rel-19) — LTE Positioning Protocol (LPP)
- **TS 44.031** (Rel-19) — Radio Resource LCS Protocol (RRLP)

---

📖 **Anglický originál a plná specifikace:** [USNO na 3GPP Explorer](https://3gpp-explorer.com/glossary/usno/)
