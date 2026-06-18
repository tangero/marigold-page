---
slug: "lma"
url: "/mobilnisite/slovnik/lma/"
type: "slovnik"
title: "LMA – Local Mobility Anchor"
date: 2025-01-01
abbr: "LMA"
fullName: "Local Mobility Anchor"
category: "Core Network"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/lma/"
summary: "Local Mobility Anchor (LMA) je funkce základní sítě v Evolved Packet Core (EPC) definovaná pro architektury založené na Proxy Mobile IPv6 (PMIPv6). Slouží jako topologický kotvící bod pro IP adresu(y)"
---

LMA je funkce základní sítě v EPC, která slouží jako topologický kotvící bod pro IP adresu UE a spravuje mobilitu v rámci důvěryhodné ne-3GPP přístupové sítě, jako je Wi-Fi.

## Popis

Local Mobility Anchor (LMA) je klíčová síťová entita specifikovaná v rámci architektury 3GPP pro propojení s ne-3GPP přístupem, primárně definovaná v kontextu Proxy Mobile IPv6 (PMIPv6). Nachází se v základní síti domácího operátora (EPC) a slouží jako topologický kotvící bod pro IP relaci(e) uživatelského zařízení (UE). Když se UE připojí prostřednictvím důvěryhodné ne-3GPP přístupové sítě, jako je Wi-Fi síť spravovaná operátorem, LMA přiřadí UE jeden nebo více Home Network Prefixů ([HNP](/mobilnisite/slovnik/hnp/)). UE si z těchto prefixů nakonfiguruje svou IP adresu(y), která zůstává konstantní bez ohledu na její bod připojení v rámci domény PMIPv6. To poskytuje UE plynulou kontinuitu IP relace, což je forma síťové mobility, kde se samotné UE nemusí účastnit signalizace mobility.

LMA spolupracuje s Mobility Access Gateway ([MAG](/mobilnisite/slovnik/mag/)), což je funkce v přístupové síti (např. v rámci evolved Packet Data Gateway (ePDG) nebo Trusted [WLAN](/mobilnisite/slovnik/wlan/) Access Gateway ([TWAG](/mobilnisite/slovnik/twag/))), která detekuje připojení a pohyb UE. MAG funguje jako proxy a provádí signalizaci mobility jménem UE. Při počátečním připojení odešle MAG zprávu Proxy Binding Update ([PBU](/mobilnisite/slovnik/pbu/)) LMA. LMA poté vytvoří Binding Cache Entry ([BCE](/mobilnisite/slovnik/bce/)), které sváže přiřazený HNP(y) UE a její network access identifier ([NAI](/mobilnisite/slovnik/nai/)) s care-of adresou reprezentovanou MAG Proxy Care-of Address (Proxy-CoA). Všechny IP pakety určené pro UE jsou směrovány na LMA, které je následně tuneluje (pomocí IP-in-IP, [GRE](/mobilnisite/slovnik/gre/) nebo PMIPv6 tunelování) k aktuálnímu MAG na základě BCE. Provoz z UE je podobně tunelován z MAG na LMA, které pak de-encapsuluje a směruje směrem k externí paketové datové síti (PDN).

Mezi klíčové architektonické role LMA patří být koncovým bodem IP tunelu s MAG, správa BCE pro všechna připojená UE a rozhraní k PCRF (Policy and Charging Rules Function) pro vynucování politik přes rozhraní Gx. Hraje také roli při alokaci IPv4 adres, pokud UE používá IPv4. Centralizovaná kotvící funkce LMA zjednodušuje mobilitu pro UE, ale centralizuje provoz, což může vést k suboptimálnímu směrování (tromboning). Aby se tento problém vyřešil, byly studovány pozdější vylepšení, jako je přesun LMA a selektivní odlehčení provozu. LMA je klíčovým prvkem referenčních bodů S2a a S2b pro důvěryhodný a nedůvěryhodný ne-3GPP přístup, což umožňuje těsnou integraci Wi-Fi do mobilní základní sítě.

## K čemu slouží

LMA bylo vytvořeno, aby umožnilo plynulé, síťové řízení mobility pro UE připojující se prostřednictvím ne-3GPP IP přístupových sítí, především Wi-Fi, do 3GPP Evolved Packet Core (EPC). Před jeho standardizací byla mobilita mezi 3GPP a ne-3GPP přístupy často typu break-before-make, což vyžadovalo, aby UE získalo novou IP adresu a přerušilo probíhající IP relace. Problémem bylo, jak zajistit kontinuitu IP relací a konzistentní vynucování politik napříč heterogenními přístupovými technologiemi bez nutnosti změn v IP zásobníku UE.

Proxy Mobile IPv6 (PMIPv6), a tím i LMA, bylo přijato 3GPP k řešení tohoto problému. Poskytuje síťové řešení, kde síťové entity (MAG a LMA) zpracovávají veškerou signalizaci mobility, čímž je mobilita pro UE transparentní. To je zvláště výhodné pro starší zařízení a pro zjednodušení implementace UE. LMA slouží jako stabilní kotvící bod v síti operátora, což zajišťuje, že IP adresa UE zůstává nezměněna, což je klíčové pro mnoho aplikací a bezpečnostních asociací. Jeho vytvoření v Rel-8 bylo součástí širšího úsilí System Architecture Evolution (SAE) o definici jednotné, IP-based základní sítě (EPC), která by mohla integrovat množství přístupových technologií mimo 3GPP rádio, čímž naplnila vizi 'access agnostic' základních služeb.

## Klíčové vlastnosti

- Slouží jako topologický kotvící bod a home agent pro IP prefix(y) UE v PMIPv6
- Udržuje Binding Cache Entries (BCE) mapující identitu UE na aktuální Mobility Access Gateway (MAG)
- Vytváří obousměrné IP tunely (např. GRE, PMIPv6) s MAG pro přenos uživatelského provozu
- Přiřazuje UE Home Network Prefixy (HNP) pro konfiguraci IP adres
- Komunikuje s PCRF přes Gx pro dynamické řízení politik a účtování
- Podporuje mobilitu pro alokaci IPv6 i IPv4 adres (pomocí IPv4 Home Address nebo DHCPv4)

## Související pojmy

- [EPDG – Evolved Packet Data Gateway](/mobilnisite/slovnik/epdg/)

## Definující specifikace

- **TS 23.380** (Rel-19) — IMS Restoration Procedures
- **TS 23.402** (Rel-19) — EPC for Non-3GPP Access (PMIP)
- **TS 29.273** (Rel-19) — AAA Protocols for Non-3GPP Access in EPS & 5GS NSWO
- **TS 29.275** (Rel-19) — PMIPv6 Mobility & Tunnelling Protocols Stage 3
- **TS 29.826** (Rel-13) — P-CSCF Restoration Enhancements for WLAN
- **TS 33.402** (Rel-19) — Security for non-3GPP access to EPS

---

📖 **Anglický originál a plná specifikace:** [LMA na 3GPP Explorer](https://3gpp-explorer.com/glossary/lma/)
