---
slug: "uesbi"
url: "/mobilnisite/slovnik/uesbi/"
type: "slovnik"
title: "UESBI – UE Specific Behaviour Information"
date: 2025-01-01
abbr: "UESBI"
fullName: "UE Specific Behaviour Information"
category: "Management"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/uesbi/"
summary: "Informace o specifickém chování uživatelského zařízení (UESBI) je soubor datových prvků charakterizujících jedinečné provozní vzorce a schopnosti uživatelského zařízení (UE). Síť je využívá k optimali"
---

UESBI je soubor datových prvků charakterizujících jedinečné provozní vzorce a schopnosti uživatelského zařízení (User Equipment), které síť využívá k optimalizaci alokace prostředků, správy mobility a poskytování služeb.

## Popis

Informace o specifickém chování uživatelského zařízení (UESBI) je komplexní profil nebo soubor parametrů popisujících charakteristiky chování a provozní vzorce konkrétního uživatelského zařízení (UE) v rámci sítě 3GPP. Definováno napříč specifikacemi jako TS 23.009, TS 23.195 a TS 43.051, zahrnuje data přesahující statické hlášení schopností (UE Capability). UESBI je dynamicky získáváno, odvozováno nebo hlášeno v čase a je využíváno různými síťovými funkcemi k přizpůsobení jejich chování.

Z architektonického hlediska není UESBI uloženo v jediném úložišti, ale využívají ho různé síťové entity. Mezi klíčové zapojené komponenty patří funkce pro správu přístupu a mobility ([AMF](/mobilnisite/slovnik/amf/)) a funkce pro správu relací ([SMF](/mobilnisite/slovnik/smf/)) v 5GC, entita pro správu mobility ([MME](/mobilnisite/slovnik/mme/)) v EPS a uzly rádiové přístupové sítě (RAN). Informace mohou být odvozeny z historických informací o UE (např. často navštěvované oblasti sledování, vzorce mobility), pozorovaného chování UE (např. typická aktivita relací paketových datových jednotek, preference úspory energie) a explicitních indikací nebo konfigurací od UE.

Jak to funguje, zahrnuje průběžné sledování a aplikaci. Síť monitoruje aktivity UE, jako je četnost předávání (handover), připojení v závislosti na denní době, vzorce navazování datových relací a interakce s funkcemi úspory energie, jako je režim úspory energie ([PSM](/mobilnisite/slovnik/psm/)) nebo rozšířené nespojité příjmy (eDRX). Tyto shromážděné informace tvoří UESBI. Síťové funkce pak tyto informace aplikují v algoritmech; například AMF může použít vzorce mobility k optimalizaci strategií pagingu nebo předvídání předávání, zatímco SMF může použít vzorce aktivity relací k efektivnější správě životního cyklu relací protokolových datových jednotek ([PDU](/mobilnisite/slovnik/pdu/)).

Jeho role spočívá v umožnění kontextově-aware a prediktivní optimalizace sítě. Porozuměním tomu, že UE je například stacionární IoT senzor, vysoce mobilní vozidlo nebo smartphone s periodickou synchronizací na pozadí, může síť činit chytřejší rozhodnutí. To snižuje signalizační režii (např. zbytečné aktualizace polohy), šetří životnost baterie UE díky lépe přizpůsobeným konfiguracím úspory energie, zlepšuje využití rádiových prostředků a zvyšuje spolehlivost procedur mobility, jako je předávání. Je to klíčový prvek pro inteligentní, na UE zaměřenou správu sítě.

## K čemu slouží

UESBI bylo vyvinuto k řešení univerzálního přístupu časných mobilních sítí, kde byly síťové politiky z velké části aplikovány jednotně bez ohledu na velké rozdíly v typech UE a vzorcích používání. To bylo neefektivní a vedlo k zbytečné signalizační zátěži, suboptimální životnosti baterie pro IoT zařízení a špatné alokaci prostředků pro specializovaná UE. Síti chyběla inteligence k přizpůsobení se specifickému 'chování' každého zařízení.

Řeší problém plýtvání síťovými prostředky a zhoršování služeb v heterogenním prostředí zařízení. S explozí IoT zařízení, každého s jedinečnými vzorci provozu (např. občasný přenos malých dat), a příchodem pokročilých typů UE, jako jsou vozidla a nositelná zařízení, se statické síťové konfigurace staly hlavním omezením. UESBI poskytuje potřebný vstup pro síťové funkce, aby dynamicky optimalizovaly své chování pro každé UE, což vede k masivnímu zlepšení škálovatelnosti, zejména pro scénáře hromadné komunikace strojového typu (mMTC).

Jeho vývoj od Release 2 (éra GSM) až po Release 19 ukazuje jeho zásadní a rostoucí význam. Zpočátku byly zvažovány koncepty jako vzorce mobility. Pozdější vydání, zejména s LTE a 5G, formalizovala a rozšířila UESBI o detailní chování týkající se úspory energie, vzorce aktivity relací a integraci se síťovou analytikou. Tento historický kontext podtrhuje posun od síťově-centrického k uživatelsky-centrickému a službám-aware provozu, kde porozumění chování zařízení je stejně kritické jako znalost jeho technických schopností.

## Klíčové vlastnosti

- Zachycuje dynamické charakteristiky UE, jako jsou vzorce mobility a historie aktivity relací
- Používá se k optimalizaci strategií pagingu a aktualizací oblastí sledování na základě mobility UE
- Informuje o konfiguraci parametrů úspory energie (např. PSM, eDRX) pro prodloužení životnosti baterie
- Umožňuje prediktivní rezervaci prostředků a přípravu na předávání (handover)
- Podporuje síťové slicing přiřazováním chování UE konkrétním instancím řezů
- Usnadňuje vyvažování zátěže a řízení zahlcení prostřednictvím předpovědi provozu specifické pro UE

## Definující specifikace

- **TS 23.009** (Rel-19) — Handover Procedures in PLMNs
- **TS 23.195** (Rel-5) — UE Specific Behaviour Information Mechanism
- **TS 23.895** (Rel-6) — UE Specific Behaviour Information Signalling
- **TS 43.051** (Rel-19) — GERAN Stage 2 Service Description

---

📖 **Anglický originál a plná specifikace:** [UESBI na 3GPP Explorer](https://3gpp-explorer.com/glossary/uesbi/)
