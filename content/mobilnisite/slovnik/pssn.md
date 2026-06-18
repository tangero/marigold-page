---
slug: "pssn"
url: "/mobilnisite/slovnik/pssn/"
type: "slovnik"
title: "PSSN – PDU Set Sequence Number"
date: 2026-01-01
abbr: "PSSN"
fullName: "PDU Set Sequence Number"
category: "Protocol"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/pssn/"
summary: "Pořadové číslo používané v 5G NR pro zajištění doručení ve správném pořadí a integrity sad protokolových datových jednotek (PDU Set), což jsou skupiny PDU patřících ke stejné aplikační datové jednotce"
---

PSSN je pořadové číslo používané v 5G NR pro zajištění doručení ve správném pořadí a integrity sad protokolových datových jednotek (PDU Set), což jsou skupiny PDU patřících ke stejné aplikační datové jednotce.

## Popis

[PDU](/mobilnisite/slovnik/pdu/) Set Sequence Number (PSSN) je protokolový mechanismus zavedený ve 3GPP Release 18 jako součást protokolového zásobníku 5G NR, konkrétně ve vrstvách Service Data Adaptation Protocol ([SDAP](/mobilnisite/slovnik/sdap/)) a Packet Data Convergence Protocol ([PDCP](/mobilnisite/slovnik/pdcp/)). PDU Set je kolekce jedné nebo více protokolových datových jednotek (PDU), které odpovídají jedné aplikační datové jednotce ([ADU](/mobilnisite/slovnik/adu/)) vygenerované aplikací vyšší vrstvy. Pro služby [URLLC](/mobilnisite/slovnik/urllc/), jako je průmyslová automatizace, autonomní řízení nebo vzdálená chirurgie, aplikace často generuje datové jednotky (např. řídicí příkaz, údaj ze senzoru), které musí být doručeny kompletně, ve správném pořadí a s extrémně vysokou spolehlivostí a nízkou latencí. PSSN je přiřazeno každé sadě PDU, aby příjemce mohl správně zrekonstruovat původní ADU, i když se jednotlivé PDU v rámci sady dostanou mimo pořadí nebo jsou ztraceny a retransmitovány.

Operačně, když aplikace vygeneruje ADU, vrstva SDAP/PDCP na straně vysílače ji (je-li třeba) segmentuje na více PDU, čímž vytvoří PDU Set. Této sadě je přiřazeno jednoznačné PSSN. Toto PSSN je zahrnuto v hlavičce každého PDU patřícího do dané sady. Na straně přijímače vrstva PDCP používá PSSN ke skupinování příchozích PDU zpět do jejich původních sad. Může tak detekovat chybějící PDU v rámci sady a v případě potřeby požádat o jejich opětovné přenesení, a nakonec doručit kompletní ADU vyšší vrstvě ve správném pořadí. To je efektivnější než pořadová čísla pro jednotlivá PDU u aplikací, kde atomovou jednotkou významu je ADU, nikoli jednotlivá PDU.

PSSN funguje ve spojení s existujícími mechanismy číslování pořadí, jako je PDCP Sequence Number ([SN](/mobilnisite/slovnik/sn/)), které zajišťuje pořadí a detekci duplicit na úrovni jednotlivých PDU. PSSN pracuje na vyšší úrovni granularity a spravuje integritu logické skupiny. To je obzvláště důležité pro služby využívající duplikaci paketů přes více cest (např. pomocí agregace nosných nebo duální konektivity), kde PDU ze stejné sady mohou putovat různými cestami a dorazit v různých časech. Příjemce používá PSSN k seřazení PDU z různých cest před rekonstrukcí ADU, čímž zajišťuje, že aplikace obdrží konzistentní a kompletní datovou jednotku.

## K čemu slouží

PSSN bylo vytvořeno k řešení přísných požadavků služeb Ultra-Reliable Low-Latency Communication ([URLLC](/mobilnisite/slovnik/urllc/)) v 5G Advanced (Release 18 a novější). Tradiční číslování pořadí pro jednotlivá [PDU](/mobilnisite/slovnik/pdu/) v PDCP, ačkoli účinné pro hromadný přenos dat, není optimální pro aplikace, kde smysluplnou datovou jednotkou je větší aplikační datová jednotka (ADU), která může být segmentována do více PDU. Ve scénářích, jako je průmyslové řízení nebo koordinace vozidel, může ztráta nebo nesprávné pořadí i jediného PDU uvnitř ADU způsobit, že celá ADU bude nepoužitelná, což vede k selhání aplikace.

Předchozí přístup spoléhal na to, že o znovusložení a integritu ADU se postarají protokoly nebo aplikace vyšších vrstev, což mohlo zavést dodatečnou latenci a složitost. PSSN přesouvá tuto funkcionalitu do nižších vrstev (PDCP/SDAP), což umožňuje rychlejší a efektivnější zpracování blíže k rádiovému rozhraní. Řeší problém zajištění kompletního a uspořádaného doručení ADU přes potenciálně nespolehlivá bezdrátová spojení s duplikací paketů a multi-konektivitou. Díky explicitní identifikaci všech PDU patřících do stejné logické sady může síť optimalizovat retransmise a přeřazování pořadí, což přímo přispívá k dosažení cílů spolehlivosti 99,9999 % a latence pod 1 ms pro kritické URLLC aplikace.

## Klíčové vlastnosti

- Jednoznačně identifikuje skupinu PDU (PDU Set) odvozenou z jedné aplikační datové jednotky (ADU)
- Umožňuje doručení ve správném pořadí a ověření integrity kompletní ADU na straně přijímače
- Funguje ve spojení s existujícími pořadovými čísly PDCP pro sledování jednotlivých PDU
- Zásadní pro efektivní fungování schémat duplikace paketů v URLLC s multi-konektivitou
- Snižuje latenci tím, že umožňuje znovusložení v nižší vrstvě a redukuje zpracování ve vyšších vrstvách
- Podporuje segmentaci a znovusložení velkých ADU napříč více PDU rádiového protokolu

## Související pojmy

- [PDCP – Packet Data Convergence Protocol](/mobilnisite/slovnik/pdcp/)
- [SDAP – Service Data Adaptation Protocol](/mobilnisite/slovnik/sdap/)
- [URLLC – Ultra Reliable Low Latency Communication](/mobilnisite/slovnik/urllc/)
- [ADP – Associated Delivery Procedures](/mobilnisite/slovnik/adp/)

## Definující specifikace

- **TS 26.822** (Rel-19) — 5G RTP Configurations Study Phase 2
- **TS 28.552** (Rel-20) — 5G Performance Management Measurements
- **TS 38.415** (Rel-19) — PDU Session User Plane Protocol

---

📖 **Anglický originál a plná specifikace:** [PSSN na 3GPP Explorer](https://3gpp-explorer.com/glossary/pssn/)
