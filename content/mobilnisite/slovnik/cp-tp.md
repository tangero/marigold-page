---
slug: "cp-tp"
url: "/mobilnisite/slovnik/cp-tp/"
type: "slovnik"
title: "CP-TP – Certificate Present (in the MExE (U)SIM) - Third Party"
date: 2025-01-01
abbr: "CP-TP"
fullName: "Certificate Present (in the MExE (U)SIM) - Third Party"
category: "Security"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/cp-tp/"
summary: "CP-TP je bezpečnostní mechanismus v rámci architektury MExE (Mobile Execution Environment), který se konkrétně týká certifikátů třetích stran uložených na (U)SIM. Umožňuje bezpečnou autentizaci a auto"
---

CP-TP je bezpečnostní mechanismus MExE pro certifikáty třetích stran uložené na (U)SIM, který umožňuje bezpečnou autentizaci a autorizaci pro důvěryhodné aplikace a služby třetích stran.

## Popis

CP-TP, neboli Certificate Present (in the MExE (U)[SIM](/mobilnisite/slovnik/sim/)) - Third Party, je bezpečnostní koncept definovaný ve specifikacích 3GPP Mobile Execution Environment (MExE). MExE poskytuje standardizované výkonové prostředí na mobilních zařízeních, které umožňuje bezpečné stahování a spouštění aplikací. CP-TP konkrétně řeší uložení a správu digitálních certifikátů od subjektů třetích stran (tj. nikoli od mobilního operátora nebo výrobce zařízení) na modulu Universal Subscriber Identity Module ([USIM](/mobilnisite/slovnik/usim/)) nebo SIM kartě. Tyto certifikáty se používají k navázání důvěry mezi mobilním zařízením a externími poskytovateli služeb, jako jsou bankovní aplikace, podnikové sítě [VPN](/mobilnisite/slovnik/vpn/) nebo poskytovatelé obsahu.

Architektura využívá (U)SIM jako bezpečný prvek, což je odolná hardwarová komponenta odolná vůči neoprávněným zásahům. (U)SIM obsahuje vyhrazený souborový systém a bezpečnostní domény. Certifikáty třetích stran jsou uloženy v chráněné oblasti souborového systému (U)SIM, často asociované s konkrétní bezpečnostní doménou nebo aplikací. Když se potřebuje poskytovatel služeb MExE třetí strany ([SP](/mobilnisite/slovnik/sp/)) autentizovat vůči zařízení nebo naopak, příslušný certifikát je načten z (U)SIM. Klient MExE v zařízení pak tento certifikát použije v kryptografických protokolech, jako je [TLS](/mobilnisite/slovnik/tls/)/[SSL](/mobilnisite/slovnik/ssl/), k ověření identity SP nebo k podepsání/zašifrování dat.

Klíčové komponenty zahrnují MExE User Agent (klientský software v zařízení), MExE Service Provider, (U)SIM s jeho zabezpečeným souborovým systémem a certifikační autoritu ([CA](/mobilnisite/slovnik/ca/)), která certifikát třetí strany vydala. Proces funguje tak, že SP předloží svůj certifikát během handshake. MExE User Agent zkontroluje, zda je odpovídající důvěryhodný certifikát přítomen v úložišti CP-TP na (U)SIM. Pokud je přítomen a platný (neexpirovaný, řádně podepsaný důvěryhodnou CA), může agent SP autentizovat. Tento mechanismus je nedílnou součástí systému bezpečnostních tříd (classmark) MExE, který definuje schopnosti zařízení a úrovně zabezpečení.

Role CP-TP v síti spočívá v rozšíření modelu důvěry mimo doménu operátora. Zatímco (U)SIM inherentně obsahuje přihlašovací údaje operátora pro přístup k síti, CP-TP mu umožňuje sloužit také jako kotva důvěry pro externí služby. To umožňuje bezpečnou autentizaci založenou na zařízení pro širokou škálu aplikací bez nutnosti samostatných hardwarových bezpečnostních tokenů. Tvoří součást širšího bezpečnostního rámce MExE, který zahrnuje další classmarky pro integritu zařízení, autentizaci uživatele a zabezpečené komunikační kanály.

## K čemu slouží

CP-TP byl vytvořen k řešení potřeby bezpečného poskytování služeb třetích stran na mobilních zařízeních v rámci architektury MExE. Jak se mobilní telefony vyvíjely z hlasové komunikace na zařízení podporující stahovatelné aplikace a služby (jako byly rané mobilní bankovnictví, e-mail nebo podnikový přístup), standardizovaná metoda pro navázání důvěry mezi zařízením a poskytovateli služeb mimo operátora se stala nezbytnou. Před takovou standardizací byla bezpečnostní řešení specifická pro služby roztříštěná a často spoléhala na méně bezpečné softwarové úložiště přihlašovacích údajů nebo proprietární hardware, což bránilo interoperabilitě a škálovatelnosti.

Primární problém, který CP-TP řeší, je bezpečné uložení a správa autentizačních přihlašovacích údajů třetích stran. Bez bezpečného, standardizovaného umístění, jako je (U)[SIM](/mobilnisite/slovnik/sim/), mohly být certifikáty uloženy v paměti zařízení, což je činilo zranitelnými vůči odcizení, klonování nebo neoprávněným zásahům. (U)SIM jako široce rozšířená, fyzicky zabezpečená komponenta poskytuje důvěryhodné prostředí. CP-TP to využívá k umožnění společné, vysoce spolehlivé metody pro autentizaci služeb vůči zařízením a pro prokázání identity zařízení vůči službám, což usnadňuje růst bezpečného ekosystému mobilních aplikací.

Historicky byl MExE zaveden k vytvoření prostředí podobného Javě pro mobilní zařízení (podobně jako rané J2ME). Bezpečnost byla prvořadým zájmem operátorů a poskytovatelů služeb pro ochranu citlivých transakcí a dat. CP-TP jako součást bezpečnostní architektury MExE definované ve 3GPP Release 4 poskytl jasnou specifikaci pro nakládání s důvěryhodnými přihlašovacími údaji třetích stran, což podpořilo jeho přijetí tím, že dalo poskytovatelům služeb důvěru v autentizační mechanismus. Řešil omezení ad-hoc přístupů tím, že poskytl standardizované řešení s hardwarovou podporou integrované s modulem identifikace účastníka.

## Klíčové vlastnosti

- Bezpečné uložení digitálních certifikátů třetích stran X.509 na (U)SIM
- Umožňuje autentizaci poskytovatelů služeb MExE vůči mobilnímu zařízení
- Usnadňuje autentizaci zařízení vůči službám třetích stran pomocí přihlašovacích údajů založených na certifikátech
- Integruje se se systémem bezpečnostních tříd (classmark) MExE pro vyjednávání schopností
- Využívá odolný hardware (U)SIM odolný vůči neoprávněným zásahům pro ochranu klíčů
- Podporuje navázání zabezpečených komunikačních kanálů (např. TLS) pro aplikační data

## Související pojmy

- [USIM – Universal Subscriber Identity Module](/mobilnisite/slovnik/usim/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 23.057** (Rel-19) — Mobile Execution Environment (MExE) Specification

---

📖 **Anglický originál a plná specifikace:** [CP-TP na 3GPP Explorer](https://3gpp-explorer.com/glossary/cp-tp/)
