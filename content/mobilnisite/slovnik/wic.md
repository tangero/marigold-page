---
slug: "wic"
url: "/mobilnisite/slovnik/wic/"
type: "slovnik"
title: "WIC – WebRTC IMS Client"
date: 2025-01-01
abbr: "WIC"
fullName: "WebRTC IMS Client"
category: "Services"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/wic/"
summary: "Klientská aplikace, která umožňuje zařízení na základě WebRTC přístup ke službám IMS, jako je hlas a video přes IP. Spojuje webový ekosystém WebRTC s robustní IMS síťou operátora, což umožňuje, aby we"
---

WIC je klientská aplikace, která umožňuje zařízení na základě WebRTC přístup ke službám IMS tím, že spojuje ekosystém WebRTC s robustní IMS síťou operátora.

## Popis

WebRTC IMS Client (WIC) je softwarová komponenta, typicky implementovaná jako JavaScriptová knihovna nebo modul nativní aplikace, která se nachází na uživatelském zařízení, jako je smartphone, tablet nebo osobní počítač. Jejím hlavním úkolem je fungovat jako překladatel protokolů a správce relací mezi WebRTC stackem a jádrovou síťou IP Multimedia Subsystem (IMS). Architektonicky WIC implementuje funkce IMS klienta – včetně [SIP](/mobilnisite/slovnik/sip/) registrace, navázání relace a media negotiace – ale využívá k tomu WebRTC [API](/mobilnisite/slovnik/api/) (např. RTCPeerConnection a RTCDataChannel) pro zpracování médií a webové transportní protokoly (WebSockets nebo [HTTPS](/mobilnisite/slovnik/https/)) pro signalizaci, namísto tradičních protokolů IMS UE. Spojuje se s síťovým elementem nazvaným WebRTC-IMS Gateway, který provádí potřebnou interoperabilitu protokolů mezi WebRTC signalizací a specifickými SIP/IMS procedurami.

WIC funguje tak, že nejprve navazuje zabezpečenou spojení s WebRTC-IMS Gateway, často využívající webový transport jako WebSocket přes [TLS](/mobilnisite/slovnik/tls/). Pro registraci WIC posílá přes tento spojení SIP-like zprávy na gateway, který je překládá na standardní IMS SIP REGISTER requesty směrem k IMS Core ([CSCF](/mobilnisite/slovnik/cscf/)). Po registraci, pro hovor nebo messaging relaci, WIC využívá WebRTC API k získání lokálních [ICE](/mobilnisite/slovnik/ice/) kandidátů pro media cestu a vytvoření [SDP](/mobilnisite/slovnik/sdp/) nabídky. Toto SDP je posláno na gateway, který ho mapuje na SIP INVITE s odpovídajícím IMS SDP, routuje ho přes IMS síť a vrátí odpověď z druhé strany. WIC pak instruuje WebRTC stack k navázání peer-to-peer nebo gateway-mediovaného media flow. Klíčové komponenty v logice WIC zahrnují SIP/[HTTP](/mobilnisite/slovnik/http/) stack pro signalizaci, handler WebRTC API pro kontrolu médií a moduly pro autentizaci, zabezpečení (DTLS-SRTP) a servisní logiku pro funkce jako presence nebo přenos souborů.

Jeho role v síti je demokratizovat přístup ke službám operátora. Umožňuje, aby každý browser nebo aplikace s podporou WebRTC mohla být plnohodnotným účastníkem v IMS doméně, což telekomunikačním operátorům umožňuje rozšířit služby VoLTE, ViLTE, RCS a další služby na základě IMS na široký ekosystém webových aplikací a zařízení, které nemají nativní IMS stacky. Tím překlenuje propast mezi Over-the-Top (OTT) webovou komunikací a standardizovanými, interoperabilními telekomunikačními službami a usnadňuje konvergenci. WIC řeší komplexnost IMS procedur, síťové autentizace (např. IMS-AKA prostřednictvím gateway), QoS značení a identifikaci služeb pro tísňové volání, a prezentuje webovému aplikativnímu developerovi zjednodušené WebRTC API interface.

## K čemu slouží

WIC byl vytvořen, aby řešil problém izolovaných komunikačních ekosystémů. Historicky byly služby IMS přístupné pouze zařízení s proprietárním, integrovaným IMS klientským softwarem, typicky poskytovaným výrobcem zařízení nebo operátorem. To limitovalo dostupnost kvalitních, zpoplatnitelných telekomunikačních služeb (např. HD hlas nebo videohovorů) pouze na subset smartphoneů. Mezitím se web rozvinul s WebRTC, poskytující standardní API pro real-time komunikaci v browserech, ale tyto relace byly často omezené na izolované webové domény nebo OTT aplikace bez interoperability nebo robustních funkcí operátora, jako je volání na číslo, roaming nebo integrace s PSTN.

Motivace pro WIC, který byl zaveden v 3GPP Release 12, byla využití masivní instalované základny webových browserů a developer-friendly prostředí WebRTC k rozšíření dostupnosti IMS. Řeší limitaci předchozího přístupu, kde IMS byla uzavřená síť pro certifikované UE. Definováním standardizovaného klienta a gateway architektury umožnil 3GPP operátorům nabízet své komunikační služby jako platformu webovým developerům. Tím řeší business problémy vytvořením nových kanálů pro poskytování služeb a technické problémy poskytnutím standardizované, zabezpečené metody pro webové klienty k přístupu k IMS autentizaci, routování a policy kontrolu. Umožňuje operátorům konkurovat OTT webovým komunikačním aplikacím využitím jejich vlastních branded služeb, síťové kvality a existující subscriber identity.

## Klíčové vlastnosti

- Interoperabilita protokolů mezi WebRTC JavaScript API/SDP a IMS SIP/SDP
- Zabezpečený přístup k IMS využitím webových transportů (WebSocket/TLS) a gateway-mediované autentizace
- Podpora IMS multimediálních služeb: hlas, video, real-time text a přenos souborů
- Integrace s IMS core pro registraci, routování a servisní triggery
- End-to-end zabezpečení médií využitím DTLS-SRTP, negotiované prostřednictvím gateway
- Exchange schopností a media negotiace kompatibilní s profilemi WebRTC i IMS

## Související pojmy

- [IMS – IP Multimedia Subsystem](/mobilnisite/slovnik/ims/)
- [SIP – Session Initiation Protocol](/mobilnisite/slovnik/sip/)
- [RCS – Return Channel via Satellite](/mobilnisite/slovnik/rcs/)

## Definující specifikace

- **TS 23.334** (Rel-19) — IMS-ALG to IMS-AGW Interface (Iq) Stage 2
- **TS 23.701** (Rel-12) — WebRTC Access to IMS Architecture Study
- **TS 24.229** (Rel-19) — IMS call control protocol based on SIP and SDP
- **TS 29.334** (Rel-19) — IMS-ALG to IMS-AGW Interface Protocol
- **TS 33.107** (Rel-19) — Lawful Interception Architecture & Functions
- **TS 33.108** (Rel-19) — LI Handover Interface Specification
- **TS 33.127** (Rel-19) — Lawful Interception Architecture and Functions
- **TS 33.871** (Rel-12) — Security for WebRTC IMS Client Access

---

📖 **Anglický originál a plná specifikace:** [WIC na 3GPP Explorer](https://3gpp-explorer.com/glossary/wic/)
