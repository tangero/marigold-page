---
slug: "contp"
url: "/mobilnisite/slovnik/contp/"
type: "slovnik"
title: "CONTP – Character Oriented Non‑Transparent Protocol"
date: 2025-01-01
abbr: "CONTP"
fullName: "Character Oriented Non‑Transparent Protocol"
category: "Protocol"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/contp/"
summary: "CONTP je 3GPP protokol pro přenos znakově orientovaných dat přes bezdrátové sítě bez požadavků na transparentnost. Umožňuje spolehlivý přenos znakových dat mezi terminály a podporuje aplikace jako dál"
---

CONTP je 3GPP protokol pro spolehlivý přenos znakově orientovaných dat přes bezdrátové sítě bez požadavků na transparentnost, podporující aplikace jako dálnopis a starší textové systémy.

## Popis

CONTP (Character Oriented Non‑Transparent Protocol) je specializovaný transportní protokol definovaný ve specifikacích 3GPP pro zpracování přenosu znakově orientovaných dat v mobilních sítích. Na rozdíl od transparentních protokolů, které zacházejí s daty jako s binárním proudem, CONTP specificky řeší potřeby aplikací založených na znacích, kde musí být zachována integrita dat a hranice znaků. Protokol pracuje na aplikační vrstvě a poskytuje mechanismy pro spolehlivý přenos znaků mezi koncovými body.

Architektura CONTP zahrnuje specifické rámovací mechanismy, které identifikují hranice znaků a zajišťují úplný přenos znaků. Zahrnuje schopnosti detekce a opravy chyb uzpůsobené pro znaková data, čímž zabraňuje částečnému přenosu znaků, který by mohl poškodit celý datový proud. Protokol zvládá řízení toku na úrovni znaků spíše než na úrovni bajtů, což jej činí vhodným pro aplikace, kde každý znak představuje diskrétní informační jednotku.

CONTP funguje tak, že mezi komunikujícími entitami navazuje spojově orientovanou relaci, kde jsou znaky přenášeny jako diskrétní jednotky s odpovídajícím rámováním. Každý přenos znaku zahrnuje hlavičky specifické pro protokol, které identifikují kódování znaků a parametry přenosu. Protokol spravuje opakovaný přenos poškozených znaků a poskytuje potvrzovací mechanismy pro zajištění spolehlivého doručení. Zahrnuje také schopnosti pro vyjednávání a konverzi znakových sad, je-li to nutné.

V architektuře sítě 3GPP CONTP typicky pracuje mezi uživatelským zařízením (UE) a aplikačními servery nebo mezi síťovými prvky vyžadujícími komunikaci založenou na znacích. Rozhraní s transportními protokoly nižších vrstev, jako je TCP/IP nebo specifické bezdrátové linkové protokoly, aby poskytoval služby přenosu znaků od konce ke konci. Návrh protokolu bere v úvahu charakteristiky bezdrátových sítí, včetně proměnlivé latence a možných přenosových chyb, a poskytuje robustnost pro znakově orientované aplikace v mobilním prostředí.

## K čemu slouží

CONTP byl vytvořen pro řešení specifických požadavků znakově orientovaných aplikací v mobilních sítích, zejména pro starší systémy a specializované komunikační potřeby. Před jeho standardizací čelily aplikace založené na znacích výzvám s integritou dat při přenosu přes bezdrátové sítě, kde přenosové chyby mohly narušit hranice znaků a učinit data nepoužitelnými. Protokol řeší problém spolehlivého přenosu znaků v prostředích, kde tradiční transparentní protokoly byly nedostatečné.

Historický kontext vývoje CONTP zahrnuje potřebu podpory dálnopisných systémů, emulace terminálů a dalších aplikací založených na znacích v rozvíjející se architektuře sítí 3GPP. Jak se mobilní sítě rozšiřovaly mimo hlasové služby o datové aplikace, vznikla potřeba zachovat kompatibilitu se stávajícími systémy orientovanými na znaky a zároveň zajistit jejich spolehlivý provoz přes bezdrátové spoje. Předchozí přístupy používající transparentní protokoly často nedokázaly zachovat integritu znakových dat, což vedlo k chybám na aplikační úrovni.

CONTP řeší omezení předchozích přístupů tím, že poskytuje mechanismy přenosu citlivé na znaky, které zajišťují úplné doručení znaků a správnou identifikaci jejich hranic. Umožňuje aplikacím, které spoléhají na komunikaci orientovanou na znaky, spolehlivě fungovat v mobilním prostředí, a podporuje tak obchodní systémy, průmyslové aplikace a specializované komunikační služby vyžadující integritu dat na úrovni znaků. Návrh protokolu odráží pochopení, že znaková data mají odlišné požadavky než binární datové proudy, zejména pro aplikace, kde každý znak nese sémantický význam.

## Klíčové vlastnosti

- Zachování a rámování hranic znaků
- Detekce a oprava chyb pro znaková data
- Schopnosti vyjednávání a konverze znakových sad
- Řízení toku na úrovni znaků spíše než na úrovni bajtů
- Spojově orientovaný spolehlivý přenos znaků
- Podpora starších aplikací založených na znacích

## Definující specifikace

- **TS 23.146** (Rel-19) — 3G Facsimile Group 3 Technical Realization

---

📖 **Anglický originál a plná specifikace:** [CONTP na 3GPP Explorer](https://3gpp-explorer.com/glossary/contp/)
