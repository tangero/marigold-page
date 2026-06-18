---
slug: "lm"
url: "/mobilnisite/slovnik/lm/"
type: "slovnik"
title: "LM – Location Management"
date: 2025-01-01
abbr: "LM"
fullName: "Location Management"
category: "Mobility"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/lm/"
summary: "Location Management (LM, správa polohy) je základní funkce mobility, která sleduje a udržuje aktuální polohu mobilního zařízení (UE) v síti. Umožňuje síti směrovat hovory a datové relace do správné bu"
---

LM (Location Management, správa polohy) je základní funkce mobility, která sleduje a udržuje polohu mobilního zařízení, aby umožnila směrování hovorů a dat, dosažitelnost účastníka, paging a mobilní procedury.

## Popis

Location Management (LM, správa polohy) je základní soubor procedur a funkcí v jádru sítě (Core Network, CN) zodpovědný za sledování geografické polohy uživatelského zařízení (UE), aby zajistil úspěšné doručení služeb iniciovaných sítí, jako jsou hlasové hovory nebo [SMS](/mobilnisite/slovnik/sms/). Funguje ve dvou primárních stavech: režimu IDLE a režimu CONNECTED. V režimu IDLE síť zná polohu UE na úrovni oblasti sledování (Tracking Area, [TA](/mobilnisite/slovnik/ta/)) nebo směrovací oblasti (Routing Area, [RA](/mobilnisite/slovnik/ra/)), což je skupina buněk. UE provádí aktualizace polohy (Tracking Area Update - [TAU](/mobilnisite/slovnik/tau/), nebo Routing Area Update - [RAU](/mobilnisite/slovnik/rau/)), když vstoupí do nové TA/RA nebo periodicky. V režimu CONNECTED síť zná polohu UE na úrovni buňky díky aktivnímu rádiovému spojení. Hlavními prováděcími entitami funkcí LM v jádru sítě jsou Mobility Management Entity ([MME](/mobilnisite/slovnik/mme/)) v 4G a Access and Mobility Management Function ([AMF](/mobilnisite/slovnik/amf/)) v 5G. Udržují mobilní kontext UE, včetně aktuální obsluhující uzlu ([eNB](/mobilnisite/slovnik/enb/)/gNB) a registrovaného seznamu TA.

Architektura LM je distribuována mezi UE, rádiovou přístupovou síť (RAN) a jádro sítě (CN). UE je zodpovědné za monitorování vysílaných systémových informací, které obsahují identifikátory TA, a za zahájení procedur aktualizace polohy v případě potřeby. RAN (eNB/gNB) zprostředkovává signalizační spojení a přenáší zprávy o aktualizaci polohy mezi UE a jádrem sítě. Uzel jádra sítě (MME/AMF) je kotvovým bodem; ukládá polohu UE, spravuje seznam TA přiřazený UE a řídí proces pagingu. Paging je klíčová procedura LM, při které síť vysílá pagingovou zprávu do všech buněk v poslední známé TA/TAs, aby našla konkrétní UE při příchozí relaci.

Klíčovými komponentami systému LM jsou registry polohy: Home Subscriber Server (HSS) v 4G nebo Unified Data Management (UDM) v 5G, které ukládají trvalá data účastníka a identitu aktuálně obsluhujícího MME/AMF. Během mobility mezi MME/AMF procedury LM zajišťují plynulý přenos kontextu UE. Efektivita LM přímo ovlivňuje signalizační zatížení sítě; příliš časté aktualizace (ping-pong) mohou způsobit zahlcení, zatímco řídké aktualizace vedou k rozsáhlým a neefektivním oblastem pagingu. Proto jsou algoritmy pro správu a optimalizaci seznamů TA klíčovou součástí návrhu LM. V 5G koncepty jako registrační oblasti (Registration Areas, které mohou být kombinací TA) a vylepšené režimy úspory energie dále zdokonalují LM pro podporu různých případů užití od massive IoT po ultra-spolehlivou komunikaci s nízkou latencí.

## K čemu slouží

Location Management existuje, aby řešila základní problém dosažitelnosti účastníka v mobilní síti. Na rozdíl od pevných sítí, kde má terminál statický přípojný bod, se může mobilní zařízení pohybovat kdekoli v oblasti pokrytí sítě. Síť musí mít mechanismus, jak s dostatečnou přesností vědět, kde se zařízení nachází, aby mohla úspěšně doručit příchozí komunikaci (provoz iniciovaný sítí), aniž by při každém hovoru zaplavovala celou síť pagingovými zprávami. Bez LM by bylo založení relace iniciované sítí nemožné nebo vysoce neefektivní.

Historicky zavedly první celulární systémy jako GSM koncepty lokalizačních oblastí (Location Areas, LAs) a Visitor Location Register (VLR) pro správu mobility. LM od 3GPP, vyvíjející se z těchto konceptů, poskytuje škálovatelnější a efektivnější rámec. Řeší omezení starších, méně podrobných přístupů zavedením hierarchického sledování (např. oblasti sledování (TA) menší než starší lokalizační oblasti) a optimalizací kompromisu mezi signalizační režií častých aktualizací polohy a zatížením pagingem potřebným k nalezení UE. Vytvoření a kontinuální vývoj LM v rámci releasů 3GPP je motivován potřebou podporovat rostoucí hustotu účastníků, vyšší rychlosti mobility (např. ve vysokorychlostních vlacích) a nové typy zařízení jako IoT senzory s extrémně nízkými nároky na spotřebu energie, a to vše při minimalizaci signalizační režie sítě a zachování životnosti baterie.

## Klíčové vlastnosti

- Sleduje polohu UE na úrovni oblasti sledování (TA) v režimu IDLE a na úrovni buňky v režimu CONNECTED
- Spravuje procedury registrace, deregistrace a periodické aktualizace polohy UE
- Řídí celosíťový paging k nalezení UE pro relace iniciované sítí
- Udržuje a optimalizuje seznamy oblastí sledování (TA Lists) specifické pro UE za účelem minimalizace signalizace
- Zpracovává přenos mobilního kontextu během předávání mezi uzly jádra sítě (např. MME/AMF)
- Integruje se s databázemi účastníků (HSS/UDM) pro autentizaci a ověření předplatného

## Související pojmy

- [MME – NPC MME Network Product Class](/mobilnisite/slovnik/mme/)
- [AMF – Access and Mobility Management Function](/mobilnisite/slovnik/amf/)
- [HSS – Home Subscriber Server](/mobilnisite/slovnik/hss/)

## Definující specifikace

- **TS 23.221** (Rel-19) — 3GPP System Architectural Requirements
- **TS 23.255** (Rel-19) — UAS Application Layer Support
- **TR 26.935** (Rel-19) — Speech Codec Performance for Packet Switched Multimedia
- **TS 32.331** (Rel-19) — Notification Log IRP Requirements

---

📖 **Anglický originál a plná specifikace:** [LM na 3GPP Explorer](https://3gpp-explorer.com/glossary/lm/)
