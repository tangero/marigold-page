---
slug: "ac"
url: "/mobilnisite/slovnik/ac/"
type: "slovnik"
title: "AC – Application Characteristics"
date: 2026-01-01
abbr: "AC"
fullName: "Application Characteristics"
category: "Services"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/ac/"
summary: "Application Characteristics (AC) jsou standardizované parametry popisující chování a požadavky aplikací v sítích 3GPP. Síťové funkce je používají k aplikování vhodných politik pro zpracování provozu,"
---

AC je standardizovaná sada parametrů popisujících chování a požadavky aplikace, které síťové funkce používají k aplikování vhodných politik pro zpracování provozu, QoS a přidělování prostředků.

## Popis

Application Characteristics (AC) jsou standardizovaná sada atributů definovaných ve specifikacích 3GPP pro profilování chování a požadavků aplikací využívajících mobilní síť. Tyto charakteristiky slouží jako klíčový vstup pro síťové funkce, zejména v rámci architektury Policy and Charging Control ([PCC](/mobilnisite/slovnik/pcc/)), aby určily, jak má být s provozem aplikace nakládáno. Parametry AC popisují aspekty jako vzorec provozu aplikace (např. v reálném čase, streamování, interaktivní, na pozadí), její toleranci k zpoždění a jitteru, požadovanou šířku pásma a očekávaný objem dat. Klasifikací aplikací na základě těchto charakteristik může síť mapovat provoz na příslušné QoS Class Identifiers (QCIs) nebo 5G QoS Identifiers (5QIs), čímž zajišťuje, že aplikace obdrží potřebné síťové prostředky a záruky výkonu.

Klíčový mechanismus zahrnuje Application Function ([AF](/mobilnisite/slovnik/af/)), například [P-CSCF](/mobilnisite/slovnik/p-cscf/) pro IMS služby nebo aplikační server třetí strany, která poskytuje informace AC funkci Policy Control Function ([PCF](/mobilnisite/slovnik/pcf/)) prostřednictvím rozhraní Rx (ve 4G) nebo N5 (v 5G). Tato komunikace obvykle probíhá při vytváření toku služebních dat. PCF, což je centrální prvek pro rozhodování o politikách, využívá přijatá AC spolu s informacemi o účastníkovi, předplatitelskými údaji a stavem sítě k formulování dynamických PCC pravidel. Tato pravidla jsou následně vynucována funkcí Policy and Charging Enforcement Function ([PCEF](/mobilnisite/slovnik/pcef/)) v bráně (např. [PGW](/mobilnisite/slovnik/pgw/), [UPF](/mobilnisite/slovnik/upf/)), aby aplikovala správnou QoS, provedla gating (povolení/blokování provozu) a spustila příslušné účtovací akce. AC tedy funguje jako 'deklarace potřeb' aplikace směrem k politickému rámci.

Klíčovými komponentami v ekosystému AC jsou samotná standardizovaná sada parametrů, AF která je generuje, PCF která je spotřebovává pro odvození politik a vymáhací body (PCEF, [SMF](/mobilnisite/slovnik/smf/)/UPF). Parametry jsou často sladěny se širšími požadavky na služby definovanými v jiných specifikacích, což zajišťuje konzistenci. Například charakteristiky pro hovor Voice over LTE (VoLTE) by indikovaly přísný profil konverzace v reálném čase, což vede k přidělení přenosu se zaručenou přenosovou rychlostí (GBR) a nízkolatenčním QCI. Toto systematické profilování zabraňuje nadměrnému přidělování síťových prostředků jednoduchým datům na pozadí nebo naopak nedostatečnému přidělení pro kritické služby, čímž dosahuje rovnováhy mezi výkonem aplikace a efektivitou sítě.

V systémech 5G se tento koncept vyvíjí s vyšší granularitou a podporou síťového řezání. Informace AC mohou ovlivnit výběr konkrétní instance síťového řezu přizpůsobené potřebám aplikace. Service-Based Architecture (SBA) jádra 5G usnadňuje dynamičtější a podrobnější výměnu dat AC mezi síťovými funkcemi, jako jsou Network Exposure Function (NEF), PCF a Application Function. To umožňuje sofistikovanější směrování provozu, využívání služeb edge computingu a diferencované účtování na základě přesného kontextu aplikace. AC v konečném důsledku poskytuje sémantický spoj mezi záměrem aplikační vrstvy a možnostmi přenosové sítě, což umožňuje inteligentní, automatizované a optimalizované poskytování služeb napříč systémy 3GPP.

## K čemu slouží

Hlavním účelem definování Application Characteristics (AC) je překlenout propast mezi požadavky aplikační vrstvy a správou prostředků na síťové vrstvě. Před standardizovanými AC sítě zacházely s většinou IP provozu jednotně jako s doručováním 'best-effort', což bylo nedostatečné pro různé kvalitativní potřeby vznikajících služeb, jako je VoIP, streamování videa a online hry. Tento jednotný přístup vedl ke špatnému uživatelskému zážitku u aplikací citlivých na latenci a k neefektivnímu využití síťové kapacity. Zavedení AC jako součásti širšího PCC rámce od 3GPP Release 5 bylo motivováno potřebou umožnit diferenciaci Quality of Service (QoS) a dynamické řízení politik na základě konkrétního typu používané aplikace.

Historicky rané mobilní datové služby jako GPRS nabízely omezené QoS mechanismy založené na statických profilech účastníků, bez reálného povědomí o aktivní aplikaci. Vývoj směrem k All-IP sítím a službám založeným na IMS vyžadoval dynamičtější a podrobnější systém. AC to řeší tím, že umožňuje samotné aplikaci, nebo proxy, která zná její potřeby, explicitně signalizovat svůj behaviorální profil systému řízení politik. To dává operátorům možnost přejít od jednoduchého objemového účtování k sofistikovaným modelům účtování s ohledem na službu a garantovat výkon prémiových služeb, čímž vytváří nové zdroje příjmů a zlepšuje spokojenost zákazníků.

AC dále řeší výzvu efektivity sítě. Přesnou charakterizací aplikačního provozu se síť může vyhnout nadměrnému přidělování cenných rádiových a přenosových prostředků nekritickým datovým tokům. Umožňuje inteligentní správu provozu, jako je omezení aktualizací na pozadí při přetížení při zachování kvality živého videohovoru. V kontextu 5G a síťového řezání poskytuje AC základní kritéria pro automatizaci výběru a konfigurace řezů, což zajišťuje, že každá aplikace je hostována na řezu s odpovídajícími výkonnostními charakteristikami. AC tedy existuje jako základní prvek pro službám vědomé, efektivní a zpeněžitelné mobilní širokopásmové sítě definované 3GPP.

## Klíčové vlastnosti

- Standardizovaná sada parametrů pro profilování chování aplikace
- Vstup pro generování dynamických pravidel Policy and Charging Control (PCC)
- Umožňuje mapování aplikačního provozu na konkrétní třídy QoS (QCIs/5QIs)
- Usnadňuje účtování a řízení gatingu s ohledem na službu
- Podporuje výběr síťového řezu a požadavky na služby v 5G
- Výměna prostřednictvím standardizovaných rozhraní (např. Rx, N5) mezi AF a PCF

## Související pojmy

- [PCC – Performance-oriented Congestion Control](/mobilnisite/slovnik/pcc/)
- [QCI – Quality of Service Class Identifier](/mobilnisite/slovnik/qci/)
- [5QI – 5G QoS Identifier](/mobilnisite/slovnik/5qi/)
- [AF – Authentication Framework](/mobilnisite/slovnik/af/)
- [PCF – Positioning Calculation Function](/mobilnisite/slovnik/pcf/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 23.171** (Rel-4) — LCS Stage 2 Specification for UMTS
- **TS 23.271** (Rel-19) — LCS Stage 2 Specification
- **TS 23.558** (Rel-20) — Architecture for Edge Applications
- **TS 23.700** (Rel-20) — XR Services Application Enablement Layer
- **TR 23.958** (Rel-19) — EDGEAPP alignment with ETSI MEC and GSMA OP
- **TS 24.167** (Rel-19) — 3GPP IMS Management Object Specification
- **TS 24.558** (Rel-19) — Edge Enabler APIs Stage 3
- **TS 25.113** (Rel-19) — EMC Requirements for UTRA Base Stations & Repeaters
- **TS 26.114** (Rel-19) — IMS Multimedia Telephony Media Handling
- **TR 26.803** (Rel-17) — 5G Media Streaming Extensions for Edge Processing
- **TR 26.942** (Rel-19) — Study on Media Energy Consumption Exposure & Evaluation
- **TS 28.680** (Rel-19) — WLAN Management Concepts and Requirements
- **TR 28.815** (Rel-17) — Charging Study for Edge Computing
- **TS 29.078** (Rel-19) — CAMEL Phase 4 CAP Specification
- … a dalších 28 specifikací

---

📖 **Anglický originál a plná specifikace:** [AC na 3GPP Explorer](https://3gpp-explorer.com/glossary/ac/)
