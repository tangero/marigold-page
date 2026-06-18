---
slug: "tau"
url: "/mobilnisite/slovnik/tau/"
type: "slovnik"
title: "TAU – Tracking Area Update"
date: 2026-01-01
abbr: "TAU"
fullName: "Tracking Area Update"
category: "Mobility"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/tau/"
summary: "Procedura prováděná uživatelským zařízením (UE) v sítích LTE a 5G za účelem aktualizace sítě o jeho aktuální umístění v oblasti sledování (Tracking Area, TA). Umožňuje efektivní vyhledávání a správu m"
---

TAU je procedura, při které mobilní zařízení aktualizuje síť o své aktuální umístění v oblasti sledování (Tracking Area), aby umožnilo efektivní vyhledávání (paging) a správu mobility pro příchozí hovory nebo datové relace.

## Popis

Aktualizace oblasti sledování (Tracking Area Update, TAU) je základní procedura správy mobility v 3GPP EPS (Evolved Packet System) pro LTE a pokračuje v 5GS (5G System). Je iniciována uživatelským zařízením (UE), když zjistí, že vstoupilo do nové oblasti sledování (Tracking Area, [TA](/mobilnisite/slovnik/ta/)), která není v jeho registrovaném seznamu TA, nebo periodicky na základě časovače. Oblast sledování je logické seskupení buněk definované pro účely lokalizace a efektivity vyhledávání. Primárním účelem TAU je informovat jádro sítě – konkrétně Mobility Management Entity ([MME](/mobilnisite/slovnik/mme/)) v LTE nebo funkci Access and Mobility Management Function ([AMF](/mobilnisite/slovnik/amf/)) v 5G – o aktuální poloze UE na úrovni TA, což síti umožňuje efektivně vyhledat UE, když jsou k dispozici downlink data nebo příchozí hovor.

Procedura zahrnuje signalizační zprávy mezi UE a sítí. Když se UE v klidovém režimu (ECM-IDLE v LTE, CM-IDLE v 5G) pohybuje a vybere novou buňku, přečte identifikaci oblasti sledování (Tracking Area Identity, [TAI](/mobilnisite/slovnik/tai/)) vysílanou v systémové informaci. Pokud tato TAI není v seznamu TAI, který UE obdrželo během poslední procedury připojení (Attach) nebo TAU (registrovaný seznam TAI), UE iniciuje zprávu TAU Request směrem k síti přes vybranou základnovou stanici ([eNB](/mobilnisite/slovnik/enb/) v LTE, gNB v 5G). Tato zpráva je přeposlána MME/AMF. MME/AMF následně aktualizuje svůj lokalizační kontext pro UE, může provést autentizační a bezpečnostní procedury a vrátí zprávu TAU Accept obsahující nový registrovaný seznam TA a případně nový dočasný identifikátor ([GUTI](/mobilnisite/slovnik/guti/) v LTE, [5G-GUTI](/mobilnisite/slovnik/5g-guti/) v 5G). Pokud se UE přesouvá do TA obsluhované jiným MME/AMF, dojde k mezilehlému TAU (inter-MME nebo inter-AMF TAU), které zahrnuje přenos kontextu mezi starým a novým uzlem jádra.

TAU je klíčové pro vyvážení signalizační zátěže a režie vyhledávání. Seskupením buněk do TA síť nemusí znát přesnou buňku UE; potřebuje vyhledat UE pouze ve všech buňkách jeho poslední známé TA. Procedura TAU zajišťuje, že tato poloha na úrovni TA je udržována aktuální. Síť může přiřadit UE seznam více TA (TA List), aby snížila frekvenci signalizace TAU – UE se může pohybovat ve všech TA v seznamu bez provedení aktualizace. Parametry řídící TAU, jako je periodický časovač TAU (T3412), jsou vysílány sítí a nastaveny v předplatném UE. TAU také slouží k opětovnému navázání síťové konektivity, aktualizaci bezpečnostních klíčů a může spustit další procedury, jako je modifikace přenosových kanálů (bearer).

## K čemu slouží

Procedura TAU byla zavedena s evolucí systémové architektury (System Architecture Evolution, [SAE](/mobilnisite/slovnik/sae/)) v 3GPP Release 8 pro LTE, aby odstranila omezení správy polohy v předchozích systémech 3GPP. V sítích 2G/3G se aktualizace polohy prováděly na úrovni lokální oblasti (Location Area, LA) nebo směrovací oblasti (Routing Area, RA), které byly relativně statické a mohly vést k neefektivnímu vyhledávání nebo nadměrné signalizaci ve scénářích s vysokou mobilitou. TAU, s konceptem konfigurovatelných oblastí sledování a seznamů TA, poskytuje flexibilnější a škálovatelnější mechanismus optimalizovaný pro plně IP, plošší architekturu EPS.

Řeší kritický problém, jak efektivně lokalizovat UE v klidovém režimu v paketově přepínané síti bez trvalého připojení. Efektivní sledování polohy je nezbytné pro služby iniciované sítí, jako jsou hlasové hovory (VoLTE) a push notifikace. TAU ve srovnání s aktualizacemi na úrovni buňky snižuje nepotřebnou signalizaci a zároveň udržuje oblasti vyhledávání optimálně velké. Možnost přiřadit seznam TA umožňuje síti přizpůsobit správu mobility vzorci pohybu uživatele – například často se pohybujícímu UE lze přiřazovat větší seznam TA, aby se minimalizovaly aktualizace. Tento návrh byl motivován potřebou podporovat trvalé připojení (always-on) s minimální spotřebou baterie na UE a sníženou signalizační zátěží na síti, což jsou klíčové požadavky pro vysokokapacitní sítě LTE a 5G.

## Klíčové vlastnosti

- Aktualizuje síť o aktuální polohu UE v oblasti sledování (Tracking Area)
- Spuštěna při vstupu do nové TA mimo registrovaný seznam TA nebo periodicky
- Umožňuje efektivní síťové vyhledávání (paging) pro transakce iniciované sítí
- Může zahrnovat přesun MME/AMF (mezilehlý TAU)
- Obnovuje signalizační konektivitu a může aktualizovat bezpečnostní kontext
- Používá konfigurovatelný seznam TA (TA List) ke snížení frekvence signalizace pro pohyblivá UE

## Související pojmy

- [GUTI – Globally Unique Temporary UE Identity](/mobilnisite/slovnik/guti/)

## Definující specifikace

- **TS 23.271** (Rel-19) — LCS Stage 2 Specification
- **TS 23.401** (Rel-19) — Evolved Packet System (EPS) Stage 2 Description
- **TS 23.700** (Rel-20) — XR Services Application Enablement Layer
- **TS 29.303** (Rel-19) — DNS Procedures for Evolved Packet System
- **TS 29.305** (Rel-19) — Interworking Functions for EPS-Legacy Systems
- **TS 29.805** (Rel-8) — IWF for MAP-Diameter Interworking
- **TS 32.422** (Rel-20) — Telecom Management: Trace Control & Configuration
- **TS 33.108** (Rel-19) — LI Handover Interface Specification
- **TS 33.401** (Rel-19) — EPS Security Architecture
- **TS 33.859** (Rel-11) — UTRAN Key Hierarchy Enhancement Study
- **TR 36.763** (Rel-17) — NB-IoT/eMTC Support for Non-Terrestrial Networks
- **TS 45.820** (Rel-13) — CIoT for Internet of Things

---

📖 **Anglický originál a plná specifikace:** [TAU na 3GPP Explorer](https://3gpp-explorer.com/glossary/tau/)
