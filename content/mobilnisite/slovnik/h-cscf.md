---
slug: "h-cscf"
url: "/mobilnisite/slovnik/h-cscf/"
type: "slovnik"
title: "H-CSCF – Home Call Session Control Function"
date: 2025-01-01
abbr: "H-CSCF"
fullName: "Home Call Session Control Function"
category: "Core Network"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/h-cscf/"
summary: "H-CSCF je základní síťový prvek IMS, který slouží jako hlavní kontaktní bod domácí sítě pro signalizaci SIP. Zajišťuje řízení relací, spouštění služeb a komunikaci s aplikačními servery. Je klíčový pr"
---

H-CSCF (Domácí funkce řízení hovorové relace) je základní prvek IMS, který slouží jako hlavní kontaktní bod domácí sítě pro signalizaci SIP a zajišťuje řízení relací a spouštění služeb pro navazování multimediálních relací.

## Popis

Home Call Session Control Function (H-CSCF) je klíčová komponenta v architektuře IP Multimedia Subsystem (IMS) definované standardy 3GPP. Působí jako centrální SIP (Session Initiation Protocol) server v domácí síti uživatele. Když uživatel iniciuje nebo přijímá hovor či multimediální relaci, signalizace SIP prochází přes H-CSCF. Jejím hlavním úkolem je provádět řízení relace, což zahrnuje zpracování SIP registrací, navazování (INVITE), modifikaci a ukončování SIP relací. H-CSCF dotazuje Home Subscriber Server ([HSS](/mobilnisite/slovnik/hss/)) za účelem stažení profilu služeb uživatele, který obsahuje Initial Filter Criteria (iFC). Tato iFC představují soubor spouštěčů, které na základě SIP požadavku určují, které aplikační servery ([AS](/mobilnisite/slovnik/as/)) musí být do relace zapojeny. To umožňuje orchestraci přidaných služeb, jako je hlasová schránka, přesměrování hovorů nebo videokonference.

Z architektonického hlediska se H-CSCF nachází v řídicí rovině jádra IMS. Rozhraní Cx ji spojuje s HSS pro autentizaci uživatele a získání profilu služeb. Rozhraní Sh může být použito pro komunikaci s aplikačními servery ohledně servisních dat. H-CSCF také komunikuje se Serving-CSCF (S-CSCF), což je entita řízení relace ve navštívené síti při roamingu uživatele, a s Interrogating-CSCF ([I-CSCF](/mobilnisite/slovnik/i-cscf/)), který slouží jako první kontaktní bod v síti operátora. Rozhodování H-CSCF je řízeno předplatitelskými daty uživatele, což umožňuje personalizované poskytování služeb.

Co se týče fungování, po přijetí SIP REGISTER požadavku H-CSCF autentizuje uživatele přes HSS a zaregistruje jeho kontaktní informace. Pro SIP INVITE vyhodnotí iFC. Pokud je splněna podmínka spouštěče – například číslo volaného odpovídá určitému vzoru – H-CSCF proxy přepošle SIP požadavek na určený aplikační server. AS pak může poskytnout službu (jako přehrání oznámení nebo úprava parametrů relace), než H-CSCF přepošle požadavek k jeho konečnému cíli. Tento model odděluje řízení hovoru od servisní logiky, což je klíčový princip IMS podporující inovace a flexibilitu služeb. H-CSCF také hraje roli v řízení politik, komunikuje s Policy and Charging Rules Function (PCRF) přes rozhraní Rx, aby zajistila, že relace dodržuje předplatitelské politiky QoS a účtování.

## K čemu slouží

H-CSCF byla zavedena, aby řešila omezení tradičních telefonních sítí s přepojováním okruhů, které pevně svazovaly servisní logiku s přepojovací infrastrukturou. To zavedení nových multimediálních služeb zpomalovalo a prodražovalo. Vytvoření architektury IMS s H-CSCF v jejím centru bylo motivováno potřebou standardizované, IP-based platformy pro poskytování konvergovaných hlasových, video a datových služeb. Umožňuje konvergenci pevných a mobilních sítí a poskytuje konzistentní uživatelský zážitek bez ohledu na přístupovou síť (např. LTE, 5G, Wi-Fi).

Jejím hlavním účelem je sloužit jako kotvící bod domácí sítě pro řízení relací založené na SIP. To řeší problém, jak spravovat identitu předplatitele, profily služeb a spouštění aplikací škálovatelným a na síti nezávislým způsobem. Centralizací této logiky v domácí síti mohou operátoři udržovat kontrolu nad poskytováním služeb i při roamingu uživatelů. H-CSCF ve spolupráci se S-CSCF a [I-CSCF](/mobilnisite/slovnik/i-cscf/) poskytuje robustní rámec pro směrování SIP zpráv, vynucování bezpečnostních politik a integraci se širokým ekosystémem aplikačních serverů, čímž připravuje síť na budoucí multimediální aplikace.

## Klíčové vlastnosti

- Řízení SIP relací pro registraci, navázání, modifikaci a ukončení
- Spouštění služeb pomocí Initial Filter Criteria (iFC) stažených z HSS
- Autentizace a autorizace předplatitele přes rozhraní Cx k HSS
- Integrace s aplikačními servery pro přidané služby
- Vynucování politik pomocí interakce s PCRF přes rozhraní Rx
- Kotvící bod pro profil služeb uživatele v domácí síti

## Související pojmy

- [IMS – IP Multimedia Subsystem](/mobilnisite/slovnik/ims/)
- [I-CSCF – Interrogating-Call Session Control Function](/mobilnisite/slovnik/i-cscf/)
- [HSS – Home Subscriber Server](/mobilnisite/slovnik/hss/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions

---

📖 **Anglický originál a plná specifikace:** [H-CSCF na 3GPP Explorer](https://3gpp-explorer.com/glossary/h-cscf/)
