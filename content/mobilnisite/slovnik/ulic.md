---
slug: "ulic"
url: "/mobilnisite/slovnik/ulic/"
type: "slovnik"
title: "ULIC – UMTS LI Correlation"
date: 2025-01-01
abbr: "ULIC"
fullName: "UMTS LI Correlation"
category: "Security"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/ulic/"
summary: "Funkční komponenta v architektuře zákonného odposlechu (LI) podle 3GPP, specifická pro UMTS (3G) sítě. Jejím hlavním úkolem je propojit odposlechnutý komunikační obsah (CC) s asociovanými informacemi"
---

ULIC je komponenta pro zákonný odposlech v UMTS, která propojuje odposlechnutý komunikační obsah s příslušnou signalizační informací o cílovém subjektu, aby vytvořila úplný zákonný záznam.

## Popis

UMTS [LI](/mobilnisite/slovnik/li/) Correlation (ULIC) je definovaná funkční entita ve standardizovaném rámci zákonného odposlechu (LI) podle 3GPP pro sítě Universal Mobile Telecommunications System (UMTS), jak je detailně specifikováno v 3GPP TS 33.108. Zákonný odposlech je zákonně schválený proces, při kterém autorizované orgány činné v trestním řízení ([LEA](/mobilnisite/slovnik/lea/)) mohou monitorovat a odposlouchávat telekomunikační provoz a související informace určeného cíle (subscribera). Kritickou výzvou v LI je, že odposlechnuté data jsou sbírána z různých bodů v síti: obsah komunikací (hlasové hovory, datové sessiony, [SMS](/mobilnisite/slovnik/sms/)) je zachycován na mediové pláně, zatímco asociovaná metadata nebo informace související s odposlechem ([IRI](/mobilnisite/slovnik/iri/) – např. čas zahájení hovoru, volané číslo, lokální updaty) jsou zachycena z signalizace řídicí plány. Tyto dva proudy jsou generovány a transportovány odděleně.

Funkce ULIC existuje, aby řešila tento problém oddělení. Funguje jako bod pro propojení, typicky umístěný v doméně operátora sítě na Mediation Function ([MF](/mobilnisite/slovnik/mf/)). ULIC přijímá oddělené proudy Communication Content ([CC](/mobilnisite/slovnik/cc/)) a IRI týkající se stejného povolení k odposlechu. Pomocí identifikátorů pro propojení – jako Correlation Number (CN) a Communication Identity (ComId), které jsou přiděleny odposlouchávajícími síťovými elementy (např. [MSC](/mobilnisite/slovnik/msc/) nebo [SGSN](/mobilnisite/slovnik/sgsn/)) – logika ULIC spojuje každou část obsahu (např. proud hlasových paketů) s odpovídajícími IRI událostmi (např. události "hovor zahájen" a "hovor ukončen"). Toto spojení je časové a na základě identifikátorů, což zajistí, že LEA přijímá synchronizovaný a souvislý záznam. Například zajistí, že audio nahrávka hovoru je doručena LEA spolu s metadata uvádějícími, kdo byl volán, kdy a z které buňky.

Architektonicky je ULIC částí delivery functionality Mediation Function (MF2). Interně komunikuje s dalšími komponentami MF, které sbírají CC a IRI z Network Elements (NEs), jako Mobile Switching Centre (MSC), Serving GPRS Support Node (SGSN) a Gateway GPRS Support Node (GGSN). Po propojení MF formátuje kombinovanou informaci podle standardizovaných Handover Interfaces (HI2 pro IRI, HI3 pro CC) a doručuje ji bezpečně do jedné nebo více Law Enforcement Monitoring Facilities (LEMFs). Operace ULIC je klíčová pro zachování zákonné integrity odposlechového důkazu. Musí řešit komplexní scénáře, jako hovory více účastníků, handover mezi síťovými elementy a datové sessiony s více packet data protocol (PDP) kontexty, správně asociující všechny relevantní datové proudy a signalizační události pro jediný cíl během trvání povolení k odposlechu.

## K čemu slouží

ULIC byl vytvořen, aby řešil základní technickou a zákonnou potřebu v zákonném odposlechu: poskytnutí úplného, přesného a auditovatelného záznamu komunikací cíle. Bez propojení by orgán činný v trestním řízení přijímal nesouvisející proudy raw audio/datových paketů a oddělené logy signalizačních událostí. Ruční spojování těchto částí pro jediný hovor nebo session by bylo náchylné na chyby, časově náročné a potenciálně nepřijatelné v soudním řízení kvůli riziku nesprávného spojení. ULIC automatizuje toto přesné spojení, zajišťuje, že důkaz je prezentován jako sjednocený, srozumitelný záznam, který jasně spojuje obsah s kontextem.

Vytvoření funkce ULIC bylo částí širšího úsilí 3GPP standardizovat zákonný odposlech přes různé generace mobilní technologie (počínaje GSM, pak UMTS a následně EPS/5GS). Před takovou standardizací byly implementace odposlechu často specifické pro dodavatele a pro země, což ztěžovalo operátorům v regionech s striktními zákonnými povinnostmi nasazovat multi-vendor sítě. Standardizovaný mechanismus pro propojení poskytovaný ULIC zajistil interoperabilitu mezi síťovými elementy od různých dodavatelů a konzistentní formát důkazů pro LEA. Řešil problém škálovatelnosti a spolehlivosti odposlechu pro UMTS sítě, které zaváděly více komplexní packet-switched datové služby vedle circuit-switched hlasu, což zvýšilo množství a různorodost dat, která potřebovala propojení.

Z pohledu regulatorní compliance existence definované funkce pro propojení jako ULIC pomáhá síťovým operátorům demonstrovat národním regulátorům, že jejich odposlechové systémy splňují požadované standardy přesnosti a spolehlivosti. Je to základní komponenta, která splňuje požadavky na "service-specific details" pro UMTS odposlech. I když následné release 3GPP definovali podobné mechanismy pro propojení pro EPS (ELIC) a 5GS, ULIC zůstává definovaným řešením pro 3G UMTS sítě, zajišťuje, že mohou pokračovat ve splnění povinností zákonného odposlechu během celé své operační životnosti. Jeho vytvoření bylo motivované potřebou robustního, standardizovaného technického procesu, který zachovává principy zákonného odposlechu, a zároveň umožňuje efektivní síťové operace.

## Klíčové vlastnosti

- Propojuje proudy Communication Content (CC) a Intercept Related Information (IRI) pro jediný cíl
- Používá standardizované identifikátory pro propojení (Correlation Number, Communication Identity) pro spojení
- Je umístěn v Mediation Function (MF) architektury zákonného odposlechu
- Řeší komplexní scénáře, jako hovory více účastníků a handover sessionů
- Zajišťuje doručení synchronizovaného, zákonně souvislého záznamu odposlechu orgánům činným v trestním řízení
- Specifický pro UMTS (3G) síťovou technologii a její definované síťové elementy (MSC, SGSN)

## Související pojmy

- [IRI – Intercept Related Information](/mobilnisite/slovnik/iri/)
- [HI2 – Handover Interface Port 2](/mobilnisite/slovnik/hi2/)
- [UMTS – Universal Mobile Telecommunications System](/mobilnisite/slovnik/umts/)

## Definující specifikace

- **TS 33.108** (Rel-19) — LI Handover Interface Specification

---

📖 **Anglický originál a plná specifikace:** [ULIC na 3GPP Explorer](https://3gpp-explorer.com/glossary/ulic/)
