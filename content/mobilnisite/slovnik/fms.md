---
slug: "fms"
url: "/mobilnisite/slovnik/fms/"
type: "slovnik"
title: "FMS – First Missing PDCP SN"
date: 2025-01-01
abbr: "FMS"
fullName: "First Missing PDCP SN"
category: "Protocol"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/fms/"
summary: "Pole ve stavové zprávě PDCP označující první chybějící pořadové číslo (SN) PDCP v přijímacím okně. Je klíčové pro efektivní detekci ztrát a retransmise založené na ARQ v LTE a NR, což umožňuje spolehl"
---

FMS je pole ve stavové zprávě PDCP, které označuje první chybějící pořadové číslo (SN) PDCP v přijímacím okně. Umožňuje efektivní detekci ztrát a retransmise pro spolehlivé doručování dat v LTE a NR.

## Popis

First Missing [PDCP](/mobilnisite/slovnik/pdcp/) [SN](/mobilnisite/slovnik/sn/) (FMS) je klíčový informační prvek ve stavové zprávě PDCP (Packet Data Convergence Protocol), definovaný v 3GPP TS 36.323. Funguje v kontextu potvrzovaného režimu ([AM](/mobilnisite/slovnik/am/)) [RLC](/mobilnisite/slovnik/rlc/) (Radio Link Control) pro datové přenosy v uživatelské rovině, kde je vyžadováno spolehlivé doručení. Vrstva PDCP, umístěná nad RLC, je zodpovědná za kompresi hlaviček, šifrování a doručování ve správném pořadí. Když jsou přijaty pakety mimo pořadí, přijímající PDCP entita použije stavové zprávy, aby informovala vysílač o chybějících paketech, přičemž pole FMS přesně určuje začátek jakékoli mezery v sekvenci.

Z architektonického hlediska si PDCP entita udržuje přijímací okno pro sledování příchozích PDCP protokolových datových jednotek ([PDU](/mobilnisite/slovnik/pdu/)). Každá PDU nese PDCP SN. Při detekci chybějícího SN (např. kvůli selhání retransmise RLC nebo chybám na rádiovém rozhraní) přijímač vygeneruje stavovou zprávu PDCP. Tato zpráva obsahuje FMS, což je nejnižší SN, který nebyl úspěšně přijat a pro který všechny nižší SN byly přijaty nebo také chybí v souvislém bloku. V podstatě označuje začátek události ztráty v sekvenčním prostoru.

Jak to funguje: přijímač sleduje PDCP SN příchozích PDU. Když je detekována mezera, přijímač nastaví hodnotu FMS na SN první chybějící PDU. Tato stavová zpráva je následně odeslána zpět vysílající PDCP entitě, obvykle spuštěna specifickými událostmi, jako je periodické hlášení nebo při detekci chybějících dat. Vysílač použije FMS spolu s bitmapou následujících chybějících SN (pokud je součástí zprávy), aby přesně identifikoval, které PDU je potřeba retransmitovat. Tento mechanismus je nedílnou součástí podpory bezestratového předávání spojení (lossless handover) na vrstvě PDCP a spolehlivé služby pro určité QoS toky.

Jeho role v síti spočívá ve zlepšení integrity a efektivity přenosu dat. Přesnou identifikací prvního chybějícího paketu minimalizuje nejednoznačnost retransmise a snižuje režii ve srovnání s úplnými výčty sekvencí. To je zvláště důležité pro aplikace citlivé na latenci a během předávání spojení, kdy musí být ztráta paketů rychle napravena. FMS je základní součástí mechanismu [ARQ](/mobilnisite/slovnik/arq/) (Automatic Repeat Request) PDCP, který zajišťuje robustní přenos dat v LTE a 5G NR rádiových přístupových sítích.

## K čemu slouží

FMS bylo zavedeno, aby řešilo potřebu efektivní a spolehlivé detekce a obnovy ztráty paketů na vrstvě [PDCP](/mobilnisite/slovnik/pdcp/) v systémech 3GPP, počínaje LTE v Release 8. Předchozí přístupy ve starších mobilních standardech se často spoléhaly pouze na [RLC](/mobilnisite/slovnik/rlc/) pro retransmise, což mohlo být nedostatečné během určitých událostí mobility, jako je předávání spojení, kdy mohou být kontexty RLC resetovány. Obnova na vrstvě PDCP poskytuje dodatečné zabezpečení integrity dat.

Primární problém, který řeší, je umožnění bezestratového předávání spojení a spolehlivé datové služby pro specifické přenosy (bearers). Běham předávání spojení mezi eNodeB v LTE nebo mezi gNB v NR zdrojový uzel přeposílá nepotvrzené PDCP PDU do cílového uzlu. Přijímající PDCP entita v cíli nebo v UE musí identifikovat případné mezery v sekvenci, aby mohla požadovat retransmise, a FMS poskytuje kompaktní způsob, jak signalizovat počáteční bod těchto mezer. To zajišťuje plynulou kontinuitu dat bez ztráty paketů, což je kritické pro aplikace jako VoIP nebo hraní v reálném čase.

Historicky, bez stavového hlášení PDCP a FMS, závisela obnova ze ztráty paketů během mobility zcela na protokolech vyšších vrstev, jako je TCP, což mohlo zavést významnou latenci kvůli pomalému startu a časovačům pro retransmise. Mechanismus FMS umožňuje rychlejší obnovu specifickou pro danou vrstvu, čímž zlepšuje uživatelský zážitek a efektivitu sítě. Řeší omezení spoléhání se pouze na ARQ RLC, které nemusí přežít předání spojení, tím, že poskytuje trvalou schopnost detekce ztrát na koncích (mezi UE a kotvícím uzlem).

## Klíčové vlastnosti

- Identifikuje první chybějící pořadové číslo (SN) PDCP v přijímacím okně
- Umožňuje efektivní retransmise založené na ARQ na vrstvě PDCP
- Podporuje procedury bezestratového předávání spojení (lossless handover) v LTE a NR
- Snižuje signalizační režii přesným určením začátku mezer v paketech
- Funguje ve spojení s bitmapou pro detailní určení následujících chybějících SN
- Je nedílnou součástí generování a zpracování stavové zprávy PDCP

## Související pojmy

- [PDCP – Packet Data Convergence Protocol](/mobilnisite/slovnik/pdcp/)

## Definující specifikace

- **TS 36.323** (Rel-19) — PDCP Protocol Specification

---

📖 **Anglický originál a plná specifikace:** [FMS na 3GPP Explorer](https://3gpp-explorer.com/glossary/fms/)
