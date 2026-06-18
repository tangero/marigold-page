---
slug: "amr-nb"
url: "/mobilnisite/slovnik/amr-nb/"
type: "slovnik"
title: "AMR-NB – Adaptive Multi-Rate Narrowband"
date: 2025-01-01
abbr: "AMR-NB"
fullName: "Adaptive Multi-Rate Narrowband"
category: "Services"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/amr-nb/"
summary: "AMR-NB je standard řečového kodeku pro úzkopásmové hlasové služby v sítích 3GPP, pracující s vzorkovací frekvencí 8 kHz a přenosovými rychlostmi od 4,75 do 12,2 kbps. Dynamicky přizpůsobuje rychlost k"
---

AMR-NB je úzkopásmový řečový kodek 3GPP, který dynamicky přizpůsobuje svou přenosovou rychlost, aby udržel kvalitu hlasu při různých podmínkách přenosového kanálu. Je základním prvkem pro hlasové služby v sítích GSM, UMTS a LTE.

## Popis

AMR-NB je víceúrovňový řečový kodek využívající technologii Algebraic Code Excited Linear Prediction ([ACELP](/mobilnisite/slovnik/acelp/)) s osmi diskrétními přenosovými rychlostmi: 4,75; 5,15; 5,90; 6,70; 7,40; 7,95; 10,20 a 12,20 kbps. Kodek pracuje s 20ms rámci řeči, z nichž každý obsahuje 160 vzorků při vzorkovací frekvenci 8 kHz. Každý rámec je zpracován sérií stupňů zpracování signálu včetně analýzy lineárního prediktivního kódování ([LPC](/mobilnisite/slovnik/lpc/)), analýzy výšky tónu (pitch) a prohledávání algebraického kódového slovníku za účelem vytvoření komprimované reprezentace řeči.

Architektura se skládá z kodéru, který analyzuje řečové signály za účelem extrakce parametrů včetně LPC koeficientů, parametrů adaptivního kódového slovníku (pitch lag a zesílení) a parametrů pevného kódového slovníku (indexy algebraického kódového slovníku a zesílení). Dekodér rekonstruuje řeč pomocí těchto parametrů prostřednictvím syntetického filtru, který kombinuje excitační signál z obou kódových slovníků. Kodek zahrnuje mechanismy detekce hlasové aktivity ([VAD](/mobilnisite/slovnik/vad/)) a nespojitého přenosu ([DTX](/mobilnisite/slovnik/dtx/)) pro snížení přenosu během období ticha, což významně šetří síťové zdroje.

AMR-NB implementuje adaptaci rychlosti řízenou zdrojem, kdy síť může nařídit mobilní stanici přepínání mezi různými módy kodeku na základě měření kvality kanálu. Tato adaptace probíhá na vrstvě řízení rádiových prostředků ([RRC](/mobilnisite/slovnik/rrc/)), přičemž změny módu typicky nastávají na hranicích rámců. Kodek zahrnuje generování komfortního šumu ([CNG](/mobilnisite/slovnik/cng/)) během DTX period, aby byla zachována přirozeně znějící pauza a předešlo se dojmu přerušení hovoru. Mechanismy maskování chyb pomáhají udržet přijatelnou kvalitu hlasu při ztrátě rámců extrapolací parametrů z předchozích nepoškozených rámců.

V síťové architektuře AMR-NB primárně funguje v uživatelské rovině mezi mobilním terminálem a mediální bránou jádra sítě. Pro přepojované hovory (circuit-switched) kodek zpracovává řeč v základnovém procesoru terminálu a přenáší ji přes rozhraní vzduchu. V implementacích s přepínáním paketů, jako je VoLTE, jsou rámce AMR-NB zapouzdřeny v paketech [RTP](/mobilnisite/slovnik/rtp/)/[UDP](/mobilnisite/slovnik/udp/)/IP pro přenos přes IP multimediální subsystém (IMS). Interoperabilita kodeku se staršími systémy je zachována prostřednictvím transkódovacích funkcí v mediálních branách při připojení k PSTN nebo jiným sítím.

## K čemu slouží

AMR-NB byl vyvinut, aby řešil omezení dřívějších řečových kodeků GSM (Full Rate, Half Rate a Enhanced Full Rate), které pracovaly s pevnými přenosovými rychlostmi a nemohly se přizpůsobit měnícím se rádiovým podmínkám. Předchozí kodeky buď poskytovaly dobrou kvalitu, ale s neefektivním využitím spektra, nebo šetřily šířku pásma na úkor kvality hlasu. Přístup s pevnou rychlostí znamenal, že sítě musely být dimenzovány na nejhorší podmínky, což vedlo k neefektivnímu využití zdrojů.

Hlavní motivací bylo vytvořit kodek, který by dokázal udržet konzistentní kvalitu hlasu při různých podmínkách kanálu a zároveň optimalizovat spektrální účinnost. Díky možnosti dynamického přepínání rychlostí umožňuje AMR-NB sítím v reálném čase hledat kompromis mezi kvalitou hlasu a kapacitou kanálu. Tato přizpůsobivost byla obzvláště důležitá, když se mobilní sítě rozšiřovaly do oblastí s náročným rádiovým prostředím a když rostla hustota účastníků, což vytvářelo tlak na omezené spektrální zdroje.

AMR-NB také řešil potřebu univerzálního řečového kodeku, který by mohl fungovat napříč různými generacemi sítí a usnadňovat mezinárodní roaming. Jeho návrh zohledňoval zpětnou kompatibilitu s existující infrastrukturou a zároveň poskytoval migrační cestu k efektivnějším hlasovým službám. Víceúrovňové možnosti kodeku umožnily operátorům implementovat různé politiky kvality služeb a optimalizovat své sítě na základě konkrétních scénářů nasazení a obchodních požadavků.

## Klíčové vlastnosti

- Osm diskrétních přenosových rychlostí od 4,75 do 12,2 kbps pro flexibilní kompromisy mezi kvalitou a šířkou pásma
- Technologie kódování Algebraic Code Excited Linear Prediction (ACELP) pro vysokou kvalitu řeči
- Dynamická adaptace rychlosti na základě podmínek kanálu řízená síťovými příkazy
- Detekce hlasové aktivity (VAD) a nespojitý přenos (DTX) pro kompresi období ticha
- Generování komfortního šumu (CNG) během období ticha pro zachování přirozeného průběhu konverzace
- Robustní mechanismy maskování chyb pro podmínky ztráty rámců

## Související pojmy

- [AMR-WB – Adaptive Multi-Rate Wideband Speech Codec](/mobilnisite/slovnik/amr-wb/)

## Definující specifikace

- **TR 22.813** (Rel-10) — Enhanced Voice Services for EPS Study
- **TS 26.114** (Rel-19) — IMS Multimedia Telephony Media Handling
- **TS 26.177** (Rel-19) — DSR Extended Advanced Front-end Test Sequences
- **TS 26.447** (Rel-19) — EVS Frame Loss Concealment Procedure
- **TR 26.935** (Rel-19) — Speech Codec Performance for Packet Switched Multimedia
- **TR 26.943** (Rel-19) — SES Codec Selection Report

---

📖 **Anglický originál a plná specifikace:** [AMR-NB na 3GPP Explorer](https://3gpp-explorer.com/glossary/amr-nb/)
