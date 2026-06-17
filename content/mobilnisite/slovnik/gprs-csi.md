---
slug: "gprs-csi"
url: "/mobilnisite/slovnik/gprs-csi/"
type: "slovnik"
title: "GPRS-CSI – GPRS CAMEL Subscription Information"
date: 2025-01-01
abbr: "GPRS-CSI"
fullName: "GPRS CAMEL Subscription Information"
category: "Services"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/gprs-csi/"
summary: "Sada dat předplatného CAMEL pro sítě GPRS, která umožňuje služby inteligentní sítě, jako je předplacené účtování a služby založené na poloze, pro paketově přepínaná data. Umožňuje síti aplikovat servi"
---

GPRS-CSI je sada dat předplatného CAMEL pro sítě GPRS, která umožňuje služby inteligentní sítě, jako je předplacené účtování, tím, že síti dovoluje aplikovat servisní logiku řízenou externím SCP během GPRS relace.

## Popis

GPRS-CSI je soubor dat specifických pro účastníka, uložený v [HLR](/mobilnisite/slovnik/hlr/), který umožňuje funkci [CAMEL](/mobilnisite/slovnik/camel/) (Customised Applications for Mobile networks Enhanced Logic) pro paketově přepínané služby [GPRS](/mobilnisite/slovnik/gprs/)/UMTS. Definuje spouštěče a informace potřebné pro SGSN k interakci s bodem řízení služeb CAMEL (gsmSCP) během aktivace PDP kontextu nebo konkrétní události paketových dat. Klíčové komponenty zahrnují samotná data GPRS-CSI, která obsahují adresu gsmSCF, servisní klíč a různé body detekce spouštěčů (TDP) pro události, jako je vytvoření PDP kontextu. Když účastník s GPRS-CSI zahájí datovou relaci, SGSN po detekci nakonfigurovaného TDP pozastaví proceduru a odešle zprávu [CAP](/mobilnisite/slovnik/cap/) (CAMEL Application Part) určenému gsmSCF. gsmSCF, hostující servisní logiku, pak může SGSN instruovat, jak pokračovat, například aplikací specifických pravidel účtování, povolením nebo zamítnutím kontextu či úpravou parametrů QoS. Tato architektura odděluje servisní logiku od přepínačů jádra sítě, což umožňuje rychlé nasazení pokročilých služeb zaměřených na účastníka bez nutnosti aktualizace každého síťového uzlu. Interakce je standardizována prostřednictvím protokolu CAP přes rozhraní Gs (mezi SGSN a gsmSCF) nebo nepřímo přes rozhraní Gr (HLR k SGSN) pro poskytování dat.

## K čemu slouží

GPRS-CSI bylo vytvořeno za účelem rozšíření schopností inteligentní sítě ([IN](/mobilnisite/slovnik/in/)) [CAMEL](/mobilnisite/slovnik/camel/), původně navržených pro okruhově přepínanou hlasovou službu, do paketově přepínané domény zavedené s [GPRS](/mobilnisite/slovnik/gprs/) a UMTS. Před jeho zavedením bylo pokročilé řízení služeb v reálném čase pro datové relace (jako předplacená data nebo účtování podle obsahu) obtížné a často vyžadovalo proprietární řešení v rámci GGSN nebo externí fakturační systémy s omezenou interakcí v reálném čase. GPRS-CSI standardizovalo mechanismus pro síť, aby mohla během datové relace vyvolat externí servisní logiku, čímž vyřešilo problém flexibilního a reálného řízení služeb pro paketová data. To operátorům umožnilo nabízet sofistikované předplacené datové tarify, služby založené na poloze a funkce kontroly utrácení přímo v rámci paketového jádra, což vytvořilo nové zdroje příjmů a zlepšilo zákaznický zážitek díky možnosti kontrol zůstatku a vynucování politik v reálném čase. Jeho vytvoření bylo motivováno komerční potřebou zpeněžit datové služby GPRS se stejnou agilitou jako hlasové služby, čímž se řešila omezení statického, předplatného založeného datového účtování.

## Klíčové vlastnosti

- Umožňuje řízení služeb CAMEL pro procedury PDP kontextu GPRS
- Uloženo v HLR jako součást profilu účastníka a staženo do SGSN
- Definuje body detekce spouštěčů (TDP) pro události, jako je vytvoření PDP kontextu
- Spouští CAP dialog mezi SGSN a externím gsmSCF
- Umožňuje řízení účtování v reálném čase (např. předplacená data)
- Podporuje servisní logiku pro pokročilé služby paketových dat

## Související pojmy

- [CAMEL – Customised Applications for Mobile network Enhanced Logic](/mobilnisite/slovnik/camel/)
- [HLR – Home Location Register](/mobilnisite/slovnik/hlr/)
- [CAP – CAMEL Application Part](/mobilnisite/slovnik/cap/)

## Definující specifikace

- **TS 23.078** (Rel-19) — CAMEL Phase 4 Stage 2 Specification

---

📖 **Anglický originál a plná specifikace:** [GPRS-CSI na 3GPP Explorer](https://3gpp-explorer.com/glossary/gprs-csi/)
