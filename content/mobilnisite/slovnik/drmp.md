---
slug: "drmp"
url: "/mobilnisite/slovnik/drmp/"
type: "slovnik"
title: "DRMP – Diameter Routing Message Priority"
date: 2026-01-01
abbr: "DRMP"
fullName: "Diameter Routing Message Priority"
category: "Protocol"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/drmp/"
summary: "Atribut v protokolu Diameter, který umožňuje uzlu Diameter přiřadit úroveň priority zprávě požadavku. To umožňuje zprostředkujícím agentům pro směrování Diameter (DRA) provádět rozhodnutí o vyrovnáván"
---

DRMP je atribut protokolu Diameter, který umožňuje uzlu přiřadí úrovni priority požadavku, což směrovacím agentům umožňuje provádět vyrovnávání zátěže, řízení přetížení a směrování na základě priority.

## Popis

Diameter Routing Message Priority (DRMP) je rozšíření protokolu definované v 3GPP pro vylepšení schopností signalizačních sítí založených na Diameteru, zejména v rámci IP Multimedia Subsystem (IMS), Evolved Packet Core (EPC) a 5G Core (5GC). Je implementováno jako pár atribut-hodnota ([AVP](/mobilnisite/slovnik/avp/)), který může být zahrnut do zpráv požadavků Diameter. AVP DRMP nese celočíselnou hodnotu reprezentující prioritu zprávy, přičemž nižší číselné hodnoty typicky označují vyšší prioritu (např. 0 pro nejvyšší prioritu). Primární funkcí DRMP je poskytnout standardizovaný signalizační mechanismus pro přenos informací o prioritě, který umožňuje uzlům Diameter činit inteligentnější rozhodnutí o směrování a zpracování.

Z architektonického hlediska DRMP funguje v rámci základního protokolového rámce Diameter (RFC 6733). Když klient nebo server Diameter vygeneruje požadavek (např. Credit-Control-Request ([CCR](/mobilnisite/slovnik/ccr/)) nebo AA-Request (AAR)), může naplnit AVP DRMP na základě lokální politiky, typu služby nebo profilu účastníka. Tato zpráva je pak odeslána do sítě Diameter, často prochází jedním nebo více agenty pro směrování Diameter ([DRA](/mobilnisite/slovnik/dra/)). Tito zprostředkující DRA, kteří jsou klíčoví pro škálovatelnost a směrování ve velkých sítích, hodnotu DRMP kontrolují. Pomocí této informace může DRA implementovat logiku směrování citlivou na prioritu. Například během období zahlcení sítě nebo přetížení uzlu může DRA upřednostnit přeposílání zpráv s vysokou prioritou (jako jsou požadavky na nouzové služby nebo zprávy pro prémiové účastníky), zatímco může potenciálně zpozdit nebo odmítnout provoz s nižší prioritou. Jedná se o klíčový nástroj pro implementaci mechanismů řízení přetížení a zahlcení, jak je specifikováno v 3GPP.

Hodnota DRMP ovlivňuje chování v několika bodech. Kromě směrovacích agentů ji může cílový server Diameter také použít k určení priority, v jakém pořadí zpracovává příchozí požadavky ze své fronty. Specifikace definují postupy pro generování, přeposílání a případnou modifikaci hodnot DRMP důvěryhodnými uzly. Jeho zavedení formalizovalo to, co bylo dříve často řešeno proprietárními nebo lokálními síťovými mechanismy, a zajišťuje tak interoperabilitu mezi zařízeními od různých výrobců v jádrových sítích s více dodavateli. DRMP je kritickou součástí pro dosažení provozovatelské spolehlivosti a diferenciace služeb ve všech-IP jádrových sítích, které jsou silně závislé na signalizaci Diameter pro autentizaci, autorizaci, účtování a řízení politik.

## K čemu slouží

DRMP bylo vytvořeno k řešení výzev spojených se správou signalizační zátěže a zajištěním dostupnosti služeb ve stále složitějších a rozsáhlých signalizačních sítích Diameter. Jak se sítě 3GPP vyvinuly na architektury all-IP (IMS, EPC), stal se Diameter primárním protokolem pro funkce [AAA](/mobilnisite/slovnik/aaa/) a řízení politik v reálném čase. Bez standardizovaného mechanismu priority byly všechny signalizační zprávy Diameter směrovacími agenty považovány za stejně důležité. To představovalo významný problém během signalizačních bouří nebo výpadků uzlů, protože kritické zprávy (např. pro nouzová volání, předávání hovorů nebo zákazníky s vysokou hodnotou) mohly být nerozlišně zahazovány spolu s méně důležitým provozem, což degradovalo základní služby.

Vývoj DRMP ve verzi 13 poskytl standardizované řešení tohoto problému. Byl motivován potřebou explicitních mechanismů řízení přetížení v samotném protokolu Diameter. DRMP umožňuje síťovým funkcím a operátorům implementovat označování priority na základě politik. To umožňuje síti se při zátěži degradovat s grácií tím, že chrání relace a služby s vysokou prioritou, což je základním požadavkem na odolnost na úrovni telekomunikací. Řešilo to omezení předchozích ad-hoc přístupů a poskytlo nástroj pro splnění regulatorních požadavků na podporu nouzových služeb a pro implementaci komerční diferenciace služeb v signalizační rovině.

## Klíčové vlastnosti

- AVP pro přenos hodnoty priority v požadavcích Diameter
- Umožňuje směrování citlivé na prioritu v agentech pro směrování Diameter (DRA)
- Podporuje mechanismy řízení přetížení a zahlcení
- Umožňuje diferenciaci priority na základě služby a účastníka
- Integruje se se základním protokolem Diameter a rozhraními 3GPP Tx, Gx, Rx
- Umožňuje degradaci s grácií během signalizačních bouří

## Související pojmy

- [IMS – IP Multimedia Subsystem](/mobilnisite/slovnik/ims/)

## Definující specifikace

- **TS 23.700** (Rel-20) — XR Services Application Enablement Layer
- **TS 24.301** (Rel-19) — NAS protocol for Evolved Packet System
- **TS 29.128** (Rel-19) — MME/SGSN-SCEF Diameter Interfaces for PDN Interworking
- **TS 29.153** (Rel-19) — Ns Reference Point Protocol between SCEF and RCAF
- **TS 29.154** (Rel-19) — Nt Reference Point Protocol
- **TS 29.172** (Rel-19) — EPC LCS Protocol (ELP) specification
- **TS 29.201** (Rel-19) — RESTful Rx Interface for AF-PC Communication
- **TS 29.212** (Rel-19) — Gx/Gxx/Sd/St Diameter Protocol
- **TS 29.213** (Rel-19) — PCC Signalling Flows and QoS Mapping
- **TS 29.214** (Rel-19) — Policy and Charging Control over Rx
- **TS 29.215** (Rel-19) — S9 Reference Point Stage 3 Specification
- **TS 29.217** (Rel-19) — Policy and Charging Control (PCC) for Np Interface
- **TS 29.219** (Rel-19) — Sy Reference Point Stage 3 Specification
- **TS 29.228** (Rel-19) — Cx and Dx Interface Signaling Flows
- **TS 29.229** (Rel-19) — Diameter Protocol for Cx/Dx Interfaces
- … a dalších 10 specifikací

---

📖 **Anglický originál a plná specifikace:** [DRMP na 3GPP Explorer](https://3gpp-explorer.com/glossary/drmp/)
