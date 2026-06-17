---
slug: "dlmc"
url: "/mobilnisite/slovnik/dlmc/"
type: "slovnik"
title: "DLMC – Downlink Multi Carrier"
date: 2025-01-01
abbr: "DLMC"
fullName: "Downlink Multi Carrier"
category: "Radio Access Network"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/dlmc/"
summary: "Technika rádiového přenosu v sítích GSM/EDGE, kdy základnová stanice (BTS) vysílá na více rádiových kmitočtových nosných současně ve směru downlink. Zvyšuje kapacitu a datovou propustnost agregací nos"
---

DLMC je technika rádiového přenosu v sítích GSM/EDGE, při níž základnová stanice (BTS) vysílá na více rádiových kmitočtových nosných současně v downlinku za účelem zvýšení kapacity buňky a datové propustnosti.

## Popis

Downlink Multi Carrier (DLMC) je funkce definovaná ve specifikacích GSM/[EDGE](/mobilnisite/slovnik/edge/) Radio Access Network ([GERAN](/mobilnisite/slovnik/geran/)). Umožňuje jedné základnové stanici ([BTS](/mobilnisite/slovnik/bts/)) využívat více než jednu rádiovou kmitočtovou nosnou v downlinku (ze sítě k uživatelskému zařízení) pro jedinou buňku. Tradičně byla buňka GSM obsluhována jednou nosnou [BCCH](/mobilnisite/slovnik/bcch/) (Broadcast Control Channel) a více nosnými TCH (Traffic Channel), ale BTS mohla být vybavena pro současný přenos na několika z těchto nosných. DLMC tuto schopnost formalizuje a optimalizuje, zejména pro vylepšení paketově přepínaných datových služeb prostřednictvím EDGE.

Technicky, v konfiguraci DLMC buňka vysílá systémové informace a řídicí kanály na primární nosné (typicky obsahující BCCH). Další nosné jsou použity jako sekundární a jsou primárně vyhrazeny pro provozní kanály. Klíčovým provozním aspektem je přidělování zdrojů. Mobilní stanice ([MS](/mobilnisite/slovnik/ms/)) schopné DLMC (indikováno v jejich rádiových přístupových schopnostech) mohou mít současně přiděleny zdroje na více downlinkových nosných. Toto je řízeno BTS a Packet Control Unit (PCU) pro provoz [GPRS](/mobilnisite/slovnik/gprs/)/EDGE. MS musí mít přijímací schopnost pro dekódování více nosných, což může zahrnovat příjem v širším pásmu nebo pokročilé zpracování signálu.

Z architektonického pohledu DLMC ovlivňuje rádiovou jednotku BTS, která vyžaduje více výkonových zesilovačů a transceiverů (jeden na nosnou). Ovlivňuje také rozhraní Abis mezi BTS a Base Station Controller ([BSC](/mobilnisite/slovnik/bsc/)), protože musí být podporována kapacita pro provoz z více nosných. Hlavním přínosem je zisk ze statistického multiplexování: buňka může obsloužit více uživatelů a přidělit vyšší datové rychlosti jednotlivým uživatelům sdružováním časových slotů (TSL) napříč více nosnými. Například uživateli EDGE mohou být přiděleny vícečetné časové sloty rozložené na dvou nebo třech různých nosných, čímž se efektivně zvýší downlinková datová rychlost nad možnosti osmi časových slotů jedné nosné.

## K čemu slouží

DLMC byl vyvinut pro řešení rostoucích požadavků na kapacitu a datovou rychlost v sítích GSM, zejména s nástupem mobilních dat přes [GPRS](/mobilnisite/slovnik/gprs/) a EDGE. Základním omezením buňky s jednou nosnou je její konečný počet časových slotů (8 na nosnou 200 kHz). S rostoucí hustotou uživatelů a datovými nároky se buňky stávaly přetíženými. Přidávání dalších buněk s jednou nosnou (sektorizace) zvyšuje náklady a složitost kvůli potřebě více lokalit a plánování kmitočtů. DLMC poskytl spektrálně efektivnější a nákladově výhodnější řešení tím, že umožnil jedné buňce (a tedy jednomu místu BTS) využívat další kmitočtové nosné ve svém přiděleném spektrálním bloku.

Vyřešil problém 'úzkého hrdla jedné nosné'. Před DLMC, i když měl operátor na lokalitě přiděleno více kmitočtových kanálů, byly často nasazeny jako logicky oddělené buňky (s vlastním BCCH). DLMC umožňuje agregaci těchto nosných pod jednu identitu buňky, což zjednodušuje správu mobility (méně hranic buněk) a zlepšuje využití zdrojů. Byl to odrazový můstek k pokročilejším konceptům více nosných a agregace nosných, které byly později vidět v 3G (Multi-Carrier HSPA) a 4G/5G. Motivací bylo prodloužit životnost a konkurenceschopnost sítí GSM/EDGE tváří v tvář se rozvíjejícím technologiím 3G a poskytnout plynulejší migrační cestu zvýšením datového výkonu na stávající infrastruktuře.

## Klíčové vlastnosti

- Přenos na více RF nosných v rámci jedné buňky GSM
- Zvýšená kapacita provozních kanálů a špičkových datových rychlostí v downlinku
- Dynamické přidělování časových slotů napříč agregovanými nosnými
- Vyžaduje přijímací schopnost MS pro současný příjem na více nosných
- Řízeno BTS a PCU pro provoz GPRS/EDGE
- Zpětná kompatibilita s mobilními stanicemi pro jednu nosnou

## Související pojmy

- [GERAN – GSM EDGE Radio Access Network](/mobilnisite/slovnik/geran/)
- [EDGE – Enhanced Data rates for Global Evolution](/mobilnisite/slovnik/edge/)
- [BTS – Base Transceiver Station](/mobilnisite/slovnik/bts/)

## Definující specifikace

- **TS 43.064** (Rel-19) — GPRS Radio Interface Lower-Layer Functions
- **TS 44.060** (Rel-19) — GERAN RLC/MAC Protocol Specification
- **TS 45.005** (Rel-19) — GSM RF Requirements for MS and BSS

---

📖 **Anglický originál a plná specifikace:** [DLMC na 3GPP Explorer](https://3gpp-explorer.com/glossary/dlmc/)
