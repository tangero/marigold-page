---
slug: "w-5gan"
url: "/mobilnisite/slovnik/w-5gan/"
type: "slovnik"
title: "W-5GAN – Wireline 5G Access Network"
date: 2026-01-01
abbr: "W-5GAN"
fullName: "Wireline 5G Access Network"
category: "Other"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/w-5gan/"
summary: "Standardizovaná architektura 3GPP umožňující integraci obecných drátových přístupových sítí s jádrem 5G Core. Umožňuje drátovým zařízením připojit se jako 5G uživatelské zařízení (UE) a využívat 5G au"
---

W-5GAN je standardizovaná architektura, která integruje obecné drátové přístupové sítě s jádrem 5G Core a umožňuje drátovým zařízením připojit se jako 5G uživatelské zařízení (UE) přes pevné širokopásmové spoje.

## Popis

Wireline 5G Access Network (W-5GAN) je klíčový architektonický rámec definovaný 3GPP, který překlenuje propast mezi tradičními pevnými širokopásmovými sítěmi a systémem 5G. Funguje tak, že zachází s drátovou přístupovou sítí (např. optická vlákna, [DSL](/mobilnisite/slovnik/dsl/)) jako s důvěryhodným přístupem typu non-3GPP. Klíčovou komponentou je Wireline Access Gateway Function ([W-AGF](/mobilnisite/slovnik/w-agf/)), která slouží jako mezisíťový uzel. W-AGF ukončuje protokoly specifické pro drátové sítě (jako jsou ty definované Broadband Forum) a mapuje relace a zařízení drátových účastníků do konstrukcí protokolů 5G, jako jsou [PDU](/mobilnisite/slovnik/pdu/) Sessions a rozhraní [N2](/mobilnisite/slovnik/n2/)/N3. Toto mapování umožňuje, aby byla koncová zařízení zákazníka ([CPE](/mobilnisite/slovnik/cpe/)) nebo integrovaná zařízení v drátové síti rozpoznána a spravována jádrem 5G Core jako standardní 5G uživatelská zařízení (UE).

Architektura zahrnuje W-AGF, která navazuje rozhraní N2 s funkcí [AMF](/mobilnisite/slovnik/amf/) pro signalizaci řídicí roviny a rozhraní N3 s funkcí [UPF](/mobilnisite/slovnik/upf/) pro datový provoz. Toto uspořádání umožňuje jádru 5G Core aplikovat své nativní procedury – včetně autentizace přes funkci [AUSF](/mobilnisite/slovnik/ausf/) a UDM, správy relací přes funkci SMF a vynucování politik přes funkci PCF – na zařízení připojená přes drátovou síť. Drátový spoj se v podstatě stává vysokokapacitním a nízkolatenčním přenosem pro signalizaci 5G a data uživatelské roviny, což plynule integruje účastníka do ekosystému 5G.

Z pohledu sítě W-5GAN umožňuje jednotný rámec pro politiky a účtování. Operátoři mohou aplikovat stejné politiky QoS, mechanismy výběru síťových řezů a pravidla účtování na uživatele bez ohledu na to, zda jsou připojeni přes rádiový stožár nebo optickou linku. Tato konvergence zjednodušuje provoz sítě a poskytování služeb. Úlohou W-5GAN je rozšířit dosah a schopnosti 5G na pevná místa, což umožňuje kontinuitu služeb, konvergenci pevných a mobilních sítí (FMC) a poskytování konzistentních služeb 5G, jako je rozšířené mobilní širokopásmové připojení (eMBB) a ultra-spolehlivá nízkolatenční komunikace (URLLC), přes drátovou infrastrukturu.

## K čemu slouží

W-5GAN byl vytvořen jako odpověď na snahu průmyslu směrem ke konvergenci pevných a mobilních sítí (FMC) a vizi jednotného jádra sítě. Před jeho standardizací fungovaly drátové a mobilní sítě jako oddělené sila s odlišnými jádry (např. EPC pro mobilní sítě, BNG/BRAS pro pevné sítě), což vedlo k provozní složitosti, duplicitě funkcí a neschopnosti nabízet bezproblémové služby napříč typy přístupu. Mezi omezení patřily oddělené databáze účastníků, odlišné rámce politik a absence nativní podpory mobility mezi pevným a bezdrátovým přístupem.

Hlavní motivací pro W-5GAN bylo využít pokročilou architekturu založenou na službách, síťové řezy a cloud-nativní principy jádra 5G Core pro drátové služby. Integrací drátového přístupu jako důvěryhodného přístupu typu non-3GPP mohou operátoři modernizovat své pevné sítě pomocí stejného jádra 5G Core, které pohání jejich mobilní síť, čímž snižují kapitálové i provozní náklady. Řeší problém fragmentace služeb a umožňuje vytváření skutečně konvergentních nabídek, kde je profil služeb účastníka, záruky QoS a bezpečnostní politiky konzistentní, ať je účastník doma na Wi-Fi/optice, nebo na cestách pomocí 5G NR.

Historicky byly pokusy o konvergenci, jako IWLAN nebo přístup non-3GPP k EPC, omezené. W-5GAN, zavedený ve verzi 16 jako část fáze 2 systému 5G, poskytuje nativnější a komplexnější integraci speciálně navrženou pro architekturu založenou na servisních rozhraních 5GC. Umožňuje nové obchodní modely, jako je poskytování podnikových služeb v kvalitě 5G přes pevný přístup, a je základním prvkem pro realizaci plného potenciálu síťových řezů napříč všemi přístupovými technologiemi.

## Klíčové vlastnosti

- Integrace drátového přístupu jako důvěryhodného přístupu typu Non-3GPP k 5GC
- Využívá funkci Wireline Access Gateway Function (W-AGF) pro mezisíťovou spolupráci protokolů
- Umožňuje 5G autentizaci (5G-AKA) a zabezpečení pro drátová zařízení
- Podporuje jednotné řízení politik (PCF) a účtování (CHF) pro služby pevných a mobilních sítí
- Umožňuje drátovému UE navazovat PDU Sessions s toky QoS přes pevnou infrastrukturu
- Umožňuje výběr a aplikaci síťových řezů pro drátové účastníky

## Související pojmy

- [W-AGF – Wireline Access Gateway Function](/mobilnisite/slovnik/w-agf/)

## Definující specifikace

- **TS 23.003** (Rel-19) — Numbering, addressing and identification in 3GPP
- **TS 23.316** (Rel-19) — Wireline and Wireless Convergence Access Support
- **TS 23.501** (Rel-20) — 5G System Architecture Stage 2
- **TS 23.716** (Rel-16) — Wireline and Trusted Non-3GPP Access to 5G Core
- **TS 29.507** (Rel-19) — 5G Access & Mobility Policy Control Service
- **TS 29.512** (Rel-19) — 5G Session Management Policy Control Service
- **TS 29.514** (Rel-19) — 5G System; Policy Authorization Service; Stage 3
- **TS 29.525** (Rel-19) — 5G UE Policy Control Service Stage 3

---

📖 **Anglický originál a plná specifikace:** [W-5GAN na 3GPP Explorer](https://3gpp-explorer.com/glossary/w-5gan/)
