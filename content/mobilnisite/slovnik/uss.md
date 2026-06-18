---
slug: "uss"
url: "/mobilnisite/slovnik/uss/"
type: "slovnik"
title: "USS – User Security Settings"
date: 2026-01-01
abbr: "USS"
fullName: "User Security Settings"
category: "Security"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/uss/"
summary: "Podmnožina obecných uživatelských bezpečnostních nastavení (GUSS) obsahující bezpečnostní předplatitelská data uživatele. Používá se v procedurách autentizace a dohody klíčů a umožňuje zabezpečený pří"
---

USS je podmnožina obecných uživatelských bezpečnostních nastavení (Generic User Security Settings) obsahující bezpečnostní předplatitelská data uživatele, která se používají pro autentizaci a dohodu klíčů za účelem zajištění zabezpečeného přístupu k síti.

## Popis

Uživatelská bezpečnostní nastavení (USS) jsou klíčovou součástí bezpečnostní architektury 3GPP, konkrétně definovanou jako součást rámce obecných uživatelských bezpečnostních nastavení ([GUSS](/mobilnisite/slovnik/guss/)). Představují soubor bezpečnostních předplatitelských parametrů spojených s konkrétním uživatelem. Tato nastavení jsou uložena v domovské síti uživatele, typicky na serveru [HSS](/mobilnisite/slovnik/hss/) (Home Subscriber Server) nebo v jednotné funkci správy dat ([UDM](/mobilnisite/slovnik/udm/)) v systémech 5G. USS obsahují klíčová data potřebná pro procedury autentizace a dohody klíčů ([AKA](/mobilnisite/slovnik/aka/)), jako je dlouhodobý tajný klíč (K), autentizační algoritmy (např. MILENAGE, TUAK) a parametry pro odvozování klíčů. Když se uživatel pokouší o přístup k síti, obsluhující síť (např. [VLR](/mobilnisite/slovnik/vlr/), [SGSN](/mobilnisite/slovnik/sgsn/), [MME](/mobilnisite/slovnik/mme/), [AMF](/mobilnisite/slovnik/amf/)) požaduje od domovské sítě autentizační vektory. Domovská síť použije USS k vygenerování těchto vektorů, které zahrnují náhodnou výzvu (RAND), očekávanou odpověď (XRES), šifrovací klíč (CK), integritní klíč (IK) a autentizační token (AUTN). Obsluhující síť pak tyto vektory použije k výzvě uživatelského zařízení (UE) a k vytvoření zabezpečených šifrovacích a integritních klíčů pro relaci.

Architektura správy USS zahrnuje rozhraní mezi HSS/UDM a dalšími síťovými funkcemi. V legacy systémech se k USS přistupuje přes rozhraní založená na protokolu MAP nebo Diameter (např. Cx, S6a, S6d). V 5G poskytuje UDM data USS autentizační serverové funkci (AUSF) a funkci správy přístupu a mobility (AMF) přes servisní rozhraní Nudm. USS není monolitický blok, ale může být strukturováno tak, aby podporovalo různé autentizační metody a služby. Například může obsahovat samostatná nastavení pro 3G/4G AKA a 5G AKA nebo pro autentizaci k IP multimediální podsystému (IMS). Tato modularita umožňuje síti aplikovat odpovídající bezpečnostní mechanismy na základě přístupové technologie a požadované služby.

Role USS v síti je zásadní pro bezpečnost předplatitele. Zajišťuje, že každý uživatel je jednoznačně autentizován a že následná komunikace je chráněna. Integrita a důvěrnost dat USS jsou prvořadé, protože jejich kompromitace by umožnila zneužití identity a odposlech. Síťové funkce nikdy neobdrží samotný dlouhodobý tajný klíč (K); místo toho dostávají odvozené autentizační vektory, v souladu s principem nikdy nevystavovat kořenový tajný klíč mimo domovskou doménu. USS také podporuje funkce jako čerstvost klíčů a správu sekvenčních čísel, aby se zabránilo opakovaným útokům. Jeho správná konfigurace a synchronizace napříč síťovými prvky jsou nezbytné pro předcházení autentizačním chybám a výpadkům služeb.

## K čemu slouží

USS existuje jako standardizované, zabezpečené a spravovatelné úložiště pro uživatelsky specifické bezpečnostní přihlašovací údaje v sítích 3GPP. Před jejich formalizací v rámci konceptu GUSS byla bezpečnostní nastavení často těsně svázána s jinými předplatitelskými daty, což ztěžovalo nezávislou správu autentizace pro více služeb (např. přepojování okruhů, přepojování paketů, IMS). To mohlo vést k neefektivitě a potenciálním bezpečnostním mezerám při zavádění nových autentizačních metod nebo služeb. Rámec USS byl vytvořen, aby oddělil bezpečnostní nastavení od ostatních předplatitelských dat, což umožňuje flexibilnější a robustnější správu zabezpečení.

Primární problém, který řeší, je potřeba konzistentního a spolehlivého zdroje pravdy pro parametry uživatelské autentizace napříč různými síťovými doménami a generacemi. Řeší výzvu podpory heterogenních přístupových technologií (2G, 3G, 4G, 5G, ne-3GPP) a servisních platforem (IMS, MMTEL) s jednotným modelem bezpečnostních dat. Díky vyhrazeným USS mohou operátoři aktualizovat bezpečnostní algoritmy nebo klíčový materiál pro uživatele nebo službu, aniž by to ovlivnilo ostatní aspekty předplatného. To je klíčové pro postupné zavádění nových bezpečnostních standardů (např. přechod z 4G EPS-AKA na 5G AKA) a pro poskytování služebně specifické autentizace, což zvyšuje celkový stav zabezpečení sítě.

Historicky, jak se sítě vyvíjely z jednoslužbových hlasových na více-službové konvergentní IP sítě, se staly zřejmými omezení monolitické správy předplatitelských dat. Vytvoření USS, zejména jako součásti GUSS od 3GPP Release 7 výše, bylo motivováno potřebou modulárního, do budoucna připraveného bezpečnostního základu. Umožňuje síti uživatele autentizovat jednou a následně využít tato pověření pro přístup k více službám (koncept jednotného přihlášení pro síťový přístup), což zlepšuje uživatelský zážitek při zachování přísné bezpečnosti. Tvoří základ pro zabezpečenou mobilitu a kontinuitu služeb v moderních celulárních sítích.

## Klíčové vlastnosti

- Ukládá dlouhodobý tajný klíč (K) a konfiguraci autentizačního algoritmu
- Používá se k vygenerování autentizačních vektorů (RAND, AUTN, XRES, CK, IK) pro procedury AKA
- Podporuje více autentizačních metod (např. 3G AKA, EPS-AKA, 5G AKA, EAP-AKA')
- Umožňuje služebně specifická bezpečnostní nastavení v rámci jednoho uživatelského předplatného
- Přístupné síťovými funkcemi přes standardizovaná rozhraní (např. Cx, S6a, Nudm)
- Základní pro odvozování šifrovacích a integritních klíčů v systémech 3GPP

## Související pojmy

- [GUSS – GBA User Security Settings](/mobilnisite/slovnik/guss/)
- [AKA – Authentication and Key Agreement](/mobilnisite/slovnik/aka/)
- [HSS – Home Subscriber Server](/mobilnisite/slovnik/hss/)

## Definující specifikace

- **TR 22.843** (Rel-19) — Study on Uncrewed Aerial Vehicle (UAV) Phase 3
- **TS 23.255** (Rel-19) — UAS Application Layer Support
- **TS 23.256** (Rel-19) — UAS Support Architecture Enhancements
- **TS 23.700** (Rel-20) — XR Services Application Enablement Layer
- **TR 23.755** (Rel-17) — Study on app layer support for UAS
- **TS 24.109** (Rel-19) — HTTP Digest AKA & GAA Stage 3
- **TS 24.257** (Rel-19) — UAS Application Enabler (UAE) Layer
- **TS 24.301** (Rel-19) — NAS protocol for Evolved Packet System
- **TS 24.501** (Rel-19) — 5G NAS Protocols Specification
- **TS 27.007** (Rel-19) — AT Command Set for UE
- **TS 28.853** (Rel-19) — Charging for Uncrewed Aerial Systems
- **TS 29.109** (Rel-19) — GAA Bootstrapping Interfaces (Zh, Dz, Zn, Zpn)
- **TS 29.255** (Rel-19) — USS Services for UAS in 5G
- **TS 29.256** (Rel-19) — UAS-NF Stage 3 Protocol Specification
- **TS 29.257** (Rel-19) — Application layer support for Uncrewed Aerial System (UAS)
- … a dalších 15 specifikací

---

📖 **Anglický originál a plná specifikace:** [USS na 3GPP Explorer](https://3gpp-explorer.com/glossary/uss/)
