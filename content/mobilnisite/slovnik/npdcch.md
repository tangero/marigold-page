---
slug: "npdcch"
url: "/mobilnisite/slovnik/npdcch/"
type: "slovnik"
title: "NPDCCH – Narrow Band Physical Downlink Control Channel"
date: 2025-01-01
abbr: "NPDCCH"
fullName: "Narrow Band Physical Downlink Control Channel"
category: "Physical Layer"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/npdcch/"
summary: "Fyzický řídicí kanál v downlinku navržený pro LTE-M (LTE pro Machine-Type Communications) a NB-IoT. Přenáší řídicí informace v downlinku (Downlink Control Information, DCI) pro plánování přenosů dat v"
---

NPDCCH je úzkopásmový fyzický řídicí kanál v downlinku (Narrow Band Physical Downlink Control Channel) v sítích LTE-M a NB-IoT, který přenáší řídicí informace v downlinku (Downlink Control Information) pro plánování přenosů dat pro nízkopříkonová IoT zařízení v široké geografické oblasti.

## Popis

Úzkopásmový fyzický řídicí kanál v downlinku (Narrow Band Physical Downlink Control Channel, NPDCCH) je základní kanál fyzické vrstvy zavedený ve specifikaci 3GPP Release 13 jako součást rádiových přístupových technologií LTE-M (eMTC) a NB-IoT. Operuje v úzkém pásmu 180 kHz (jeden blok fyzických zdrojů, Physical Resource Block, v LTE), což je klíčový konstrukční princip pro IoT pro snížení složitosti a spotřeby energie zařízení. Primární funkcí NPDCCH je přenášet řídicí informace v downlinku (Downlink Control Information, [DCI](/mobilnisite/slovnik/dci/)), které poskytují uživatelskému zařízení (UE) potřebné plánovací příkazy a řídicí povely. Konkrétně informuje UE o přidělení zdrojů pro úzkopásmový fyzický sdílený kanál v downlinku (Narrowband Physical Downlink Shared Channel, [NPDSCH](/mobilnisite/slovnik/npdsch/)) pro příjem dat a pro úzkopásmový fyzický sdílený kanál v uplinku (Narrowband Physical Uplink Shared Channel, [NPUSCH](/mobilnisite/slovnik/npusch/)) pro přenos dat.

Z architektonického hlediska je NPDCCH mapován na specifické prvky zdrojů (resource elements) v rámci úzkopásmového nosiče. Podporuje různé formáty DCI přizpůsobené pro případy užití IoT, jako je plánování malých datových paketů a paging. Kritickým aspektem jeho fungování je koncept opakování (repetice) a rozšířeného pokrytí. NPDCCH může být vysílán s mnoha opakováními (pokrývajícími více podrámců) pro dosažení zařízení v náročných rádiových podmínkách, jako jsou hluboko uvnitř budov nebo sklepy, což je běžný požadavek pro nasazení IoT. Kanál využívá specifický prohledávací prostor (search space), kde UE monitoruje potenciální zprávy DCI, a toto monitorování je konfigurováno tak, aby probíhalo v konkrétních, potenciálně řídkých intervalech za účelem šetření životnosti baterie zařízení.

Z procesního hlediska je NPDCCH klíčový pro proceduru náhodného přístupu (random access), paging a navázání spojení v LTE-M/NB-IoT. Síť konfiguruje UE parametry jako perioda NPDCCH, počáteční podrámec a počet opakování. UE se z úsporného režimu nečinnosti (např. Power Saving Mode nebo rozšířený Discontinuous Reception, eDRX) probouzí v těchto nakonfigurovaných časech, aby provedlo slepou dekódaci NPDCCH pro případné zprávy. Úspěšná dekódace poskytne UE informace o časově-frekvenčních zdrojích a modulačním a kódovacím schématu pro následný datový kanál (NPDSCH/NPUSCH), což umožňuje efektivní komunikaci šetřící baterii.

## K čemu slouží

NPDCCH byl vytvořen, aby řešil specifické potřeby řídicí signalizace pro nízkopříkonová IoT zařízení v široké geografické oblasti (Low-Power Wide-Area, [LPWA](/mobilnisite/slovnik/lpwa/)) v rámci ekosystému 3GPP. Před Release 13 byly standardní fyzické řídicí kanály LTE ([PDCCH](/mobilnisite/slovnik/pdcch/), [EPDCCH](/mobilnisite/slovnik/epdcch/)) navrženy pro vysokovýkonný mobilní širokopásmový přístup, což vyžadovalo, aby zařízení často monitorovala široké pásmo, což vedlo k nepřijatelné spotřebě energie a nákladům pro jednoduché senzory a měřiče napájené bateriemi. Stávající kanály také nebyly optimalizovány pro extrémní rozšíření pokrytí (až o 20 dB nad rámec běžného pokrytí LTE) požadované pro mnohé průmyslové IoT aplikace.

Zavedení NPDCCH spolu s [NPDSCH](/mobilnisite/slovnik/npdsch/) a [NPUSCH](/mobilnisite/slovnik/npusch/) bylo základním kamenem standardizace celulárního IoT. Jeho úzkopásmová povaha přímo snižuje požadavky na základnové pásmo UE a jeho cenu. Co je ještě důležitější, jeho podpora rozsáhlého opakování a flexibilní, na UE specifické konfigurace monitorovacích okamžiků umožňuje dramatické zlepšení životnosti baterie – umožňuje provozní životnost zařízení 10 let a více na jedno nabití baterie. Řeší problém doručení spolehlivé řídicí signalizace masově nasazeným zařízením s nízkou složitostí ve všech podmínkách pokrytí, od výborných po extrémní, aniž by je zatěžoval režií plnohodnotného LTE přijímače. To učinilo celulární technologii životaschopnou a konkurenceschopnou volbou pro rozsáhlý tržní segment LPWA IoT.

## Klíčové vlastnosti

- Operuje v rámci úzkopásmového nosiče o šířce 180 kHz
- Přenáší řídicí informace v downlinku (Downlink Control Information, DCI) pro plánování NPDSCH a NPUSCH
- Podporuje rozsáhlé opakování (repetice) pro rozšíření pokrytí až do 164 dB MCL
- Konfigurovatelné monitorovací okamžiky pro ultra nízkou spotřebu energie prostřednictvím rozšířeného DRX (eDRX)
- Používá specifické formáty DCI optimalizované pro malé IoT datové pakety
- Nezbytný pro procedury jako náhodný přístup (random access), paging a navázání RRC spojení v LTE-M/NB-IoT

## Související pojmy

- [NPDSCH – Narrow Band Physical Downlink Shared Channel](/mobilnisite/slovnik/npdsch/)
- [NPUSCH – Narrowband Physical Uplink Shared Channel](/mobilnisite/slovnik/npusch/)
- [DCI – Downlink Control Information](/mobilnisite/slovnik/dci/)

## Definující specifikace

- **TS 36.201** (Rel-19) — LTE Physical Layer General Description
- **TS 36.211** (Rel-19) — LTE Physical Layer Specification
- **TS 36.212** (Rel-19) — LTE Multiplexing and Channel Coding
- **TS 36.300** (Rel-19) — E-UTRAN Radio Interface Protocol Architecture Overview
- **TS 36.302** (Rel-19) — E-UTRA Physical Layer Services
- **TS 36.321** (Rel-19) — E-UTRA MAC Protocol Specification
- **TS 36.331** (Rel-19) — LTE RRC Protocol Specification
- **TR 38.889** (Rel-16) — NR-based access to unlicensed spectrum study

---

📖 **Anglický originál a plná specifikace:** [NPDCCH na 3GPP Explorer](https://3gpp-explorer.com/glossary/npdcch/)
