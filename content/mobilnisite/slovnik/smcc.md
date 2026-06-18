---
slug: "smcc"
url: "/mobilnisite/slovnik/smcc/"
type: "slovnik"
title: "SMCC – Session Management Congestion Control"
date: 2025-01-01
abbr: "SMCC"
fullName: "Session Management Congestion Control"
category: "Core Network"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/smcc/"
summary: "Session Management Congestion Control je soubor síťových mechanismů navržených speciálně k prevenci, detekci a zmírnění zahlcení v řídicích rovinách procedur souvisejících se správou PDU relací. Chrán"
---

SMCC je soubor síťových mechanismů navržených k prevenci, detekci a zmírnění zahlcení v řídicích rovinách procedur správy PDU relací za účelem ochrany SMF a signalizačních rozhraní před přetížením.

## Popis

Session Management Congestion Control (SMCC) je sofistikovaný rámec zavedený v 5G pro ochranu řídicí roviny jádra sítě, zejména funkce správy relací ([SMF](/mobilnisite/slovnik/smf/)), před zahlcením a přetížením. Na rozdíl od zahlcení v uživatelské rovině se SMCC zaměřuje na signalizační bouři, která může nastat, když obrovské množství UE současně pokouší o zřízení, modifikaci nebo uvolnění [PDU](/mobilnisite/slovnik/pdu/) relací. Toto zahlcení může být vyvoláno legitimními událostmi (např. zaplňováním stadionu) nebo škodlivými útoky (např. distribuovaným útokem typu odepření služby zaměřeným na rozhraní N11/N7). Architektura SMCC zahrnuje koordinované akce mezi SMF, funkcí správy přístupu a mobility ([AMF](/mobilnisite/slovnik/amf/)) a funkcí řízení politik ([PCF](/mobilnisite/slovnik/pcf/)).

SMCC funguje prostřednictvím vícefázového procesu monitorování, rozhodování a akce. SMF průběžně sleduje klíčové ukazatele výkonu ([KPI](/mobilnisite/slovnik/kpi/)), jako je rychlost příchozích požadavků na správu relací, latence zpracování a vytížení [CPU](/mobilnisite/slovnik/cpu/)/paměti. Při překročení předdefinovaných prahových hodnot SMF přejde do stavu zahlcení. Poté uplatňuje zásady řízení zahlcení, které jsou často předkonfigurované nebo dynamicky poskytované PCF. Primární akcí je, že SMF signalizuje informace o zahlcení směrem k AMF pomocí rozhraní N11. AMF, která funguje jako agregátor signalizace od mnoha UE, pak může uplatnit zpětný tlak. To zahrnuje odmítání nových požadavků na správu relací od UE s časovačem čekání nebo jejich přesměrování, čímž efektivně reguluje zátěž u zdroje.

Mechanismy v rámci SMCC jsou detailní. Dokážou rozlišovat mezi typy procedur správy relací (např. upřednostňovat zřizování relací pro nouzové služby před běžným prohlížením) a mohou uplatňovat řízení na základě předplatného UE, síťového řezu ([S-NSSAI](/mobilnisite/slovnik/s-nssai/)) nebo názvu datové sítě ([DNN](/mobilnisite/slovnik/dnn/)). Například během zahlcení může SMF odmítat požadavky pro nekritický IoT řez, zatímco bude nadále přijímat požadavky z řezu podporujícího veřejnou bezpečnost. SMF může také implementovat lokální algoritmy řazení do front a stanovení priorit. Díky proaktivní správě signalizační zátěže SMCC zajišťuje, že SMF zůstává dostupné pro nezbytné relace, a že zahlcení nekaskádovitě nezpůsobí širší selhání řídicí roviny sítě, čímž udržuje celkovou síťovou stabilitu a dostupnost služeb.

## K čemu slouží

SMCC bylo vytvořeno, aby řešilo kritickou zranitelnost v 5G a budoucích sítích: přetížení signalizace řídicí roviny. Předchozí generace měly řízení zahlcení, ale architektura založená na službách v 5G, síťové řezy a podpora pro masivní IoT exponenciálně zvyšují rozsah a složitost signalizace správy relací. Jedna instance SMF může být zodpovědná za miliony relací. Bez SMCC by náhlý nárůst signalizace – ať už z legitimní hromadné události nebo z koordinovaného útoku – mohl přetížit SMF, což by vedlo k odepření služeb všem uživatelům, včetně těch s vysokoprioritními službami.

Tato technologie řeší problém zajištění spolehlivosti služeb a spravedlnosti v hyperpropojeném prostředí. Umožňuje síti se pod zátěží elegantně degradovat, nikoli katastroficky selhat. Motivací pro její standardizaci ve vydání 17 byly zkušenosti operátorů a předvídání, že jak se sítě stanou více softwarově definované a řezané, je nezbytný standardizovaný, interoperabilní přístup k řízení zahlcení správy relací. SMCC poskytuje nástroje pro implementaci „inteligentního“ řízení zahlcení, které dokáže rozlišovat mezi různými službami a řezy, což je základním požadavkem pro naplnění slibů 5G o garantovaných smluvních úrovních služeb (SLA) pro různé případy užití, od rozšířeného mobilního širokopásmového připojení až po ultra spolehlivou komunikaci s nízkou latencí.

## Klíčové vlastnosti

- Monitoruje zatížení SMF a spouští se při detekci zahlcení
- Signalizuje stav zahlcení ze SMF na AMF prostřednictvím rozhraní N11
- Umožňuje AMF uplatnit zpětný tlak a odmítat požadavky s časovači čekání
- Podporuje zásady řízení zahlcení diferencované podle S-NSSAI, DNN a skupiny UE
- Stanovuje priority procedur správy relací během zahlcení
- Zabraňuje kaskádovým selháním v řídicí rovině jádra 5G sítě

## Definující specifikace

- **TS 29.508** (Rel-19) — 5G Session Management Event Exposure Service
- **TS 29.520** (Rel-19) — 5G Network Data Analytics Services Stage 3

---

📖 **Anglický originál a plná specifikace:** [SMCC na 3GPP Explorer](https://3gpp-explorer.com/glossary/smcc/)
