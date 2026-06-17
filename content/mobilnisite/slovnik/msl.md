---
slug: "msl"
url: "/mobilnisite/slovnik/msl/"
type: "slovnik"
title: "MSL – Minimum Security Level"
date: 2002-01-01
abbr: "MSL"
fullName: "Minimum Security Level"
category: "Security"
segment: "Security"
canonical: "https://3gpp-explorer.com/glossary/msl/"
summary: "MSL je parametr bezpečnostní politiky vynucované sítí, asociovaný s účastníkem. Definuje minimální požadované zabezpečovací algoritmy (např. pro šifrování), které musí být použity pro komunikaci danéh"
---

MSL je parametr minimálního požadovaného zabezpečovacího algoritmu, který síť vynucuje pro účastníka, aby zabránila návratu k slabším a prolomeným šifrovacím metodám.

## Popis

Minimální úroveň zabezpečení (MSL) je parametr specifický pro účastníka, uložený v jeho profilu v autentizačním centru (AuC) a potenciálně předávaný obslužnému síťovému uzlu (jako [MSC](/mobilnisite/slovnik/msc/) nebo SGSN). Jedná se o mechanismus politiky, který stanovuje základní sílu kryptografických algoritmů používaných k ochraně komunikace účastníka. MSL je typicky definován jako uspořádaný seznam nebo prahová hodnota odkazující na konkrétní zabezpečovací algoritmy. Například v kontextu šifrování v okruhově spínané ([CS](/mobilnisite/slovnik/cs/)) doméně v GSM a UMTS může specifikovat, že musí být použit proudový šifr [A5/1](/mobilnisite/slovnik/a5-1/) nebo A5/3, a že slabší [A5/2](/mobilnisite/slovnik/a5-2/) nebo A5/0 (bez šifrování) nejsou pro tohoto účastníka přípustné.

Když se účastník připojí k síti nebo iniciuje službu, provedou se autentizační a šifrovací procedury. Síť (např. VLR/SGSN) získá bezpečnostní kontext účastníka z [HLR](/mobilnisite/slovnik/hlr/)/AuC, který zahrnuje šifrovací klíče a indikátor MSL. Síť poté navrhne mobilní stanici ([MS](/mobilnisite/slovnik/ms/)) šifrovací algoritmus na základě jejích schopností a MSL. Mobilní stanice také zná MSL, který je typicky uložen na USIM. Pokud síť navrhne algoritmus pod stanoveným MSL (např. navrhne A5/2, když MSL vyžaduje A5/1 nebo silnější), musí mobilní stanice příkaz k nastavení šifrovacího režimu odmítnout a může spojení ukončit. Tím je zajištěno, že komunikace nemůže být navázána s úrovní zabezpečení, která je pro daného účastníka považována za nedostatečnou.

Mechanismus MSL je klíčovou obranou proti útokům typu bidding-down (nucení k nižší úrovni), při kterých může útočník manipulací s negociačními zprávami donutit síť a mobilní stanici, aby se dohodly na slabém, prolomitelném šifrovacím algoritmu. Existence předem dohodnuté minimální úrovně uložené jak v síti, tak na USIM takové útoky znemožňuje, protože mobilní stanice nepřijme podstandardní algoritmus. Koncept MSL je obzvláště důležitý pro vysokorizikové cíle (např. vládní, korporátní uživatele) a získal na významu s odhalením historických slabin v raných algoritmech jako A5/1 a A5/2. Umožňuje operátorům proaktivně řídit bezpečnostní rizika aktualizací MSL pro účastníky, jakmile se stanou dostupnější nové, silnější algoritmy a starší jsou vyřazovány.

## K čemu slouží

MSL byl zaveden, aby řešil zranitelnost vlastní protokolům pro dohodu algoritmu, konkrétně hrozbu útoků typu bidding-down. Raná bezpečnost v celulárních sítích, zejména v GSM, spoléhala na sadu šifrovacích algoritmů ([A5/x](/mobilnisite/slovnik/a5-x/)) různé síly. Síť a mobilní stanice se dohodly na použitém algoritmu na základě vzájemné podpory. Tento vyjednávací proces nebyl chráněn, což umožňovalo útoku typu man-in-the-middle zachytit a upravit zprávy tak, aby se obě strany dohodly na nejslabším algoritmu, který obě podporovaly (např. [A5/2](/mobilnisite/slovnik/a5-2/) nebo dokonce žádné šifrování A5/0), který pak útočník mohl snadno prolomit.

MSL poskytuje řešení tohoto problému založené na politice. Statickou konfigurací minimální přijatelné úrovně zabezpečení v profilu účastníka (AuC) a na USIM vytváří důvěryhodný referenční bod. Tím odstraňuje závislost na integritě dynamického vyjednávacího signalizace pro stanovení síly zabezpečení. Jeho vytvoření bylo motivováno rostoucí sofistikovaností útoků na mobilní sítě a potřebou chránit konkrétní účastníky nebo třídy služeb nad rámec základní úrovně poskytované široké veřejnosti. Umožňuje síťovým operátorům vynucovat silnější bezpečnostní politiky pro citlivou komunikaci, aniž by vyžadovali univerzální upgrade všech mobilních stanic a síťových uzlů, a umožňuje tak fázovaný a riziky řízený přístup k posilování síťové bezpečnosti.

## Klíčové vlastnosti

- Parametr bezpečnostní politiky specifický pro účastníka, uložený v AuC/USIM
- Definuje povinnou minimální sílu kryptografických algoritmů
- Chrání před útoky typu bidding-down při dohodě šifrovacího algoritmu
- Vynucován jak sítí, tak mobilní stanicí
- Umožňuje vrstvené bezpečnostní politiky pro různé skupiny účastníků
- Umožňuje fázované vyřazování slabých, prolomených algoritmů

## Související pojmy

- [AUC – Authentication Centre](/mobilnisite/slovnik/auc/)

## Definující specifikace

- **TS 23.048** (Rel-5) — Secured Packets for UICC Remote Management

---

📖 **Anglický originál a plná specifikace:** [MSL na 3GPP Explorer](https://3gpp-explorer.com/glossary/msl/)
