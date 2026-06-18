---
slug: "pap"
url: "/mobilnisite/slovnik/pap/"
type: "slovnik"
title: "PAP – Password Authentication Protocol"
date: 2026-01-01
abbr: "PAP"
fullName: "Password Authentication Protocol"
category: "Security"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/pap/"
summary: "PAP je jednoduchý autentizační protokol, který přenáší nešifrovaná uživatelská jména a hesla přes síťové spojení. V kontextech 3GPP je často uváděn jako zastaralý nebo srovnávací mechanismus ve specif"
---

PAP je jednoduchý zastaralý (legacy) autentizační protokol, který přenáší nešifrovaná uživatelská jména a hesla, používaný v raných systémech 3GPP, jako je vytáčené připojení a GPRS.

## Popis

Password Authentication Protocol (PAP) je základní autentizační protokol původně definovaný v rámci sady Point-to-Point Protocol ([PPP](/mobilnisite/slovnik/ppp/)) ([RFC](/mobilnisite/slovnik/rfc/) 1334, později RFC 1994). Jeho fungování je přímočaré: klient (peer) žádající o síťový přístup odešle autentizační požadavek obsahující uživatelské jméno a heslo v prostém textu k autentizátoru (síťovému přístupovému serveru). Autentizátor tyto přihlašovací údaje ověří proti lokální databázi nebo autentizačnímu serveru a odpoví potvrzením (Accept) nebo zamítnutím (Reject). Tato výměna probíhá během úvodní fáze navázání spojení PPP.

Ve specifikacích 3GPP není PAP primárním autentizačním mechanismem pro základní buněčný přístup, jako je 5G [NAS](/mobilnisite/slovnik/nas/) nebo EAP-AKA', ale je zmiňován v několika kontextech. Historicky byl používán pro vytáčený přístup k internetu přes Integrated Services Digital Network ([ISDN](/mobilnisite/slovnik/isdn/)) a pro autentizaci uživatelů v raných sítích General Packet Radio Service ([GPRS](/mobilnisite/slovnik/gprs/)) při interakci s externími paketovými datovými sítěmi ([PDN](/mobilnisite/slovnik/pdn/)). Specifikace jako 3GPP TS 29.061 (Interworking between the Public Land Mobile Network and Packet Data Networks) podrobně popisují, jak lze PAP (a [CHAP](/mobilnisite/slovnik/chap/)) použít pro externí [AAA](/mobilnisite/slovnik/aaa/) (Authentication, Authorization, and Accounting), když se mobilní zařízení chová jako vytáčený klient k poskytovateli internetových služeb (ISP).

Architektura protokolu zahrnuje dvě hlavní zprávy ve fázi PPP Link Control Protocol (LCP): Authenticate-Request a Authenticate-Ack nebo Authenticate-Nak. PAP funguje na principu dvoucestného handshake a neposkytuje žádnou ochranu přihlašovacích údajů během přenosu; jsou odesílány v prostém textu, což je činí zranitelnými vůči odposlechu na spojení. Kvůli této slabině standardy 3GPP obvykle vyžadují nebo upřednostňují použití protokolu Challenge-Handshake Authentication Protocol (CHAP) nebo robustnějších metod, jako je EAP (Extensible Authentication Protocol), pokud jde o bezpečnost. Zařazení PAP do specifikací 3GPP často slouží k zajištění zpětné kompatibility se zastaralými externími sítěmi nebo jako základní příklad v popisech protokolů.

## K čemu slouží

PAP byl vytvořen v počátcích vytáčeného přístupu k internetu, aby poskytl jednoduchou, univerzálně implementovatelnou metodu pro síťový přístupový server k ověření identity uživatele pomocí dvojice uživatelské jméno/heslo. Jeho účelem bylo poskytnout základní řízení přístupu pro PPP spoje bez výpočetní režie kryptografických výzev. Během vývoje sítí 2G a raných 3G potřebovali mobilní operátoři spolupracovat s existující internetovou infrastrukturou, kde byl PAP běžnou metodou používanou ISP. Proto standardy 3GPP zahrnuly podporu PAP, aby umožnily mobilním stanicím připojit se k těmto externím PDN pomocí známých paradigmat vytáčeného připojení.

Protokol řeší jednoduchý problém ověření přihlašovacích údajů, ale přináší významná bezpečnostní omezení. Řeší problém autentizace typu 'what you know' (co znáte) nejpřímějším možným způsobem. Motivace pro jeho zařazení do 3GPP však byla z velké části o kompatibilitě, nikoli o vedení v oblasti bezpečnosti. Jak se sítě 3GPP vyvíjely, omezení PAP – konkrétně nedostatek šifrování a náchylnost k replay útokům – se stala pro mobilní specifickou autentizaci nepřijatelnými. To vedlo ke specifikaci a preferenci CHAP, který používá mechanismus challenge-response, a později k integraci mnohem silnější, SIM-based autentizace prostřednictvím protokolu AKA a frameworků EAP. PAP zůstává ve specifikacích jako zastaralá (legacy) volba, což zdůrazňuje historický vývoj zabezpečení v datových službách.

## Klíčové vlastnosti

- Jednoduchá autentizace dvoucestným handshake (požadavek/odpověď)
- Přenáší uživatelské přihlašovací údaje (jméno a heslo) v prostém textu
- Funguje v rámci fáze navázání spojení PPP
- Poskytuje základní funkci udělení nebo zamítnutí přístupu
- Široce podporován pro zpětnou kompatibilitu se zastaralými externími sítěmi
- Definován v IETF RFC a profilován pro použití v interworking scénářích 3GPP

## Související pojmy

- [CHAP – Challenge Handshake Authentication Protocol](/mobilnisite/slovnik/chap/)
- [PPP – Priority Precedence Preemption](/mobilnisite/slovnik/ppp/)
- [GPRS – CSI GPRS CAMEL Subscription Information](/mobilnisite/slovnik/gprs/)
- [AAA – Authentication, Authorization, and Accounting](/mobilnisite/slovnik/aaa/)
- [EAP – Extensible Authentication Protocol](/mobilnisite/slovnik/eap/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 23.179** (Rel-13) — MCPTT Functional Architecture
- **TS 23.379** (Rel-20) — MCPTT Functional Architecture
- **TS 24.008** (Rel-19) — 3GPP TS 24008: Core Network Protocols
- **TS 24.501** (Rel-19) — 5G NAS Protocols Specification
- **TS 29.061** (Rel-19) — Packet Domain Interworking for PLMN
- **TS 29.561** (Rel-19) — 5G Interworking with External Data Networks

---

📖 **Anglický originál a plná specifikace:** [PAP na 3GPP Explorer](https://3gpp-explorer.com/glossary/pap/)
