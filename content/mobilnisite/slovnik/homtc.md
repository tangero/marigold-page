---
slug: "homtc"
url: "/mobilnisite/slovnik/homtc/"
type: "slovnik"
title: "HOMTC – Higher Order Modulation and Turbo Codes"
date: 2025-01-01
abbr: "HOMTC"
fullName: "Higher Order Modulation and Turbo Codes"
category: "Physical Layer"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/homtc/"
summary: "Soubor pokročilých technik fyzické vrstvy kombinujících modulační schémata vyššího řádu, jako je 64-QAM, s Turbo kódy pro kanálové kódování. Významně zvyšuje spektrální účinnost a datovou propustnost"
---

HOMTC je soubor pokročilých technik fyzické vrstvy 3GPP kombinujících modulaci vyššího řádu s Turbo kódy za účelem zvýšení spektrální účinnosti a datové propustnosti.

## Popis

Higher Order Modulation and Turbo Codes (HOMTC) je zásadní vylepšení ve specifikacích 3GPP [GERAN](/mobilnisite/slovnik/geran/) (GSM/[EDGE](/mobilnisite/slovnik/edge/) Radio Access Network), konkrétně podrobně popsané v TS 45.912. Představuje dvoupronged přístup ke zvýšení přenosové kapacity a spolehlivosti rádiového rozhraní. Složka 'Higher Order Modulation' znamená posun od tradičních schémat [GMSK](/mobilnisite/slovnik/gmsk/) a [8-PSK](/mobilnisite/slovnik/8-psk/) používaných ve standardním EDGE k spektrálně účinnějším modulacím, jako jsou 16-QAM, 32-QAM a 64-QAM. Tato schémata mapují více bitů na každý vysílaný symbol, což přímo zvyšuje možnou špičkovou datovou rychlost v daném kanálovém pásmu. Složka 'Turbo Codes' zavádí výkonné schéma kódování pro dopřednou korekci chyb ([FEC](/mobilnisite/slovnik/fec/)). Turbo kódování, charakterizované svou paralelně zřetězenou konvoluční strukturou a iterativním dekódováním, poskytuje výkon korekce chyb blízký Shannonově limitě. Tato robustnost je klíčová, protože modulační schémata vyššího řádu jsou náchylnější k šumu a interferencím; vynikající korekce chyb Turbo kódů kompenzuje tuto zvýšenou zranitelnost a zajišťuje spolehlivý přenos dat i při vyšších modulačních řádech.

Architektonicky je HOMTC implementováno ve fyzické vrstvě základnové stanice GERAN ([BTS](/mobilnisite/slovnik/bts/)) a mobilní stanice. Zahrnuje úpravy bloků modulačního mapovače a kanálového kodéru na straně vysílače a odpovídajícím způsobem demodulátoru a kanálového dekodéru na straně přijímače. Systém musí podporovat adaptivní modulaci a kódování ([AMC](/mobilnisite/slovnik/amc/)), kdy síť dynamicky vybírá optimální kombinaci modulačního řádu a rychlosti Turbo kódu na základě ukazatelů kvality kanálu (CQIs) v reálném čase hlášených UE. Toto přizpůsobení spojení zajišťuje použití nejvyšší možné datové rychlosti při zachování přijatelné míry chybovosti bloků ([BLER](/mobilnisite/slovnik/bler/)). Mezi klíčové komponenty patří Turbo kodér/dekodér, symbolový mapovač/demapovař pro konstelace vyššího řádu a algoritmy pro odhad kanálu a iterativní dekódování.

Role HOMTC je ústřední pro projekt EDGE Evolution, jehož cílem bylo významně zvýšit výkonnost sítí GSM/EDGE jako doplněk k nasazením 3G HSPA. Posunutím teoretických limitů 200 kHz nosné GSM umožnilo HOMTC dosáhnout špičkových rychlostí na downlinku přesahujících 1 Mbps a na uplinku přes 500 kbps, čímž efektivně vytvořilo '3G-like' uživatelský zážitek na vyvinuté infrastruktuře 2.5G. Demonstrovalo, jak pokročilé techniky zpracování signálu mohou vdechnout nový život stávajícím spektrovým aktivům, a poskytnout tak operátorům nákladově efektivní zvýšení kapacity a propustnosti bez nutnosti kompletní přestavby sítě na WCDMA.

## K čemu slouží

HOMTC bylo vytvořeno jako odpověď na rostoucí poptávku po mobilních datových službách na konci první dekády 21. století, zejména pro operátory s rozsáhlým spektrem a infrastrukturou GSM/EDGE, kteří hledali konkurenceschopnou datovou nabídku před nebo souběžně s nasazením 3G/HSPA. Primárním problémem byla omezená spektrální účinnost standardního EDGE (používajícího 8-PSK a konvoluční kódy), která omezovala praktické datové rychlosti a kapacitu sítě. HOMTC tento problém přímo řešilo zavedením dvou osvědčených konceptů teorie informace do standardu GERAN.

Motivace vycházela z potřeby hladké evoluční cesty. Nasazení zcela nové rádiové přístupové technologie, jako je WCDMA, vyžadovalo nové licenční pásmo a nákladnou výstavbu paralelní sítě. HOMTC nabídlo alternativu: podstatné výkonnostní vylepšení v rámci stávající 200 kHz kanalizace a síťové architektury. Řešilo problém, jak dosáhnout vyšších datových rychlostí ve stejném omezeném přenosovém pásmu, což je základní výzva v bezdrátové komunikaci. Kombinací modulace vyššího řádu pro vysokou rychlost a Turbo kódů pro odolnost poskytlo vyvážené řešení, které maximalizovalo využitelnost nosné GSM. To umožnilo operátorům vylepšit svou služební nabídku, podporovat nově vznikající mobilní internetové aplikace a lépe využít své stávající investice při plánování migračních strategií na 3G/4G.

## Klíčové vlastnosti

- Podpora modulačních schémat vyššího řádu až do 64-QAM
- Integrace Turbo kódů pro výkonnou dopřednou korekci chyb
- Dynamické přizpůsobení spojení (AMC) na základě stavu kanálu
- Zpětná kompatibilita s legacy režimy GMSK a 8-PSK
- Významné zvýšení špičkové i průměrné spektrální účinnosti
- Umožňuje špičkové datové rychlosti na downlinku přesahující 1 Mbps v GERAN

## Související pojmy

- [GERAN – GSM EDGE Radio Access Network](/mobilnisite/slovnik/geran/)

## Definující specifikace

- **TR 45.912** (Rel-19) — GERAN Evolution Feasibility Study

---

📖 **Anglický originál a plná specifikace:** [HOMTC na 3GPP Explorer](https://3gpp-explorer.com/glossary/homtc/)
