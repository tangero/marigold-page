---
slug: "mei"
url: "/mobilnisite/slovnik/mei/"
type: "slovnik"
title: "MEI – Mobile Equipment Identity"
date: 2025-01-01
abbr: "MEI"
fullName: "Mobile Equipment Identity"
category: "Identifier"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/mei/"
summary: "Globálně jednoznačný identifikátor mobilního zařízení (UE), odlišný od SIM karty uživatele. Síť jej používá pro identifikaci zařízení, sledování a bezpečnostní funkce, jako je například znepřístupnění"
---

MEI je globálně jednoznačný identifikátor mobilního zařízení, který síť využívá pro identifikaci zařízení, sledování a bezpečnostní funkce, jako je například zařazování na černou listinu.

## Popis

Mobile Equipment Identity (MEI) je klíčový identifikátor v systémech 3GPP, který jednoznačně rozlišuje fyzický hardware uživatelského zařízení (UE) od identity účastníka ([IMSI](/mobilnisite/slovnik/imsi/)) uložené na kartě UICC/[SIM](/mobilnisite/slovnik/sim/). Jedná se o trvalý, ve výrobě naprogramovaný identifikátor samotného mobilního terminálu. Nejběžnější a standardizovanou formou MEI je International Mobile Equipment Identity ([IMEI](/mobilnisite/slovnik/imei/)), což je 15místné desetinné číslo obsahující Type Allocation Code ([TAC](/mobilnisite/slovnik/tac/)), Serial Number ([SNR](/mobilnisite/slovnik/snr/)) a kontrolní číslici. Síť může požádat o MEI od UE během procedur, jako je připojování k síti (attachment), aktualizace polohy, nebo dle uvážení operátora, typicky prostřednictvím procesu dotazu na Equipment Identity Register ([EIR](/mobilnisite/slovnik/eir/)).

Z architektonického hlediska MEI využívají funkce jádra sítě, konkrétně Mobility Management Entity ([MME](/mobilnisite/slovnik/mme/)) v LTE nebo Access and Mobility Management Function ([AMF](/mobilnisite/slovnik/amf/)) v 5GC. Když se UE připojí k síti, může MME/AMF odeslat žádost o kontrolu MEI do Equipment Identity Register (EIR). EIR spravuje seznamy (bílý, šedý, černý) MEI. Síť tuto kontrolu využívá k ověření, zda je zařízení nahlášeno jako ukradené, vadné nebo jinak omezené v přístupu k síti. To poskytuje vrstvu zabezpečení a správy oddělenou od autentizace účastníka. MEI je přenášeno v dedikovaných zprávách NAS a RRC, jako je například Attach Request nebo UE Capability Information.

Princip jeho fungování je nedílnou součástí správy zařízení a bezpečnostních politik. Po obdržení MEI vrátí EIR odpověď udávající stav zařízení. Pokud je MEI na černé listině, síť může odmítnout službu nebo omezit služby dostupné danému zařízení, i když jsou přihlašovací údaje účastníka platné. To pomáhá v boji proti krádežím telefonů a podvodům. Dále se MEI používá pro statistické účely, identifikaci typu zařízení a pro podporu funkcí, jako je zákonné odposlouchávání. Jeho role zajišťuje, že řízení přístupu k síti může být vynucováno jak na úrovni účastníka (SIM), tak na úrovni zařízení, což operátorům poskytuje podrobné možnosti správy.

## K čemu slouží

MEI bylo standardizováno za účelem řešení problému podvodů a krádeží založených na zařízení, které nemohly být řešeny identifikátory založenými na účastníkovi, jako je IMSI. Před jeho rozšířeným zavedením mohl být ukradený mobilní telefon jednoduše používán s jinou SIM kartou, což znemožňovalo síti zařízení samotné pro účely zamítnutí služby vysledovat. MEI poskytuje neměnnou identitu hardwaru, která umožňuje síťovým operátorům zařadit konkrétní zařízení na černou listinu, čímž je učiní nepoužitelnými v jejich sítích, a tím sníží motivaci ke krádeži.

Jeho zavedení bylo také motivováno potřebou přesné identifikace zařízení z regulatorních, technických a komerčních důvodů. Regulační orgány mohou vyžadovat sledování typů zařízení pro certifikaci nebo shodu s předpisy. Technicky znalost přesného modelu zařízení (prostřednictvím části TAC v IMEI) pomáhá při správě kompatibility sítí a optimalizaci využití rádiových zdrojů pro konkrétní schopnosti zařízení. Komerčně napomáhá správě zásob, sledování záruk a porozumění penetraci zařízení v síti. MEI jako základní kámen systému EIR zavedlo zásadní, na zařízení zaměřenou vrstvu do celkového rámce zabezpečení a správy sítě.

## Klíčové vlastnosti

- Globálně jednoznačný identifikátor hardwaru mobilního zařízení
- Základ pro IMEI (International Mobile Equipment Identity)
- Používá se pro ověření zařízení proti Equipment Identity Register (EIR)
- Umožňuje zařazení zařízení na černou listinu pro ukradená nebo nevyhovující zařízení
- Odděluje identitu zařízení od identity účastníka (IMSI)
- Používá se v procedurách připojování k síti a správy zařízení

## Související pojmy

- [IMEI – International Mobile Station Equipment Identities](/mobilnisite/slovnik/imei/)
- [EIR – Equipment Identity Register](/mobilnisite/slovnik/eir/)
- [IMSI – International Mobile Subscriber Identity](/mobilnisite/slovnik/imsi/)

## Definující specifikace

- **TS 29.274** (Rel-19) — GTPv2-C Control Plane Protocol Specification

---

📖 **Anglický originál a plná specifikace:** [MEI na 3GPP Explorer](https://3gpp-explorer.com/glossary/mei/)
