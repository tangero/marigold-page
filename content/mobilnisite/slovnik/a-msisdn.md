---
slug: "a-msisdn"
url: "/mobilnisite/slovnik/a-msisdn/"
type: "slovnik"
title: "A-MSISDN – Additional Mobile Subscriber Integrated Services Digital Network Number"
date: 2025-01-01
abbr: "A-MSISDN"
fullName: "Additional Mobile Subscriber Integrated Services Digital Network Number"
category: "Security"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/a-msisdn/"
summary: "A-MSISDN je dodatečné MSISDN přiřazené uživateli pro účely zákonného odposlechu. Umožňuje oprávněným orgánům odposlouchávat komunikaci na konkrétním předplatném bez prozrazení primárního MSISDN uživat"
---

A-MSISDN je dodatečné MSISDN přiřazené uživateli pro účely zákonného odposlechu, které umožňuje orgánům odposlouchávat komunikaci na předplatném bez prozrazení primárního čísla uživatele.

## Popis

Dodatečné [MSISDN](/mobilnisite/slovnik/msisdn/) (A-MSISDN) je specializovaný identifikátor definovaný v bezpečnostních specifikacích 3GPP, především v TS 33.108, která detailně popisuje architekturu a požadavky zákonného odposlechu ([LI](/mobilnisite/slovnik/li/)). Funguje jako sekundární, administrativně přiřazené číslo mobilního účastníka v síti [ISDN](/mobilnisite/slovnik/isdn/), které je spojeno s předplatným uživatele vedle jeho primárního MSISDN. Z pohledu síťové architektury je A-MSISDN zřízeno v domácím serveru účastníka ([HSS](/mobilnisite/slovnik/hss/)) nebo podobném úložišti dat o účastnících. Je propojeno s mezinárodním identifikátorem mobilního účastníka ([IMSI](/mobilnisite/slovnik/imsi/)) a primárním MSISDN uživatele, čímž vytváří mapování klíčové pro funkci zákonného odposlechu. Prvky jádra sítě, jako je mobilní ústředna ([MSC](/mobilnisite/slovnik/msc/)), podpůrný uzel [GPRS](/mobilnisite/slovnik/gprs/) ([SGSN](/mobilnisite/slovnik/sgsn/)) a entita správy mobility (MME), jsou nakonfigurovány tak, aby tento identifikátor rozpoznaly a zpracovávaly při provádění činností souvisejících s odposlechem.

Provozně, když je pro cíl aktivován příkaz k zákonnému odposlechu, může být síť instruována, aby používala A-MSISDN jako referenční identifikátor pro veškerou komunikaci související s odposlechem a pro hlášení dat odesílaná zařízenímu pro monitorování orgánů činných v trestním řízení (LEMF). Řídicí prvek odposlechu (ICE) v síti, jako je bránový podpůrný uzel GPRS (GGSN) nebo brána paketové datové sítě (PGW), bude používat A-MSISDN při generování hlášení informací souvisejících s odposlechem (IRI) a obsahu komunikace (CC). Tento mechanismus zajišťuje, že skutečné, veřejné MSISDN cíle není odhaleno v datových tocích odposlechu, které jsou doručovány externím orgánům. Zpracování A-MSISDN je pro koncového uživatele transparentní a neovlivňuje běžné poskytování služeb; uživatel nadále používá své primární MSISDN pro všechny běžné hovory a datové relace.

Technická implementace zahrnuje zabezpečená rozhraní v rámci architektury LI 3GPP, konkrétně předávací rozhraní HI1, HI2 a HI3. A-MSISDN se primárně používá na rozhraní HI1, které přenáší administrativní informace a informace o příkazu, a na rozhraní HI2, které doručuje IRI. Jeho role je klíčová pro oddělení identity používané pro poskytování síťových služeb od identity používané pro zabezpečené hlášení orgánům činným v trestním řízení. Toto oddělení je základním principem bezpečnosti a ochrany soukromí v systémech zákonného odposlechu, který zabraňuje odhalení provozní identity účastníka během procesu odposlechu a zachovává důvěrnost vyšetřování.

## K čemu slouží

A-MSISDN bylo zavedeno k řešení specifických požadavků na provozní bezpečnost a ochranu soukromí v rámci rámců zákonného odposlechu. Před jeho standardizací činnosti odposlechu typicky používaly primární MSISDN účastníka jako klíčový identifikátor v hlášeních zasílaných orgánům činným v trestním řízení. Tato praxe představovala riziko, protože odhalení skutečného telefonního čísla v tocích dat odposlechu mohlo ohrozit vyšetřování, pokud by data byla zachycena nebo nesprávně zacházena. Dále to nebylo v souladu se zásadami minimalizace dat a ochrany soukromí účastníků, a to ani v zákonném kontextu.

Vytvoření A-MSISDN poskytuje metodu pro anonymizaci nebo pseudonymizaci identity cíle v rámci dodavatelského řetězce odposlechu. Jeho účelem je vyřešit problém přímého vystavení veřejného identifikátoru cíle (MSISDN) orgánu činnému v trestním řízení (LEA) a jeho systémům. Použitím administrativně přiřazeného alternativního čísla pro veškeré hlášení související s odposlechem síť chrání integritu vyšetřování a zabezpečuje primární identifikátor účastníka. To je obzvláště důležité ve scénářích zahrnujících citlivá vyšetřování nebo ochranu utajovaných operací.

Historicky, jak se požadavky na zákonný odposlech vyvíjely se systémy 3G, 4G a 5G, stala se zřejmou potřeba sofistikovanější správy identit. Koncept A-MSISDN formalizuje osvědčený postup pro oddělení identit, což zajišťuje, že sítě 3GPP splňují přísné regionální předpisy o ochraně soukromí a dat i při plnění zákonných povinností týkajících se odposlechu. Řeší omezení předchozího přístupu oddělením služební identity od identity pro odposlech, čímž zvyšuje celkovou bezpečnostní úroveň systému zákonného odposlechu.

## Klíčové vlastnosti

- Poskytuje alternativní identifikátor pro hlášení zákonného odposlechu
- Zabraňuje vystavení primárního MSISDN účastníka systémům orgánů činných v trestním řízení
- Transparentní pro koncového uživatele a neovlivňuje běžné služby
- Zřízeno a spravováno v databázi účastníků jádra sítě (např. HSS)
- Používá se specificky na předávacích rozhraních zákonného odposlechu (HI1, HI2)
- Zvyšuje provozní bezpečnost a integritu vyšetřování

## Související pojmy

- [MSISDN – Mobile Station International Subscriber Directory Number](/mobilnisite/slovnik/msisdn/)
- [IMSI – International Mobile Subscriber Identity](/mobilnisite/slovnik/imsi/)

## Definující specifikace

- **TS 33.108** (Rel-19) — LI Handover Interface Specification

---

📖 **Anglický originál a plná specifikace:** [A-MSISDN na 3GPP Explorer](https://3gpp-explorer.com/glossary/a-msisdn/)
