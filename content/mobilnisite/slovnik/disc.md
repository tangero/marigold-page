---
slug: "disc"
url: "/mobilnisite/slovnik/disc/"
type: "slovnik"
title: "DISC – Disconnect"
date: 2025-01-01
abbr: "DISC"
fullName: "Disconnect"
category: "Protocol"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/disc/"
summary: "DISC je specifický typ rámce v protokolu LAPDm (Link Access Procedure on the Dm channel) používaném v GSM. Je to příkaz (command) odeslaný za účelem logického ukončení spojení na vrstvě datového spoje"
---

DISC je řídicí rámec v protokolu GSM LAPDm používaný k logickému ukončení spojení na vrstvě datového spoje (link layer) mezi mobilní stanicí a sítí, čímž zajišťuje uspořádané uvolnění prostředků.

## Popis

DISC (Disconnect) rámec je základní součástí signalizačního protokolu vrstvy 2 v GSM, známého jako LAPDm, který je adaptací protokolu [ISDN](/mobilnisite/slovnik/isdn/) [LAPD](/mobilnisite/slovnik/lapd/) pro mobilní rádiové prostředí. Operuje na vyhrazeném řídicím kanálu ([DCCH](/mobilnisite/slovnik/dcch/)). DISC rámec je příkaz (command), který může odeslat mobilní stanice ([MS](/mobilnisite/slovnik/ms/)) nebo síť (typicky část Base Station System, [BSS](/mobilnisite/slovnik/bss/)), aby zahájil ukončení potvrzovaného režimu přenosu informací (multiframe operation) na vrstvě datového spoje (vrstva 2). Tento postup se liší od fyzického uvolnění rádiového kanálu; jedná se o logické odpojení, které zajišťuje, že se obě strany shodnou na neaktivním stavu spojení pro signalizaci, což umožní vyprázdnění vyrovnávacích pamětí a resetování pořadových čísel.

Funguje na základě definovaného handshake. Subjekt, který si přeje spojení ukončit (iniciátor), odešle řídicí rámec DISC. Tento rámec obsahuje poll bit nastavený na '1', čímž vyžaduje odezvu od přijímající strany. Po přijetí platného příkazu DISC musí přijímající entita odpovědět rámcem Unnumbered Acknowledgment (UA), také s příslušně nastaveným poll/final bitem, aby potvrdila odpojení. Jakmile iniciátor obdrží rámec UA, je spojení na vrstvě datového spoje považováno za formálně ukončené. Teprve po tomto dokončení odpojení na vrstvě 2 mohou být přidružené fyzické prostředky (časový slot a frekvence) bezpečně uvolněny pro jiná volání nebo signalizační procedury. Tento uspořádaný proces brání ztrátě dat a nejednoznačnostem ve stavu protokolu.

Úloha DISC rámce je klíčová pro robustní správu signalizace v GSM. Používá se v různých scénářích, například při dokončování hovoru, provádění přechodu buňky (handover) a uvolňování vyhrazených signalizačních spojení. Tím, že LAPDm poskytuje mechanismus potvrzovaného odpojení, zajišťuje integritu řízení signalizačního spoje. DISC je součástí sady nečíslovaných rámců (kam patří také SABM pro navázání spojení, UA pro potvrzení a [DM](/mobilnisite/slovnik/dm/) pro mód odpojení), které spravují provozní stav spoje. Specifikace řídící jeho použití, jako je TS 24.022 pro aspekty vrstvy 3 a TS 37.462 pro signalizaci na rozhraní [GERAN](/mobilnisite/slovnik/geran/) Iur-g, zajišťují interoperabilitu mezi zařízeními různých výrobců sítí.

## K čemu slouží

DISC rámec existuje proto, aby poskytoval spolehlivou a uspořádanou metodu pro ukončení logického spojení datového spoje v signalizačním zásobníku GSM. Bez takového mechanismu by se partnerská entita mohla dál pokoušet vysílat signalizační zprávy na spoji, který druhá strana považuje za mrtvý, což by vedlo k chybám protokolu, plýtvání prostředky a potenciální nestabilitě systému. Řeší problém synchronizace stavu spojení vrstvy 2 mezi [MS](/mobilnisite/slovnik/ms/) a sítí.

Jeho vznik je zakořeněn v principech spolehlivých protokolů datového spoje, adaptovaných z pevných telekomunikačních standardů (ISDN) pro bezdrátovou doménu. Mobilní prostředí s možností náhlé ztráty signálu činí proceduru potvrzovaného odpojení ještě důležitější než v kabelových systémech. Handshake pomocí DISC zajišťuje, že obě strany explicitně potvrdí ukončení signalizačního dialogu pro konkrétní transakci, což je předpoklad pro čisté uvolnění síťových prostředků a přípravu na dalšího uživatele nebo proceduru. Řeší tak omezení implicitního odpojení, které by mohlo být způsobeno únikem rádiového signálu, vynucením explicitní signalizační výměny.

## Klíčové vlastnosti

- Nečíslovaný řídicí rámec (unnumbered command frame) protokolu LAPDm používaný pro logické ukončení spoje
- Zahajuje proceduru potvrzovaného odpojení vyžadující odezvu UA (Unnumbered Acknowledgment)
- Operuje na vyhrazeném řídicím kanálu (DCCH) v GSM
- Zajišťuje synchronizaci stavu vrstvy 2 mezi MS a sítí
- Předchází fyzickému uvolnění kanálu za účelem zachování integrity signalizace
- Definován v základních GSM signalizačních specifikacích (24.022) a později pro signalizaci mezi BSS (37.462)

## Související pojmy

- [DCCH – Dedicated Control Channel](/mobilnisite/slovnik/dcch/)

## Definující specifikace

- **TS 24.022** (Rel-19) — Radio Link Protocol (RLP) for Circuit Switched Data
- **TS 37.462** (Rel-19) — Iuant Interface Data Link Layer for RETAP/TMAAP

---

📖 **Anglický originál a plná specifikace:** [DISC na 3GPP Explorer](https://3gpp-explorer.com/glossary/disc/)
