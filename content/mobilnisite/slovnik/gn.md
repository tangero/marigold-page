---
slug: "gn"
url: "/mobilnisite/slovnik/gn/"
type: "slovnik"
title: "GN – Generic Number"
date: 2025-01-01
abbr: "GN"
fullName: "Generic Number"
category: "Identifier"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/gn/"
summary: "Generic Number (GN) je flexibilní adresní parametr používaný ve signalizaci 3GPP, zejména v CAMEL a IMS. Reprezentuje různé typy čísel (např. MSISDN, služební čísla) v generickém formátu, což umožňuje"
---

GN (Generic Number) je flexibilní adresní parametr používaný ve signalizaci 3GPP k reprezentaci různých typů čísel v generickém formátu pro přenos rozmanitých adresních informací přes síťová rozhraní.

## Popis

Generic Number (GN) je parametr definovaný v signalizačních protokolech 3GPP, nejvýznamněji v rámci architektury Customised Applications for Mobile network Enhanced Logic ([CAMEL](/mobilnisite/slovnik/camel/)) a IP Multimedia Subsystem (IMS). Jedná se o univerzální datovou strukturu používanou k přenosu adresních informací v generickém, na typu nezávislém formátu. Parametr GN může zapouzdřovat různé typy čísel, jako je Mobile Station International Subscriber Directory Number ([MSISDN](/mobilnisite/slovnik/msisdn/)), služební čísla nebo jiné identifikátory, spolu s atributy, které specifikují povahu čísla, omezení jeho prezentace a charakteristiky screeningu. Tato flexibilita umožňuje funkcím řízení služeb zpracovávat a směrovát hovory nebo relace na základě dynamických číselných informací, aniž by byly těsně svázány s konkrétním číslovacím plánem.

Z architektonického hlediska je GN přenášen v rámci signalizačních zpráv, jako je Initial Detection Point ([IDP](/mobilnisite/slovnik/idp/)) v CAMEL nebo v rámci zpráv SIP v IMS. Skládá se z několika podpolí: indikátoru číslovacího plánu, který identifikuje číslovací schéma (např. E.164, privátní); typu čísla, který označuje formát čísla (např. mezinárodní, národní); vlastních číslic čísla; a indikátorů prezentace a screeningu, které řídí, zda lze číslo prezentovat volané straně a jak má být screenedováno. Tento strukturovaný formát umožňuje přijímacímu síťovému uzlu, jako je Service Control Point (SCP) nebo Application Server ([AS](/mobilnisite/slovnik/as/)), interpretovat číslo správně a aplikovat odpovídající servisní logiku.

Během provozu, když je splněna spouštěcí podmínka (např. hovor iniciovaný mobilním zařízením), navštívená ústředna Mobile Switching Center ([MSC](/mobilnisite/slovnik/msc/)) nebo funkce Call Session Control Function ([CSCF](/mobilnisite/slovnik/cscf/)) zahrne parametr GN do signalizační zprávy odeslané na servisní platformu. Servisní logika, umístěná na SCP nebo AS, analyzuje GN – spolu s dalšími parametry – aby učinila rozhodnutí o směrování, aplikovala tarifní pravidla nebo vyvolala přidané služby, jako je překlad čísel nebo řízení předplacených hovorů. Například ve scénáři předplaceného roamingu může GN nést volajícího MSISDN do tarifního systému domovské sítě. Generická povaha GN znamená, že stejná struktura parametru může být znovu použita napříč různými službami a síťovými generacemi, což podporuje interoperabilitu.

Role GN je klíčová pro standardizovanou realizaci služeb inteligentních sítí ([IN](/mobilnisite/slovnik/in/)) a služeb založených na IMS. Abstrahováním specifik čísla do dobře definovaného kontejneru specifikace 3GPP (jako TS 29.163 pro interworking mezi IMS a [CS](/mobilnisite/slovnik/cs/) sítěmi) zajišťují, že servisní logika zůstává přenositelná a vývoj sítě (např. z CS na IMS) nenarušuje stávající implementace služeb. Odděluje provádění služby od podkladového přenosu a číslovacích detailů, což je nezbytné pro bezproblémový provoz složitých služeb, jako jsou virtuální privátní sítě, bezplatná čísla a správa mobility v heterogenních sítích.

## K čemu slouží

Parametr Generic Number (GN) byl vytvořen, aby vyřešil problém standardizovaného a flexibilního přenosu různorodých a proměnných adresních informací v rámci telekomunikačních signalizačních protokolů. Rané architektury inteligentních sítí (IN) vyžadovaly způsob předávání čísel volajícího/volaného a dalších identifikátorů mezi síťovými ústřednami a body řízení služeb, avšak různé služby a regiony používaly různé formáty čísel a atributy. GN poskytuje univerzální kontejner, který může nést jakýkoli typ čísla spolu s metadaty o jeho prezentaci a screeningu, což umožňuje opakovaně použitelnou servisní logiku nezávislou na konkrétním číslovacím kontextu.

Historicky, před standardizací parametrů jako je GN, byly implementace služeb často proprietární a těsně integrované se specifickými signalizačními rozšířeními dodavatelů ústředen. To činilo nasazení služeb složitým, nákladným a bránilo interoperabilitě, zejména v více-dodavatelských sítích a scénářích mezinárodního roamingu. Zavedení GN v CAMEL (od 3GPP Rel-99 dále, přičemž Rel-8 zdokonalilo jeho použití v EPS) poskytlo společný jazyk pro přenos čísel. Umožnilo síťovým operátorům nasazovat služby jako předplacené, přenosnost čísel a bezplatné volání konzistentně napříč jejich sítěmi a ve spolupráci s dalšími operátory.

Dále, GN řeší evoluci směrem k plně IP sítím a IMS. Jak služby migrovaly z okruhově spínaného CAMEL na signalizaci SIP založenou na IMS, objevila se potřeba přenášet stejnou bohatou sadu číselných informací. GN, specifikované v protokolech jako SIP pro IMS (např. v TS 29.163), zajišťuje kontinuitu servisní logiky. Řeší problém interoperability mezi staršími CS sítěmi a IMS, což umožňuje servisním platformám přijímat známý parametr GN bez ohledu na to, zda hovor pochází z tradičního telefonu nebo IMS klienta. Tato zpětná kompatibilita a výhledový design motivují jeho pokračující relevanci v moderních architekturách 3GPP.

## Klíčové vlastnosti

- Flexibilní kontejner pro přenos různých typů čísel (MSISDN, služebních čísel) ve signalizaci
- Obsahuje podpole pro číslovací plán, typ čísla a číslice čísla
- Podporuje indikátory prezentace a screeningu pro řízení zobrazení čísla koncovému uživateli
- Klíčový pro služby inteligentních sítí založené na CAMEL, jako jsou předplacené služby a VPN
- Používán ve signalizaci IMS (např. SIP) pro spouštění služeb a interworking s CS sítěmi
- Umožňuje přenositelnost servisní logiky a interoperabilitu mezi více dodavateli

## Související pojmy

- [CAMEL – Customised Applications for Mobile network Enhanced Logic](/mobilnisite/slovnik/camel/)
- [MSISDN – Mobile Station International Subscriber Directory Number](/mobilnisite/slovnik/msisdn/)
- [IMS – IP Multimedia Subsystem](/mobilnisite/slovnik/ims/)

## Definující specifikace

- **TS 29.163** (Rel-19) — Interworking between 3GPP IM CN and CS networks

---

📖 **Anglický originál a plná specifikace:** [GN na 3GPP Explorer](https://3gpp-explorer.com/glossary/gn/)
