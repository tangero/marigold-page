---
slug: "tscai"
url: "/mobilnisite/slovnik/tscai/"
type: "slovnik"
title: "TSCAI – Time Sensitive Communication Assistance Information"
date: 2026-01-01
abbr: "TSCAI"
fullName: "Time Sensitive Communication Assistance Information"
category: "Services"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/tscai/"
summary: "Time Sensitive Communication Assistance Information (TSCAI) jsou metadata poskytovaná aplikací 5G síti o jejích časově kritických přenosových vzorcích. Informují RAN a core network o očekávaných časec"
---

TSCAI jsou metadata, která aplikace poskytuje 5G síti o svých časově kritických přenosových vzorcích, což síti umožňuje proaktivně plánovat prostředky pro splnění přísných požadavků na latenci a spolehlivost.

## Popis

Time Sensitive Communication Assistance Information (TSCAI) je klíčový prvek pro deterministickou komunikaci v 5G sítích, specifikovaný v rámci architektury 5G System v TS 23.501 a souvisejících specifikacích signalizační roviny (např. TS 29.512, 29.513). Nejde o uživatelská data, ale o řídicí informace popisující časové charakteristiky nadcházejícího datového toku Time Sensitive Communication ([TSC](/mobilnisite/slovnik/tsc/)). Primárním účelem TSCAI je překlenout propast ve znalostech mezi aplikací, která zná svůj vlastní vzor generování provozu, a sítí, která řídí přenosové prostředky.

Architektonicky je TSCAI generováno Application Function ([AF](/mobilnisite/slovnik/af/)) spojenou s časově citlivou aplikací, jako je výrobní řídicí systém nebo robotický kontrolér. Toto AF komunikuje s Network Exposure Function ([NEF](/mobilnisite/slovnik/nef/)) 5G Core Network nebo přímo s Policy Control Function ([PCF](/mobilnisite/slovnik/pcf/)) přes rozhraní N5/N7. PCF následně tuto informaci začlení do pravidel [PCC](/mobilnisite/slovnik/pcc/) (Policy and Charging Control), která jsou poskytnuta Session Management Function ([SMF](/mobilnisite/slovnik/smf/)). SMF je zodpovědná za nastavení příslušných QoS Flow pro [PDU](/mobilnisite/slovnik/pdu/) Session a, což je klíčové, za předání relevantního TSCAI do (R)[AN](/mobilnisite/slovnik/an/) přes Access and Mobility Management Function (AMF) během procedur zřizování nebo modifikace PDU Session.

Princip fungování je prediktivní a proaktivní. Typický kontejner TSCAI obsahuje parametry jako 'Periodicita' kritických paketů (např. každé 2 ms), 'Čas příchodu burstu' (očekávaný čas prvního paketu v burstu vzhledem k časovému referenčnímu bodu) a 'Rozpočet zpoždění paketu' pro každý paket. Po přijetí těchto informací může uzel (R)AN (gNB) provádět "time-aware plánování". Místo reakce na pakety při jejich příchodu do své fronty – což zavádí nepředvídatelné zpoždění ve frontě – může plánovač předem alokovat uplink granty nebo downlink prostředky v přesném rádiovém rámci/podrámci, který odpovídá očekávanému příchodu paketu. Tím je zajištěn přenos paketu s minimální dobou čekání. Pro downlink může být UPF instruováno, aby předávalo pakety do RAN právě včas pro jejich naplánovaný přenosový slot.

Role TSCAI spočívá v přeměně sítě z reaktivní na prediktivní pro kritický provoz. Umožňuje 5G systému splnit extrémní limity latence a jitteru vyžadované průmyslovými řídicími smyčkami. Bez TSCAI pracuje plánovač RAN naslepo, což vede k potenciálnímu nedodržení termínů kvůli konkurenci s jiným provozem. S TSCAI může síť rezervovat "deterministický pruh" ve sdíleném rádiovém spektru pro každý kritický paket, čímž se bezdrátové chování podobá časově řízené kabelové síti.

## K čemu slouží

TSCAI bylo vytvořeno k řešení zásadní výzvy při podpoře Time Sensitive Communications (TSC) přes sdílenou paketovou síť se statistickým multiplexováním, jako je 5G. I s pokročilými rádiovými funkcemi pro URLLC nemůže síťový plánovač optimálně upřednostňovat provoz, pokud neví, *kdy* kritické pakety přijdou. Bez této předzvěsti mohou být pakety zařazeny do fronty za jiným provozem, čímž se poruší přísné limity latence. Předchozí přístupy v mobilních sítích se spoléhaly čistě na identifikátory třídy QoS (QCIs) a úrovně priority, které jsou reaktivní a nedostatečné pro časovou přesnost na úrovni mikrosekund.

Konkrétním problémem, který TSCAI řeší, je nepředvídatelnost časů příchodu paketů z pohledu sítě. V průmyslové automatizaci mnoho řídicích aplikací generuje provoz v dokonale periodickém, předvídatelném vzoru (např. odečet senzoru každý řídicí cyklus). TSCAI umožňuje aplikaci komunikovat tento známý vzor síťové infrastruktuře. To bylo motivováno potřebou, aby 5G podporovalo IEEE Time-Sensitive Networking (TSN), kde je provoz často plánován časově uvědomělým způsobem na základě známého rozvrhu. Aby se 5G mohlo integrovat jako TSN most, potřebovalo mechanismus pro přijímání takových informací o rozvrhu a jednání na jejich základě.

Jeho zavedení v 3GPP Release 16 byla přímou reakcí na požadavky vertikálních průmyslových odvětví účastnících se 3GPP. Umožňuje klíčový posun paradigmatu: učinit síť "aplikací uvědomělou" z hlediska časování. To umožňuje 5G jít nad rámec pouhého nabízení nízké průměrné latence a garantovat maximální latenci pro každý jednotlivý paket v předvídatelném proudu, což je základním kamenem spolehlivého průmyslového bezdrátového řízení.

## Klíčové vlastnosti

- Poskytuje síti prediktivní informace o vzorcích generování paketů (periodicita, čas příchodu burstu)
- Umožňuje časově uvědomělé plánování v (R)AN, což umožňuje alokaci prostředků sladěnou s příchodem paketů
- Přenášeno z Application Function do Policy Control Function a nakonec do (R)AN přes signalizaci core networku
- Integrální součást rámce 5G QoS pro deterministické toky, odkazováno při zřizování QoS Flow
- Podporuje časově citlivou komunikaci jak v uplinku, tak v downlinku
- Nezbytné pro integraci 5G System jako TSN mostu, přenáší informace o rozvrhu TSN streamu

## Související pojmy

- [TSC – Time Sensitive Communications](/mobilnisite/slovnik/tsc/)
- [URLLC – Ultra Reliable Low Latency Communication](/mobilnisite/slovnik/urllc/)

## Definující specifikace

- **TS 23.501** (Rel-20) — 5G System Architecture Stage 2
- **TS 29.122** (Rel-19) — T8 Reference Point for Northbound APIs
- **TS 29.512** (Rel-19) — 5G Session Management Policy Control Service
- **TS 29.513** (Rel-19) — 5G PCC Signalling Flows & QoS Mapping
- **TS 29.514** (Rel-19) — 5G System; Policy Authorization Service; Stage 3
- **TS 29.522** (Rel-19) — 5G NEF Northbound APIs Stage 3
- **TS 29.565** (Rel-19) — Time Synchronization Function Services

---

📖 **Anglický originál a plná specifikace:** [TSCAI na 3GPP Explorer](https://3gpp-explorer.com/glossary/tscai/)
