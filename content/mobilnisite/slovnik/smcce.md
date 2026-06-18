---
slug: "smcce"
url: "/mobilnisite/slovnik/smcce/"
type: "slovnik"
title: "SMCCE – Session Management Congestion Control Experience"
date: 2025-01-01
abbr: "SMCCE"
fullName: "Session Management Congestion Control Experience"
category: "QoS"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/smcce/"
summary: "Rámec 3GPP pro správu zahlcení sítě na úrovni správy relací za účelem zajištění konzistentního uživatelského zážitku. Zavádí mechanismy pro detekci, hlášení a zmírňování zahlcení, zvýhodňuje kritické"
---

SMCCE je rámec 3GPP pro správu zahlcení sítě na úrovni relací, který zajišťuje konzistentní uživatelský zážitek detekcí, hlášením a zmírňováním zahlcení za účelem zvýšení priority kritických služeb.

## Popis

Session Management Congestion Control Experience (SMCCE) je rámec standardizovaný v 3GPP Release 17 pro zlepšení kvality služeb (QoS) proaktivní správou zahlcení ve vrstvě správy relací 5G Core sítě. Funguje tak, že umožňuje funkci správy relací ([SMF](/mobilnisite/slovnik/smf/)) detekovat stavy zahlcení na základě ukazatelů zatížení sítě, jako je vytížení prostředků na funkci uživatelské roviny ([UPF](/mobilnisite/slovnik/upf/)) nebo v rámci konkrétních síťových řezů. Po detekci může SMF uplatnit různé politiky zmírňování, které mohou zahrnovat omezení datových toků pro nerelokové relace, zamítání žádostí o zřízení nových relací pro určité služby nebo spouštění síťově iniciovaných modifikací relací za účelem přerozdělení prostředků. Rámec také definuje mechanismy, pomocí nichž SMF hlásí události zahlcení funkci řízení politik ([PCF](/mobilnisite/slovnik/pcf/)) pro dynamické úpravy politik a funkci analýzy síťových dat ([NWDAF](/mobilnisite/slovnik/nwdaf/)) pro širší síťové analýzy a optimalizaci.

Architektura SMCCE je integrována do stávající servisně orientované architektury ([SBA](/mobilnisite/slovnik/sba/)) 5G. Klíčové interakce zahrnují SMF, PCF, UPF a funkci správy přístupu a mobility ([AMF](/mobilnisite/slovnik/amf/)). SMF funguje jako centrální řadič, který přijímá informace související se zahlcením od UPF přes rozhraní N4, jako je obsazenost vyrovnávací paměti nebo míra ztráty paketů. Na základě předem nakonfigurovaných politik nebo dynamických pokynů od PCF může SMF vynucovat opatření proti zahlcení. Tato opatření se uplatňují na úrovni [PDU](/mobilnisite/slovnik/pdu/) relace nebo toku QoS, což umožňuje detailní řízení. Například SMF může nařídit UPF, aby pro konkrétní tok QoS použil nižší garantovaný bitový tok (GFBR), nebo aby označoval pakety pro explicitní oznámení o zahlcení ([ECN](/mobilnisite/slovnik/ecn/)).

Role SMCCE je klíčová pro udržování smluv o úrovni služeb (SLA), zejména pro síťové řezy a služby ultra-spolehlivé komunikace s nízkou latencí (URLLC). Zamezením nekontrolovaného zahlcení pomáhá předejít kaskádovým selháním a zajišťuje, že aplikace kritické pro misi získají potřebné prostředky. Rámec podporuje jak reaktivní, tak proaktivní správu zahlcení, přičemž NWDAF může poskytovat prediktivní poznatky pro spouštění akcí dříve, než dojde k závažnému zahlcení. Díky tomu je SMCCE základním prvkem pro automatizovanou správu sítě a zajištění zážitku v nasazeních 5G Standalone (SA).

## K čemu slouží

SMCCE bylo vytvořeno za účelem řešení výzvy udržování konzistentního uživatelského zážitku a plnění záruk SLA v stále složitějších a hustších 5G sítích. Předchozí verze 3GPP měly mechanismy řízení zahlcení, ale ty byly často lokalizované (např. v RAN nebo na transportní vrstvě) nebo nebyly těsně integrovány s řízením relací a politik v jádru sítě. To mohlo vést k neoptimálním rozhodnutím, jako je například zahazování paketů transportním uzlem bez vědomí SMF, což znemožňovalo inteligentní nápravu na úrovni relace. Motivací pro SMCCE byla potřeba holistického přístupu ke správě zahlcení, který je vědomý kontextu relace a který odpovídá paradigmatu síťových řezů v 5G, kde mají různé řezy výrazně odlišné požadavky na výkon a spolehlivost.

Historicky se zahlcení často řešilo jednoduchou správou front (např. zahazováním z konce) v routerech nebo prostřednictvím plánování rádiových prostředků. Tyto metody postrádají kontext aplikace a účastníka dostupný v jádru 5G. SMCCE tento kontext zavádí využitím znalostí SMF o aktivních PDU relacích, jejich přidružených profilech QoS a síťovém řezu, do kterého patří. To umožňuje inteligentnější akce, jako je selektivní degradace best-effort provozu při současné ochraně URLLC relace pro tovární automatizaci. Rámec řeší problém neprůhledného zahlcení, kdy jádro sítě nemá povědomí o úzkých místech v uživatelské rovině, a umožňuje tak koordinované zmírňování, které může zachovat ziskové služby a celkovou stabilitu sítě během špiček provozu nebo částečných výpadků.

## Klíčové vlastnosti

- Detekce a hlášení zahlcení z UPF do SMF přes rozhraní N4
- Detailní akce pro zmírnění zahlcení na úrovni PDU relace nebo toku QoS
- Integrace s PCF pro dynamickou reakci na zahlcení založenou na politikách
- Podpora politik řízení zahlcení s ohledem na síťové řezy
- Mechanismy pro síťově iniciovanou modifikaci relace z důvodu zahlcení
- Hlášení analytických údajů do NWDAF pro celosíťový přehled o zahlcení

## Související pojmy

- [SMF – Service Management Function](/mobilnisite/slovnik/smf/)
- [PCF – Positioning Calculation Function](/mobilnisite/slovnik/pcf/)
- [NWDAF – Network Data Analytics Function](/mobilnisite/slovnik/nwdaf/)

## Definující specifikace

- **TS 29.508** (Rel-19) — 5G Session Management Event Exposure Service
- **TS 29.520** (Rel-19) — 5G Network Data Analytics Services Stage 3

---

📖 **Anglický originál a plná specifikace:** [SMCCE na 3GPP Explorer](https://3gpp-explorer.com/glossary/smcce/)
