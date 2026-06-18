---
slug: "uri"
url: "/mobilnisite/slovnik/uri/"
type: "slovnik"
title: "URI – Universal Resource Identifier"
date: 2026-01-01
abbr: "URI"
fullName: "Universal Resource Identifier"
category: "Other"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/uri/"
summary: "URI je obecný řetězcový identifikátor používaný napříč systémy 3GPP k pojmenování nebo lokalizaci zdrojů, jako jsou služby, uživatelé nebo síťové prvky. Je základním prvkem pro objevování služeb, zasí"
---

URI (Universal Resource Identifier) je obecný řetězcový identifikátor používaný napříč systémy 3GPP k pojmenování nebo lokalizaci zdrojů, jako jsou služby, uživatelé nebo síťové prvky, pro standardizované odkazování ve funkcích, jako je objevování služeb, zasílání zpráv a adresování v IMS.

## Popis

Universal Resource Identifier (URI) je v kontextu 3GPP kompaktní posloupnost znaků identifikující abstraktní nebo fyzický zdroj, která se řídí standardy [IETF](/mobilnisite/slovnik/ietf/) [RFC](/mobilnisite/slovnik/rfc/) 3986 a souvisejícími specifikacemi. Je hojně používána napříč specifikacemi 3GPP pro pojmenovávání, adresování a identifikaci entit, jako jsou uživatelé, služby, aplikace a síťové uzly. URI slouží jako společná syntaxe pro identifikátory zdrojů a umožňuje interoperabilitu mezi sítěmi 3GPP a širším internetovým ekosystémem. V architekturách, jako je IP Multimedia Subsystem (IMS), jsou URI klíčové pro uživatelské identity (např. [SIP](/mobilnisite/slovnik/sip/) URI ve tvaru sip:user@domain.com), identifikátory služeb a směrovací informace a tvoří základ pro navazování relací a vyvolávání služeb.

URI fungují tak, že poskytují strukturovaný formát zahrnující schéma (např. sip, tel, http), autoritu, cestu, dotazovací část a fragment. V rámci 3GPP jsou pro různé účely standardizována konkrétní schémata URI. Například SIP URI se používají pro uživatelské identity a směrování v IMS, tel URI pro telefonní čísla a [HTTP](/mobilnisite/slovnik/http/) URI pro webové služby. Když UE nebo síťový prvek potřebuje odkazovat na zdroj, vytvoří nebo parsuje URI podle těchto pravidel. Při registraci v IMS poskytne UE SIP URI jako svou veřejnou uživatelskou identitu, kterou Home Subscriber Server ([HSS](/mobilnisite/slovnik/hss/)) uloží a použije pro autentizaci a poskytování služeb. Směrovací mechanismy v Call Session Control Functions ([CSCF](/mobilnisite/slovnik/cscf/)) pak tyto URI používají k nasměrování signalizačních zpráv na správné koncové body.

Klíčové komponenty v 3GPP zahrnující URI zahrnují jádro IMS, kde jsou URI vloženy v hlavičkách SIP, jako jsou From, To a Contact; aplikační vrstvu služeb, která používá URI pro objevování služeb prostřednictvím Uniform Resource Names ([URN](/mobilnisite/slovnik/urn/)); a řídicí systémy, kde URI identifikují spravované objekty. Syntaxe URI umožňuje rozšiřitelnost a podporuje parametry přenášející dodatečné informace, jako jsou transportní protokoly nebo uživatelské preference. V službách zasílání zpráv, jako je [SMS](/mobilnisite/slovnik/sms/) over IP (SMSoIP) nebo multimediální zprávy, mohou URI specifikovat cílové adresy nebo umístění obsahu. Parsování a validaci URI provádějí protokolové zásobníky v UE a síťových funkcích, což zajišťuje konzistentní interpretaci napříč různými implementacemi.

Role URI v sítích 3GPP je mnohostranná: umožňuje identifikaci uživatele a směrování v IMS, usnadňuje zpřístupnění služeb prostřednictvím API (např. použitím URI v RESTful rozhraních) a podporuje lokalizaci zdrojů v řídicích protokolech, jako je OMA DM nebo řídicí služby 3GPP. Přijetím internetových standardů zajišťuje 3GPP, že mobilní sítě mohou hladce integrovat webové služby a aplikace. URI také podporují vývoj číslování a adresování a umožňují přechod od čísel E.164 k IP identifikátorům. Tato univerzálnost činí z URI základní kámen pro All-IP sítě, podporující vše od hlasových služeb přes LTE (VoLTE) až po komunikaci na servisní vrstvě pro IoT.

## K čemu slouží

Universal Resource Identifier (URI) byl do 3GPP začleněn, aby vyřešil potřebu standardizované a flexibilní identifikace zdrojů v rozvíjejících se mobilních sítích. Před jeho přijetím telekomunikační systémy silně závisely na číslech E.164 a proprietárních adresních schématech, která byla nedostatečná pro IP multimediální služby a internetovou interoperabilitu. Když se 3GPP s vydáním Release 5 posunulo k architekturám All-IP s IMS, vznikla potřeba univerzálního systému pojmenování, který by dokázal identifikovat různé zdroje – uživatele, služby, obsah – napříč heterogenními sítěmi. URI, jak je definuje IETF, poskytla dobře definovanou syntaxi, která mohla sjednotit adresování napříč telekomunikační a internetovou doménou.

URI řeší problémy fragmentace a nekompatibility v odkazování na zdroje. Umožňuje bezproblémové objevování služeb, zahájení relací a zasílání zpráv mezi mobilními zařízeními a internetovými servery. Například v IMS umožňují SIP URI identifikovat uživatele nezávisle na jejich zařízeních nebo umístění, což podporuje pokročilé komunikační služby. Bez URI by byla integrace webových technologií, jako jsou HTTP, e-mail nebo instant messaging, do mobilních sítí obtížná. URI také zajišťují budoucí odolnost adresování tím, že umožňují začlenění nových schémat a parametrů s vývojem služeb, například pro identifikátory zařízení IoT nebo API koncové body.

Historicky bylo přijetí URI v 3GPP motivováno konvergencí telekomunikací a IT, poháněnou nástupem multimediálních a datových služeb. Ve verzi 2 se objevilo první použití v zasílání zpráv, ale až s IMS se URI staly ústředními. Řešily omezení tradičních telekomunikačních identifikátorů tím, že podporovaly alfanumerické formáty, doménové směrování a rozšiřitelnost. To umožnilo sítím 3GPP nabízet inovativní služby, jako je přítomnost, videohovory a integrace s webem, a konkurovat tak OTT poskytovatelům. URI zůstávají klíčové pro architektury založené na službách a síťové segmentaci v 5G, kde zdroje potřebují jedinečné a škálovatelné identifikátory.

## Klíčové vlastnosti

- Standardizovaná syntax podle IETF RFC 3986 pro konzistentní parsování
- Podpora více schémat (např. sip, tel, http, urn) pro různé typy zdrojů
- Umožňuje identifikaci uživatelů a služeb v IMS a dalších systémech
- Umožňuje interoperabilitu s internetovými protokoly a službami
- Rozšiřitelné parametry pro dodatečný kontext nebo směrovací informace
- Používá se pro adresování v zasílání zpráv, řízení a API

## Související pojmy

- [SIP-URI – SIP Uniform Resource Identifier](/mobilnisite/slovnik/sip-uri/)
- [IMS – IP Multimedia Subsystem](/mobilnisite/slovnik/ims/)
- [URN – Uniform Resource Name](/mobilnisite/slovnik/urn/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 22.495** (Rel-7) — NGN Requirements for IMS Services
- **TR 22.977** (Rel-19) — Speech Enabled Services and Multimodal Framework
- **TS 23.057** (Rel-19) — Mobile Execution Environment (MExE) Specification
- **TS 23.140** (Rel-6) — MMS Non-Realtime Service Definition
- **TS 23.179** (Rel-13) — MCPTT Functional Architecture
- **TS 23.222** (Rel-19) — Common API Framework for 3GPP Northbound APIs
- **TS 23.280** (Rel-20) — Common Architecture for Mission Critical Services
- **TS 23.283** (Rel-20) — Mission Critical Communication Interworking
- **TS 23.379** (Rel-20) — MCPTT Functional Architecture
- **TS 23.700** (Rel-20) — XR Services Application Enablement Layer
- **TS 23.722** (Rel-15) — Common API Framework (CAPIF) for 3GPP Northbound APIs
- **TR 23.758** (Rel-17) — Study on Edge Application Architecture
- **TS 23.782** (Rel-15) — Interworking between LTE MC and non-LTE MC systems
- **TR 23.783** (Rel-18) — Technical Report on Mission Critical Services over 5GS
- … a dalších 80 specifikací

---

📖 **Anglický originál a plná specifikace:** [URI na 3GPP Explorer](https://3gpp-explorer.com/glossary/uri/)
