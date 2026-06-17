---
slug: "gvns"
url: "/mobilnisite/slovnik/gvns/"
type: "slovnik"
title: "GVNS – Global Virtual Network Service"
date: 2025-01-01
abbr: "GVNS"
fullName: "Global Virtual Network Service"
category: "Services"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/gvns/"
summary: "Servisní rámec umožňující bezproblémové globální roamování a kontinuitu služeb napříč 3GPP a ne-3GPP přístupovými sítěmi. Poskytuje jednotný servisní zážitek pro uživatele tím, že abstrahuje síťové sl"
---

GVNS je servisní rámec, který umožňuje bezproblémové globální roamování a kontinuitu služeb napříč různými přístupovými sítěmi tím, že abstrahuje síťové složitosti, aby zajistil jednotný uživatelský zážitek.

## Popis

Global Virtual Network Service (GVNS) je komplexní servisní architektura definovaná v dokumentu 3GPP TS 29.163. Funguje jako rámec na servisní vrstvě navržený k usnadnění globálního poskytování služeb vytvořením virtualizovaného, konzistentního síťového prostředí pro účastníky. Architektura je postavena na IP Multimedia Subsystem (IMS) a využívá stávající funkce jádra sítě, ale zavádí smlouvy o úrovni služeb (SLA) a politiky, které jsou centrálně spravovány, aby poskytly jednotný uživatelský zážitek. V podstatě vytváří 'virtuální domovskou síť' pro roamující uživatele, která maskuje specifické konfigurace a možnosti podkladové navštívené sítě.

V jádru GVNS funguje tak, že stanovuje sadu standardizovaných servisních profilů a politik, které jsou rozpoznávány a vynucovány napříč účastnícími se sítěmi operátorů. Když uživatel roamuje, jeho servisní požadavky jsou zachyceny a zpracovány podle jeho profilu GVNS, který je načten z jeho domovské sítě. To zahrnuje koordinaci funkcí Policy and Charging Control (PCC), aplikačních funkcí a potenciálně funkcí pro vystavení servisních schopností. Zdroje navštívené sítě jsou přiděleny a nakonfigurovány tak, aby splňovaly záruky SLA definované v uživatelském předplatném GVNS, jako je minimální šířka pásma, latence nebo přístup ke specifickým službám založeným na IMS, jako je VoLTE.

Klíčové komponenty v architektuře GVNS zahrnují GVNS Application Server, který hostuje servisní logiku a uživatelské profily, a interakci s architekturou PCC (PCRF a PCEF) pro dynamické vynucování politik. Rozhraní má také s účtovacími systémy, aby zajistilo přesné účtování za rozšířené roamové služby. Protokol specifikovaný v TS 29.163 definuje zprávy a procedury mezi entitami obsluhující sítě a platformou GVNS v domovské síti. Jeho rolí je oddělit poskytování služeb od fyzické topologie sítě, což operátorům umožňuje nabízet prémiové, předvídatelné roamové zážitky a podporovat globální interoperabilitu služeb nad rámec základní konektivity.

## K čemu slouží

GVNS byl vytvořen, aby řešil problémy s nekonzistentní a často sníženou kvalitou služeb, kterou uživatelé zažívají při mezinárodním roamingu. Před jeho zavedením byly roamové služby z velké části omezeny na základní hlasovou a datovou konektivitu, přičemž pokročilé služby jako hlas ve vysoké kvalitě (VoLTE), videohovory nebo garantované datové rychlosti byly na navštívených sítích často nedostupné nebo se chovaly nepředvídatelně. Servisní zážitek závisel na bilaterálních dohodách a specifických možnostech navštívené sítě, což vedlo k roztříštěnému uživatelskému zážitku.

Hlavní problém, který GVNS řeší, je nedostatek kontinuity služeb a záruky kvality pro roamující účastníky. Umožňuje operátorům nabízet služby v různých úrovních, které garantují určité výkonnostní parametry (např. 'business class' datový roaming) bez ohledu na polohu účastníka. To bylo motivováno rostoucí poptávkou po bezproblémových zážitcích z mobilního širokopásmového připojení a komerční potřebou operátorů diferencovat své nabídky a vytvářet nové zdroje příjmů z roamingu. Virtualizací servisní vrstvy GVNS umožňuje 'domácí' zážitek v zahraničí, což byl významný krok nad rámec starších roamových rámců, které primárně řešily autentizaci a základní směrování hovorů.

## Klíčové vlastnosti

- Globální kontinuita služeb pro služby založené na IMS
- Standardizované servisní profily a SLA pro roaming
- Integrace s Policy and Charging Control (PCC) pro dynamický správu zdrojů
- Podpora pro 3GPP i ne-3GPP přístupové sítě
- Centralizovaná správa servisní logiky a uživatelských profilů
- Rozšířené účtovací mechanismy pro roamové služby s přidanou hodnotou

## Související pojmy

- [IMS – IP Multimedia Subsystem](/mobilnisite/slovnik/ims/)

## Definující specifikace

- **TS 29.163** (Rel-19) — Interworking between 3GPP IM CN and CS networks

---

📖 **Anglický originál a plná specifikace:** [GVNS na 3GPP Explorer](https://3gpp-explorer.com/glossary/gvns/)
