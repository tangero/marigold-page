---
slug: "tbcp"
url: "/mobilnisite/slovnik/tbcp/"
type: "slovnik"
title: "TBCP – Talk Burst Control Protocol"
date: 2026-01-01
abbr: "TBCP"
fullName: "Talk Burst Control Protocol"
category: "Services"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/tbcp/"
summary: "Řídicí protokol používaný ve službách Push-to-Talk over Cellular (PoC) ke správě stavu přidělování řečového práva – určuje, který účastník ve skupinové relaci má v daném okamžiku povolení (tzv. 'právo"
---

TBCP (Talk Burst Control Protocol) je protokol pro řízení řečového bloku používaný ve službě Push-to-Talk over Cellular (PoC) ke správě přidělování řečového práva koordinací žádostí, udělení a uvolnění povolení mluvit ve skupinové relaci.

## Popis

Talk Burst Control Protocol (TBCP) je klient-server protokol fungující přes IP, typicky používající [SIP](/mobilnisite/slovnik/sip/) a [RTP](/mobilnisite/slovnik/rtp/) jako přenosové nosiče. Je klíčovou součástí služby Push-to-Talk over Cellular (PoC) od Open Mobile Alliance ([OMA](/mobilnisite/slovnik/oma/)), kterou 3GPP přijala a odkazuje na ni pro standardizované služby skupinové komunikace pro misně-kritické i komerční účely. Zprávy TBCP jsou přenášeny v rámci protokolu RTP Control Protocol ([RTCP](/mobilnisite/slovnik/rtcp/)) nebo jako samostatné SIP zprávy, což umožňuje efektivní řízení v pásmu spolu s mediálním proudem. Protokol definuje stavový automat pro přidělování řečového práva zahrnující PoC klienta (účastníka) a PoC server (řídicí entitu).

Protokol funguje prostřednictvím řady definovaných zpráv: Talk Burst Request (žádost o řečový blok), Talk Burst Granted (řečový blok udělen), Talk Burst Deny (řečový blok zamítnut), Talk Burst Release (uvolnění řečového bloku) a Talk Burst Taken (řečový blok převzat). Když chce uživatel mluvit, jeho klient odešle PoC serveru TBCP zprávu Talk Burst Request. Server, aplikující přednastavená pravidla (jako fronta, přednostní přerušení nebo princip prvního příchodu), se rozhodne právo mluvit udělit. Poté odešle zprávu Talk Burst Granted žádajícímu klientovi a zprávu Talk Burst Taken všem ostatním účastníkům relace, čímž je informuje, že právo mluvit je obsazeno. Mluvící klient streamuje hlasové pakety (řečový blok) přes RTP. Po dokončení klient odešle zprávu Talk Burst Release a server aktualizuje stav řečového práva na volný, případně o tom účastníky notifikuje.

Mezi klíčové architektonické komponenty patří Participating PoC Function (klient) a Controlling PoC Function (server). Logika přidělování řečového práva na serveru je kritická, zejména pro misně-kritické služby, kde jsou priority, přednostní přerušení a fronty zásadní. TBCP také podporuje notifikace jako Talk Burst Idle (řečové právo nečinné) a Talk Burst Revoke (odebrání řečového práva). Jeho integrace se systémy 3GPP je specifikována pro službu Mission Critical Push To Talk ([MCPTT](/mobilnisite/slovnik/mcptt/)), kde zajišťuje disciplinované řízení s nízkou latencí nad tím, kdo vysílá ve skupinovém hovoru, což je zásadní pro komunikaci složek integrovaného záchranného systému a pracovních týmů v utilities. Protokol je navržen pro minimální latenci při udělování řečového práva, aby poskytoval přirozený uživatelský zážitek typu 'vysílačka'.

## K čemu slouží

TBCP byl vytvořen k řešení základního problému koordinovaného přístupu ke sdílenému poloduplexnímu komunikačnímu kanálu v IP skupinové komunikační službě. Rané skupinové hlasové hovory v mobilních sítích byly přepojovány okruhy a řízeny sítí. S přechodem na plně IP sítě (IMS) byl potřeba standardizovaný, efektivní protokol pro přidělování řečového práva, který by umožnil služby Push-to-Talk napodobující okamžitý, jeden-k-více charakter tradičních vysílaček, ale přes celoplošné mobilní sítě.

Protokol řešil omezení ad-hoc nebo proprietárních řešení a zajišťoval interoperabilitu mezi PoC klienty a servery různých výrobců. Jeho návrh v rámci [OMA](/mobilnisite/slovnik/oma/) a následné přijetí 3GPP pro Mission Critical Services ([MCS](/mobilnisite/slovnik/mcs/)) bylo motivováno potřebou spolehlivé, okamžité skupinové komunikace ze strany složek integrovaného záchranného systému. TBCP poskytuje deterministické, síťově řízené rozhodování nezbytné k zabránění chaotickým kolizím audio signálů od více mluvčích, což je klíčové v situacích s vysokými nároky. Umožňuje funkce jako přednostní mluvčí, které umožňují dispečerům nebo velitelům zásahu přerušit ostatní, čímž přímo řeší operační požadavky, které předchozí spotřebitelské hlasové služby nemohly splnit.

## Klíčové vlastnosti

- Spravuje stav přidělování řečového práva pro poloduplexní skupinovou komunikaci
- Používá RTCP nebo SIP pro přenos řídicích zpráv
- Definuje zprávy pro Žádost, Udělení, Zamítnutí, Uvolnění a Převzetí řečových bloků
- Podporuje přidělování řečového práva založené na prioritách a frontách pro misně-kritické použití
- Integrován do služby 3GPP Mission Critical Push To Talk (MCPTT)
- Poskytuje všem účastníkům notifikace o změnách stavu řečového práva

## Související pojmy

- [MCPTT – Mission Critical Push to Talk Identity](/mobilnisite/slovnik/mcptt/)
- [RTCP – Real-time Transport Control Protocol](/mobilnisite/slovnik/rtcp/)

## Definující specifikace

- **TS 32.272** (Rel-19) — Charging for Push-to-Talk over Cellular (PoC)
- **TS 33.179** (Rel-13) — MCPTT Security Architecture and Procedures
- **TS 33.180** (Rel-20) — Security of Mission Critical (MC) Service
- **TS 33.879** (Rel-13) — MCPTT Security Study

---

📖 **Anglický originál a plná specifikace:** [TBCP na 3GPP Explorer](https://3gpp-explorer.com/glossary/tbcp/)
