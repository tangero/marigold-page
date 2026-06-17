---
slug: "bl"
url: "/mobilnisite/slovnik/bl/"
type: "slovnik"
title: "BL – Bandwidth reduced Low complexity"
date: 2025-01-01
abbr: "BL"
fullName: "Bandwidth reduced Low complexity"
category: "IoT"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/bl/"
summary: "BL (Bandwidth reduced Low complexity) je funkce 3GPP umožňující sítím LTE podporovat nízkonákladová a nízkopříkonová IoT zařízení. Snižuje složitost zařízení omezením šířky pásma na 1,4 MHz a zjednodu"
---

BL je funkce 3GPP pro sítě LTE, která podporuje nízkonákladová IoT zařízení snížením složitosti prostřednictvím omezené šířky pásma 1,4 MHz a zjednodušených RF požadavků.

## Popis

Bandwidth reduced Low complexity (BL) je standardizační funkce 3GPP zavedená za účelem umožnění efektivní podpory zařízení pro komunikaci typu stroj-stroj ([MTC](/mobilnisite/slovnik/mtc/)), často označovaných jako IoT zařízení, v sítích LTE. Základním architektonickým principem je vytvoření zjednodušené kategorie zařízení (kategorie M1), které pracuje v redukované šířce pásma 1,4 MHz v uplinku i downlinku bez ohledu na systémovou šířku pásma nosné LTE. To je výrazný odklon od standardního uživatelského zařízení (UE) LTE, které musí podporovat celou šířku nosné (až 20 MHz). Síť identifikuje BL UE během počátečního přístupu a nakonfiguruje je pro provoz v této úzkopásmové oblasti, čímž zajišťuje jejich koexistenci s běžným provozem LTE na stejné nosné.

Z pohledu protokolového zásobníku BL ovlivňuje více vrstev. Na fyzické vrstvě (PHY) používají BL UE redukované svazování přenosových časových intervalů (TTI) a specifické konfigurace referenčních signálů vhodné pro vylepšení pokrytí. Vrstva řízení přístupu k médiu ([MAC](/mobilnisite/slovnik/mac/)) zajišťuje plánování BL UE v přiděleném úzkém pásmu, zatímco vrstva řízení rádiových prostředků ([RRC](/mobilnisite/slovnik/rrc/)) obsahuje specifické procedury pro signalizaci schopností BL UE a správu spojení. Přístupová síť (RAN), konkrétně eNodeB, je zodpovědná za plánování prostředků, správu interference a aplikaci technik vylepšení pokrytí, jako je opakování přenosů, pro BL zařízení.

Provoz BL UE začíná hledáním buňky a synchronizací pomocí primárního a sekundárního synchronizačního signálu (PSS/SSS), které jsou přenášeny ve středovém pásmu 1,4 MHz. Po synchronizaci UE čte hlavní informační blok ([MIB](/mobilnisite/slovnik/mib/)) a bloky systémových informací (SIB), které obsahují základní informace pro provoz BL. eNodeB plánuje jak společné, tak vyhrazené kanály (jako [PDSCH](/mobilnisite/slovnik/pdsch/) a PUSCH) pro BL UE v rámci úzkého pásma. Klíčovým mechanismem je frekvenční hopping, kdy se přiřazení úzkého pásma může měnit mezi podrámci za účelem zajištění frekvenční diverzity a zlepšení výkonu v náročných rádiových podmínkách.

Úloha BL v síti spočívá v tom, že slouží jako základ pro LTE-M (také známé jako eMTC). Poskytuje základní charakteristiky na úrovni spojení, které umožňují dlouhou životnost baterie (až 10+ let), hluboké pokrytí (až o 15 dB lepší než základní LTE) a nízkou cenu zařízení. Díky opětovnému využití spektra LTE a jádra sítě s minimálními úpravami umožnilo BL operátorům rychle nasazovat služby IoT. Funguje in-band s běžným LTE, což znamená, že segment 1,4 MHz používaný BL zařízeními je vyčleněn ze standardní nosné LTE, čímž je zajištěno efektivní využití spektra a zpětná kompatibilita.

## K čemu slouží

BL bylo vytvořeno za účelem řešení základních ekonomických a technických překážek, které bránily využití celulárních sítí pro masivní nasazení internetu věcí (IoT). Před jeho zavedením byla standardní LTE zařízení příliš složitá, energeticky náročná a drahá pro jednoduché senzory a měřiče, které vyžadují desetiletou životnost baterie a velmi nízkou cenu modulu. Technologie jako [GPRS](/mobilnisite/slovnik/gprs/)/[EDGE](/mobilnisite/slovnik/edge/) nabízely nižší složitost, ale postrádaly spektrální účinnost, kapacitu a pokrytí potřebné pro budoucí masivní IoT. Hlavním problémem, který BL řeší, je snížení složitosti UE za účelem snížení nákladů při zachování výhod systému založeného na LTE.

Historický kontext spočívá v raných letech 2010, kdy průmysl očekával exponenciální růst připojených zařízení pro utility, sledování majetku a chytrá města. 3GPP uznalo, že v rámci architektury LTE je potřeba nové, optimalizované rozhraní pro přenos po rádiu. BL přímo řeší omezení předchozích přístupů tím, že stanovuje maximální šířku kanálu 1,4 MHz, což drasticky snižuje náklady na RF komponenty (např. nižší vzorkovací frekvence, jednodušší filtry). Také zjednodušuje požadavky na základní pásmové zpracování a protokolový zásobník, což umožňuje provoz s jedinou anténou a half-duplex [FDD](/mobilnisite/slovnik/fdd/) režim, což dále snižuje náklady a spotřebu energie.

Navíc BL zahrnuje konstrukční prvky pro vylepšené pokrytí, čímž řeší problém IoT zařízení nasazených v náročných lokalitách, jako jsou sklepy nebo venkovské oblasti. Kombinací redukované šířky pásma s technikami, jako jsou opakované přenosy a uvolněné požadavky na výkon, dosahuje BL významného zlepšení rozpočtu spoje. Toto účelové řešení učinilo celulární IoT poprvé komerčně životaschopným, vytvořilo jasnou migrační cestu od 2G IoT a stanovilo technický základ pro následná vylepšení v pozdějších vydáních 3GPP.

## Klíčové vlastnosti

- Omezení provozu na šířku kanálu 1,4 MHz v uplinku i downlinku
- Podpora half-duplex FDD provozního režimu pro snížení ceny zařízení
- Povinná podpora režimů vylepšení pokrytí (až 15 dB zlepšení)
- In-band provoz v rámci standardních nosných LTE pro efektivitu spektra
- Snížené špičkové datové rychlosti (přibližně 1 Mbps) optimalizované pro IoT provoz
- Rozšířené přerušované příjímání (eDRX) a režim úspory energie (PSM) pro ultra-nízkou spotřebu

## Definující specifikace

- **TR 26.948** (Rel-19) — Video enhancements for 3GPP Multimedia Services
- **TS 27.007** (Rel-19) — AT Command Set for UE
- **TR 28.841** (Rel-18) — Technical Report on IoT NTN Enhancements
- **TR 33.937** (Rel-19) — Protection against Unsolicited Communication in IMS
- **TS 36.300** (Rel-19) — E-UTRAN Radio Interface Protocol Architecture Overview
- **TS 36.302** (Rel-19) — E-UTRA Physical Layer Services
- **TS 36.304** (Rel-19) — UE Idle Mode Procedures in E-UTRA
- **TS 36.321** (Rel-19) — E-UTRA MAC Protocol Specification
- **TS 36.331** (Rel-19) — LTE RRC Protocol Specification
- **TS 36.423** (Rel-19) — X2 Application Protocol (X2AP) Specification
- **TS 38.300** (Rel-19) — NG-RAN Overall Description

---

📖 **Anglický originál a plná specifikace:** [BL na 3GPP Explorer](https://3gpp-explorer.com/glossary/bl/)
