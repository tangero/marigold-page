---
slug: "urc"
url: "/mobilnisite/slovnik/urc/"
type: "slovnik"
title: "URC – Uplink Rate Command"
date: 2025-01-01
abbr: "URC"
fullName: "Uplink Rate Command"
category: "Radio Access Network"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/urc/"
summary: "URC je řídicí signál v HSPA, který přikazuje UE upravit svou rychlost vysílání v uplinku. Je součástí signalizace na kanálu E-DCH Absolute Grant Channel (E-AGCH) a umožňuje dynamické přidělování uplin"
---

URC je řídicí signál v HSPA, který přikazuje UE upravit svou rychlost vysílání v uplinku, což umožňuje dynamické přidělování zdrojů pro efektivní využití uplinkové kapacity.

## Popis

Uplink Rate Command (URC, příkaz pro rychlost v uplinku) je klíčovou součástí Enhanced Dedicated Channel ([E-DCH](/mobilnisite/slovnik/e-dch/)) v High-Speed Uplink Packet Access ([HSUPA](/mobilnisite/slovnik/hsupa/)), zavedenou ve 3GPP Release 8. Funguje jako součást kanálu E-DCH Absolute Grant Channel ([E-AGCH](/mobilnisite/slovnik/e-agch/)), což je downlinkový fyzický kanál používaný Node B k odesílání příkazů pro plánování User Equipment (UE). URC je konkrétní hodnota ve zprávě Absolute Grant, která přímo instruuje UE o maximální povolené E-DCH Transport Format Combination ([E-TFC](/mobilnisite/slovnik/e-tfc/)), čímž řídí její rychlost přenosu dat v uplinku. Tento příkaz je zásadní pro rychlé plánování na úrovni buňky, protože umožňuje Node B spravovat uplinkový interference a efektivně přidělovat rádiové zdroje na základě aktuálních podmínek sítě a stavu vyrovnávací paměti UE.

Mechanismus URC funguje tak, že Node B monitoruje zátěž v uplinku, interference a požadavky QoS. Když je potřeba změna, přenese přes E-AGCH zprávu Absolute Grant obsahující hodnotu URC. UE po přijetí tohoto příkazu musí odpovídajícím způsobem upravit svou uplinkovou rychlost výběrem E-TFC, který nepřekročí přidělenou rychlost. Tento proces probíhá na bázi přenosového časového intervalu ([TTI](/mobilnisite/slovnik/tti/)), typicky 2 ms nebo 10 ms, což umožňuje rychlou adaptaci na kolísání provozu. Hodnoty URC odpovídají předdefinovaným podmnožinám E-TFC nebo specifickým limitům rychlosti, čímž zajišťují, že UE pracuje v rámci kapacitních omezení sítě a zachovává kvalitu služby pro všechny uživatele.

Mezi klíčové architektonické prvky patří plánovač v Node B, který generuje URC na základě algoritmů zohledňujících faktory jako nárůst šumu v uplinku, rezerva výkonu UE a priorita logických kanálů. E-AGCH je přenášen pomocí specifického kanalizačního kódu a nese 5bitovou hodnotu Absolute Grant, jejíž část tvoří URC. Entita Medium Access Control ([MAC](/mobilnisite/slovnik/mac/)) v UE interpretuje URC a omezuje výběr E-TFC ve vrstvě MAC-e/es. Toto centralizované řízení na Node B, na rozdíl od plánování řízeného [RNC](/mobilnisite/slovnik/rnc/) v dřívějších releasech, snižuje latenci a zlepšuje propustnost v uplinku, čímž činí HSUPA citlivější pro interaktivní a burstové datové aplikace.

Role URC v síti je klíčová pro správu uplinkových zdrojů v [HSPA](/mobilnisite/slovnik/hspa/). Umožňuje dynamické řízení rychlosti, které optimalizuje spektrální účinnost a zmírňuje problém blízký-vzdálený tím, že zabraňuje UE vysílat na nadměrně vysokých rychlostech, které by mohly způsobit interference. Úpravou uplinkových rychlostí na úrovni jednotlivých UE může Node B vyvažovat zátěž v buňce, upřednostňovat provoz s vysokými nároky na QoS a zvyšovat celkovou kapacitu systému. Toto plánování založené na příkazech je základním aspektem výkonnostních zisků HSUPA oproti předchozím 3G uplinkovým technologiím a podporuje služby jako nahrávání videa, online hraní a přenosy velkých souborů se zlepšenou latencí a spolehlivostí.

## K čemu slouží

Uplink Rate Command (URC, příkaz pro rychlost v uplinku) byl zaveden, aby řešil omezení v plánování a kapacitě uplinku v sítích WCDMA před Release 8. Dřívější 3GPP release se spoléhaly na plánování řízené Radio Network Controller (RNC) pro Dedicated Channel (DCH), které zahrnovalo vyšší latenci a méně citlivé řízení. To bylo nedostatečné pro paketové datové služby s proměnlivými požadavky na uplink, což vedlo k neefektivnímu využití zdrojů a suboptimálnímu uživatelskému zážitku. HSUPA s plánováním řízeným Node B včetně URC byla vytvořena, aby poskytla rychlejší a jemnější adaptaci rychlosti v uplinku, což umožňuje vyšší propustnost a nižší latenci pro aplikace náročné na uplink.

Hlavní problém, který URC řeší, je potřeba řízení interference v uplinku a optimalizace kapacity v reálném čase. Ve WCDMA je uplink limitován interferencí; nekontrolované přenosy UE mohou zhoršit výkon sítě. URC umožňuje Node B přímo nařídit snížení nebo zvýšení rychlosti na základě okamžitých podmínek, jako je rostoucí šum nebo dostupná rezerva výkonu. Tato dynamická kontrola předchází přetížení, zajišťuje spravedlivé sdílení zdrojů a udržuje QoS pro služby citlivé na zpoždění. Přesunutím plánování na Node B jsou minimalizovány zpoždění obousměrného přenosu, čímž se uplink stává efektivnějším pro burstové vzorce provozu běžné při používání mobilního internetu.

Historicky byl vývoj URC motivován růstem uživateli generovaného obsahu a symetrických datových aplikací, které zvýšily poptávku po uplinku. Vylepšení HSUPA v Release 8, včetně URC, byla součástí vývoje 3G pro konkurenceschopnost s nově se objevujícími technologiemi. URC umožnilo HSPA poskytovat vyváženější a vysoce výkonný mobilní broadbandový zážitek, podporovalo přechod na plně IP sítě a položilo základy pro pozdější uplinkové funkce LTE. Zaplnilo mezeru, kde byl upřednostňován downlink, a zajistilo, že uplink dokáže držet krok s aplikacemi jako videokonference nebo nahrávání do cloudu.

## Klíčové vlastnosti

- Úprava uplinkové rychlosti řízená Node B pomocí signalizace přes E-AGCH
- Dynamické přidělování na základě aktuálních podmínek interference a zátěže
- Podpora TTI 2 ms a 10 ms pro rychlé plánování
- Používá zprávy Absolute Grant k určení maximálního E-TFC
- Zvyšuje spektrální účinnost a kapacitu uplinku
- Snižuje latenci ve srovnání s plánováním řízeným RNC

## Související pojmy

- [E-AGCH – EDCH – Absolute Grant Channel](/mobilnisite/slovnik/e-agch/)
- [E-DCH – Enhanced Dedicated Channel](/mobilnisite/slovnik/e-dch/)
- [HSUPA – High Speed Uplink Packet Access](/mobilnisite/slovnik/hsupa/)
- [E-TFC – E-DCH Transport Format Combination](/mobilnisite/slovnik/e-tfc/)

## Definující specifikace

- **TS 26.102** (Rel-19) — Mapping of AMR and other codecs to interfaces
- **TS 26.202** (Rel-19) — AMR-WB Speech Codec Mapping Specification

---

📖 **Anglický originál a plná specifikace:** [URC na 3GPP Explorer](https://3gpp-explorer.com/glossary/urc/)
