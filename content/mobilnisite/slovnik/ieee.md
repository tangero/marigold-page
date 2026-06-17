---
slug: "ieee"
url: "/mobilnisite/slovnik/ieee/"
type: "slovnik"
title: "IEEE – Institute of Electrical and Electronics Engineers"
date: 2025-01-01
abbr: "IEEE"
fullName: "Institute of Electrical and Electronics Engineers"
category: "Other"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/ieee/"
summary: "Globální profesní organizace vyvíjející standardy pro širokou škálu technologií, včetně mnoha odkazovaných 3GPP pro integraci bezdrátových lokálních sítí (Wi-Fi) a další oblasti. Její standardy, jako"
---

IEEE je globální profesní organizace, která vyvíjí standardy, například IEEE 802.11 pro Wi-Fi, na které odkazuje 3GPP pro integraci bezdrátových lokálních sítí a spolupráci s přístupem mimo 3GPP.

## Popis

Institute of Electrical and Electronics Engineers (IEEE) je globální profesní sdružení zaměřené na rozvoj technologií ve prospěch lidstva. Ačkoli samo není součástí 3GPP, jeho standardy jsou v ekosystému 3GPP rozsáhle odkazovány a integrovány, zejména pro umožnění interoperability se sítěmi přístupu mimo 3GPP. Nejvýznamnějším příkladem je rodina standardů IEEE 802.11 pro bezdrátové lokální sítě (WLAN), běžně známá jako Wi-Fi. Specifikace 3GPP definují architektury a protokoly – například pro důvěryhodný a nedůvěryhodný přístup mimo 3GPP – které umožňují uživatelskému zařízení (UE) bezproblémově se připojit k jádrovým sítím 3GPP (jako 5GC nebo EPC) prostřednictvím přístupových bodů založených na IEEE 802.11. Tato integrace je řízena síťovými funkcemi, jako je Non-3GPP Interworking Function ([N3IWF](/mobilnisite/slovnik/n3iwf/)), a zahrnuje specifické bezpečnostní protokoly, například EAP-AKA' pro autentizaci přes tyto spoje.

Kromě WLAN standardy IEEE ovlivňují další oblasti, na které 3GPP odkazuje. Například IEEE 802.3 (Ethernet) může být relevantní pro přenosové sítě a IEEE 1588 pro synchronizaci pomocí protokolu přesného času. Vztah je formalizován prostřednictvím normativních odkazů v technických specifikacích 3GPP (TS). Například TS 23.402 (Architecture enhancements for non-3GPP accesses) a TS 24.302 (Access to the 3GPP Evolved Packet Core via non-3GPP access networks) podrobně popisují, jak jsou využívána rozhraní IEEE 802.11. Uvedené specifikace, jako je 21.905 (Vocabulary for 3GPP Specifications), zahrnují termíny IEEE, zatímco jiné, například 23.234 (3GPP system to Wireless Local Area Network interworking), definují samotnou architekturu spolupráce.

Role IEEE v 3GPP je zásadní pro konvergenci sítí. Umožňuje operátorům budovat heterogenní sítě, které kombinují širokoplošné pokrytí a mobilitu přístupu 3GPP (např. 5G NR, LTE) s vysokou přenosovou kapacitou a možnostmi lokálních sítí Wi-Fi. To poskytuje jednotný uživatelský zážitek, podporuje přesměrování provozu a umožňuje konvergenci pevných a mobilních sítí. Technická práce zahrnuje sladění specifikací IEEE pro vrstvu 1 a 2 s protokoly 3GPP pro vrstvu 3 a výše v oblasti mobility, správy relací a zabezpečení, což zajišťuje ucelený koncový systém.

## K čemu slouží

IEEE existuje jako nezávislý normalizační orgán pro vývoj globálně přijímaných technických standardů napříč elektrotechnickými, elektronickými a výpočetními obory. Jejím účelem v kontextu 3GPP je poskytovat zralé, široce implementované standardy pro doplňkové přístupové technologie, především WLAN, které mohou sítě 3GPP využívat. Tím se řeší problém fragmentace sítí a umožňuje se kontinuita služeb napříč různými typy bezdrátového přístupu. Historicky fungovaly mobilní a Wi-Fi sítě odděleně. Motivací pro integraci byla potřeba poskytnout uživatelům bezproblémové připojení, optimalizovat síťové zdroje přesměrováním provozu na Wi-Fi, kde je dostupné, a vytvořit konvergované nabídky služeb.

Odkazováním na standardy IEEE se 3GPP vyhýbá znovuvynalézání kola v oblasti bezdrátové konektivity pro lokální sítě. Staví na masivním globálním nasazení a úsporách z rozsahu zařízení IEEE 802.11. Omezení předchozích přístupů zahrnovala proprietární nebo nestandardní řešení spolupráce, která bránila interoperabilitě. Formální integrace prostřednictvím specifikací 3GPP, která začala naplno ve vydání 6 s WLAN spoluprací, poskytla standardizovaný, na dodavateli nezávislý rámec. To umožňuje jakémukoli kompatibilnímu UE připojit se k jakémukoli kompatibilnímu jádrové síti 3GPP prostřednictvím jakéhokoli kompatibilního přístupového bodu IEEE 802.11, což je nezbytné pro škálovatelnost na hromadném trhu a inovace v kombinovaných pevných a mobilních službách.

## Klíčové vlastnosti

- Poskytuje globálně uznávané standardy pro bezdrátové lokální sítě (IEEE 802.11/Wi-Fi)
- Umožňuje standardizovanou spolupráci mezi sítěmi přístupu 3GPP a mimo 3GPP
- Základ pro architektury důvěryhodného a nedůvěryhodného přístupu mimo 3GPP v jádru 3GPP
- Podporuje autentizační a bezpečnostní protokoly (např. EAP) pro integrovaný přístup
- Umožňuje politiky přesměrování a odlehčování provozu mezi 3GPP RAN a WLAN
- Umožňuje scénáře pevného bezdrátového přístupu (FWA) a konvergovaných sítí

## Související pojmy

- [N3IWF – Non-3GPP access InterWorking Function](/mobilnisite/slovnik/n3iwf/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TR 22.804** (Rel-16) — 5G Automation in Vertical Domains Study
- **TS 23.234** (Rel-13) — 3GPP-WLAN Interworking Index
- **TS 24.302** (Rel-19) — Access to EPC via non-3GPP networks; Stage 3
- **TS 25.133** (Rel-19) — UTRAN RRM Requirements for FDD
- **TS 26.804** (Rel-19) — 5G Media Streaming Extensions Study
- **TS 32.406** (Rel-19) — Performance Management for CN PS Domain
- **TS 37.834** (Rel-12) — WLAN/3GPP Radio Interworking Study
- **TS 37.870** (Rel-13) — Study on Multi-RAT Joint Coordination

---

📖 **Anglický originál a plná specifikace:** [IEEE na 3GPP Explorer](https://3gpp-explorer.com/glossary/ieee/)
