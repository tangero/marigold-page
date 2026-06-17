---
slug: "ccbs"
url: "/mobilnisite/slovnik/ccbs/"
type: "slovnik"
title: "CCBS – Completion of Communications to Busy Subscriber"
date: 2026-01-01
abbr: "CCBS"
fullName: "Completion of Communications to Busy Subscriber"
category: "Services"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/ccbs/"
summary: "CCBS je doplňková služba, která volající straně umožňuje požádat o automatické dokončení hovoru, když se dříve zaneprázdněný volaný účastník stane dostupným. Odstraňuje nutnost opakovaného ručního pře"
---

CCBS je doplňková služba, která automaticky dokončí hovor na zaneprázdněného účastníka, jakmile se stane dostupným, čímž odpadá nutnost ručního opětovného vytočení.

## Popis

Completion of Communications to Busy Subscriber (CCBS, Dokončení komunikace se zaneprázdněným účastníkem) je síťově řízená doplňková služba standardizovaná organizací 3GPP. Když volající strana (Uživatel A) pokusí se navázat hovor s volanou stranou (Uživatel B), která je zaneprázdněna (např. je v jiném hovoru), a je vyvolána služba CCBS, síť uloží žádost o hovor. Síť poté monitoruje stav Uživatele B. Jakmile se Uživatel B uvolní (tj. dokončí probíhající hovor a stane se dostupným pro nové hovory), síť automaticky zahájí nový pokus o sestavení hovoru z Uživatele A k Uživateli B. Tento proces je řízen sítí bez nutnosti, aby Uživatel A ručně převolával.

Architektonická implementace CCBS zahrnuje několik funkčních entit jádra sítě (CN), především v rámci Home Subscriber Server ([HSS](/mobilnisite/slovnik/hss/)) a Mobile Switching Center ([MSC](/mobilnisite/slovnik/msc/)) nebo uzlů IP Multimedia Subsystem (IMS) v pozdějších vydáních. Když je CCBS aktivována pro pokus o hovor, MSC obsluhující Uživatele A vystupuje jako iniciátor CCBS. Zaznamená podrobnosti žádosti o hovor, včetně identit Uživatele A a Uživatele B, a zaregistruje žádost CCBS u HSS nebo vyhrazeného aplikačního serveru CCBS. Obsluhující MSC pro Uživatele B (nebo monitorovací funkce) je upozorněno, aby sledovalo stav Uživatele B. Toto monitorování stavu je dosaženo prostřednictvím mechanismů registrace a dohledu nad stavem hovoru.

Klíčové provozní komponenty zahrnují procedury CCBS Request (žádost), CCBS Recall (zpětné volání) a CCBS Call (hovor). CCBS Request je iniciována volajícím uživatelem, typicky pomocí specifické [DTMF](/mobilnisite/slovnik/dtmf/) sekvence nebo servisního kódu, což vyzve síť k uložení žádosti. Síť poté vstoupí do monitorovací fáze. Po detekci přechodu Uživatele B do stavu volno síť spustí CCBS Recall směrem k Uživateli A, čímž jej upozorní, že volaná strana je nyní dostupná, a vyžádá si autorizaci k pokračování v automatickém sestavení hovoru. Pokud Uživatel A přijme (často zvednutím sluchátka), síť provede proceduru CCBS Call a naváže hovor k Uživateli B. Během celého tohoto procesu časovače řídí dobu platnosti žádosti a služba udržuje logiku priority a fronty, pokud pro stejného zaneprázdněného účastníka existuje více žádostí CCBS.

V architektuře IMS (od Release 5 výše) je funkčnost CCBS implementována jako Application Server ([AS](/mobilnisite/slovnik/as/)) v rámci servisní vrstvy IMS. CCBS AS komunikuje s Serving-Call Session Control Function (S-CSCF) pomocí rozhraní [ISC](/mobilnisite/slovnik/isc/) a využívá pro řízení služby protokoly SIP. AS uloží žádost, přihlásí se k odběru událostí stavu registrace a dialogu volané strany (pomocí SIP SUBSCRIBE/NOTIFY) a iniciuje sestavení hovoru, když jsou splněny podmínky. Tento přechod k službě založené na IMS a řízené SIP umožnil ve srovnání s dřívější implementací v přepojování okruhů ([CS](/mobilnisite/slovnik/cs/)) větší integraci s dalšími multimediálními službami a flexibilnější servisní logiku.

## K čemu slouží

CCBS bylo vytvořeno za účelem řešení problému uživatelského komfortu spojeného s opakovaným a ručním vytáčením čísla, které je často obsazené. Před jeho zavedením museli volající pamatovat na to, že mají hovor zkusit později, což často vedlo k nezdařeným spojením a frustraci. To bylo obzvláště neefektivní v obchodním kontextu nebo pro časově citlivou komunikaci. Služba tento proces opakovaného pokusu automatizuje a přenáší zátěž z uživatele na síť, čímž zvyšuje pravděpodobnost úspěšného spojení a šetří čas a úsilí uživatele.

Z pohledu síťového operátora slouží CCBS také ke zvýšení vytížení sítě a míry dokončení hovorů. Řízením žádostí o dokončení hovoru uspořádaným a frontovým způsobem může snížit objem opakovaných, současných pokusů o hovor, které nastávají, když se zaneprázdněný účastník uvolní, což by mohlo způsobit špičky signalizace. Poskytuje řízený mechanismus pro dokončení hovoru, který může být spravován s ohledem na spravedlnost a prioritu. Historicky podobné koncepty existovaly v pevných sítích a 3GPP standardizovalo CCBS, aby přineslo tuto hodnotnou komfortní funkci mobilním uživatelům, čímž obohatilo portfolio služeb a konkurenceschopnost sítí GSM a UMTS.

Motivace pro jeho vytvoření v Release 99 byla součástí širšího úsilí o obohacení základní telefonní služby o inteligentní doplňkové služby, což znamenalo posun od jednoduchých hlasových hovorů k funkcím, které napodobují nebo vylepšují uživatelský komfort služeb pevných linek. Řešilo to omezení základního modelu mobilního hovoru, kde stav obsazeno byl konečnou událostí vyžadující zcela novou akci uživatele. CCBS pro tyto scénáře zavedlo do síťové logiky obsluhy hovorů stavovost a proaktivitu.

## Klíčové vlastnosti

- Automatický nový pokus o hovor při dostupnosti volané strany
- Síťové uložení žádosti a monitorování stavu účastníka
- Upozornění uživatele (zpětné volání) volající strany před finálním sestavením
- Konfigurovatelná doba platnosti žádosti s expirací řízenou časovačem
- Řízení priority a fronty pro více žádostí
- Podpora jak v doméně přepojování okruhů (CS), tak v IP Multimedia Subsystem (IMS)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 22.093** (Rel-19) — Completion of Calls to Busy Subscriber (CCBS)
- **TS 22.173** (Rel-20) — IMS Multimedia Telephony Service Definition
- **TS 22.273** (Rel-7) — IMS Multimedia Telephony with PSTN/ISDN Simulation
- **TS 22.401** (Rel-8) — Videotelephony Service Requirements for NGN
- **TR 22.976** (Rel-2) — Release 2000 Services Overview
- **TS 23.018** (Rel-19) — Basic call handling in 3GPP CS domain
- **TS 23.066** (Rel-19) — Mobile Number Portability Technical Realization
- **TS 23.119** (Rel-19) — Gateway Location Register (GLR) Stage 2 Description
- **TS 23.417** (Rel-7) — IMS Core Component for NGN Architecture
- **TS 23.517** (Rel-8) — IMS Core Component for NGN Architecture
- **TS 24.093** (Rel-19) — CCBS Supplementary Service Stage 3
- **TS 24.186** (Rel-19) — IMS Data Channel applications
- **TS 24.196** (Rel-19) — Enhanced Calling Name (eCNAM) Stage 3 Protocol
- **TS 24.292** (Rel-19) — IMS Centralized Services (ICS) Protocol
- … a dalších 12 specifikací

---

📖 **Anglický originál a plná specifikace:** [CCBS na 3GPP Explorer](https://3gpp-explorer.com/glossary/ccbs/)
