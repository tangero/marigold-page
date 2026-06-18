---
slug: "lwp"
url: "/mobilnisite/slovnik/lwp/"
type: "slovnik"
title: "LWP – Light-weight Protocol"
date: 2026-01-01
abbr: "LWP"
fullName: "Light-weight Protocol"
category: "Protocol"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/lwp/"
summary: "LWP je zjednodušený protokol zavedený ve 3GPP Release 17 pro zařízení s omezenými zdroji, zejména v IoT a průmyslových aplikacích. Snižuje signalizační režii a spotřebu energie a umožňuje efektivní ko"
---

LWP je zjednodušený 3GPP protokol navržený pro IoT zařízení s omezenými zdroji, jehož cílem je snížit signalizační režii a spotřebu energie a umožnit tak efektivní komunikaci pro obrovské množství jednoduchých senzorů a aktuátorů.

## Popis

Light-weight Protocol (LWP) je komunikační protokol definovaný ve specifikacích 3GPP, konkrétně v TS 23.434. Je navržen jako základní stavební prvek pro umožnění efektivního přenosu dat pro obrovské množství zařízení s nízkou složitostí. Architektonicky LWP funguje jako aplikační vrstvový protokol, který může být přenášen přes různé podkladové přenosové vrstvy, včetně Non-IP Data Delivery ([NIDD](/mobilnisite/slovnik/nidd/)) a IP spojení, což umožňuje flexibilitu nasazení. Jeho návrh je záměrně minimalistický a zaměřuje se na snížení složitosti protokolového zásobníku ve srovnání s tradičními protokoly, jako jsou [HTTP](/mobilnisite/slovnik/http/) nebo CoAP.

V jádru LWP funguje pomocí vysoce kompaktního formátu zpráv. Využívá efektivní kódovací schémata, jako je Concise Binary Object Representation ([CBOR](/mobilnisite/slovnik/cbor/)), pro minimalizaci velikosti přenosových datových jednotek ([PDU](/mobilnisite/slovnik/pdu/)). Protokol podporuje základní operace, jako je hlášení dat ze zařízení do sítě a doručování příkazů z aplikací do zařízení, ale odstranil funkce jako rozsáhlé zpracování chyb, správu relací a složité struktury hlaviček, které se nacházejí v robustnějších protokolech. Tato jednoduchost je klíčová pro jeho fungování v prostředích s omezenými zdroji.

Role protokolu v síti je fungovat jako rozhraní mezi uživatelským zařízením (UE) s omezenými zdroji a aplikačními servery, často prostřednictvím funkce pro vystavení sítě nebo vyhrazené LWP Adaptation Function (LWAF). Klíčové komponenty zahrnují LWP klienta na zařízení a LWP server v síti. LWAF může zvládat překlad protokolu, zabezpečení a adaptaci na servisní schopnosti. Přesunutím složitosti na síťovou stranu zůstává implementace v koncovém zařízení extrémně jednoduchá, což šetří jak výpočetní výkon, tak životnost baterie, což je klíčové pro dlouhodobá IoT nasazení.

## K čemu slouží

LWP byl vytvořen, aby řešil specifické výzvy scénářů massive Machine-Type Communication (mMTC) a Industrial IoT (IIoT) v sítích 5G a novějších. Předchozí IoT řešení často spoléhala na adaptaci stávajících internetových protokolů, které byly navrženy pro výkonné koncové body a bohatou výměnu dat. Protokoly jako [HTTP](/mobilnisite/slovnik/http/), MQTT nebo i CoAP, ačkoli jsou lehké ve srovnání s HTTP, stále zaváděly významnou režii z hlediska velikosti zpráv, navazování spojení a správy stavu pro ultrajednoduchá zařízení, jako jsou senzory nebo aktuátory.

Historický kontext je exponenciální růst IoT zařízení s různorodými požadavky. Mnoho z těchto zařízení potřebuje pouze posílat malé, nepravidelné datové pakety (např. teplotní údaje, stavové aktualizace), ale musí fungovat roky na jedné baterii. Omezení předchozích přístupů byla jejich energetická náročnost a spotřeba síťových zdrojů potřebná k udržování relací a zpracování podrobných hlaviček pro miliardy zařízení. LWP byl motivován potřebou nativního 3GPP protokolu optimalizovaného od základů pro toto prostředí s omezenými zdroji, který snižuje signalizační zátěž jak na zařízení, tak v jádru sítě, a tím umožňuje skutečně škálovatelná a efektivní nasazení massive IoT.

## Klíčové vlastnosti

- Ultra kompaktní kódování zpráv pomocí efektivních schémat jako CBOR
- Podpora přenosu jak přes Non-IP, tak IP-based data delivery
- Minimální požadavky na stav relace, umožňující provoz bez spojení
- Optimalizováno pro malá, nepravidelná hlášení dat a příkazy
- Adaptační funkce na síťové straně (LWAF) pro zvládnutí složitosti protokolu
- Snížená signalizační režie pro registraci zařízení a přenos dat

## Související pojmy

- [NIDD – Non-IP Data Delivery](/mobilnisite/slovnik/nidd/)

## Definující specifikace

- **TS 23.434** (Rel-20) — Service Enabler Architecture for Verticals

---

📖 **Anglický originál a plná specifikace:** [LWP na 3GPP Explorer](https://3gpp-explorer.com/glossary/lwp/)
