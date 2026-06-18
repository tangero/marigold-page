---
slug: "vas"
url: "/mobilnisite/slovnik/vas/"
type: "slovnik"
title: "VAS – Value Added Services"
date: 2025-01-01
abbr: "VAS"
fullName: "Value Added Services"
category: "Services"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/vas/"
summary: "Široká kategorie služeb v mobilních sítích, které jdou nad rámec základního hlasového a datového připojení a poskytují odběratelům přidanou hodnotu. Zahrnuje zasílání zpráv (SMS, MMS), doručování obsa"
---

VAS je široká kategorie služeb mobilní sítě nad rámec základního hlasu a dat, poskytující přidanou hodnotu, jako je zasílání zpráv, doručování obsahu a služby založené na poloze.

## Popis

Value Added Services (VAS) v 3GPP není jediná technologie, ale komplexní rámec a soubor specifikací pro umožnění, nasazení a správu rozšířených služeb. Tyto služby využívají schopnosti jádra sítě k poskytování funkcionality, která není součástí standardní telefonní služby nebo služby přenosu paketových dat. Architektura VAS je distribuovaná a zahrnuje několik specializovaných síťových uzlů, které interagují s jádrem sítě. Mezi klíčové architektonické komponenty patří samotné VAS platformy (např. [SMS](/mobilnisite/slovnik/sms/) centrum, [MMS](/mobilnisite/slovnik/mms/) centrum, server polohy, streamovací server), brány (např. [WAP](/mobilnisite/slovnik/wap/) brána, Parlay brána) a kritické podpůrné systémy, jako je účtovací systém ([OCS](/mobilnisite/slovnik/ocs/), [OFCS](/mobilnisite/slovnik/ofcs/)) a Home Location Register ([HLR](/mobilnisite/slovnik/hlr/)) nebo Home Subscriber Server ([HSS](/mobilnisite/slovnik/hss/)) pro data odběratele.

Jak VAS funguje, závisí na konkrétní službě. Pro VAS stahování obsahu je žádost uživatele z jeho koncového zařízení směrována přes paketovou datovou síť na VAS platformu (např. obsahový portál). Platforma uživatele autentizuje, často dotazem na HSS, zpracuje žádost a doručí obsah. Klíčové je, že celá transakce je sledována pro účtování. Charging Trigger Function ([CTF](/mobilnisite/slovnik/ctf/)) sítě generuje účtovací události na základě využití služby, které jsou odeslány do Online Charging System (OCS) pro předplacené nebo hybridní zákazníky nebo do Offline Charging System (OFCS) pro účtování postpaid. Pro síťově iniciovanou VAS, jako je upozornění založené na poloze, aplikační server použije standardizované rozhraní (jako OSA/Parlay nebo SCP) k dotazu sítě na polohu uživatele a poté odešle cílenou zprávu.

Úlohou rámce VAS je poskytnout standardizovanou 'infrastrukturu', která umožňuje bezpečnou, spolehlivou a účtovatelnou integraci těchto různorodých služeb do sítě mobilního operátora. Definuje protokoly, datové formáty a procedury pro vyvolání služby, ochranu soukromí odběratele, řízení kvality služby a především detailní korelaci účtování. To operátorům umožňuje vytvářet komplexní balíčky služeb a partnerství s poskytovateli obsahu třetích stran při zachování kontroly nad autentizací, politikami a výběrem příjmů.

## K čemu slouží

Koncept VAS existuje pro zpeněžení mobilní sítě nad rámec jednoduché konektivity. Hlavním účelem je generovat dodatečný průměrný příjem na uživatele (ARPU) nabídkou služeb, které zákazníci vnímají jako hodnotná vylepšení. Z technického hlediska byly specifikace 3GPP VAS vytvořeny k řešení problémů chaosu a nekompatibility. V počátcích výrobci a operátoři vyvíjeli proprietární platformy, což vedlo k závislosti na dodavateli, nemožnosti kombinovat služby od různých poskytovatelů a složitým integračním výzvám. Standardizace byla motivována potřebou interoperability, škálovatelnosti a usnadnění globálního ekosystému poskytovatelů aplikací a obsahu.

Řešila klíčová omezení ad-hoc nasazení služeb: nedostatek standardizovaných účtovacích mechanismů ztěžoval fakturaci; absence společných rozhraní pro data odběratele bránila personalizaci; a absence jednotných rámců pro správu služeb zvyšovala provozní náklady. Architektura 3GPP VAS, zejména jak se vyvíjela s IP Multimedia Subsystem (IMS), poskytla strukturovaný způsob zavádění nových služeb. Oddělila vrstvu služeb od transportní vrstvy, což umožnilo vyvíjet služby nezávisle na podkladové přístupové technologii (GSM, UMTS, LTE). Tento rámec umožnil explozivní růst mobilního zasílání zpráv, mobilního internetu, obchodů s aplikacemi a nesčetných dalších služeb tím, že poskytl spolehlivou, účtovatelnou a spravovatelnou platformu, na které lze stavět.

## Klíčové vlastnosti

- Rámec pro tvorbu, nasazení a správu životního cyklu služeb
- Standardizovaná rozhraní pro přístup poskytovatelů služeb třetích stran (např. OSA/Parlay)
- Integrované, detailní účtovací mechanismy pro využití služby (např. Diameter Ro/Rf)
- Spoléhání se na data odběratele a autentizaci z jádra sítě (HLR/HSS)
- Podpora různorodých typů služeb: zasílání zpráv, obsah, poloha, přítomnost
- Oddělení aplikační logiky služeb od transportních/připojovacích vrstev

## Související pojmy

- [IMS – IP Multimedia Subsystem](/mobilnisite/slovnik/ims/)
- [OCS – Originating Call Screening](/mobilnisite/slovnik/ocs/)
- [MMS – Multimedia Messaging Service](/mobilnisite/slovnik/mms/)
- [SCP – Service Communication Proxy](/mobilnisite/slovnik/scp/)
- [CAMEL – Customised Applications for Mobile network Enhanced Logic](/mobilnisite/slovnik/camel/)

## Definující specifikace

- **TS 23.140** (Rel-6) — MMS Non-Realtime Service Definition
- **TS 32.240** (Rel-19) — Charging Management Architecture & Principles
- **TS 32.250** (Rel-19) — Circuit Switched Offline Charging
- **TS 32.270** (Rel-19) — MMS Charging Management Specification
- **TS 32.272** (Rel-19) — Charging for Push-to-Talk over Cellular (PoC)
- **TS 32.273** (Rel-19) — MBMS Charging Management
- **TS 32.293** (Rel-19) — Proxy Function in Domestic Service Provider
- **TS 32.808** (Rel-8) — Common User Profile Storage Framework

---

📖 **Anglický originál a plná specifikace:** [VAS na 3GPP Explorer](https://3gpp-explorer.com/glossary/vas/)
