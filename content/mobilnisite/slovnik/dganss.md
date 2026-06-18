---
slug: "dganss"
url: "/mobilnisite/slovnik/dganss/"
type: "slovnik"
title: "DGANSS – Differential Global Navigation Satellite System"
date: 2025-01-01
abbr: "DGANSS"
fullName: "Differential Global Navigation Satellite System"
category: "Services"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/dganss/"
summary: "DGANSS je lokalizační služba 3GPP, která poskytuje diferenciální korekce přijímačům GNSS prostřednictvím mobilních sítí. Zvyšuje přesnost určení polohy kompenzací atmosférických chyb a chyb satelitníc"
---

DGANSS je lokalizační služba 3GPP, která zvyšuje přesnost polohy z GNSS tím, že prostřednictvím mobilních sítí doručuje diferenciální korekce pro kompenzaci atmosférických chyb a chyb satelitních drah.

## Popis

DGANSS je síťově asistovaná lokalizační technologie standardizovaná v 3GPP, která doručuje data diferenciálních korekcí mobilním zařízením za účelem zvýšení přesnosti měření Globálního navigačního satelitního systému ([GNSS](/mobilnisite/slovnik/gnss/)). Systém funguje tak, že referenční stanice na přesně známých polohách kontinuálně monitorují signály GNSS z více satelitních konstelací ([GPS](/mobilnisite/slovnik/gps/), [GLONASS](/mobilnisite/slovnik/glonass/), Galileo, BeiDou). Tyto referenční stanice vypočítávají rozdíly mezi změřenými satelitními polohami a jejich známými teoretickými polohami a generují korekční data, která zohledňují různé zdroje chyb včetně ionosférického a troposférického zpoždění, chyb satelitních hodin a nepřesností efemerid.

Architektura zahrnuje několik klíčových komponent: Lokalizační měřicí jednotky ([LMU](/mobilnisite/slovnik/lmu/)) neboli DGANSS referenční stanice, které sbírají nezpracovaná GNSS měření; DGANSS server, který tato měření zpracovává za účelem generování diferenciálních korekcí; a infrastrukturu mobilní sítě, která tyto korekce doručuje uživatelskému zařízení (UE). Korekce jsou přenášeny přes standardizovaná rozhraní mezi síťovými elementy, typicky za použití protokolů definovaných ve specifikacích 3GPP. UE přijímá jak nezpracované signály satelitů GNSS, tak diferenciální korekce prostřednictvím mobilní sítě, a následně tyto korekce aplikuje na své výpočty polohy, čímž dosahuje výrazně zvýšené přesnosti.

Diferenciální korekce mohou být doručovány v různých formátech v závislosti na implementaci a požadavcích. Korekce pro reálnou kinematiku ([RTK](/mobilnisite/slovnik/rtk/)) poskytují přesnost na úrovni centimetrů pro specializované aplikace, zatímco standardní diferenciální korekce typicky dosahují přesnosti na úrovni pod metr až několik metrů. Systém podporuje různé metody doručování včetně point-to-point spojení pro jednotlivá UE a broadcastových metod, kde jsou korekce vysílány více zařízením současně. DGANSS se integruje s existujícími lokalizačními architekturami 3GPP a spolupracuje s dalšími lokalizačními metodami, jako je [OTDOA](/mobilnisite/slovnik/otdoa/) a Assisted GNSS ([A-GNSS](/mobilnisite/slovnik/a-gnss/)), aby poskytovala komplexní lokalizační služby.

Během provozu DGANSS server kontinuálně počítá korekční parametry na základě vstupů z více referenčních stanic, aby zajistil pokrytí a spolehlivost. Tyto korekce jsou následně formátovány podle standardizovaných strukturovaných zpráv (jako je RTCM SC-104 nebo proprietární formáty) a doručovány prostřednictvím řídicí nebo uživatelské roviny mobilní sítě. Polohovací engine v UE kombinuje satelitní měření s přijatými korekcemi pomocí algoritmů, které typicky zahrnují techniky vážených nejmenších čtverců nebo Kalmanova filtru, aby vypočítal finální polohu. Tento hybridní přístup využívá jak satelitní signály, tak pozemní síťovou infrastrukturu k překonání omezení samostatného GNSS, zejména v náročných prostředích, jako jsou městské kaňony nebo vnitřní prostory, kde je viditelnost satelitů omezená.

## K čemu slouží

DGANSS byl vyvinut k řešení omezení přesnosti konvenčního [GNSS](/mobilnisite/slovnik/gnss/) určování polohy, které za ideálních podmínek typicky poskytuje přesnost 5-10 metrů, ale výrazně se zhoršuje vlivem atmosférických jevů, chyb satelitních hodin a mnohacestného šíření. Tato omezení byla obzvláště problematická pro aplikace vyžadující přesné informace o poloze, jako jsou záchranné služby (E911/E112), navigace autonomních vozidel, precizní zemědělství a mapování. Diferenciální přístup byl úspěšně používán ve specializovaných pozemních systémech, ale vyžadoval dedikovanou infrastrukturu; jeho integrace s mobilními sítěmi učinila vysoce přesné určování polohy široce dostupným.

Před DGANSS mobilní sítě primárně nabízely síťově založené lokalizační metody jako Cell-ID a OTDOA, nebo Assisted GNSS (A-GNSS), které pomáhaly s rychlejším zachycením signálu, ale významně nezvyšovaly přesnost. Samostatné diferenciální GNSS systémy existovaly, ale vyžadovaly samostatné přijímače a služby předplatného, což omezovalo jejich rozšíření. DGANSS využil existující mobilní infrastrukturu k efektivnímu doručování korekcí a vytvořil standardizovaný přístup, který mohl být implementován různými síťovými operátory a výrobci zařízení. Tato integrace byla obzvláště důležitá, protože služby založené na poloze se staly náročnějšími a regulační požadavky na lokalizaci nouzových volajících přísnějšími.

Vytvoření DGANSS bylo motivováno rostoucí potřebou spolehlivého, vysoce přesného určování polohy, které by mohlo fungovat v různých prostředích bez nutnosti dodatečného uživatelského vybavení. Využitím broadcastových schopností mobilní sítě nebo vyhrazených datových kanálů učinil DGANSS přesnost na úrovni centimetrů až metrů proveditelnou pro zařízení masového trhu. To umožnilo nové aplikace a služby a zároveň vylepšilo ty stávající, čímž vytvořilo obchodní příležitosti pro síťové operátory a zvýšilo bezpečnost veřejnosti prostřednictvím přesnějších lokalizačních schopností pro nouzové případy.

## Klíčové vlastnosti

- Poskytuje diferenciální korekce pro více konstelací GNSS (GPS, GLONASS, Galileo, BeiDou)
- Doručuje korekce prostřednictvím řídicí nebo uživatelské roviny mobilní sítě
- Podporuje jak reálnou kinematiku (RTK), tak standardní diferenciální určování polohy
- Integruje se s existující lokalizační architekturou a protokoly 3GPP
- Umožňuje přesnost na úrovni centimetrů až metrů v závislosti na implementaci
- Využívá síť referenčních stanic pro výpočet korekcí

## Související pojmy

- [A-GNSS – Assisted Global Navigation Satellite Systems](/mobilnisite/slovnik/a-gnss/)
- [OTDOA – Observed Time Difference Of Arrival](/mobilnisite/slovnik/otdoa/)
- [SUPL – Secure User Plane for Location](/mobilnisite/slovnik/supl/)

## Definující specifikace

- **TS 25.331** (Rel-19) — UTRAN RRC Protocol Specification
- **TS 25.423** (Rel-19) — UTRAN RNSAP Specification
- **TS 25.433** (Rel-19) — Node B Application Part (NBAP) Protocol
- **TS 25.453** (Rel-19) — PCAP Protocol Specification

---

📖 **Anglický originál a plná specifikace:** [DGANSS na 3GPP Explorer](https://3gpp-explorer.com/glossary/dganss/)
