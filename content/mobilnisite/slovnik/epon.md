---
slug: "epon"
url: "/mobilnisite/slovnik/epon/"
type: "slovnik"
title: "EPON – Ethernet Passive Optical Network"
date: 2025-01-01
abbr: "EPON"
fullName: "Ethernet Passive Optical Network"
category: "Other"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/epon/"
summary: "Optická přístupová síťová technologie standardizovaná IEEE a odkazovaná 3GPP pro integraci pevných sítí. Využívá topologii bod–více bodů s pasivními rozdělovači pro poskytování vysokorychlostních ethe"
---

EPON je optická přístupová technologie využívající topologii typu bod–více bodů s pasivními rozdělovači pro poskytování vysokorychlostních ethernetových služeb z centrální ústředny více koncovým uživatelům.

## Popis

Ethernet Passive Optical Network (EPON) je technologie optického vlákna až k účastníkovi (fiber-to-the-premises) implementující architekturu bod–více bodů (P2MP). V kontextu 3GPP je odkazována jako klíčová technologie pevného přístupu pro podporu konvergence pevných a mobilních sítí ([FMC](/mobilnisite/slovnik/fmc/)) a jako potenciální přenosové médium pro prvky sítí 5G, zejména v segmentech fronthaulu a backhaulu. Síť se skládá z optické linkové terminace (OLT) umístěné v centrální ústředně poskytovatele služeb a z více optických síťových jednotek (ONU) nebo optických síťových terminálů (ONT) u zákazníka. Ty jsou propojeny prostřednictvím jediného optického vlákna a pasivních optických rozdělovačů/kombinérů, které nevyžadují napájení, což zvyšuje spolehlivost a snižuje nároky na údržbu venkovní části sítě.

Přenos dat v EPON využívá standardní ethernetové rámce. Směr downstream (z OLT k ONU) je broadcastové médium; OLT vysílá rámce určené všem ONU a každá ONU filtruje rámce na základě jedinečného identifikátoru logického spoje (LLID). Směr upstream (z ONU k OLT) je sdílené médium vyžadující protokol řízení přístupu k médiu ([MAC](/mobilnisite/slovnik/mac/)) pro zabránění kolizím. Toto řídí OLT pomocí algoritmu dynamické alokace šířky pásma (DBA). OLT přiděluje přenosová okna (časové sloty) každé ONU na základě poptávky, čímž zajišťuje efektivní využití upstream šířky pásma. Tento přístup s multiplexováním s časovým dělením ([TDMA](/mobilnisite/slovnik/tdma/)) je základním provozním mechanismem.

Zájem 3GPP o EPON, dokumentovaný ve specifikacích jako TS 22.104 (požadavky na služby) a TS 22.821 (studie FMC), spočívá v jeho roli jako výkonného a nákladově efektivního řešení pevného přístupu, které lze integrovat s mobilními sítěmi. Pro FMC poskytuje EPON spolehlivou, vysokokapacitní 'pevnou' část pro konvergované služby. Pro 5G je považován za kandidátskou technologii pro přenosové sítě díky vysoké šířce pásma (standardy 1 Gbps a 10 Gbps), nízké latenci (zejména v novějších profilech) a podpoře přesné časové synchronizace (přes [IEEE](/mobilnisite/slovnik/ieee/) 1588), což je klíčové pro koordinaci rádiových jednotek v centralizovaných RAN (C-RAN) architekturách. Představuje 'pevnou' složku v holistickém návrhu systému 5G.

## K čemu slouží

EPON byl vyvinut mimo 3GPP (primárně v [IEEE](/mobilnisite/slovnik/ieee/) 802.3ah a 802.3av) k řešení 'poslední míle' jako budoucně odolná, na vláknech založená technologie. Jeho účelem je poskytovat nákladově efektivní vysokorychlostní širokopásmový přístup maximalizací využití jediného optického vlákna pro obsluhu více zákazníků, čímž se snižují náklady na účastníka ve srovnání s point-to-point vláknem. Pasivní povaha rozdělovačů snižuje provozní náklady a zvyšuje spolehlivost sítě.

3GPP začalo formálně odkazovat na EPON od Release 16, motivováno snahou průmyslu o konvergenci pevných a mobilních sítí ([FMC](/mobilnisite/slovnik/fmc/)) a potřebou specifikovat holistické systémy 5G zahrnující pevný přístup. Předchozí generace mobilních sítí se téměř výhradně zaměřovaly na rádiovou část a mobilní core síť. Nicméně vize 5G zahrnuje bezproblémové poskytování služeb napříč pevnými a bezdrátovými sítěmi. EPON, jako široce nasazená pevná přístupová technologie s gigabitovou kapacitou, je přirozeným kandidátem pro tuto konvergovanou infrastrukturu. Jeho zahrnutí do studií 3GPP řeší omezení spočívající v izolovaném uvažování o mobilních sítích. Umožňuje 3GPP specifikovat, jak mohou funkce core sítě 5G interagovat s pevnými přístupovými sítěmi, jako je EPON, a spravovat jejich zdroje, což umožňuje skutečné konvergované služby, síťové segmentování (network slicing) zahrnující obě domény a využití spolehlivého pevného přenosu pro zahušťování mobilní sítě.

## Klíčové vlastnosti

- Topologie bod–více bodů využívající pasivní optické rozdělovače
- Pro zapouzdření dat využívá standardní ethernetové rámce
- Pro upstream přenos využívá TDMA a dynamickou alokaci šířky pásma (DBA)
- Podporuje symetrické přenosové rychlosti 1 Gbps (1G-EPON) a 10 Gbps (10G-EPON)
- Poskytuje přesnou časovou synchronizaci prostřednictvím IEEE 1588 pro mobilní přenos
- Umožňuje dlouhé dosahy optického spojení (až 20 km) mezi OLT a ONU

## Definující specifikace

- **TS 22.104** (Rel-19) — Service requirements for cyber-physical control apps
- **TS 22.821** (Rel-16) — 5G LAN-type Services Requirements

---

📖 **Anglický originál a plná specifikace:** [EPON na 3GPP Explorer](https://3gpp-explorer.com/glossary/epon/)
