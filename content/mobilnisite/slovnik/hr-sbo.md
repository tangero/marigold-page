---
slug: "hr-sbo"
url: "/mobilnisite/slovnik/hr-sbo/"
type: "slovnik"
title: "HR-SBO – Home Routed with Session Breakout in VPLMN"
date: 2026-01-01
abbr: "HR-SBO"
fullName: "Home Routed with Session Breakout in VPLMN"
category: "Core Network"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/hr-sbo/"
summary: "Architektura roamingu v 5G, kde je spojení v uživatelské rovině zakotveno v domovské síti (HPLMN), ale může být lokálně vypuštěno ve visitované síti (VPLMN) pro specifické datové služby. Tím se optima"
---

HR-SBO je architektura roamingu v 5G, kde je uživatelská rovina směrována přes domovskou síť (home-routed), ale může být lokálně vypuštěna (broken out) ve visitované síti pro optimalizovaný přístup ke konkrétním službám náročným na nízké latence nebo k lokálnímu obsahu.

## Popis

HR-SBO (Home Routed with Session Breakout in [VPLMN](/mobilnisite/slovnik/vplmn/)) je architektura roamingu v systému 5G (5GS) definovaná ve specifikacích 3GPP Release 18. Představuje evoluci tradičního modelu Home Routed ([HR](/mobilnisite/slovnik/hr/)), kde je veškerý provoz uživatelské roviny tunelován zpět do domovské veřejné pozemní mobilní sítě ([HPLMN](/mobilnisite/slovnik/hplmn/)). V HR-SBO je protokolová datová jednotka ([PDU](/mobilnisite/slovnik/pdu/)) Session stále zakotvena u domovské [UPF](/mobilnisite/slovnik/upf/) (User Plane Function), čímž je zachována kontrola domovské sítě a vynucování politik pro primární relaci. Architektura však zavádí klíčové vylepšení: schopnost vytvořit cestu pro lokální vypuštění (local breakout) specifických, autorizovaných datových toků přímo ve visitované [PLMN](/mobilnisite/slovnik/plmn/) (VPLMN). Toho je dosaženo zřízením sekundárního lokalizovaného bodu kotvení PDU session ([PSA](/mobilnisite/slovnik/psa/)) nebo specializované funkce pro odklon provozu v uživatelské rovině VPLMN.

Architektonická implementace se opírá o vylepšení funkce pro správu relací ([SMF](/mobilnisite/slovnik/smf/)) a funkce řízení politik (PCF) v jádru 5G. Domovská SMF (H-SMF), která sídlí v HPLMN, zůstává hlavním správcem relace. Spolupracuje s visitovanou SMF (V-SMF) v síti VPLMN při orchestraci lokálního vypuštění. Rozhodnutí o použití SBO je řízeno politikami z domovské PCF, které mohou určovat, že určité požadavky aplikační funkce (AF) nebo názvy datových sítí (DNN) jsou lépe obsluhovány lokálně. Například politika může stanovit, že provoz směřující k aplikaci v lokálním edge computingu nebo k uzlu sítě pro doručování obsahu (CDN) ve visitované zemi má použít cestu s lokálním vypuštěním.

Z pohledu signalizace H-SMF vybere V-SMF ve visitované síti, aby zpracovávala část relace s lokálním vypuštěním. Následně V-SMF vytvoří instanci lokální UPF (L-UPS) v síti VPLMN, která slouží jako bod vypuštění. Provoz uživatelské roviny odpovídající politice pro vypuštění je směrován z (R)AN k této L-UPS, která jej pak přeposílá přímo do lokální datové sítě (DN), čímž se vyhne dlouhému putování do HPLMN. H-SMF zachovává celkový kontext relace a může uplatňovat účtování a řízení politik jak pro provoz směrovaný přes domovskou síť, tak pro lokálně vypuštěný provoz prostřednictvím interakce s funkcí účtování (CHF) a PCF. Tento model vyžaduje zabezpečená rozhraní N16 (mezi V-SMF/H-SMF) a N9 (mezi L-UPS/Home UPF).

Úlohou HR-SBO je umožnit efektivní roaming v 5G, který podporuje jak globální konzistenci služeb, tak lokalizovanou optimalizaci výkonu. Je základním prvkem pro roamingové scénáře vyžadující ultranízkou latenci, jako jsou mobilní hraní, rozšířená realita nebo přístup k lokalizovaným regulatorním službám, a zároveň zajišťuje, že domovský operátor si ponechává kontrolu nad účtováním, politikami a bezpečností. Představuje střední cestu mezi úplnou kontrolou roamingu typu Home Routed a úplnou lokalizací roamingu typu Local Breakout (LBO).

## K čemu slouží

HR-SBO byl vytvořen, aby vyřešil inherentní problémy s latencí a neefektivitou tradičního roamingu typu Home Routed (HR) v éře 5G, zejména pro služby citlivé na latenci a lokálně relevantní. V klasickém HR roamingu je veškerý uživatelský provoz tunelován zpět do domovské sítě, i když je obsah nebo aplikační server geograficky blízko aktuálního umístění uživatele ve visitované zemi. Tento 'trombónový' efekt přináší významné zpoždění zpáteční cesty, zvyšuje náklady na přenos na mezifunkčních spojích a snižuje kvalitu uživatelského zážitku u aplikací, jako je cloudové hraní, průmyslový IoT a analýza videa v reálném čase. Primární motivací bylo vylepšit roaming v 5G tak, aby splňoval přísné požadavky na výkon nových vertikálních segmentů, aniž by se obětovala kontrola domovského operátora nad účastnickou relací.

Předchozí přístupy nabízely binární volbu: HR pro úplnou kontrolu nebo Local Breakout (LBO) pro optimální směrování. LBO směruje veškerý provoz přímo ve visitované síti, což minimalizuje latenci, ale přenechává významnou kontrolu (např. detailní účtování, politiky v reálném čase) visitovanému operátorovi a může komplikovat přístup ke službám domovské sítě. HR-SBO řeší omezení obou přístupů zavedením možnosti výběru. Umožňuje operátorům definovat politiky, které určují, které datové toky mají prospěch z lokálního vypuštění, čímž se řeší problém s výkonem pro konkrétní služby, zatímco primární relace a ostatní provoz zůstávají směrovány přes domovskou síť kvůli kontrole a konzistenci.

Vznik HR-SBO byl hnán prací 3GPP na vylepšených roamingových architekturách pro 5G v Release 18, se zaměřením na umožnění edge computingu a poskytování služeb s nízkou latencí přes hranice. Poskytuje standardizovaný, politikami řízený mechanismus pro 'roaming založený na službách', kde rozhodnutí o vypuštění není vše nebo nic, ale je vázáno na potřeby aplikace. To usnadňuje nové roamingové obchodní modely mezi operátory, což jim umožňuje nabízet stupňované roamingové balíčky se zaručenou nízkou latencí pro prémiové služby, a to vše v rámci bezpečného a účtovatelného rámce definovaného domovskou sítí.

## Klíčové vlastnosti

- Politikami řízené lokální vypuštění (local breakout) pro vybrané datové toky v rámci PDU Session směrované přes domovskou síť
- Dvojí body kotvení PDU Session: domovská UPF v HPLMN a lokální UPF (L-UPS) v VPLMN
- Spolupráce při správě relace mezi domovskou SMF (H-SMF) a visitovanou SMF (V-SMF)
- Zachovává kontrolu domovské sítě nad účtováním, politikami a celkovou správou relace
- Optimalizuje směrování pro aplikace náročné na nízkou latenci a přístup k lokálnímu obsahu ve visitované síti
- Využívá standardizovaná rozhraní N16 (SMF-to-SMF) a N9 (UPF-to-UPF) pro koordinaci mezi PLMN

## Definující specifikace

- **TS 23.503** (Rel-20) — 5G Policy and Charging Control Framework
- **TS 23.548** (Rel-19) — 5G System Edge Computing Enhancements
- **TS 29.244** (Rel-19) — PFCP Specification for Control/User Plane Separation
- **TS 29.502** (Rel-19) — 5G System; Nsmf Service Based Interface; Stage 3
- **TS 29.512** (Rel-19) — 5G Session Management Policy Control Service
- **TS 29.513** (Rel-19) — 5G PCC Signalling Flows & QoS Mapping
- **TS 29.556** (Rel-19) — EASDF Service Based Interface Protocol

---

📖 **Anglický originál a plná specifikace:** [HR-SBO na 3GPP Explorer](https://3gpp-explorer.com/glossary/hr-sbo/)
