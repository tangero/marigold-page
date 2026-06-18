---
slug: "rna"
url: "/mobilnisite/slovnik/rna/"
type: "slovnik"
title: "RNA – RAN-based Notification Area"
date: 2026-01-01
abbr: "RNA"
fullName: "RAN-based Notification Area"
category: "Mobility"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/rna/"
summary: "Koncept v LTE a NR, kdy je UE ve stavu RRC_INACTIVE přiřazena specifická oblast, zahrnující jednu nebo více buněk, v rámci které se může pohybovat bez provedení aktualizace polohy. Umožňuje efektivní"
---

RNA je specifická oblast, zahrnující jednu nebo více buněk, přiřazená UE ve stavu RRC_INACTIVE, aby se mohla pohybovat v této RAN-based Notification Area bez provedení aktualizace polohy, což umožňuje úsporu energie a snížení signalizační zátěže.

## Popis

RAN-based Notification Area (RNA) je klíčový koncept správy mobility pro stav [RRC](/mobilnisite/slovnik/rrc/)_INACTIVE zavedený v LTE (eNB-based) a rozvinutý v NR (gNB-based). Definuje geografickou oblast, konfigurovanou RAN, v rámci které se může uživatelské zařízení (UE) volně pohybovat bez nutnosti informovat síť o své poloze na úrovni buňky. RNA se skládá z jedné nebo více buněk, které mohou být nakonfigurovány jako seznam buněk, seznam RAN oblastí (kde každá je skupinou buněk) nebo jako tracking area. Když UE přejde do stavu RRC_INACTIVE, poslední obsluhující základnová stanice (poslední obsluhující gNB v NR nebo [eNB](/mobilnisite/slovnik/enb/) v LTE) jí přiřadí RNA, typicky na základě pohybových vzorců UE, předplatného nebo síťové politiky.

Hlavní operační mechanismus spočívá v tom, že UE provádí periodické nebo spouštěné aktualizace RNA (RNA Updates). Zatímco je ve stavu RRC_INNECTIVE, UE monitoruje systémovou informaci, aby identifikovalo RNA Identity (RNA ID) své aktuální buňky. Pokud se UE přesune do buňky, jejíž RNA ID není součástí její přiřazené RNA, musí zahájit proceduru RNA Update, aby informovala RAN o své nové poloze a potenciálně získala novou RNA přiřazenou. Tato procedura je odlehčeným obnovením RRC spojení (RRC connection resume), které reaktivuje kontext UE uložený v RAN a core networku. Naopak, pokud UE zůstává ve své RNA, může v tomto stavu s nízkou spotřebou setrvat neomezeně dlouho. Když pro UE dorazí downlink data, RAN zahájí proceduru pagingu ve všech buňkách poslední známé RNA UE, aby ji lokalizoval a obnovil spojení.

Architektura je založena na schopnosti RAN ukládat kontext přístupové vrstvy (Access Stratum - [AS](/mobilnisite/slovnik/as/)) UE a spravovat oblast RNA. V NR je to umožněno architekturou NG-RAN, kde jsou gNB vzájemně propojeny přes rozhraní Xn. Poslední obsluhující gNB funguje jako „Anchor“ gNB, který si udržuje kontext UE. Ostatní gNB v rámci RNA mohou asistovat při pagingu. Konfigurace RNA je signalizována UE prostřednictvím zpráv RRCRelease a vysílána v systémových informačních blocích (SIBs). Tento mechanismus odděluje správu mobility pro neaktivní UE od Tracking Area ([TA](/mobilnisite/slovnik/ta/)) core networku, čímž snižuje signalizační zátěž na rozhraních [N2](/mobilnisite/slovnik/n2/)/N3 a umožňuje rychlejší přechody stavů ve srovnání s tradičními procedurami pro stav IDLE.

## K čemu slouží

RNA byla vytvořena, aby řešila problémy signalizační režie a spotřeby energie spojené s obrovským množstvím IoT zařízení a smartphonů, které přenášejí data nepravidelně, ale vyžadují neustálé připojení. Tradiční mobilita v LTE spoléhala na dva hlavní stavy: [RRC](/mobilnisite/slovnik/rrc/)_IDLE a RRC_CONNECTED. Stav IDLE vyžadoval zapojení core networku ([MME](/mobilnisite/slovnik/mme/)) pro aktualizace polohy (Tracking Area Updates) a paging, což způsobovalo latenci a signalizační zátěž. Stav CONNECTED udržoval rádiové prostředky aktivní, což plýtvalo energií při přerušovaném provozu. Stav RRC_INACTIVE, pro který je RNA klíčovým prvkem, byl zaveden, aby poskytl střední cestu.

Motivace vycházela z 5G případů užití, jako je massive Machine-Type Communication (mMTC) a enhanced Mobile Broadband (eMBB) s přerušovaným charakterem provozu. RNA problém řeší tím, že udržuje kontext UE v RAN a umožňuje mobilitu v rámci oblasti bez signalizace s core networkem. To drasticky snižuje signalizační bouři, která by nastala, kdyby každá změna malé buňky vyžadovala Tracking Area Update. Také umožňuje rychlejší obnovení spojení (ve srovnání s přechodem z IDLE do CONNECTED) a lepší výdrž baterie než setrvání ve stavu CONNECTED. RNA představuje přesun odpovědnosti za správu mobility z core networku na RAN, optimalizovaný pro scénáře, kde je klíčová kontinuita relace s nízkou latencí a nízkou signalizací.

## Klíčové vlastnosti

- Definuje oblast pro mobilitu UE ve stavu RRC_INACTIVE bez aktualizací polohy
- Konfigurována a spravována RAN (gNB/eNB), nikoli core networkem
- Spouští proceduru RNA Update, když se UE přesune mimo přiřazenou oblast
- Umožňuje RAN-based paging v rámci RNA pro oznámení downlink dat
- Podporuje flexibilní konfigurace: seznam buněk, seznam RAN oblastí nebo tracking area
- Snižuje signalizaci směrem k core networku (AMF/MME) a šetří baterii UE ve srovnání s častými TAUs

## Definující specifikace

- **TS 23.725** (Rel-16) — Study on URLLC Architecture Enhancements
- **TS 25.471** (Rel-19) — RNSAP User Adaptation (RNA) for Iurh
- **TS 28.552** (Rel-20) — 5G Performance Management Measurements
- **TS 36.300** (Rel-19) — E-UTRAN Radio Interface Protocol Architecture Overview
- **TS 36.304** (Rel-19) — UE Idle Mode Procedures in E-UTRA
- **TS 36.331** (Rel-19) — LTE RRC Protocol Specification
- **TS 38.300** (Rel-19) — NG-RAN Overall Description
- **TS 38.304** (Rel-19) — UE RRC_IDLE and RRC_INACTIVE Procedures
- **TS 38.331** (Rel-19) — NR Radio Resource Control (RRC) Protocol Specification

---

📖 **Anglický originál a plná specifikace:** [RNA na 3GPP Explorer](https://3gpp-explorer.com/glossary/rna/)
