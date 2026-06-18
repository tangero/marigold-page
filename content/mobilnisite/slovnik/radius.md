---
slug: "radius"
url: "/mobilnisite/slovnik/radius/"
type: "slovnik"
title: "RADIUS – Remote Authentication Dial In User Service"
date: 2025-01-01
abbr: "RADIUS"
fullName: "Remote Authentication Dial In User Service"
category: "Protocol"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/radius/"
summary: "Široce rozšířený síťový protokol poskytující centralizovanou správu ověřování, autorizace a účtování (AAA) pro uživatele připojující se k síti. V 3GPP se používá pro interoperabilitu s přístupovými sí"
---

RADIUS je široce nasazený AAA protokol používaný v 3GPP pro interoperabilitu s přístupovými sítěmi mimo 3GPP a pro některé funkce řízení politik.

## Popis

Remote Authentication Dial In User Service (RADIUS) je protokol typu klient-server, původně definovaný [IETF](/mobilnisite/slovnik/ietf/) ([RFC](/mobilnisite/slovnik/rfc/) 2865, 2866), pro přenos informací o ověřování, autorizaci a účtování ([AAA](/mobilnisite/slovnik/aaa/)). V architektuře 3GPP není RADIUS nativním 3GPP protokolem, ale je specifikován pro interoperabilitu, především pro rozhraní s důvěryhodnými nebo nedůvěryhodnými IP přístupovými sítěmi mimo 3GPP, jako jsou bezdrátové lokální sítě ([WLAN](/mobilnisite/slovnik/wlan/)), pevné širokopásmové připojení nebo WiMAX, když se integrují s 3GPP jádrovou sítí.

V systémech 3GPP se RADIUS klient typicky nachází v síťovém přístupovém bránovém uzlu (např. WLAN Access Gateway, evolved Packet Data Gateway (ePDG) pro nedůvěryhodný přístup nebo Trusted WLAN Access Gateway ([TWAG](/mobilnisite/slovnik/twag/))). RADIUS server je součástí 3GPP AAA infrastruktury, která zahrnuje AAA Server a často komunikuje s Home Subscriber Server ([HSS](/mobilnisite/slovnik/hss/)) pro ověření přihlašovacích údajů. Protokol funguje přes [UDP](/mobilnisite/slovnik/udp/), přičemž pro zabezpečení zpráv používá sdílené tajemství mezi klientem a serverem. Proces začíná, když se uživatelské zařízení pokusí připojit přes přístup mimo 3GPP. Přístupová brána shromáždí uživatelské přihlašovací údaje (jako Network Access Identifier - [NAI](/mobilnisite/slovnik/nai/)) a odešle zprávu RADIUS Access-Request na 3GPP AAA Server.

3GPP AAA Server ověří uživatele dotazem na HSS pomocí rozhraní založených na Diameteru (jako SWx), ale výsledek je zpět do přístupové sítě přenesen pomocí RADIUS. Po úspěšném ověření AAA server odpoví zprávou RADIUS Access-Accept, která obsahuje autorizační parametry. Tyto parametry jsou klíčové a mohou zahrnovat profil kvality služeb (QoS) předplacený uživatelem, povolené názvy přístupových bodů (APN) a důležité informace o tunelování. Například v případě důvěryhodného přístupu WLAN k EPC může Access-Accept autorizovat vytvoření GTP tunelu mezi TWAG a PGW a poskytnout IP adresu PGW. Zprávy RADIUS Accounting (Accounting-Request/Response) se používají pro hlášení začátku relace, průběžných aktualizací a událostí ukončení pro účely fakturace a monitorování.

Role RADIUS v 3GPP je tedy role mostního protokolu, který umožňuje starším nebo přístupovým sítím mimo 3GPP, které široce podporují RADIUS, integrovat se s 3GPP AAA rámcem. Umožňuje operátorům využít stávající infrastrukturu WLAN pro přesun dat z mobilní sítě nebo konvergenci. Protokol přenáší atributy specifické pro 3GPP ve Vendor-Specific Attributes (VSA), aby přenesl potřebné informace zaměřené na mobilní sítě (např. 3GPP-Charging-Characteristics, 3GPP-APN) mezi bránou mimo 3GPP a 3GPP jádrem.

## K čemu slouží

RADIUS byl přijat do standardů 3GPP, aby vyřešil problém integrace heterogenních přístupových technologií, konkrétně IP přístupových sítí mimo 3GPP jako WLAN, do jednotného 3GPP servisního rámce. Když mobilní operátoři začali nabízet hotspoty WLAN, potřebovali způsob, jak rozšířit své systémy ověřování účastníků, vynucování politik a účtování na tyto nové přístupové body. RADIUS byl de facto standardní AAA protokol ve světě IP sítí, což z něj učinilo přirozenou volbu pro tuto interoperabilitu.

Jeho zahrnutí řešilo omezení spočívající v oddělených, izolovaných systémech ověřování pro mobilní síť a WLAN. Bez protokolu jako RADIUS by museli operátoři spravovat zcela oddělené databáze uživatelů a fakturační systémy pro přístup WLAN, což by bránilo bezproblémovému uživatelskému zážitku. Specifikací způsobu interakce RADIUS s 3GPP infrastrukturou HSS/AAA umožnilo 3GPP 'ověřování založené na SIM kartě' pro WLAN, což uživatelům umožnilo připojit se pomocí přihlašovacích údajů z mobilního předplatného, což byl klíčový krok k pevně-mobilní konvergenci.

Motivace byla hnána komerční potřebou přesunu dat a kontinuity služeb. RADIUS poskytl osvědčený, škálovatelný a široce implementovaný protokol k překlenutí mezery mezi paketově orientovaným IP světem WLAN a telekomunikačně inspirovaným jádrem sítí 3GPP založeným na Diameteru. Umožnil operátorům znovu využít stávající investice do infrastruktury WLAN při zachování centralizované kontroly nad správou účastníků a politikami, což bylo zásadní pro vytváření integrovaných fakturačních a servisních plánů.

## Klíčové vlastnosti

- Protokol klient-server pro ověřování, autorizaci a účtování (AAA)
- Používá transport přes UDP s transakčním modelem požadavek/odpověď
- Podporuje rozšiřitelné dvojice atribut-hodnota (AVP) pro výměnu informací
- Využívá Vendor-Specific Attributes (VSA) pro parametry specifické pro 3GPP
- Poskytuje integritu a zabezpečení zpráv pomocí sdílených tajemství
- Umožňuje integraci přístupových sítí mimo 3GPP s 3GPP jádrem

## Související pojmy

- [HSS – Home Subscriber Server](/mobilnisite/slovnik/hss/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 23.140** (Rel-6) — MMS Non-Realtime Service Definition
- **TR 23.923** (Rel-4) — Mobile IP+ Feasibility Study for UMTS/GPRS
- **TS 29.061** (Rel-19) — Packet Domain Interworking for PLMN
- **TS 29.161** (Rel-12) — 3GPP-WLAN Interworking Requirements
- **TS 29.234** (Rel-11) — WLAN-3GPP Interworking Stage-3 Protocol
- **TS 32.808** (Rel-8) — Common User Profile Storage Framework

---

📖 **Anglický originál a plná specifikace:** [RADIUS na 3GPP Explorer](https://3gpp-explorer.com/glossary/radius/)
