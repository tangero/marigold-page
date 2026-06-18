---
slug: "ssac"
url: "/mobilnisite/slovnik/ssac/"
type: "slovnik"
title: "SSAC – Service Specific Access Control"
date: 2025-01-01
abbr: "SSAC"
fullName: "Service Specific Access Control"
category: "Services"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/ssac/"
summary: "Service Specific Access Control (SSAC) je mechanismus pro řízení zahlcení sítě v LTE a 5G, který umožňuje síti omezovat pokusy o přístup ke konkrétním službám, jako jsou hlasová nebo videohovory, v ob"
---

SSAC je mechanismus pro řízení zahlcení v sítích LTE a 5G, který omezuje pokusy o přístup ke konkrétním službám, jako jsou hlasová volání, při vysokém zatížení, aby zabránil signalizačním bouřím a zajistil dostupnost služeb.

## Popis

Service Specific Access Control (SSAC) je funkce pro správu rádiových prostředků a řízení zahlcení definovaná v 3GPP pro Evolved Packet System (EPS) a 5G System (5GS). Jejím hlavním účelem je řídit pokusy o přístup z uživatelského zařízení (UE) ke konkrétním službám, když síť zažívá zahlcení, zejména v řídicí rovině. SSAC funguje tak, že síť může vysílat parametry blokování pro konkrétní služby přes rozhraní rádiového přístupu, které musí uživatelská zařízení dodržet před zahájením pokusu o přístup k dané službě.

Architektonicky je SSAC řízeno jádrem sítě, konkrétně Mobility Management Entity ([MME](/mobilnisite/slovnik/mme/)) v 4G nebo funkcí Access and Mobility Management Function ([AMF](/mobilnisite/slovnik/amf/)) v 5G. Tyto síťové funkce určují úroveň zahlcení a rozhodují o příslušných faktorech blokování. Parametry blokování jsou pak odeslány do základnové stanice ([eNB](/mobilnisite/slovnik/enb/) v LTE, gNB v NR), která je zahrne do bloků systémových informací ([SIB](/mobilnisite/slovnik/sib/)) vysílaných všem UE v buňce. Klíčové parametry zahrnují 'ssac-BarringFactor' (pravděpodobnostní hodnota mezi 0 a 1) a 'ssac-BarringTime' (dobu trvání).

Funguje na pravděpodobnostním principu. Když chce UE zahájit konkrétní službu (např. IMS hlasový hovor), nejprve si přečte příslušné parametry SSAC z vysílaných systémových informací. UE poté vygeneruje náhodné číslo mezi 0 a 1. Pokud je toto náhodné číslo nižší než vysílaný 'ssac-BarringFactor', je pokus o přístup povolen k pokračování. Pokud je vyšší, je přístup zablokován a UE musí počkat po dobu určenou parametrem 'ssac-BarringTime', než vygeneruje nové náhodné číslo pro následný pokus. Tento mechanismus se uplatňuje na úrovni služby; síť může například nastavit vysoký faktor blokování pro videohovory, zatímco přístup pro hlasové hovory ponechá relativně otevřený, nebo může blokovat všechny pokusy o signalizaci iniciovanou ze zařízení. Tím se pokusy o přístup rozloží v čase a zabrání se signalizační bouři, která by mohla při hromadné události nebo výpadku sítě způsobit pád MME nebo AMF.

## K čemu slouží

SSAC bylo vytvořeno k řešení problému přetížení řídicí roviny v paketových sítích, jako jsou LTE a 5G, což byla nová výzva ve srovnání se sítěmi s přepojováním okruhů. V [CS](/mobilnisite/slovnik/cs/) sítích zahlcení primárně ovlivňovalo prostředky přenosu (trunky), ale v plně IP sítích mohla náhlá vlna signalizačních požadavků (např. miliony zařízení současně se snažících o opětovnou registraci nebo uskutečnění VoLTE hovorů po výpadku) přetížit řídicí uzly jádra sítě ([MME](/mobilnisite/slovnik/mme/)/[AMF](/mobilnisite/slovnik/amf/)). Účelem SSAC je poskytnout standardizovanou, na služby citlivou metodu pro omezení této signalizační zátěže.

Řeší kritický problém odolnosti sítě během mimořádných událostí, katastrof nebo oblíbených akcí, kdy se mnoho uživatelů současně pokouší používat služby. Bez SSAC by taková signalizační bouře mohla vést k úplnému selhání jádra sítě a odepření služby všem uživatelům. SSAC umožňuje síti elegantně degradovat selektivním omezením méně kritických služeb, čímž zajišťuje, že může být zachována určitá úroveň služeb (např. tísňová volání, základní registrace). Motivací byly poznatky z prvních nasazení LTE a potřeba sofistikovaného řízení zahlcení v modelu poskytování služeb založeném na IMS, kde je klíčová diferenciace služeb. Řeší omezení hrubších mechanismů řízení přístupu, jako je Access Class Barring (ACB), tím, že poskytuje podrobnou kontrolu na úrovni služeb.

## Klíčové vlastnosti

- Parametry blokování specifické pro službu vysílané v systémových informacích (SIB)
- Pravděpodobnostní řízení přístupu pomocí faktoru blokování a generování náhodného čísla v UE
- Nezávislá kontrola pro různé služby (např. hlas, video, signalizace)
- Řízeno jádrem sítě (MME/AMF), prováděno rádiovou přístupovou sítí
- Zabraňuje přetížení signalizace řídicí roviny a selhání uzlů jádra sítě
- Umožňuje elegantní degradaci služeb při zahlcení sítě nebo v katastrofických scénářích

## Související pojmy

- [MME – NPC MME Network Product Class](/mobilnisite/slovnik/mme/)
- [IMS – IP Multimedia Subsystem](/mobilnisite/slovnik/ims/)

## Definující specifikace

- **TS 22.011** (Rel-19) — Service Accessibility Procedures
- **TS 22.806** (Rel-13) — Application Specific Congestion Control for Data
- **TS 36.306** (Rel-19) — E-UTRA UE Radio Access Capability Parameters
- **TS 36.331** (Rel-19) — LTE RRC Protocol Specification
- **TS 36.848** (Rel-12) — Study on Smart Congestion Mitigation in E-UTRAN

---

📖 **Anglický originál a plná specifikace:** [SSAC na 3GPP Explorer](https://3gpp-explorer.com/glossary/ssac/)
