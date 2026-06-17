---
slug: "bps"
url: "/mobilnisite/slovnik/bps/"
type: "slovnik"
title: "BPS – Body Proximity Sensing"
date: 2025-01-01
abbr: "BPS"
fullName: "Body Proximity Sensing"
category: "Services"
segment: "User Equipment"
canonical: "https://3gpp-explorer.com/glossary/bps/"
summary: "Body Proximity Sensing (BPS) je funkce 3GPP, která umožňuje uživatelskému zařízení (UE) detekovat svou blízkost k lidskému tělu. Umožňuje UE upravit svůj výkon rádiového vysílání (RF), aby vyhovělo re"
---

BPS je funkce 3GPP, která umožňuje uživatelskému zařízení (UE) detekovat svou blízkost k lidskému tělu, aby mohlo upravit výkon vysílání rádiových frekvencí pro dodržení bezpečnostních limitů specifické míry absorpce (SAR).

## Popis

Body Proximity Sensing (BPS) je standardizovaný mechanismus zavedený ve 3GPP Release 17, který umožňuje uživatelskému zařízení (UE) dynamicky detekovat svou blízkost k lidskému tělu a podle toho upravit své parametry rádiového vysílání. Primárním technickým cílem je zajistit dodržování regulatorních limitů specifické míry absorpce (SAR), která měří rychlost absorpce RF energie tělesnou tkání. BPS funguje integrací senzorů (např. kapacitních, infračervených nebo ultrazvukových) v rámci UE, které sledují vzdálenost nebo kontakt s tělem. Při detekci blízkosti je modem a RF front-end UE upozorněn, aby provedl snížení výkonu nebo jiné strategie zmírnění, jako je úprava konfigurace antén nebo vzorců doby vysílání, aby SAR zůstala v bezpečných mezích.

Architektonicky BPS zahrnuje koordinaci mezi aplikačním procesorem UE, subsystémy senzorů a zásobníkem protokolů 3GPP, zejména vrstvou řízení rádiových prostředků ([RRC](/mobilnisite/slovnik/rrc/)). UE hlásí svou schopnost BPS a stav síti prostřednictvím signalizace RRC, což umožňuje síti být informována o provozních omezeních UE. Toto hlášení je definováno ve specifikaci 3GPP 38.306, která zahrnuje schopnosti přístupu k rádiu UE. Síť může tyto informace využít pro správu rádiových prostředků, jako je úprava přidělení přenosových zdrojů nebo parametrů předávání spojení, aby vyhověla sníženému vysílacímu výkonu UE, a tím minimalizovala dopad na přenosové rychlosti a latenci.

Klíčové součásti BPS zahrnují senzory blízkosti, řadič BPS uvnitř UE, který zpracovává data ze senzorů, a vylepšení protokolu 3GPP pro indikaci schopností a koordinaci se sítí. Řadič BPS vyhodnocuje vstupy ze senzorů, aby určil stavy blízkosti (např. 'blízko' nebo 'daleko' od těla), a spouští předdefinované profily snížení RF výkonu. Tyto profily jsou navrženy tak, aby splňovaly regionální předpisy SAR (např. [FCC](/mobilnisite/slovnik/fcc/) v USA, [CE](/mobilnisite/slovnik/ce/) v Evropě) a zároveň byly optimalizovány pro scénáře jako hlasové hovory, datové relace nebo použití nositelných zařízení. Integrace s existujícími mechanismy řízení výkonu, jako je řízení výkonu v uplinku a maximální snížení výkonu ([MPR](/mobilnisite/slovnik/mpr/)), zajišťuje plynulý provoz bez nutnosti nové síťové infrastruktury.

V síti BPS zvyšuje bezpečnost uživatelů a regulatorní shodu bez obětování kvality služeb. Například když UE detekuje kontakt s tělem během vysílání s vysokým výkonem (např. 5G FR2 mmWave), může snížit výkon nebo přepnout antény pro snížení SAR, a síť to může kompenzovat přidělením více prostředků nebo úpravou modulačních schémat. Tento proaktivní přístup je zvláště důležitý pro zařízení jako chytré hodinky, [AR](/mobilnisite/slovnik/ar/)/VR brýle a chytré telefony používané v ručním režimu, kde jsou rizika RF expozice vyšší. BPS tedy představuje konvergenci hardwarového snímání a standardů 3GPP k řešení zdravotních obav v moderních bezdrátových ekosystémech.

## K čemu slouží

BPS bylo vytvořeno k řešení rostoucích regulatorních a bezpečnostních požadavků souvisejících s RF expozicí z mobilních zařízení, zejména když 5G zavádí vyšší frekvenční pásma a nové formáty jako nositelná zařízení. Před BPS zařízení používala statické limity výkonu nebo zjednodušenou detekci blízkosti (např. pomocí akcelerometrů), což často vedlo ke konzervativnímu, výkon degradujícímu snížení výkonu. Tyto přístupy postrádaly standardizaci, což vedlo k roztříštěným implementacím a potenciálnímu nesplnění vyvíjejících se globálních standardů SAR. Motivací pro BPS ve 3GPP Release 17 byla potřeba jednotné, síťově informované metody pro dynamické řízení RF expozice na základě reálné blízkosti těla, což umožňuje bezpečnější a efektivnější provoz zařízení.

Historicky se shoda s předpisy SAR řídila pomocí pevných konstrukčních rezerv, jako je snížení maximálního vysílacího výkonu ve všech scénářích použití, což mohlo zbytečně omezit výkon sítě a uživatelský zážitek. S rozšířením zařízení pracujících v těsném kontaktu s tělem (např. fitness trackery, lékařské senzory) vznikla naléhavá potřeba chytřejších, adaptivních řešení. BPS to řeší využitím pokročilých senzorů a signalizace 3GPP k poskytnutí detailní kontroly, což umožňuje zařízením vysílat s vyššími výkony, když je to bezpečné (např. dál od těla), a snižovat výkon pouze v případě nutnosti. Tím se optimalizuje jak bezpečnost, tak konektivita, a řeší se omezení předchozích nestandardizovaných nebo pouze hardwarových přístupů.

BPS navíc podporuje regulatorní sladění v různých regionech tím, že poskytuje standardizovaný rámec pro řízení expozice. Umožňuje výrobcům zařízení implementovat konzistentní bezpečnostní funkce a zároveň snižovat složitost certifikace. Vytvoření BPS bylo hnací silou průmyslové spolupráce, aby byly sítě připraveny na budoucí přísnější směrnice pro RF expozici, a zajistilo se, že 5G a další generace mohou nasadit technologie s vysokým výkonem bez kompromisů v oblasti zdraví uživatelů. Integrací BPS do ekosystému 3GPP se usnadňuje inovace v nositelných a IoT zařízeních, kde je blízkost těla stálým faktorem, čímž se zvyšuje životaschopnost těchto služeb v každodenním životě.

## Klíčové vlastnosti

- Dynamické nastavení RF výkonu na základě detekce blízkosti těla v reálném čase
- Standardizované hlášení schopností UE síti prostřednictvím signalizace RRC
- Integrace se senzory (např. kapacitními, infračervenými) pro přesné vyhodnocení blízkosti
- Podpora regulatorní shody SAR v různých globálních regionech
- Koordinace se správou síťových zdrojů pro minimalizaci dopadu na výkon
- Použitelnost pro různé formáty zařízení včetně nositelných zařízení a chytrých telefonů

## Definující specifikace

- **TS 38.306** (Rel-19) — NR UE Radio Access Capability Parameters

---

📖 **Anglický originál a plná specifikace:** [BPS na 3GPP Explorer](https://3gpp-explorer.com/glossary/bps/)
