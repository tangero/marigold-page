---
slug: "raa"
url: "/mobilnisite/slovnik/raa/"
type: "slovnik"
title: "RAA – Re-Auth-Answer"
date: 2025-01-01
abbr: "RAA"
fullName: "Re-Auth-Answer"
category: "Protocol"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/raa/"
summary: "Re-Auth-Answer (RAA) je zpráva protokolu Diameter odeslaná serverem Diameter (např. PCRF) jako odpověď na požadavek Re-Auth-Request (RAR). Je klíčovou součástí architektury Policy and Charging Control"
---

RAA je zpráva protokolu Diameter odeslaná serverem jako odpověď na požadavek Re-Auth-Request (RAR), která potvrzuje aplikaci nových pravidel politiky nebo účtování v architektuře PCC (Policy and Charging Control) 3GPP.

## Popis

Re-Auth-Answer (RAA) je příkaz v základním protokolu Diameter ([RFC](/mobilnisite/slovnik/rfc/) 6733) a je specificky využíván v rámci architektury Policy and Charging Control ([PCC](/mobilnisite/slovnik/pcc/)) 3GPP definované v TS 29.212. Funguje jako konečná odpověď serveru Diameter, například funkce Policy and Charging Rules Function ([PCRF](/mobilnisite/slovnik/pcrf/)), na dříve přijatý příkaz Re-Auth-Request ([RAR](/mobilnisite/slovnik/rar/)). Výměna RAR/RAA je procedura iniciovaná serverem, která umožňuje síti dynamicky měnit parametry probíhající relace [IP-CAN](/mobilnisite/slovnik/ip-can/) (IP Connectivity Access Network) bez čekání na podnět od strany klienta.

Když se PCRF rozhodne upravit pravidla politiky nebo účtování pro účastníka (např. z důvodu změny předplatného, detekce aplikace nebo síťových podmínek), odešle příkaz RAR k funkci Policy and Charging Enforcement Function ([PCEF](/mobilnisite/slovnik/pcef/)) umístěné v bráně (např. [PGW](/mobilnisite/slovnik/pgw/), [TDF](/mobilnisite/slovnik/tdf/) nebo SMF v 5G). RAR obsahuje nová pravidla nebo instrukce ve formě atribut-hodnota párů (AVPs). Po přijetí a úspěšné aplikaci těchto instrukcí musí PCEF odpovědět zprávou Re-Auth-Answer (RAA). Tato zpráva RAA obsahuje AVP Result-Code udávající úspěch (např. DIAMETER_SUCCESS) nebo konkrétní chybový kód, pokud požadavek nemohl být splněn.

Zpráva RAA není pouhé potvrzení; je povinnou součástí stavového automatu transakce Diameter. Její absence nebo přijetí chybového kódu informuje PCRF o neúspěchu aktualizace politiky, což může spustit nápravné akce, jako je ukončení relace nebo zřízení alternativních pravidel. Zpráva obsahuje AVP Session-Id pro korelaci s konkrétní relací a příkazem RAR. V rámci architektury PCC je tento mechanismus zásadní pro řízení služeb v reálném čase a umožňuje funkce jako on-demand změna QoS, řízení přístupu (gating control) pro aplikační toky a aktualizace účtování v průběhu relace.

## K čemu slouží

Zpráva RAA existuje proto, aby poskytla spolehlivý, potvrzovaný mechanismus pro aktualizace politiky iniciované sítí v rámci standardizovaného frameworku online účtování a řízení politiky. Před PCC a Diameter bylo řízení politiky často statické nebo závislé na proprietární signalizaci, což činilo úpravy v reálném čase a na úrovni relace složitými a závislými na dodavateli. Dvojice příkazů RAR/RAA protokolu Diameter byla přijata, aby tento problém vyřešila, a to poskytnutím robustního modelu požadavek-odpověď pro reautorizaci relace iniciovanou serverem.

Její vznik byl motivován potřebou operátorů dynamicky řídit uživatelský zážitek a síťové zdroje na základě měnících se podmínek. Například operátor může chtít zvýšit uživateli šířku pásma během videohovoru nebo aplikovat nové limity utrácení bez přerušení relace. Zpráva RAA poskytuje nezbytné potvrzení, že tyto kritické instrukce byly přijaty a provedeny v místě vynucení. Tato komunikace v uzavřené smyčce je zásadní pro přesnost účtování, zajištění služeb a implementaci pokročilých obchodních modelů, jako je sponzorovaný přenos dat nebo nabídky QoS na různých úrovních.

## Klíčové vlastnosti

- Povinná odpověď na příkaz Re-Auth-Request (RAR) v protokolu Diameter.
- Nese AVP Result-Code udávající úspěch nebo selhání aktualizace politiky.
- Používá AVP Session-Id pro přesnou korelaci s konkrétní uživatelskou relací.
- Umožňuje úpravu pravidel PCC v průběhu relace iniciovanou serverem.
- Základní pro činnost architektury PCC 3GPP v reálném čase.
- Zajišťuje spolehlivé doručení a aplikaci dynamických instrukcí politiky a účtování.

## Související pojmy

- [RAR – Re-Auth-Request](/mobilnisite/slovnik/rar/)
- [PCRF – Policy and Charging Rules Function](/mobilnisite/slovnik/pcrf/)
- [PCEF – Policy and Charging Enforcement Function](/mobilnisite/slovnik/pcef/)

## Definující specifikace

- **TS 29.212** (Rel-19) — Gx/Gxx/Sd/St Diameter Protocol
- **TS 29.806** (Rel-12) — P-CSCF Restoration Analysis & Solutions
- **TS 29.826** (Rel-13) — P-CSCF Restoration Enhancements for WLAN
- **TS 32.299** (Rel-19) — Diameter Charging Applications for 3GPP

---

📖 **Anglický originál a plná specifikace:** [RAA na 3GPP Explorer](https://3gpp-explorer.com/glossary/raa/)
