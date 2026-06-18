---
slug: "hi3"
url: "/mobilnisite/slovnik/hi3/"
type: "slovnik"
title: "HI3 – Handover Interface Port 3"
date: 2025-01-01
abbr: "HI3"
fullName: "Handover Interface Port 3"
category: "Interface"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/hi3/"
summary: "HI3 je standardizované rozhraní pro zákonné odposlechy, které doručuje skutečný obsah komunikace (CC), jako je zvuk hovoru nebo datové pakety uživatele, od síťového operátora k monitorovacímu zařízení"
---

HI3 je standardizované rozhraní pro zákonné odposlechy, které doručuje skutečný obsah komunikace od síťového operátora k monitorovacímu zařízení orgánů činných v trestním řízení.

## Popis

Handover Interface Port 3 (HI3) je základní rozhraní v rámci architektury zákonných odposlechů 3GPP, specifikované v dokumentu 33.108. Je určeno pro doručování obsahu komunikace ([CC](/mobilnisite/slovnik/cc/)), který představuje skutečnou přenášenou informaci sledovaného účastníka. To zahrnuje zvuk hovoru v okruhově přepínaných sítích, pakety VoIP v IMS a datové pakety uživatelské roviny (např. z prohlížení webu, zasílání zpráv) v paketově přepínaných doménách. Rozhraní HI3 propojuje Mediační funkci ([MF](/mobilnisite/slovnik/mf/)) nebo Doručovací funkci ([DF](/mobilnisite/slovnik/df/)) síťového operátora s monitorovacím zařízením orgánů činných v trestním řízení ([LEMF](/mobilnisite/slovnik/lemf/)). Jeho jediným účelem je přenos kopie komunikačního obsahu cíle, a to spolehlivě, bezpečně a synchronizovaně s přidruženými metadaty doručovanými přes rozhraní [HI2](/mobilnisite/slovnik/hi2/).

Operačně, když je pro cíl aktivní příkaz k zákonnému odposlechu, síťové uzly (např. [MSC](/mobilnisite/slovnik/msc/) pro hlas, [SGSN](/mobilnisite/slovnik/sgsn/)/GGSN/[UPF](/mobilnisite/slovnik/upf/) pro data) jsou instruovány ke kopírování relevantního provozu uživatelské roviny. Tento zkopírovaný obsah je odeslán do Mediační funkce, která jej formátuje a zabalí pro doručení. Pro hlas to typicky zahrnuje doručování proudů Real-time Transport Protocol (RTP) nebo zakódovaných zvukových rámců. Pro paketová data to zahrnuje doručování IP paketů nebo strukturovaných datových záznamů. Specifikace HI3 definuje transportní mechanismy a formáty paketů pro tento obsah. Podobně jako HI2 často spoléhá na standardizované protokoly pro zajištění interoperability, ačkoli samotný obsah může být v nativním kodeku nebo paketovém formátu. Rozhraní musí zvládat proudy v reálném čase pro odposlech hlasu a potenciálně objemné datové toky pro odposlech širokopásmových dat, což vyžaduje robustní přenosovou kapacitu a nízkolatenční spojení k LEMF.

Rozhraní HI3 pracuje v přísné koordinaci s HI2. Informace o odposlechu (IRI) doručované na HI2 poskytují kontext – signalizaci začátku hovoru nebo IP relace – který umožňuje LEMF korelovat a správně interpretovat obsahové proudy přijímané na HI3. Toto oddělení umožňuje efektivní návrh sítě a cílené doručování dat. Bezpečnostní opatření pro HI3 jsou extrémně přísná, protože přenáší nejcitlivější odposlechnutá data. Přenos probíhá vždy přes vysoce zabezpečené, často fyzicky oddělené sítě se silným šifrováním, aby byla zaručena důvěrnost a integrita. Architektura zajišťuje, že obsah je doručen bez zhoršení kvality nebo změn, čímž zachovává svou důkazní hodnotu. Pro moderní služby se mechanismy doručování HI3 vyvinuly tak, aby zvládaly různé typy obsahu, včetně hlasu a videa založeného na IMS, SMS přes IP a datových relací z 5G síťových řezů, což demonstruje jeho adaptabilní roli v ekosystému zákonných odposlechů.

## K čemu slouží

HI3 bylo standardizováno, aby poskytlo jednotnou metodu pro síťové operátory k doručování skutečného obsahu odposlechnutých komunikací orgánům činným v trestním řízení. Před standardizací 3GPP bylo doručování obsahu hovorů řešeno různými proprietárními a země-specifickými mechanismy, což komplikovalo operace zákonných odposlechů, zejména pro orgány činné v trestním řízení pracující s více poskytovateli služeb. Nedostatek standardu hrozil neúplnými odposlechy, ztrátou důkazů a vysokými integračními náklady pro monitorovací centra. HI3, zavedené společně s HI2 ve verzi 8, vytvořilo konzistentní a spolehlivý kanál pro komunikační obsah.

Účel HI3 přímo souvisí s plněním technických požadavků zákonů o zákonných odposleších, které ukládají povinnost zachytit jak signalizační informace, tak obsah komunikace. Zatímco metadata z HI2 odhalují komunikační vzorce, obsah z HI3 je často klíčovým důkazem v vyšetřování. Rozhraní řeší technickou výzvu kopírování a přesměrování mediálních proudů a datových toků v reálném čase ze složité architektury sítí 3GPP (od okruhového přepojování 2G/3G po plně IP sítě 4G/5G) a jejich externího doručování bez dopadu na kvalitu služeb pro cíl nebo ostatní uživatele. Jeho vznik byl motivován potřebou budoucnostné, technologicky neutrální metody doručování obsahu, která by se mohla vyvíjet spolu se síťovými technologiemi, od tradičních hlasových hovorů po VoIP a vysokorychlostní internetová data.

## Klíčové vlastnosti

- Standardizované doručování obsahu komunikace (CC) orgánům činným v trestním řízení
- Přenáší skutečný zvuk hovoru, video nebo datové pakety uživatele
- Zpracovává mediální proudy v reálném čase (např. RTP pro hlas) a datové toky paketů
- Navrženo pro vysokou přenosovou kapacitu, nízkou latenci a zabezpečený přenos
- Pracuje synchronizovaně s HI2 pro korelaci metadat a obsahu
- Podporuje odposlech v okruhově i paketově přepínaných doménách

## Související pojmy

- [HI2 – Handover Interface Port 2](/mobilnisite/slovnik/hi2/)
- [LEMF – Law Enforcement Monitoring Facility](/mobilnisite/slovnik/lemf/)

## Definující specifikace

- **TS 33.108** (Rel-19) — LI Handover Interface Specification

---

📖 **Anglický originál a plná specifikace:** [HI3 na 3GPP Explorer](https://3gpp-explorer.com/glossary/hi3/)
