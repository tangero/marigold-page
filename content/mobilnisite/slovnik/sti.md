---
slug: "sti"
url: "/mobilnisite/slovnik/sti/"
type: "slovnik"
title: "STI – Session Transfer Identifier"
date: 2026-01-01
abbr: "STI"
fullName: "Session Transfer Identifier"
category: "Services"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/sti/"
summary: "Jedinečný identifikátor používaný v IP multimediálním podsystému (IMS) ke sledování a správě multimediální relace při jejím přenosu mezi uživatelskými zařízeními nebo přístupovými sítěmi. Je klíčovou"
---

STI je jedinečný identifikátor používaný v IP multimediální podsystému (IMS) ke sledování a správě multimediální relace při převodech mezi zařízeními nebo sítěmi za účelem kontinuity služby.

## Popis

Session Transfer Identifier (STI) je klíčový parametr v architektuře IP multimediálního podsystému (IMS) podle 3GPP, konkrétně definovaný pro mechanismy kontinuity služby. Jedná se o globálně jedinečný identifikátor přidělený multimediální relaci (např. hlasovému nebo videohovoru) v okamžiku, kdy je zahájen proces přenosu relace. Hlavní úlohou STI je korelovat původní relaci (relaci určenou k přenosu) s novou, nahrazující relací, která je zřízena na cílovém zařízení nebo přístupové síti. Tato korelace je nezbytná pro síťové entity, aby mohly správně ukotvit, řídit a účtovat kontinuální službu.

Z architektonického hlediska STI generuje a spravuje Service Centralization and Continuity Application Server ([SCC](/mobilnisite/slovnik/scc/) [AS](/mobilnisite/slovnik/as/)), což je centrální uzel pro IMS Service Continuity ([ISC](/mobilnisite/slovnik/isc/)). Když se uživatel rozhodne přenést probíhající relaci z jednoho uživatelského zařízení (UE) na jiné (např. ze smartphonu na tablet) nebo mezi různými typy přístupu (např. z LTE na Wi-Fi), SCC AS zahájí proces přenosu. V rámci toho vygeneruje jedinečný STI a zahrne jej do požadavku [SIP](/mobilnisite/slovnik/sip/) INVITE používaného k vytvoření nové větve relace směrem k cíli. Tento STI je také předán zpět ke zdrojové větvi a uložen v kontextu.

Identifikátor funguje tak, že je přenášen v rámci signalizace SIP, typicky ve vyhrazených hlavičkových polích nebo parametrech SIP [URI](/mobilnisite/slovnik/uri/), jak je specifikováno v příslušných dokumentech TS 24.237 a TS 24.294. Všechny zúčastněné IMS uzly, včetně SCC AS, Proxy-CSCF ([P-CSCF](/mobilnisite/slovnik/p-cscf/)) a Serving-CSCF ([S-CSCF](/mobilnisite/slovnik/s-cscf/)), STI kontrolují a zpracovávají, aby identifikovaly kontext přenosu relace. To umožňuje SCC AS provádět klíčové funkce, jako je ukotvení relace, kdy zůstává v mediální cestě, aby usnadnil přenos, a provedení přesného okamžiku přepojení mediálního toku od protistrany ze zdrojové na cílovou větev. STI zajišťuje stavové zpracování, čímž předchází problémům, jako jsou duplicitní relace nebo nesprávné ukončení původní relace, a udržuje tak jednu logickou relaci z pohledu protistrany a fakturačních systémů.

## K čemu slouží

STI byl vytvořen, aby vyřešil problém plynulé mobility relací v sítích založených na IMS. Před jeho standardizací byl přenos aktivní multimediální relace mezi zařízeními nebo sítěmi problematický a často vyžadoval, aby uživatel hovor ukončil a znovu vytočil, což vedlo k přerušení služby. Hnacím motorem byla snaha o "follow-me" uživatelský zážitek, kdy by se služby jako hlasové hovory mohly přesouvat spolu s uživatelem mezi různými terminály a přístupovými technologiemi bez přerušení.

Řeší klíčovou technickou výzvu korelace dvou různých [SIP](/mobilnisite/slovnik/sip/) dialogů (původní relace a nové relace) jako součásti jedné instance uživatelské služby. Bez jedinečného identifikátoru, jako je STI, by síťové servery vnímaly zřízení nové relace jako zcela samostatný hovor, což by vedlo k záměně v servisní logice, účtování a potenciálně by způsobilo, že protistrana by viděla dvě současné větve hovoru. STI, zavedený jako součást frameworku IMS Service Continuity (ISC) od Release 8, poskytl potřebné pojivo. Vyvinul se z dřívějších konceptů, jako je Voice Call Continuity (VCC), ale byl zobecněn pro všechny multimediální relace v rámci IMS. Jeho vznik byl motivován konvergencí pevných, mobilních a podnikových sítí pod jediné IMS jádro, které vyžadovalo robustní a standardizovanou správu mobility pro prémiové telefonní a konverzační video služby.

## Klíčové vlastnosti

- Globálně jedinečný identifikátor pro instanci přenosu relace
- Generován a spravován SCC Application Server
- Přenášen v rámci signalizace SIP pro korelaci mezi větvemi relace
- Umožňuje ukotvení relace a řízené přepínání mediální cesty
- Základní prvek pro IMS Service Continuity (ISC) a VCC
- Zajišťuje správné účtování a servisní logiku pro přenesené relace

## Definující specifikace

- **TS 23.237** (Rel-19) — IMS Service Continuity (ISC) Stage 2
- **TS 23.700** (Rel-20) — XR Services Application Enablement Layer
- **TS 24.216** (Rel-19) — Communication Continuity Management Object
- **TS 24.237** (Rel-19) — IMS Service Continuity Protocol Details
- **TS 24.294** (Rel-19) — IMS Centralized Services (ICS) I1 Interface Protocol
- **TS 24.337** (Rel-19) — IMS Inter-UE Transfer Protocol Specification

---

📖 **Anglický originál a plná specifikace:** [STI na 3GPP Explorer](https://3gpp-explorer.com/glossary/sti/)
