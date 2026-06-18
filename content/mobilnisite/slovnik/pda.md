---
slug: "pda"
url: "/mobilnisite/slovnik/pda/"
type: "slovnik"
title: "PDA – Personal Digital Assistant"
date: 2025-01-01
abbr: "PDA"
fullName: "Personal Digital Assistant"
category: "Other"
segment: "User Equipment"
canonical: "https://3gpp-explorer.com/glossary/pda/"
summary: "Ruční mobilní zařízení, často s dotykovým rozhraním, které kombinuje výpočetní funkce, telefon/fax a síťové funkce. V kontextu 3GPP je považováno za typ uživatelského terminálu (UE) schopného přístupu"
---

PDA (Personal Digital Assistant) je ruční mobilní zařízení, považované za typ uživatelského terminálu (UE), které kombinuje výpočetní a komunikační funkce pro přístup k mobilním sítím pro datové a hlasové služby.

## Popis

Personal Digital Assistant (PDA) je třída uživatelského terminálu (UE) definovaná ve specifikacích 3GPP. Jedná se o ruční výpočetní zařízení navržené pro správu osobních informací, které typicky zahrnuje funkce jako kalendář, adresář, poznámky a často také e-mail a webový prohlížeč. Z pohledu sítě 3GPP je PDA koncové zařízení, které se připojuje k mobilní síti, primárně přes rozhraní buněčného rádiového přístupu (jako UMTS nebo LTE), ale může podporovat i další konektivitu jako Wi-Fi. Zařízení komunikuje se sítí prostřednictvím standardizovaných protokolů a přenosových kanálů pro přístup k paketově přepínaným ([PS](/mobilnisite/slovnik/ps/)) a v dřívějších vydáních i k okruhově přepínaným ([CS](/mobilnisite/slovnik/cs/)) službám.

Z architektonického hlediska PDA obsahuje funkci mobilního ukončení ([MT](/mobilnisite/slovnik/mt/)), která zajišťuje rádiovou komunikaci s základnovou stanicí (Node B nebo eNodeB/gNB). Obsahuje také funkčnost koncového zařízení ([TE](/mobilnisite/slovnik/te/)), což je část zařízení pro zpracování aplikací (např. operační systém a uživatelské aplikace). MT komunikuje pomocí protokolů definovaných ve specifikacích rádiového přístupu a jádra sítě. Pro datové služby PDA navazuje kontexty Packet Data Protocol ([PDP](/mobilnisite/slovnik/pdp/)) nebo Packet Data Unit ([PDU](/mobilnisite/slovnik/pdu/)) relace, aby získalo IP adresu a přístup k datovým službám. Schopnosti zařízení, jako jsou podporovaná frekvenční pásma, výkonová třída a technologie rádiového přístupu, jsou definovány v konformních specifikacích.

Jeho role v síti je jako koncový bod pro komunikační služby. Síť PDA autentizuje (prostřednictvím jeho [USIM](/mobilnisite/slovnik/usim/)), spravuje jeho mobilitu (předávání hovorů, aktualizace oblasti sledování) a poskytuje mu přenosové kanály řízené kvalitou služeb (QoS) pro aplikace. Specifikace jako TS 22.800 (scénáře pro 5G) a TS 23.221 (architektonické požadavky) zahrnují PDA v rámci servisních požadavků. Specifikace pro správu (např. TS 32.808) definují, jak lze taková zařízení vzdáleně spravovat operátorem sítě. Zatímco termín 'PDA' je poněkud historický, v 3GPP formálně reprezentuje chytré, připojené mobilní zařízení předcházející moderním smartphonům.

## K čemu slouží

PDA jako třída zařízení 3GPP byla definována za účelem standardizace požadavků a chování pro rostoucí kategorii pokročilých ručních datově orientovaných terminálů. Před rozšířením smartphonů představovaly PDA významný krok v oblasti mobilních výpočetních zařízení, spojující osobní organizéry s bezdrátovou konektivitou. Jejich zařazení do standardů 3GPP zajistilo, že síťoví operátoři a výrobci zařízení mají společný rámec pro zajištění interoperability, výkonu a poskytování služeb pro tato zařízení.

Motivací bylo řešení omezení základních mobilních telefonů, které měly omezené datové a výpočetní schopnosti. PDA vyžadovaly robustnější datové služby, trvalé připojení a podporu pro IP aplikace. Jejich standardizace jako typu UE umožnila vývoj síťových funkcí přizpůsobených datově orientovaným vzorcům použití, což ovlivnilo aspekty kvality služeb (QoS), účtování a správy zařízení. Toto připravilo cestu pro vývoj směrem k modernímu smartphonu, který funkce PDA pohltil.

## Klíčové vlastnosti

- Definována jako třída uživatelského terminálu (UE) ve specifikacích 3GPP
- Schopna přístupu k okruhově přepínaným i paketově přepínaným síťovým službám
- Podporuje IP aplikace a služby přes mobilní přenosové kanály
- Podléhá konformnímu testování rádiového výkonu a výkonu protokolů
- Lze ji vzdáleně spravovat operátorem sítě (Device Management)
- Zohledněna v servisních požadavcích pro budoucí sítě (např. 5G)

## Související pojmy

- [USIM – Universal Subscriber Identity Module](/mobilnisite/slovnik/usim/)

## Definující specifikace

- **TS 22.800** (Rel-6) — IMS Subscription Scenarios Analysis
- **TR 22.944** (Rel-19) — UE Functionality Split Scenarios and Requirements
- **TS 23.221** (Rel-19) — 3GPP System Architectural Requirements
- **TS 23.234** (Rel-13) — 3GPP-WLAN Interworking Index
- **TS 26.131** (Rel-19) — Terminal Acoustic Performance Requirements
- **TS 26.132** (Rel-19) — Terminal Acoustic Test Methods
- **TS 32.808** (Rel-8) — Common User Profile Storage Framework
- **TS 37.544** (Rel-16) — UE Radiated Performance Test Procedures

---

📖 **Anglický originál a plná specifikace:** [PDA na 3GPP Explorer](https://3gpp-explorer.com/glossary/pda/)
