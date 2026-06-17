---
slug: "ifpei"
url: "/mobilnisite/slovnik/ifpei/"
type: "slovnik"
title: "IFPEI – International Fixed Part Equipment Identity"
date: 2025-01-01
abbr: "IFPEI"
fullName: "International Fixed Part Equipment Identity"
category: "Identifier"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/ifpei/"
summary: "Jedinečný identifikátor pro zařízení pevné části (Fixed Part) v systému DECT (Digital Enhanced Cordless Telecommunications), který je součástí řešení Fixed Mobile Convergence (FMC) založeného na 3GPP"
---

IFPEI je jedinečný identifikátor zařízení pevné části (Fixed Part) v systému DECT v rámci řešení Fixed Mobile Convergence založeného na 3GPP IMS, používaný pro registraci, autentizaci a správu zařízení.

## Popis

International Fixed Part Equipment Identity (IFPEI) je globálně jedinečný identifikátor přidělený zařízení pevné části (Fixed Part) v systému [DECT](/mobilnisite/slovnik/dect/). V kontextu specifikací 3GPP nabývá IFPEI významu v architekturách pro Fixed Mobile Convergence ([FMC](/mobilnisite/slovnik/fmc/)), zejména těch, které integrují bezšňůrové systémy založené na DECT s IP Multimedia Subsystem (IMS). Pevná část ([FP](/mobilnisite/slovnik/fp/)) je základnová stanice nebo síťový přístupový bod systému DECT, který poskytuje rádiové připojení přenosným částem (PP), tedy bezšňůrovým telefonním přístrojům. IFPEI slouží jako trvalá, výrobně naprogramovaná hardwarová identita tohoto zařízení základnové stanice.

Architektonicky, když je systém DECT integrován do sítě 3GPP IMS – což je scénář definovaný pro podnikovou nebo rezidenční FMC – funguje FP jako přístupová brána. Převádí rádiové protokoly DECT na SIP a RTP přes IP pro komunikaci s jádrem IMS. Aby síť IMS dokázala toto zařízení FP rozpoznat, ověřit a spravovat, je vyžadována jedinečná a ověřitelná identita. Tuto roli plní IFPEI. Používá se při počáteční registraci FP v síti, často ve spojení s autentizačními procedurami, které mohou využívat IFPEI k získání bezpečnostních přihlašovacích údajů.

IFPEI je strukturován podle standardů [ITU-T](/mobilnisite/slovnik/itu-t/) a [ETSI](/mobilnisite/slovnik/etsi/) DECT. Jeho formát je hierarchický a typicky zahrnuje kód výrobce pevné části (FPMC) a výrobcem přidělené sériové číslo zařízení. Tato struktura zajišťuje globální jedinečnost. V rámci procedur 3GPP může být IFPEI komunikován z FP do síťových entit, jako je [P-CSCF](/mobilnisite/slovnik/p-cscf/) nebo aplikační server, během registrace. Umožňuje síti autorizovat konkrétní hardwarové zařízení, aplikovat služební profily specifické pro dané FP (např. pro podnikový systém DECT) a v případě potřeby provádět zákonné odposlechy nebo zablokování zařízení. Je to klíčový parametr pro ukotvení služby uživatele založené na DECT v IMS, protože identita uživatele (jako SIP URI) je často asociována s FP/IFPEI, přes který je registrovaný.

## K čemu slouží

IFPEI existuje za účelem poskytnutí jednoznačné identifikace zařízení v systémech [DECT](/mobilnisite/slovnik/dect/), což je požadavek, který se stává kritickým, když jsou tyto systémy integrovány do větších standardizovaných telekomunikačních sítí, jako je 3GPP IMS. V samostatných nasazeních DECT může být identifikace jednodušší, ale pro konvergenci s IMS – umožňující služby jako jediné telefonní číslo pro mobilní i DECT přístroje – je robustní, standardizovaná identifikace zásadní pro zabezpečení, správu a poskytování služeb.

Řeší několik problémů v kontextu [FMC](/mobilnisite/slovnik/fmc/). Za prvé umožňuje zabezpečený síťový přístup: síť může ověřit nejen uživatele (pomocí SIM nebo přihlašovacích údajů v přenosné části), ale také legitimitu samotného přístupového zařízení (pevné části), čímž zabrání neautorizovaným základnovým stanicím v připojení k IMS operátora. Za druhé usnadňuje přesnou provizionáž služeb a účtování; operátor ví, přes který konkrétní hardware (např. podniková základnová stanice DECT) je uživatel připojen, což umožňuje přizpůsobené služby a přesnou lokalizaci/směrování (např. pro tísňová volání). Za třetí poskytuje prostředek pro správu životního cyklu zařízení, včetně vzdálené diagnostiky, softwarových aktualizací cílených na konkrétní modely FP a dodržování regulatorních požadavků na registraci zařízení. Jeho specifikace v rámcových standardech 3GPP zajišťuje interoperabilitu mezi zařízeními DECT od libovolného výrobce a sítěmi 3GPP IMS, což byl klíčový cíl iniciativ Fixed Mobile Convergence.

## Klíčové vlastnosti

- Globálně jedinečný, trvalý identifikátor pro zařízení pevné části DECT (základnovou stanici)
- Strukturovaný formát zahrnující kód výrobce a sériové číslo
- Používá se pro autentizaci a autorizaci zařízení v architekturách 3GPP IMS FMC
- Umožňuje síťovou správu a služební profilaci pro konkrétní hardwarové zařízení FP
- Podporuje regulatorní funkce, jako je zákonný odposlech a kontrola identity zařízení
- Definován v souladu se standardy ITU-T a ETSI DECT pro konzistenci

## Související pojmy

- [DECT – Digital Enhanced Cordless Telecommunications](/mobilnisite/slovnik/dect/)
- [IMS – IP Multimedia Subsystem](/mobilnisite/slovnik/ims/)

## Definující specifikace

- **TS 42.056** (Rel-19) — GSM Cordless Telephony System (CTS)
- **TS 43.020** (Rel-19) — Security Procedures for GSM

---

📖 **Anglický originál a plná specifikace:** [IFPEI na 3GPP Explorer](https://3gpp-explorer.com/glossary/ifpei/)
