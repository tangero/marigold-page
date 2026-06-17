---
slug: "mnpf"
url: "/mobilnisite/slovnik/mnpf/"
type: "slovnik"
title: "MNPF – Mobile Number Portability Function"
date: 2025-01-01
abbr: "MNPF"
fullName: "Mobile Number Portability Function"
category: "Services"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/mnpf/"
summary: "Funkce 5G sítě, která poskytuje služby přenositelnosti mobilních čísel (Mobile Number Portability) v rámci architektury 5G založené na službách (SBA). Umožňuje ostatním síťovým funkcím dotazovat se na"
---

MNPF je funkce 5G sítě, která umožňuje ostatním funkcím dotazovat se na aktuální obsluhující síť u přeneseného mobilního čísla, čímž podporuje přenositelnost pro služby jako hlas a SMS.

## Popis

Funkce přenositelnosti mobilních čísel (MNPF) je síťová funkce založená na službách, zavedená v architektuře 5G Standalone (SA) pro správu přenositelnosti mobilních čísel ([MNP](/mobilnisite/slovnik/mnp/)). Funguje v rámci architektury 5G Core založené na službách (SBA) a své schopnosti zpřístupňuje jako producent služeb objevitelných funkcí Network Repository Function ([NRF](/mobilnisite/slovnik/nrf/)), primárně pro Unified Data Management ([UDM](/mobilnisite/slovnik/udm/)) a další funkce správy relací. Když síťová funkce potřebuje určit aktuální obsluhující veřejnou pozemní mobilní síť (PLMN) pro dané číslo mobilního účastníka ([MSISDN](/mobilnisite/slovnik/msisdn/)) – například při směrování SMS-MT nebo IMS hlasové relace – může vyvolat servisní operaci (např. Nnpf_NPResolution_Get) poskytovanou MNPF. MNPF pak funguje jako centralizovaný kontaktní bod pro řešení přenositelnosti čísel, interně se dotazuje externích databází přenositelnosti čísel ([NPDB](/mobilnisite/slovnik/npdb/)) nebo cache, aby získala směrovací informace.

Architektonicky je MNPF navržena jako cloud-nativní, škálovatelná mikroslužba. Komunikuje s ostatními funkcemi 5G Core pomocí rozhraní založených na službách využívajících [HTTP](/mobilnisite/slovnik/http/)/2, konkrétně rozhraní Nnpf. Její klíčová vnitřní logika zahrnuje přijetí žádosti o řešení obsahující MSISDN, aplikaci případné nezbytné normalizace čísla, provedení vyhledání prostřednictvím nakonfigurovaného zdroje dat (kterým může být přímý dotaz na externí NPDB, interní cache nebo synchronizace z centrálního datového úložiště) a vrácení odpovědi. Odpověď obsahuje aktuálně obsluhující identifikátor PLMN (Mobile Country Code a Mobile Network Code) pro dotazované číslo. Tyto informace pak používá vyžádající funkce, jako je UDM, k určení správné sítě pro následné procedury, jako je směrování SMS nebo získávání dat účastníka.

Jak funguje, zahrnuje bezproblémovou integraci s 5G procedurami. Například když funkce služby krátkých zpráv (SMSF) potřebuje doručit SMS účastníkovi, který přenesl své číslo, může se obrátit na UDM pro směrovací informace. UDM následně vyvolá MNPF, pokud data účastníka indikují přenesený stav nebo je-li vyžadováno řešení. Návrh MNPF klade důraz na nízkou latenci a vysokou dostupnost, což je klíčové pro služby komunikace v reálném čase. Podporuje také funkce jako hromadné dotazy a odběr změn dat přenositelnosti čísel, což umožňuje ostatním funkcím efektivně ukládat data do cache. Její role je odlišná od starší [MNP-SRF](/mobilnisite/slovnik/mnp-srf/), protože nejde o signalizační přenosový bod, ale o čistě dotazovací službu integrovanou do servisní sítě řídicí roviny.

## K čemu slouží

MNPF byla vytvořena za účelem modernizace a integrace přenositelnosti mobilních čísel do architektury 5G založené na službách (SBA). Předchozí řešení, jako [MNP-SRF](/mobilnisite/slovnik/mnp-srf/), byla navržena pro starší sítě s přepojováním okruhů a rané IMS sítě a často fungovala jako bod pro zachycení signalizace. 5G core se svým cloud-nativním, na mikroslužbách založeným návrhem vyžadoval nový přístup, kde je schopnost MNP poskytována jako spotřebovatelná služba různým síťovým funkcím, což je v souladu s principy SBA, jako je oddělení, znovupoužitelnost a dynamické objevování.

Řeší problém efektivního a škálovatelného poskytování informací o přenositelnosti v prostředí 5G, kde jsou služby rozloženy na menší části. Bez vyhrazené MNPF by každá síťová funkce (jako UDM, SMSF) musela implementovat vlastní složitou logiku pro rozhraní s externími NPDB, což by vedlo k duplikaci, nekonzistentnímu chování a zvýšené provozní složitosti. MNPF tuto schopnost centralizuje a poskytuje jediný standardizovaný servisní koncový bod.

Motivací pro její zavedení ve vydání Release 17 bylo zajistit plnou podporu regulatorních požadavků na MNP v 5G SA sítích, pokrývající všechny komunikační služby včetně hlasu, SMS a vznikajících služeb. Řeší omezení spočívající v závislosti na propojení se staršími sítěmi pro řešení MNP, což umožňuje čistým 5G nasazením být soběstačnými. Také usnadňuje snadnější nasazení pokročilých funkcí, jako je přenositelnost čísel pro IoT a scénáře hromadné komunikace mezi stroji v rámci 5G architektury.

## Klíčové vlastnosti

- Rozhraní založené na službách (Nnpf) využívající HTTP/2 pro integraci s 5G Core SBA
- Poskytuje převod MSISDN na obsluhující PLMN jako síťovou službu
- Navržena jako cloud-nativní, škálovatelná mikroslužba
- Podporuje dotazy od základních funkcí jako UDM a SMSF pro rozhodování o směrování
- Může komunikovat s externími NPDB nebo využívat interní mechanismy cache
- Umožňuje efektivní směrování pro SMS, IMS hlas a další 5G služby

## Související pojmy

- [UDM – Unified Data Management](/mobilnisite/slovnik/udm/)
- [NEF – Network Exposure Function](/mobilnisite/slovnik/nef/)
- [NRF – Network Resource Fulfilment](/mobilnisite/slovnik/nrf/)

## Definující specifikace

- **TS 23.540** (Rel-19) — 5G Service Based SMS Stage 2
- **TS 29.578** (Rel-19) — 3GPP TS 29578: MNPF Service Based Interface

---

📖 **Anglický originál a plná specifikace:** [MNPF na 3GPP Explorer](https://3gpp-explorer.com/glossary/mnpf/)
