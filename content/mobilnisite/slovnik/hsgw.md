---
slug: "hsgw"
url: "/mobilnisite/slovnik/hsgw/"
type: "slovnik"
title: "HSGW – HRPD Serving Gateway"
date: 2025-01-01
abbr: "HSGW"
fullName: "HRPD Serving Gateway"
category: "Core Network"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/hsgw/"
summary: "HSGW je brána jádra sítě v architektuře 3GPP EPS pro vzájemnou spolupráci se sítěmi 3GPP2 CDMA2000 HRPD. Slouží jako kotvicí bod pro mobilitu a zajišťuje konektivitu mezi přístupovou sítí eHRPD a brán"
---

HSGW je brána v síti 3GPP, která zajišťuje vzájemnou spolupráci (interworking), kotvení mobility a konektivitu mezi přístupovou sítí eHRPD a bránou paketové datové sítě (Packet Data Network Gateway).

## Popis

[HRPD](/mobilnisite/slovnik/hrpd/) Serving Gateway (HSGW) je klíčová funkční entita definovaná v architektuře Evolved Packet Core (EPC) standardu 3GPP, která umožňuje plynulou mobilitu a kontinuitu služeb mezi sítěmi 3GPP LTE a sítěmi 3GPP2 CDMA2000 High Rate Packet Data (HRPD). Toto řešení vzájemné spolupráce je standardizováno pod označením evolved High Rate Packet Data (eHRPD). HSGW se nachází v EPC a slouží jako brána mezi přístupovou rádiovou sítí (RAN) eHRPD a jádrovou bránou Packet Data Network Gateway ([PGW](/mobilnisite/slovnik/pgw/)). Jejím hlavním úkolem je napodobovat chování Serving Gateway ([SGW](/mobilnisite/slovnik/sgw/)) a do určité míry i Mobility Management Entity ([MME](/mobilnisite/slovnik/mme/)) z pohledu HRPD přístupu, což jí umožňuje připojit se ke společným kotvicím bodům EPC.

Z architektonického hlediska HSGW rozhraní s několika síťovými prvky. Na straně přístupu se připojuje k HRPD Radio Network Controller ([RNC](/mobilnisite/slovnik/rnc/)) nebo ekvivalentu eNodeB přes referenční bod [S101](/mobilnisite/slovnik/s101/) pro řídicí signalizaci a přes referenční bod [S103](/mobilnisite/slovnik/s103/) pro tunelování datové roviny (user plane) pro downlink data během předávání hovoru (handover). Na straně jádra sítě se připojuje k PGW přes referenční bod S2a založený na protokolu Proxy Mobile IPv6 (PMIPv6), což je standardní rozhraní pro důvěryhodné přístupy ne-3GPP. HSGW také komunikuje se serverem 3GPP [AAA](/mobilnisite/slovnik/aaa/) (přes STa) pro autentizaci, autorizaci a účtování a s Home Subscriber Server (HSS) pro získávání profilů účastníků.

HSGW plní několik klíčových funkcí. Slouží jako lokální kotvicí bod mobility pro UE připojené přes síť eHRPD, spravuje mobilní tunel (GTP nebo PMIPv6) k PGW. Účastní se procedur autentizace a vytváření relace, přičemž komunikuje s infrastrukturou AAA. Během aktivního předávání hovoru mezi LTE a eHRPD (optimalizované předávání) hraje HSGW ústřední roli v signalizaci založené na S101, usnadňuje přenos kontextu UE a buffruje downlink data. Také vynucuje zásady kvality služeb (QoS) přijaté od funkce Policy and Charging Rules Function (PCRF) přes PGW pro relace zřízené přes eHRPD.

Z pohledu protokolů HSGW implementuje PMIPv6 jako mobilní protokol směrem k PGW, na rozdíl od protokolu GTP používaného mezi SGW a PGW u nativních přístupů 3GPP. Toto návrhové rozhodnutí odpovídá správě mobility založené na IETF pro přístupy ne-3GPP v rámci EPC. HSGW také zajišťuje překlad mezi signalizací specifickou pro HRPD (např. v zprávách rozhraní A11) a signalizačními procedurami 3GPP EPC, díky čemuž se síť HRPD jeví EPC jako důvěryhodná přístupová síť ne-3GPP. Tato abstrakce je zásadní pro poskytování jednotné uživatelské zkušenosti napříč heterogenními technologiemi.

## K čemu slouží

HSGW byla vytvořena, aby vyřešila kritický tržní a technologický problém: umožnit plynulou migraci z existujících sítí 3GPP2 CDMA2000 (především HRPD/EV-DO) na sítě 3GPP LTE, zejména v regionech, jako je Severní Amerika, Japonsko a Jižní Korea, kde měli operátoři CDMA významný podíl na trhu. Bez takové funkce vzájemné spolupráce by operátoři čelili „kompletní výměně“ (forklift upgrade), která by vyžadovala úplnou a současnou náhradu rádiových i jádrových sítí pro nasazení LTE, což je ekonomicky a provozně neproveditelné.

Hlavním problémem, který HSGW řeší, je kontinuita služeb a plynulá mobilita. Umožňuje operátorovi postupně nasazovat síť LTE a zároveň využívat stávající síť HRPD pro pokrytí, zejména v počátečních fázích nasazení LTE, kdy je pokrytí omezeno na hotspoty nebo městské oblasti. Účastník s více režimovým zařízením (LTE/HRPD) se může pohybovat mezi těmito dvěma technologiemi bez přerušení probíhajících datových relací (jako je VoIP hovor nebo video stream). Tato schopnost „optimalizovaného předávání hovoru“ byla zásadní pro udržení vysoké kvality uživatelského zážitku a pro to, aby byla zařízení LTE atraktivní od prvního dne.

Historicky, před EPC a HSGW, byla vzájemná spolupráce mezi různými technologickými rodinami složitá a často zahrnovala přepojování do okruhově spínané sítě pro hlas a předávání datových relací s přerušením (break-before-make). Architektura EPC se svým přístupově agnostickým jádrem definovaným ve vydání 8 poskytla rámec. HSGW je konkrétní implementací funkce Trusted Non-3GPP Access Gateway pro eHRPD. Vyřešila omezení předchozích řešení vzájemné spolupráce se slabou vazbou (loose-coupling) tím, že poskytla těsnou integraci na úrovni jádra sítě, což umožnilo konzistenci zásad, jednotné účtování a společné služební prvky napříč oběma přístupy, což byl základní požadavek operátorů spravujících konvergentní sítě.

## Klíčové vlastnosti

- Slouží jako kotvicí bod mobility a brána pro UE připojená přes přístup eHRPD
- Podporuje protokol Proxy Mobile IPv6 (PMIPv6) na rozhraní S2a směrem k PGW
- Umožňuje optimalizované předávání hovoru (plynulou mobilitu) mezi sítěmi LTE a eHRPD s využitím rozhraní S101
- Spolupracuje se serverem 3GPP AAA pro autentizaci a autorizaci uživatelů eHRPD
- Vynucuje zásady QoS pro datové relace zřízené přes síť eHRPD
- Poskytuje datovou cestu pro uplink a downlink provoz během připojení přes eHRPD

## Související pojmy

- [PGW – PDN Gateway](/mobilnisite/slovnik/pgw/)
- [PMIP – Proxy Mobile Internet Protocol version 6](/mobilnisite/slovnik/pmip/)

## Definující specifikace

- **TS 23.203** (Rel-19) — Policy and charging control architecture
- **TS 24.302** (Rel-19) — Access to EPC via non-3GPP networks; Stage 3
- **TS 29.215** (Rel-19) — S9 Reference Point Stage 3 Specification
- **TS 29.276** (Rel-19) — EPS S101/S121/S103 Interfaces Stage 3
- **TS 32.251** (Rel-19) — PS Domain Charging Management
- **TS 32.299** (Rel-19) — Diameter Charging Applications for 3GPP

---

📖 **Anglický originál a plná specifikace:** [HSGW na 3GPP Explorer](https://3gpp-explorer.com/glossary/hsgw/)
