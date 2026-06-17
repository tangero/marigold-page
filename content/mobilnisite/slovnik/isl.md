---
slug: "isl"
url: "/mobilnisite/slovnik/isl/"
type: "slovnik"
title: "ISL – Inter-Satellite Links"
date: 2026-01-01
abbr: "ISL"
fullName: "Inter-Satellite Links"
category: "Radio Access Network"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/isl/"
summary: "Inter-Satellite Links (ISL) jsou bezdrátová spojení mezi satelity v neterestriální síti (NTN). Umožňují směrování a přenos dat mezi satelity bez nutnosti průchodu přes pozemní stanice, čímž vytvářejí"
---

ISL je bezdrátové spojení mezi satelity v neterestriální síti, které umožňuje směrování dat bez nutnosti pozemních stanic, čímž vytváří prostorovou síť typu mesh pro snížení latence a zlepšení globální konektivity.

## Popis

Inter-Satellite Links (ISL) jsou základní technologií pro pokročilé neterestriální sítě (NTN), jak je standardizuje 3GPP. Vytvářejí přímé komunikační cesty mezi satelity obíhajícími Zemi, jako jsou ty v konstelacích na nízké oběžné dráze ([LEO](/mobilnisite/slovnik/leo/)) nebo na geostacionární dráze ([GEO](/mobilnisite/slovnik/geo/)). Tato spojení mohou být optická (laserová) nebo na bázi rádiových frekvencí (RF), přičemž optická ISL nabízejí extrémně vysokou přenosovou kapacitu a zabezpečení. Primární architektonickou rolí ISL je vytvoření dynamické prostorové sítě typu mesh nebo přenosové sítě, která umožňuje směrovat datové pakety ze zdrojového satelitu k cílovému satelitu, přičemž mohou procházet přes více 'skoků' napříč konstelací.

Z pohledu provozu sítě transformují ISL konstelaci z jednoduché architektury typu 'bent-pipe' (ohnutá trubka), kde každý satelit pouze odráží signály k/z pozemní brány, na inteligentní, vzájemně propojenou prostorovou síť. To vyžaduje sofistikované palubní zpracování, směrovací protokoly a správu zdrojů v každém satelitu. Satelity musí udržovat stabilní, vysokokapacitní spoje navzdory jejich vysokým relativním rychlostem a velkým vzdálenostem. Protokoly pro navázání spojení, předávání spojení (handover) a směrování provozu jsou přizpůsobeny podmínkám kosmického prostředí s ohledem na faktory jako zpoždění šíření a přerušovaná viditelnost.

Integrace ISL do systémové architektury 3GPP, zejména pro 5G-Advanced a 6G, zahrnuje definici toho, jak satelitní síť rozhraní s terestriální jádrovou sítí. Satelit s možnostmi ISL funguje jako uzel radiového přístupu (např. jako IAB donor nebo gNB). Uživatelská data mohou putovat z uživatelského zařízení (UE) na Zemi k obsluhujícímu satelitu, poté přes jedno nebo více ISL k jinému satelitu, který má příznivé spojení s pozemní bránou nebo s jádrovou sítí. To umožňuje optimální výběr cesty, vyvažování zátěže napříč konstelací a zajištění kontinuity služby i v případě, že přímé pozemní spojení od obsluhujícího satelitu není k dispozici. Klíčové technické specifikace pokrývají aspekty jako fyzická vrstva pro ISL (38.811), síťová architektura (23.700) a bezpečnostní hlediska (33.700) pro tyto kritické prostorové spoje.

## K čemu slouží

ISL byly zavedeny, aby překonaly základní omezení tradičních architektur satelitní komunikace, konkrétně závislost na husté globální síti pozemních bránových stanic. V modelu 'bent-pipe' může satelit obsluhovat pouze uživatele v současné stopě, která pokrývá jak uživatele, tak pozemní stanici. To vytváří mezery v pokrytí nad oceány, polárními oblastmi a dalšími oblastmi bez bran a může způsobovat významnou latenci, pokud je pozemní stanice daleko od konečného cíle dat.

Vznik technologie ISL byl motivován rozvojem mega-konstelací a vizí poskytování bezproblémového globálního pokrytí 5G/6G. Tím, že umožňují satelitům přímo mezi sebou komunikovat, mohou být data směrována prostorem k nejoptimálnější pozemní bráně, nebo dokonce přímo mezi uživateli přes satelity, bez průchodu terestriální sítí. Tím se řeší problém pokrytí a může se dramaticky snížit koncová latence pro dálkovou komunikaci díky využití přímějších cest prostorem. ISL dále zvyšují odolnost sítě a kapacitu tím, že poskytují více redundantních cest pro data a umožňují efektivní vyvažování zátěže napříč celou satelitní konstelací.

## Klíčové vlastnosti

- Umožňuje prostorové síťování typu mesh pro směrování a přenos dat
- Snižuje závislost na husté globální síti pozemních bran
- Může významně snížit latenci u dálkových mezikontinentálních spojení
- Zlepšuje pokrytí služeb nad oceány, pouštěmi a polárními oblastmi
- Podporuje jak optické (laserové), tak rádiové frekvenční (RF) technologie spojů
- Zvyšuje odolnost sítě a kapacitu prostřednictvím redundance cest

## Definující specifikace

- **TS 22.261** (Rel-20) — 5G System Service Requirements
- **TR 22.865** (Rel-19) — Study on satellite access Phase 3
- **TS 23.700** (Rel-20) — XR Services Application Enablement Layer
- **TS 28.874** (Rel-19) — Study on Management Aspects of NTN Phase 2
- **TS 29.514** (Rel-19) — 5G System; Policy Authorization Service; Stage 3
- **TS 33.700** — 3GPP TR 33.700
- **TS 38.811** (Rel-15) — Study on NR Support for Non-Terrestrial Networks
- **TS 38.821** (Rel-16) — NR Support for Non-Terrestrial Networks
- **TS 38.863** (Rel-19) — NR NTN RF and Co-existence Spec

---

📖 **Anglický originál a plná specifikace:** [ISL na 3GPP Explorer](https://3gpp-explorer.com/glossary/isl/)
