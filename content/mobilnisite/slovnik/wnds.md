---
slug: "wnds"
url: "/mobilnisite/slovnik/wnds/"
type: "slovnik"
title: "WNDS – WiMAX Network Discovery and Selection"
date: 2025-01-01
abbr: "WNDS"
fullName: "WiMAX Network Discovery and Selection"
category: "Mobility"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/wnds/"
summary: "WNDS je mechanismus 3GPP definovaný pro rané sítě LTE/EPC, který umožňuje uživatelskému zařízení (UE) objevovat a vybírat sítě WiMAX jako technologii přístupu mimo 3GPP. Poskytuje UE potřebné síťové i"
---

WNDS je mechanismus 3GPP pro sítě LTE/EPC, který umožňuje uživatelskému zařízení (UE) objevovat a vybírat sítě WiMAX tím, že poskytuje potřebné informace o síti a zásady pro připojení a předání spojení.

## Popis

WiMAX Network Discovery and Selection (WNDS) je funkce specifikovaná v 3GPP TS 24.312, která poskytuje uživatelskému zařízení (UE) informace potřebné k objevení a připojení k sítím WiMAX, které jsou standardizovány jako typ důvěryhodné přístupové sítě mimo 3GPP. Mechanismus funguje tak, že doručuje do UE z jádra Evolved Packet Core (EPC) 3GPP specifické informace pro objevování sítí ([NDI](/mobilnisite/slovnik/ndi/)) a zásady pro výběr sítě. Tyto informace jsou do UE typicky provisionovány prostřednictvím funkce Access Network Discovery and Selection Function ([ANDSF](/mobilnisite/slovnik/andsf/)), která je součástí síťové architektury EPC pro správu mezisystémové mobility a výběru přístupové sítě.

Informace WNDS zahrnují technické parametry potřebné pro identifikaci a autentizaci UE v síti WiMAX. Mezi klíčové datové prvky mohou patřit domény Network Access Identifier ([NAI](/mobilnisite/slovnik/nai/)), identifikátory sítě WiMAX (např. NAP-ID, NSP-ID), identifikátory roamingových konsorcií a informace o přidružené důvěryhodné bráně pro přístup mimo 3GPP (např. ePDG nebo [TWAG](/mobilnisite/slovnik/twag/)) pro vytvoření tunelu [IPsec](/mobilnisite/slovnik/ipsec/) nebo přímé konektivity. UE tyto informace používá k vyhledání dostupných sítí WiMAX, porovnání nalezených sítí s provisionovanými profily a určení preferované sítě pro připojení na základě zásad definovaných operátorem (např. 'připoj se k WiMAX, pokud je dostupné a jde o domovskou síť').

Z architektonického hlediska WNDS spoléhá na ANDSF, která komunikuje s UE přes referenční bod S14 (pro LTE) nebo prostřednictvím IP komunikace, když je UE připojeno přes jakýkoli IP přístup. ANDSF může poskytovat správní objekty ([MO](/mobilnisite/slovnik/mo/)) obsahující informace pro objevování a zásady mezisystémové mobility ([ISMP](/mobilnisite/slovnik/ismp/)) nebo mezisystémového směrování ([ISRP](/mobilnisite/slovnik/isrp/)). Pro WiMAX jsou v rámci frameworku ANDSF definovány specifické správní objekty pro WiMAX. Role WNDS byla obzvláště důležitá během počátečních fází nasazení LTE, kdy byla WiMAX považována za životaschopnou doplňkovou technologii širokopásmového bezdrátového přístupu pro odlehčení datového provozu nebo zachování kontinuity služeb, zejména na trzích, kde byly sítě WiMAX nasazeny. Umožnila jednotný rámec zásad pro výběr sítě v rámci architektury 3GPP EPC s více přístupy.

## K čemu slouží

WNDS byl vytvořen, aby řešil specifickou potřebu integrace sítí Worldwide Interoperability for Microwave Access (WiMAX) – založených na standardech IEEE 802.16 – do architektury jádra Evolved Packet Core (EPC) 3GPP definované kolem Release 8. V té době byla WiMAX konkurenční 4G technologie nasazená v několika regionech a v odvětví panoval zájem o umožnění dvou režimů pro zařízení LTE/WiMAX a plynulé kontinuity služeb mezi těmito heterogenními technologiemi rádiového přístupu. Problém spočíval v tom, že UE potřebovala standardizovanou metodu pro efektivní objevování dostupných sítí WiMAX a porozumění zásadám operátora, kdy je vybrat, aniž by se spoléhala pouze na ruční konfiguraci nebo nestandardní mechanismy.

Motivace vycházela z širší práce 3GPP na agnosticismu přístupové sítě v SAE/EPC, jejímž cílem byla podpora důvěryhodných a nedůvěryhodných přístupů mimo 3GPP. Zatímco byly definovány obecné mechanismy pro přístup mimo 3GPP (jako ePDG), WiMAX měla specifické síťové identifikátory a postupy ověřování, které se lišily od například generického WLAN. WNDS poskytl chybějící část: standardizovaný kontejner v rámci frameworku ANDSF pro doručení specifických parametrů pro objevování a pravidel výběru pro WiMAX do UE. Tím byl vyřešen problém, jak může UE s podporou LTE autonomně najít a připojit se k síti WiMAX v souladu s politikou operátora, což umožnilo scénáře jako odlehčení datového provozu na WiMAX nebo použití WiMAX pro rozšíření pokrytí, a tím usnadnilo konvergenci sítí 3GPP a mimo 3GPP pod společným jádrem a rámcem zásad.

## Klíčové vlastnosti

- Doručuje informace pro objevování sítí WiMAX (NDI) do UE prostřednictvím ANDSF
- Zahrnuje specifické identifikátory pro WiMAX: NAP-ID, NSP-ID, identifikátory roamingových konsorcií
- Poskytuje zásady operátora pro výběr a stanovení priority sítě WiMAX
- Používá standardizované správní objekty (MO) ANDSF přes rozhraní S14 nebo IP
- Umožňuje automatizované objevování a připojení k důvěryhodným přístupovým sítím WiMAX
- Podporuje mezisystémovou mobilitu mezi sítěmi 3GPP LTE a WiMAX

## Související pojmy

- [ANDSF – Access Network Discovery and Selection Function](/mobilnisite/slovnik/andsf/)
- [EPC – Evolved Packet Core Network](/mobilnisite/slovnik/epc/)

## Definující specifikace

- **TS 24.312** (Rel-19) — ANDSF Management Objects Specification

---

📖 **Anglický originál a plná specifikace:** [WNDS na 3GPP Explorer](https://3gpp-explorer.com/glossary/wnds/)
