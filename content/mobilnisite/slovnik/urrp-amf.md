---
slug: "urrp-amf"
url: "/mobilnisite/slovnik/urrp-amf/"
type: "slovnik"
title: "URRP-AMF – UE Reachability Request Parameter for AMF"
date: 2026-01-01
abbr: "URRP-AMF"
fullName: "UE Reachability Request Parameter for AMF"
category: "Core Network"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/urrp-amf/"
summary: "Parametr, který SMF používá k vyžádání, aby AMF provedla procedury dosažitelnosti UE v síti 5G. Spouští v AMF paging UE nebo kontrolu jejího stavu spojení, čímž umožňuje efektivní doručování dat ve sm"
---

URRP-AMF je parametr, který SMF používá k vyžádání, aby AMF provedla procedury dosažitelnosti UE, jako je paging, a umožnila tak doručení dat ve směru downlink, když je UE v režimu idle nebo inactive.

## Popis

Parametr URRP-AMF (UE Reachability Request [Parameter](/mobilnisite/slovnik/parameter/) for [AMF](/mobilnisite/slovnik/amf/)) je signalizační parametr používaný v jádru sítě 5G (5GC) na rozhraní N11 mezi [SMF](/mobilnisite/slovnik/smf/) (Session Management Function) a AMF (Access and Mobility Management Function). Jeho primární funkcí je umožnit SMF explicitně požádat AMF o provedení procedur dosažitelnosti UE. K tomu dochází, když SMF obdrží data ve směru downlink pro [PDU](/mobilnisite/slovnik/pdu/) session patřící UE, která je ve stavu CM-IDLE nebo CM-CONNECTED s [RRC](/mobilnisite/slovnik/rrc/) Inactive, a SMF rozhodne, že je vyžadována procedura service request iniciovaná sítí k vytvoření prostředků uživatelské roviny.

Parametr je přenášen v rámci servisní operace Nsmf_PDUSession_UpdateSMContext request, kterou SMF zasílá AMF. URRP-AMF obsahuje konkrétní instrukce pro AMF. Typicky zahrnuje indikaci, která spouští v AMF proceduru pagingu směrem k registrované oblasti UE, pokud je UE ve stavu CM-IDLE. Pro UE ve stavu RRC Inactive vyzývá AMF, aby požádala RAN o provedení pagingu založeného na RAN nebo o obnovení spojení. AMF tento požadavek zpracuje, interaguje s (R)[AN](/mobilnisite/slovnik/an/) (Radio Access Network) za účelem lokalizace a kontaktování UE a spravuje následnou proceduru service request pro přechod UE do stavu CM-CONNECTED a opětovné vytvoření cesty uživatelské roviny.

Z architektonického hlediska je URRP-AMF klíčovým prvkem v oddělení funkcí řídicí roviny v 5GC. SMF spravuje kontext session, ale neřeší mobilitu nebo dosažitelnost – to je role AMF. Tento parametr je definovaným mechanismem pro mezifunkční koordinaci. AMF po úspěšném dosažení UE aktualizuje SMF o novém stavu UE a, pokud je to relevantní, o nových informacích o tunelu uživatelské roviny. Parametr může také nést dodatečný kontext, například indikátor priority, aby ovlivnil strategii pagingu (např. pro služby citlivé na zpoždění). Tím je zajištěno efektivní a spolehlivé oznámení o datech ve směru downlink, což je zásadní pro always-on služby a aplikace očekávající push notifikace.

## K čemu slouží

URRP-AMF byl vytvořen k formalizaci a optimalizaci interakce mezi [SMF](/mobilnisite/slovnik/smf/) a [AMF](/mobilnisite/slovnik/amf/) při správě dosažitelnosti UE v servisně orientované architektuře (SBA) 5G. V předchozích architekturách, jako je 4G EPC, SGW zpracovávalo oznámení o datech ve směru downlink a spouštělo paging přes MME, ale funkce byly více provázané. Jasné oddělení správy session (SMF) a správy mobility (AMF) v 5GC vyžadovalo pro tuto zásadní koordinaci standardizované, servisně orientované rozhraní.

Řeší problém, jak může funkce orientovaná na session (SMF) požádat funkci orientovanou na mobilitu (AMF) o lokalizaci UE, aniž by měla přímý přístup ke stavům mobility nebo možnostem pagingu. Bez URRP-AMF by SMF nebylo schopno efektivně spustit opětovné vytvoření konektivity uživatelské roviny, což by vedlo ke ztrátě paketů ve směru downlink nebo nadměrnému bufferingu. Tento parametr umožňuje efektivní správu dosažitelnosti na vyžádání, což je klíčové pro úsporné stavy UE, jako jsou RRC Inactive a CM-IDLE, protože minimalizuje zbytečnou signalizaci tím, že spouští paging pouze při příchodu dat.

Dále podporuje pokročilé funkce 5G, jako je network slicing. Různé slice mohou mít různé požadavky na latenci dosažitelnosti. Mechanismus URRP-AMF umožňuje SMF, které je slice-aware, předat AMF priority nebo parametry dosažitelnosti specifické pro slice, což umožňuje diferencované strategie pagingu. Tím se řeší omezení jednotného přístupu k pagingu a je to zásadní pro podporu služeb kritických pro provoz IoT nebo ultra-spolehlivé komunikace s nízkou latencí (URLLC), kde je včasné doručení prvořadé.

## Klíčové vlastnosti

- Standardizovaný parametr pro vyžádání procedur dosažitelnosti UE od AMF ze strany SMF přes rozhraní N11
- Spouští paging iniciovaný AMF pro UE ve stavu CM-IDLE nebo obnovení spojení pro UE ve stavu RRC Inactive
- Podporuje proceduru Service Request iniciovanou sítí pro oznámení o datech ve směru downlink
- Umožňuje koordinaci mezi oddělenými funkcemi správy session a mobility v SBA 5GC
- Může zahrnovat indikátory priority pro ovlivnění naléhavosti nebo metody pokusu o dosažení UE
- Integruje se se správou kontextu PDU session během přechodů stavů UE

## Související pojmy

- [AMF – Access and Mobility Management Function](/mobilnisite/slovnik/amf/)
- [SMF – Service Management Function](/mobilnisite/slovnik/smf/)

## Definující specifikace

- **TS 23.501** (Rel-20) — 5G System Architecture Stage 2

---

📖 **Anglický originál a plná specifikace:** [URRP-AMF na 3GPP Explorer](https://3gpp-explorer.com/glossary/urrp-amf/)
