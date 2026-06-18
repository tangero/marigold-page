---
slug: "x-mac"
url: "/mobilnisite/slovnik/x-mac/"
type: "slovnik"
title: "X-MAC – Computed MAC-I"
date: 2025-01-01
abbr: "X-MAC"
fullName: "Computed MAC-I"
category: "Security"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/x-mac/"
summary: "X-MAC (vypočítaný MAC-I) je bezpečnostní parametr používaný v LTE a NR k ověření integrity a původu signalizačních zpráv RRC a NAS. Jedná se o očekávaný kód pro ověření zprávy (Message Authentication"
---

X-MAC je očekávaný kód pro ověření zprávy (Message Authentication Code) vypočítaný přijímající entitou za účelem ověření integrity a původu signalizačních zpráv porovnáním s přijatou hodnotou MAC-I.

## Popis

X-MAC je kryptografická hodnota vypočítávaná během ověřování integrity v protokolech řízení rádiových prostředků ([RRC](/mobilnisite/slovnik/rrc/)) a ne-přístupové vrstvy ([NAS](/mobilnisite/slovnik/nas/)) v LTE ([E-UTRAN](/mobilnisite/slovnik/e-utran/)) a NR (NG-RAN). Nejde o přenášené pole, ale o interně vypočítanou hodnotu. Když je odeslána zabezpečená zpráva, vysílající entita (např. gNB nebo [AMF](/mobilnisite/slovnik/amf/)) vypočítá kód pro ověření integrity zprávy ([MAC-I](/mobilnisite/slovnik/mac-i/)) pomocí kryptografického integritního algoritmu (jako 128-EIA1, EIA2 nebo EIA3), tajného integritního klíče (K_{RRCint}, K_{RRCint} pro NR, nebo K_{NASint}), hodnoty COUNT (čítače bránícího opakovaným útokům), identifikátoru přenosového kanálu, směrového bitu a samotné zprávy. Tento MAC-I je připojen ke zprávě.

Po přijetí přijímající entita (např. UE nebo síťový uzel) provede stejný výpočet nad přijatými daty zprávy před ověřením MAC-I. Výsledek tohoto lokálního výpočtu je X-MAC. Příjemce následně porovná vypočítaný X-MAC s MAC-I přijatým ve zprávě. Pokud se přesně shodují, potvrzuje to, že zpráva nebyla během přenosu změněna (integrita) a že pochází od entity disponující správným tajným klíčem (autentizace). Pokud se neshodují, je zpráva zahozena a selhání je zaznamenáno, což může spustit procedury obnovy bezpečnosti.

Výpočet je podrobně specifikován v dokumentech 3GPP TS 33.401 (pro LTE) a TS 33.501 (pro 5G). Integritní klíče jsou odvozeny během procedury autentizace a dohody klíčů ([AKA](/mobilnisite/slovnik/aka/)) a jsou specifické pro UE, relaci a protokolovou vrstvu. Hodnota COUNT je systematicky inkrementována a její synchronizace mezi odesílatelem a příjemcem je klíčová; neshoda způsobí selhání ověření X-MAC versus MAC-I. Tento mechanismus chrání kritické signalizační příkazy, jako jsou instrukce k předání spojení, rekonfigurace spojení a žádosti o služby, před neoprávněnou manipulací nebo paděláním.

## K čemu slouží

Ověření X-MAC existuje za účelem splnění základních bezpečnostních požadavků na integritu a autentizaci původu dat pro signalizaci řídicí roviny. Bez něj by útočník mohl modifikovat nebo falšovat signalizační zprávy, což by vedlo k narušení služeb, vynucenému předání spojení do nelegitimních buněk, odmítnutí služby nebo narušení soukromí. Před 3G a plnou implementací kryptografické integrity v LTE/5G měly některé signalizační zprávy slabší nebo žádnou ochranu integrity, což činilo sítě zranitelnými vůči určitým útokům.

Zavedení povinné integritní ochrany se silnými algoritmy v LTE Rel-8 a její pokračování v NR byla přímou reakcí na vyvíjející se prostředí hrozeb pro mobilní sítě. Porovnání X-MAC je operačním srdcem této ochrany. Umožňuje přijímači autonomně a efektivně ověřit každou zabezpečenou zprávu bez další interakce se sítí. Koncepce využívající vypočítanou hodnotu (X-MAC) versus přijatou ([MAC-I](/mobilnisite/slovnik/mac-i/)) poskytuje jasné procedurální oddělení mezi krokem výpočtu a ověření, což je důležité pro bezpečnou implementaci a testování softwaru.

## Klíčové vlastnosti

- Lokálně vypočítaná hodnota pro ověření integrity zpráv RRC/NAS
- Používá standardizované integritní algoritmy (EIA1, EIA2, EIA3, NIA1 atd.)
- Odvozena z tajných relacích klíčů, hodnot COUNT a obsahu zprávy
- Zásadní pro prevenci neoprávněné manipulace se zprávami, padělání a opakovaných útoků
- Selhání ověření vede ke zahození zprávy a nahlášení bezpečnostní události
- Základní prvek bezpečnostní architektury LTE i 5G NR

## Související pojmy

- [MAC-I – Message Authentication Code for Integrity](/mobilnisite/slovnik/mac-i/)
- [RRC – Radio Resource Control](/mobilnisite/slovnik/rrc/)
- [NAS – Non-Access Stratum](/mobilnisite/slovnik/nas/)
- [AKA – Authentication and Key Agreement](/mobilnisite/slovnik/aka/)

## Definující specifikace

- **TS 36.323** (Rel-19) — PDCP Protocol Specification
- **TS 38.323** (Rel-19) — Packet Data Convergence Protocol (PDCP)

---

📖 **Anglický originál a plná specifikace:** [X-MAC na 3GPP Explorer](https://3gpp-explorer.com/glossary/x-mac/)
