---
slug: "scvp"
url: "/mobilnisite/slovnik/scvp/"
type: "slovnik"
title: "SCVP – Simple Certificate Validation Protocol"
date: 2025-01-01
abbr: "SCVP"
fullName: "Simple Certificate Validation Protocol"
category: "Security"
segment: "User Equipment"
canonical: "https://3gpp-explorer.com/glossary/scvp/"
summary: "Protokol umožňující klientovi delegovat složitou validaci certifikační cesty a kontrolu stavu na důvěryhodný server. Zjednodušuje validaci certifikátů pro zařízení s omezenými prostředky přesunutím vý"
---

SCVP je protokol, který umožňuje klientovi delegovat složitou validaci certifikační cesty a kontrolu stavu na důvěryhodný server, čímž zjednodušuje operace pro zařízení s omezenými prostředky v sítích 3GPP.

## Popis

Simple Certificate Validation Protocol (SCVP) je protokol typu klient-server definovaný [IETF](/mobilnisite/slovnik/ietf/) ([RFC](/mobilnisite/slovnik/rfc/) 5055) a přijatý ve specifikacích 3GPP. Jeho hlavní funkcí je umožnit klientovi, který může mít omezené výpočetní prostředky nebo neúplné informace o důvěryhodných kořenových certifikátech, delegovat složitý proces validace certifikační cesty na důvěryhodný SCVP server. Klient odešle požadavek obsahující certifikát k ověření spolu s požadavky na validační politiku a případným potřebným kontextem. SCVP server následně provede kompletní validaci, která zahrnuje sestavení a ověření certifikační cesty zpět k důvěryhodnému kořeni, kontrolu stavu odvolání certifikátu (např. prostřednictvím [CRL](/mobilnisite/slovnik/crl/) nebo [OCSP](/mobilnisite/slovnik/ocsp/)) a aplikaci požadované validační politiky. Server vrátí klientovi podrobnou odpověď udávající, zda je certifikát platný, a pokud ne, konkrétní důvody selhání. Tato architektura centralizuje složitou logiku [PKI](/mobilnisite/slovnik/pki/) a správu důvěryhodných kořenů na straně serveru. V systémech 3GPP je SCVP specifikován pro použití ve scénářích vyžadujících validaci certifikátů, jako je Generic Bootstrapping Architecture ([GBA](/mobilnisite/slovnik/gba/)) nebo pro ověřování certifikátů používaných v síťových aplikacích, a poskytuje standardizovaný, spolehlivý mechanismus pro zajištění důvěry v digitální certifikáty bez zatěžování koncového zařízení.

## K čemu slouží

SCVP byl vytvořen k řešení výzev spojených s validací certifikátů veřejného klíče v prostředích s omezenými zařízeními nebo tam, kde je místní správa [PKI](/mobilnisite/slovnik/pki/) nepraktická. Tradiční validace certifikátů vyžaduje, aby klient měl aktuální důvěryhodné kořenové certifikáty, prováděl objevování cesty a kontroloval stav odvolání, což je výpočetně náročné a vyžaduje neustálé aktualizace. Pro mobilní zařízení s omezeným výpočetním výkonem, výdrží baterie nebo úložnou kapacitou je toto významná zátěž. SCVP tento problém řeší přesunutím těchto složitých úloh na specializovaný, vždy aktualizovaný server v důvěryhodné doméně operátora sítě. To zajišťuje, že se i jednoduchá zařízení mohou účastnit bezpečné autentizace a autorizace založené na certifikátech. Jeho přijetí v 3GPP, počínaje Release 10, bylo motivováno potřebou standardizované a efektivní metody pro validaci certifikátů v rámci síťových architektur, jako je [GBA](/mobilnisite/slovnik/gba/), což umožňuje bezpečný přístup ke službám a zjednodušuje implementaci bezpečnostních protokolů napříč různými možnostmi UE.

## Klíčové vlastnosti

- Deleguje složitou validaci certifikační cesty a kontrolu odvolání na server
- Definuje jasný protokol typu požadavek/odpověď mezi klientem a serverem (CVRequest/CVResponse)
- Podporuje specifikaci validačních politik a kontextu v požadavcích
- Vrací podrobné výsledky validace včetně úspěchu/selhání a kódů důvodů
- Snižuje výpočetní a úložné nároky na klientech s omezenými prostředky
- Centralizuje správu důvěryhodných kořenových certifikátů a certifikačních politik na serveru

## Definující specifikace

- **TS 23.057** (Rel-19) — Mobile Execution Environment (MExE) Specification

---

📖 **Anglický originál a plná specifikace:** [SCVP na 3GPP Explorer](https://3gpp-explorer.com/glossary/scvp/)
