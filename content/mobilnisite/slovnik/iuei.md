---
slug: "iuei"
url: "/mobilnisite/slovnik/iuei/"
type: "slovnik"
title: "IUEI – International Mobile Subscriber Station Identity"
date: 2001-01-01
abbr: "IUEI"
fullName: "International Mobile Subscriber Station Identity"
category: "Identifier"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/iuei/"
summary: "IUEI je jedinečný identifikátor stanice mobilního účastníka, standardizovaný v raných vydáních 3GPP. Slouží jako klíčový identifikátor účastnického zařízení v mezinárodních mobilních sítích, usnadňuje"
---

IUEI je jedinečný identifikátor standardizovaný v 3GPP R99 pro stanici mobilního účastníka, který slouží jako klíč pro mezinárodní identifikaci, roaming a správu účastnického zařízení v sítích UMTS.

## Popis

International Mobile Subscriber Station Identity (IUEI) je globálně jedinečný identifikátor přidělený stanici mobilního účastníka, což typicky označuje uživatelské zařízení (UE) neboli mobilní terminál. Je definován v rámci specifikací 3GPP, konkrétně v TS 23.171, jako součást rámce pro identitu a adresování v sítích UMTS (Universal Mobile Telecommunications System). IUEI je klíčový pro rozlišení jednotlivých účastnických stanic uvnitř a napříč hranicemi síťových operátorů, což umožňuje funkcím základní sítě správně směrovat komunikaci a spravovat účastnické relace. Z architektonického hlediska IUEI působí v doméně základní sítě a komunikuje s entitami jako Home Location Register ([HLR](/mobilnisite/slovnik/hlr/)) nebo Home Subscriber Server ([HSS](/mobilnisite/slovnik/hss/)) pro správu účastnických dat. Používá se v procedurách, jako je registrace, autentizace a správa mobility, kde síť potřebuje jednoznačně identifikovat účastníkovu stanici pro poskytování služeb. Identifikátor je strukturován tak, aby zajišťoval globální jedinečnost, a často zahrnuje prvky, které jej vážou ke konkrétnímu síťovému operátorovi nebo kódu země, podobně jako jiné mobilní identifikátory, ale uzpůsobené pro samotné zařízení stanice. V praxi IUEI funguje ve spojení s dalšími identifikátory, jako je [IMSI](/mobilnisite/slovnik/imsi/) (International Mobile Subscriber Identity), a poskytuje tak komplexní identifikační rámec. Zatímco IMSI identifikuje účastníka, IUEI konkrétně identifikuje fyzickou nebo logickou účastnickou stanici, což umožňuje podrobnější správu atributů specifických pro zařízení. Toto oddělení podporuje scénáře, kdy účastník může používat více zařízení, protože každá stanice může mít svůj vlastní IUEI při sdílení jednoho účastnického profilu. Role IUEI v síti zahrnuje umožnění zákonného odposlechu, detekci podvodů a přesné účtování prostřednictvím sledování aktivit specifických pro danou stanici. Přenáší se během počátečního připojení k síti a může být použit v signalizačních zprávách napříč rozhraními, jako je rozhraní vzduch a uzly základní sítě. V průběhu času, jak se sítě vyvíjely, byl koncept identity stanice zpřesňován, ale IUEI položil základy pro pozdější identifikátory v LTE a 5G, čímž zdůraznil důležitost jedinečné identifikace zařízení v mobilní telekomunikaci.

## K čemu slouží

IUEI byl vytvořen, aby uspokojil potřebu standardizovaného, globálně jedinečného identifikátoru pro stanice mobilních účastníků v sítích 3G UMTS. Před jeho zavedením se mobilní sítě spoléhaly na identifikátory jako [IMSI](/mobilnisite/slovnik/imsi/) pro účastníky, ale postrádaly konzistentní způsob, jak jednoznačně identifikovat samotné zařízení stanice, což mohlo vést k nejednoznačnostem v správě zařízení a roamingových scénářích. Motivace vycházela z rostoucí složitosti mobilních služeb a expanze mezinárodního roamingu, kde se přesná identifikace stanice stala nezbytnou pro síťové operace, zabezpečení a regulatorní shodu. Historicky v sítích 2G GSM existovaly identifikátory jako [IMEI](/mobilnisite/slovnik/imei/) (International Mobile Equipment Identity) pro zařízení, ale IUEI poskytl v rámci architektury 3GPP pro účastnické stanice integrovanější přístup, zahrnující jak hardwarové, tak logické aspekty. Řešil problémy související se sledováním účastnické stanice, zejména v případech, kdy s jedním účastníkem mohlo být spojeno více stanic, což umožnilo lepší diferenciaci a správu služeb. Omezení předchozích přístupů zahrnovala fragmentovaná schémata identit, která nebyla plně sladěna s architektonickou vizí 3GPP, což potenciálně bránilo interoperabilitě a efektivnímu využití síťových zdrojů. Standardizací IUEI v [R99](/mobilnisite/slovnik/r99/) 3GPP vytvořil jasnou identifikační vrstvu, která podporovala pokročilé možnosti UMTS, jako jsou vylepšené datové služby a mobilita, a zároveň zajistila zpětnou kompatibilitu a budoucí vývoj.

## Klíčové vlastnosti

- Globálně jedinečný identifikátor pro stanice mobilních účastníků
- Definován v 3GPP TS 23.171 pro sítě UMTS
- Podporuje mezinárodní roaming a správu účastníků
- Používá se v síťových procedurách registrace a autentizace
- Umožňuje sledování specifické pro zařízení pro účely účtování a zabezpečení
- Integruje se s entitami základní sítě, jako je HLR/HSS

## Související pojmy

- [IMSI – International Mobile Subscriber Identity](/mobilnisite/slovnik/imsi/)
- [IMEI – International Mobile Station Equipment Identities](/mobilnisite/slovnik/imei/)
- [HLR – Home Location Register](/mobilnisite/slovnik/hlr/)
- [HSS – Home Subscriber Server](/mobilnisite/slovnik/hss/)
- [UMTS – Universal Mobile Telecommunications System](/mobilnisite/slovnik/umts/)

## Definující specifikace

- **TS 23.171** (Rel-4) — LCS Stage 2 Specification for UMTS

---

📖 **Anglický originál a plná specifikace:** [IUEI na 3GPP Explorer](https://3gpp-explorer.com/glossary/iuei/)
