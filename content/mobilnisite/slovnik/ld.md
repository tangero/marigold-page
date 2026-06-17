---
slug: "ld"
url: "/mobilnisite/slovnik/ld/"
type: "slovnik"
title: "LD – Local Descriptor"
date: 2025-01-01
abbr: "LD"
fullName: "Local Descriptor"
category: "Protocol"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/ld/"
summary: "Protokolový prvek v rámci řídicího protokolu mediálních bran H.248/Megaco. Popisuje vlastnosti ukončení (termination) na mediální bráně (MG), které jsou specifické pro její lokální kontext, jako jsou"
---

LD je protokolový prvek v H.248/Megaco, který popisuje lokální vlastnosti, jako IP adresu a kodek, ukončení (termination) mediální brány pro správu streamů.

## Popis

Lokální deskriptor (LD) je základní datová struktura v rámci protokolu H.248, známého také jako Media Gateway Control Protocol ([MGCP](/mobilnisite/slovnik/mgcp/)) Megaco. H.248 je standardní protokol používaný pro řízení mediálních bran (MGs) z řadiče mediálních bran ([MGC](/mobilnisite/slovnik/mgc/)) nebo softswitchu v dekomponovaných síťových architekturách, jako je IMS a VoLTE. 'Ukončení' (Termination) v H.248 představuje logickou entitu na [MG](/mobilnisite/slovnik/mg/), která zdrojuje nebo přijímá mediální nebo řídicí streamy, například fyzický okruh trunku (TDM) nebo koncový bod RTP streamu (IP). Každé ukončení má vlastnosti popsané deskriptory. Lokální deskriptor konkrétně definuje vlastnosti ukončení, které jsou lokální pro samotnou mediální bránu. To typicky zahrnuje transportní informace potřebné k navázání mediální relace. Pro IP-based ukončení obsahuje LD klíčové podrobnosti, jako je lokální IP adresa (v4 nebo v6), číslo portu UDP/TCP pro RTP/RTCP, podporované mediální kodeky (např. [AMR](/mobilnisite/slovnik/amr/), G.711), parametry paketizace, šířku pásma a další atributy podobné protokolu pro popis relace (SDP). Když MGC instruuje MG ke změně ukončení (např. pro přípravu hovoru), odešle příkaz, který může obsahovat LD, aby MG sdělil 'použij tuto IP adresu a port s těmito kodeky'. MG odpoví Vzdáleným deskriptorem (RD) obsahujícím odpovídající informace z druhého konce relace. Pár LD/RD je zásadní pro správnou konfiguraci mediální roviny MG. LD je přenášen v rámci transakčních zpráv H.248, nejčastěji v příkazu 'Modify' nebo v deskriptorech 'LocalControl' a 'Local' příkazu 'Add'. Jeho struktura je flexibilní, umožňující širokou škálu mediálních typů a síťových scénářů, což z něj činí primární mechanismus pro MGC k provizionování prostředků pro přenos médií na bráně.

## K čemu slouží

Lokální deskriptor existuje, aby poskytl standardizovaný, abstrahovaný způsob pro řídicí entitu hovoru ([MGC](/mobilnisite/slovnik/mgc/)), jak nakonfigurovat parametry specifické pro média na samostatném zařízení pro zpracování médií ([MG](/mobilnisite/slovnik/mg/)). Před protokoly jako H.248 byly média a řízení hovoru často integrovány v monolitických přepínačích, což činilo sítě nepružnými. Snaha o dekomponované sítě příští generace ([NGN](/mobilnisite/slovnik/ngn/)) a IP Multimedia Subsystem (IMS) vyžadovala čisté oddělení řídicí a mediální roviny. Protokol H.248 byl vytvořen pro správu tohoto oddělení a LD je jeho klíčovou součástí. Řeší problém, jak může řadič, který rozumí logice hovoru a vyjednávání relace, přesně instruovat jednoduché mediální zařízení, jak odesílat a přijímat mediální streamy. Usnadňuje potřebu interoperability mezi řadiči a bránami od různých výrobců tím, že poskytuje standardizovanou syntaxi pro předávání parametrů mediální relace. LD umožňuje, aby MGC zůstal agnostický vůči konkrétnímu hardwaru nebo nízkoúrovňovému softwaru MG, a jednoduše poskytuje potřebný popis relace. To umožňuje škálovatelné, flexibilní síťové architektury, kde výkonné řadiče mohou spravovat velké fondy specializovaných mediálních prostředků, což je základním kamenem moderních VoIP a telekomunikačních sítí.

## Klíčové vlastnosti

- Konfigurace mediální relace: Nese základní parametry pro nastavení mediálního streamu, včetně IP adresy, portu a seznamu kodeků.
- Prvek protokolu H.248: Definovaný typ deskriptoru v rámci standardu H.248/Megaco (často odkazovaný v balíčcích - packages).
- Spárován se vzdáleným deskriptorem: Spolupracuje s RD, aby poskytl kompletní informace o relaci pro obousměrný mediální stream.
- Podpora různých typů médií: Umí popsat parametry pro audio (RTP), video, text a další média podle definice v balíčcích H.248.
- Použití v příkazech Modify/Add: Primárně je zahrnut v příkazech 'Modify' a 'Add' protokolu H.248 odesílaných z MGC na MG.
- Umožňuje oddělení řízení a médií: Klíčový prvek pro dekomponovanou architekturu, který umožňuje MGC řídit mediální rovinu MG.

## Související pojmy

- [MGC – Media Gateway Controller](/mobilnisite/slovnik/mgc/)

## Definující specifikace

- **TS 29.238** (Rel-19) — H.248 Profile for IBCF-TrGW Interface
- **TS 29.334** (Rel-19) — IMS-ALG to IMS-AGW Interface Protocol

---

📖 **Anglický originál a plná specifikace:** [LD na 3GPP Explorer](https://3gpp-explorer.com/glossary/ld/)
