---
slug: "is"
url: "/mobilnisite/slovnik/is/"
type: "slovnik"
title: "IS – Information Service"
date: 2025-01-01
abbr: "IS"
fullName: "Information Service"
category: "Services"
segment: "Management"
canonical: "https://3gpp-explorer.com/glossary/is/"
summary: "Široká kategorie služeb v 3GPP, která poskytuje uživatelům doručování informací, jako je počasí, zprávy nebo obsah založený na poloze. Zahrnuje architektonické prvky, řídicí funkce a účtovací mechanis"
---

IS (Information Service – informační služba) je široká kategorie služeb 3GPP, která poskytuje uživatelům doručování informací, jako je počasí nebo zprávy, a zahrnuje architektonické prvky, řídicí funkce a účtovací mechanismy pro poskytování obsahu.

## Popis

Informační služba (IS) v 3GPP označuje komplexní rámec pro doručování informačního obsahu mobilním uživatelům, zahrnující služby jako aktualizace zpráv, předpovědi počasí, burzovní kotace a upozornění založená na poloze. Nejde o jednu konkrétní službu, ale o koncepční kategorii definovanou v širokém spektru specifikací, především v řadě 32 (Řízení a účtování) a řadě 28 (Řízení a orchestrace). Architektura zahrnuje více síťových prvků, včetně servisní platformy (např. obsahový server), jádra sítě pro doručování a řídicích systémů pro zřizování, monitorování a účtování. Mezi klíčové komponenty patří Server schopností služeb ([SCS](/mobilnisite/slovnik/scs/)) pro servisní logiku, Gateway Mobile Location Centre ([GMLC](/mobilnisite/slovnik/gmlc/)) pro služby založené na poloze a účtovací systémy jako Online Charging System ([OCS](/mobilnisite/slovnik/ocs/)) a Offline Charging System ([OFCS](/mobilnisite/slovnik/ofcs/)) pro zpracování fakturace za doručování informací.

Jak funguje: Informační služba typicky následuje model typu žádost-odpověď nebo push. V modelu žádosti zařízení uživatele (UE) odešle dotaz přes mobilní síť na aplikační server poskytovatele informační služby. Požadavek prochází jádrem sítě (např. přes IMS nebo přímá IP připojení) a server jej zpracuje, případně s načtením dat z externích zdrojů (např. rozhraní [API](/mobilnisite/slovnik/api/) pro počasí). Odpověď je poté doručena zpět k UE přes síť s použitím příslušné kvality služby (QoS). V push modelu poskytovatel služby iniciuje doručení na základě spouštěčů, jako je čas nebo poloha, pomocí mechanismů jako [SMS](/mobilnisite/slovnik/sms/), Multimedia Messaging Service ([MMS](/mobilnisite/slovnik/mms/)) nebo IP push notifikace. Specifikace řízení (např. 32.101) definují, jak jsou tyto služby monitorovány z hlediska výkonu, poruch a konfigurace, aby byl zajištěn spolehlivý provoz.

Role informační služby v síti spočívá v umožnění přidaných služeb nad rámec základního hlasu a dat, což generuje příjmy operátorů a zlepšuje uživatelský zážitek. Integruje se s různými podsystémy 3GPP: účtovací systém (např. 32.295 pro záznamy o účtovaných datech) sleduje využití pro fakturaci; rámec politik (např. [PCRF](/mobilnisite/slovnik/pcrf/)) může aplikovat specifickou QoS; a bezpečnostní rámec zajišťuje ochranu soukromí dat. Specifikace jako 29.163 pokrývají spolupráci s jinými sítěmi (např. služby založené na SIP), zatímco 36.171 a 38.171 zahrnují požadavky na výkon pro doručování přes LTE a NR rádiové rozhraní. Tato rozsáhlá standardizace zajišťuje, že informační služby mohou být konzistentně nasazeny napříč různými operátory a technologiemi, od 2G po 5G, a podporují vývoj směrem k pokročilým komunikačním službám (RCS) a doručování IoT dat.

## K čemu slouží

Účelem standardizace informační služby (IS) v 3GPP je poskytnout jednotný rámec pro doručování služeb založených na obsahu přes mobilní sítě, který zajistí interoperabilitu, možnost řízení a zpeněžení. Před takovou standardizací byly informační služby často proprietární, což vedlo k fragmentaci, kdy služby fungovaly pouze na konkrétních sítích nebo zařízeních. To omezovalo škálovatelnost a zvyšovalo náklady pro operátory a poskytovatele obsahu. Definováním IS napříč specifikacemi jako 32.101 (Principy telekomunikačního řízení) se 3GPP těmto problémům věnuje stanovením společných architektur, řídicích postupů a účtovacích mechanismů, což umožňuje bezproblémové nasazení služeb a roaming.

Historicky se první mobilní informační služby, jako upozornění přes SMS nebo portály WAP, objevily v sítích 2G, ale postrádaly komplexní standardy řízení. Zavedení IS v Release 8 spolu s růstem paketově přepínaných dat v 3G/4G bylo motivováno potřebou podporovat složitější služby, jako je multimediální zpráva, služby založené na poloze a obsah mobilního internetu. Tento vývoj řešil omezení ad-hoc implementací poskytnutím standardizovaných rozhraní pro zřizování služeb, monitorování kvality a účtování, což je klíčové pro kontrolu operátora a jistotu příjmů. Rámec také podporuje regulatorní požadavky, jako jsou nouzová upozornění nebo systémy veřejného varování, definováním spolehlivých mechanismů doručování.

Motivace pro standardizaci IS vychází z obchodní potřeby vytvořit ekosystém, kde mohou operátoři, poskytovatelé obsahu a uživatelé efektivně interagovat. Řeší problémy jako nekonzistentní kvalita služeb, složitá integrace fakturace a nedostatek přehledu o řízení. Tím, že IS zahrnuje široké spektrum specifikací – od síťového řízení (řada 32) po servisní architekturu (řada 28) – umožňuje operátorům nabízet rozmanité informační služby při zachování výkonu a bezpečnosti sítě. Toto otevřelo cestu pokročilým službám v 5G, jako je hromadné rozesílání IoT dat a doručování informací založené na edge computingu, a zajišťuje zpětnou kompatibilitu a budoucí rozšiřitelnost.

## Klíčové vlastnosti

- Rámec pro služby doručování obsahu (např. zprávy, počasí, upozornění založená na poloze)
- Definováno napříč specifikacemi pro řízení (řada 32) a služby (řada 28)
- Podporuje jak push, tak modely služeb typu žádost-odpověď
- Integruje se s účtovacími systémy (OCS/OFCS) pro fakturaci a účtování
- Zahrnuje možnosti monitorování výkonu a správy poruch
- Umožňuje interoperabilitu napříč operátory a zařízeními pro konzistentní uživatelský zážitek

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 25.172** (Rel-19) — A-GANSS UE Minimum Performance Requirements (FDD)
- **TS 25.766** (Rel-13) — Network-Assisted Interference Cancellation for UMTS
- **TS 28.518** (Rel-19) — Fault Management for Virtualized Networks Stage 3
- **TS 28.536** (Rel-19) — Management services for communication service assurance
- **TS 28.606** (Rel-12) — CN and non-3GPP interworking NRM IRP Solution Sets
- **TS 28.616** (Rel-19) — EPC and non-3GPP access NRM IRP SS definitions
- **TS 28.621** (Rel-19) — Generic Network Resource Model (NRM) IRP Requirements
- **TS 28.624** (Rel-19) — State Management Data Definition IRP Requirements
- **TS 28.625** (Rel-19) — State Management Data Definition IRP Information Service
- **TS 28.626** (Rel-19) — State Management Data Definition IRP Solution Set
- **TS 28.629** (Rel-19) — SON Policy NRM IRP Solution Set Definitions
- **TS 28.633** (Rel-19) — Inventory Management NRM IRP Solution Set definitions
- **TS 28.653** (Rel-19) — UTRAN NRM IRP Solution Set Definition
- **TS 28.654** (Rel-19) — GERAN NRM IRP Requirements
- … a dalších 173 specifikací

---

📖 **Anglický originál a plná specifikace:** [IS na 3GPP Explorer](https://3gpp-explorer.com/glossary/is/)
