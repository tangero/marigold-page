---
slug: "ctsagch"
url: "/mobilnisite/slovnik/ctsagch/"
type: "slovnik"
title: "CTSAGCH – CTS Access Grant Channel"
date: 2025-01-01
abbr: "CTSAGCH"
fullName: "CTS Access Grant Channel"
category: "Radio Access Network"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/ctsagch/"
summary: "Downlink řídicí kanál v sítích GSM/EDGE, který přenáší zprávy o udělení přístupu k mobilním stanicím. Je součástí systému CTS (Cellular Text Telephone Modem) a umožňuje služby textové telefonie pro už"
---

CTSAGCH je downlink řídicí kanál v sítích GSM/EDGE, který přenáší zprávy o udělení přístupu pro zřizování služeb textové telefonie v rámci systému CTS pro uživatele se sluchovým postižením.

## Popis

Kanál pro udělení přístupu [CTS](/mobilnisite/slovnik/cts/) (CTSAGCH) je specifický downlink logický kanál definovaný v sítích GSM/[EDGE](/mobilnisite/slovnik/edge/) v rámci architektury CTS (Cellular Text Telephone Modem) specifikované v 3GPP TS 43.052. Tento kanál funguje v okruhově spínané doméně a slouží jako vyhrazený signalizační kanál, který přenáší zprávy o udělení přístupu ze sítě k mobilním stanicím pokoušejícím se navázat CTS relace. Je vysílán na specifických časových slotech a frekvencích vyhrazených pro služby CTS, typicky využívá stejnou fyzickou vrstvu jako ostatní řídicí kanály GSM, ale s odlišným kódováním logického kanálu a formáty zpráv optimalizovanými pro signalizaci textové telefonie.

Architektonicky se CTSAGCH nachází v podsystému základnové stanice ([BSS](/mobilnisite/slovnik/bss/)) a rozhraní s ústřednou mobilní sítě ([MSC](/mobilnisite/slovnik/msc/)) pro řízení služeb. Když mobilní stanice iniciuje žádost o zřízení CTS hovoru přes náhodný přístupový kanál ([RACH](/mobilnisite/slovnik/rach/)), síť tuto žádost zpracuje a odpoví zprávou o okamžitém přidělení na CTSAGCH. Tato zpráva obsahuje klíčové parametry včetně přidělení vyhrazeného kanálu pro přenos, informace o časovém předstihu, příkazy pro řízení výkonu a specifické parametry služby CTS, jako jsou schémata kódování textu a parametry konfigurace modemu. Kanál pracuje s robustními schématy kódování, aby zajistil spolehlivý příjem za různých rádiových podmínek, což je klíčové pro uživatele se sluchovým postižením, kteří jsou závislí na spolehlivé textové komunikaci.

Z protokolového hlediska následují zprávy CTSAGCH strukturu protokolu správy rádiových prostředků ([RR](/mobilnisite/slovnik/rr/)) vrstvy 3, ale s informačními prvky specifickými pro CTS. Kanál pracuje v režimu vysílání pro všechny mobilní stanice s podporou CTS v buňce, ačkoli jednotlivé zprávy jsou adresovány konkrétním mobilním stanicím pomocí dočasné identity mobilního účastníka ([TMSI](/mobilnisite/slovnik/tmsi/)) nebo mezinárodní identity mobilního účastníka ([IMSI](/mobilnisite/slovnik/imsi/)). Síť dynamicky přiděluje prostředky CTSAGCH na základě zatížení CTS provozem, s možností sdílet fyzické prostředky s dalšími řídicími kanály v obdobích nízké poptávky po CTS. Tento kanál je nezbytný pro kompletní proceduru zřizování CTS hovoru, neboť poskytuje kritický spoj mezi počátečními pokusy o přístup a přidělením vyhrazených prostředků pro relace textové telefonie.

V provozu umožňuje CTSAGCH efektivní správu prostředků pro služby CTS minimalizací zpoždění při zřizování pomocí vyhrazené signalizace. Kanál podporuje jak komunikaci bod-bod, tak bod-více bodů, což umožňuje konferenční textové konverzace, když je tak nakonfigurován. Také přenáší příkazy pro předávání spojení a zprávy o rekonfiguraci kanálu během aktivních CTS relací, čímž zajišťuje kontinuitu služby při pohybu uživatelů mezi buňkami. Návrh kanálu zahrnuje mechanismy detekce a opravy chyb specifické pro požadavky textové telefonie, kde je integrita znaků důležitější než absolutní latence, což jej odlišuje od hlasově orientovaných řídicích kanálů.

## K čemu slouží

CTSAGCH byl vytvořen, aby řešil specifické komunikační potřeby uživatelů se sluchovým a řečovým postižením v mobilních sítích. Před implementací CTS měli tito uživatelé omezený přístup k mobilním telekomunikačním službám, protože tradiční hlasově orientované sítě nepodporovaly textovou telefonii s potřebnou spolehlivostí a charakteristikami reálného času. Systém CTS, včetně CTSAGCH, byl vyvinut, aby poskytl standardizované řešení textové telefonie, které by mohlo spolupracovat s existujícími zařízeními pro textovou telefonii a zároveň využívat infrastrukturu mobilní sítě.

Primární motivací pro CTSAGCH bylo vyřešit signalizační výzvy specifické pro služby textové telefonie. Na rozdíl od hlasových hovorů, které snesou krátká signalizační zpoždění, textová telefonie vyžaduje přesnou koordinaci mezi synchronizací textového modemu a přidělením kanálu. CTSAGCH poskytuje vyhrazenou signalizaci, která přenáší nejen standardní informace o přidělení rádiových prostředků, ale také parametry specifické pro CTS, jako jsou schémata kódování textu, inicializační sekvence modemů a podrobnosti konfigurace relace. Tato specializovaná signalizace zajišťuje, že se relace textové telefonie rychle navážou a udrží integritu znaků požadovanou pro efektivní komunikaci.

Historicky CTSAGCH řešil omezení pokusů o využití standardních signalizačních kanálů GSM pro služby textové telefonie. Běžné kanály pro udělení přístupu nebyly optimalizovány pro jedinečné požadavky komunikace textového modemu, zejména pokud jde o časové vztahy mezi signalizací a aktivací přenosového kanálu. Vytvořením vyhrazeného kanálu v rámci architektury CTS umožnilo 3GPP efektivní a spolehlivou textovou telefonii, která mohla koexistovat s hlasovými službami na stejné síťové infrastruktuře a zároveň splňovat požadavky na dostupnost požadované různými regulačními orgány po celém světě.

## Klíčové vlastnosti

- Přenáší zprávy o udělení přístupu pro zřízení CTS relace
- Vysílá na vyhrazených časových slotech a frekvencích pro služby CTS
- Obsahuje parametry specifické pro CTS, jako jsou schémata kódování textu a konfigurace modemu
- Podporuje jak režim komunikace bod-bod, tak bod-více bodů
- Poskytuje robustní detekci a opravu chyb pro integritu textu
- Umožňuje efektivní předávání spojení a rekonfiguraci kanálu během aktivních relací

## Související pojmy

- [CTS – Cordless Telephony System](/mobilnisite/slovnik/cts/)
- [RACH – Random Access Channel](/mobilnisite/slovnik/rach/)
- [AGCH – Access Grant Channel](/mobilnisite/slovnik/agch/)

## Definující specifikace

- **TS 43.052** (Rel-19) — GSM Cordless Telephony System (CTS) Radio Interface

---

📖 **Anglický originál a plná specifikace:** [CTSAGCH na 3GPP Explorer](https://3gpp-explorer.com/glossary/ctsagch/)
