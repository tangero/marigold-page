---
slug: "ueiri"
url: "/mobilnisite/slovnik/ueiri/"
type: "slovnik"
title: "UEIRI – UE Initiated Report Indication"
date: 2025-01-01
abbr: "UEIRI"
fullName: "UE Initiated Report Indication"
category: "Protocol"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/ueiri/"
summary: "UE Initiated Report Indication (UEIRI) je mechanismus protokolu zavedený ve 3GPP Release 19. Umožňuje uživatelskému zařízení (UE) proaktivně iniciovat a odesílat měřicí hlášení nebo indikace stavu do"
---

UEIRI je mechanismus protokolu 3GPP Release 19, který umožňuje uživatelskému zařízení (UE) proaktivně iniciovat a odesílat měřicí hlášení nebo indikace stavu do sítě bez předchozího vyžádání.

## Popis

UE Initiated Report Indication (UEIRI) je funkce protokolu v rámci specifikací 3GPP pro rádiový přístupový síť (RAN). Mění tradiční paradigma hlášení, kde síť (prostřednictvím gNB) typicky spouští hlášení odesláním měřicí konfigurace nebo požadavku na UE. S UEIRI je UE zmocněno iniciovat přenos hlášení na základě interních spouštěčů nebo zjištěných podmínek. Toto hlášení může obsahovat různé typy informací, jako jsou měření kvality kanálu ([CQI](/mobilnisite/slovnik/cqi/)), informace pro beamforming, polohová data, stav baterie nebo požadavky aplikační vrstvy.

Mechanismus funguje definováním nových signalizačních zpráv nebo rozšířením stávajících (např. v rámci protokolu [RRC](/mobilnisite/slovnik/rrc/) nebo prostřednictvím [MAC](/mobilnisite/slovnik/mac/) Control Elements), které může UE odeslat v uplinku bez předchozího downlinkového příkazu. Síť musí být schopna tyto nevyžádané indikace přijímat a zpracovávat. Specifikace (38.212, 38.213, 38.214, 38.300) podrobně popisují podmínky, za kterých může UE hlášení iniciovat, formát obsahu hlášení a jak by na něj měla síť reagovat. To často zahrnuje předkonfiguraci během navazování spojení, kdy síť udělí UE povolení pro určité typy iniciovaných hlášení.

Jeho úlohou je vytvořit responsivnější a efektivnější RAN. Tím, že UE může hlásit okamžitě při zjištění významné změny (např. náhlého poklesu kvality signálu nebo přechodu do režimu úspory energie), může síť reagovat rychleji, než kdyby musela UE periodicky dotazovat. Tím se podporuje vylepšené zvládání mobility, lepší správa QoS pro trhavý provoz a lepší podpora funkcí zaměřených na UE, jako je podmíněný handover nebo dynamická úspora energie.

## K čemu slouží

UEIRI bylo vytvořeno, aby řešilo omezení reaktivního, síťově řízeného modelu hlášení, zejména pro pokročilé scénáře 5G a budoucí 6G. V tradičních systémech síť nemusela mít včasné informace o náhlých změnách stavu UE, což vedlo ke zpožděným rozhodnutím o handoveru, neefektivní alokaci zdrojů nebo promarněným příležitostem k úspoře energie. UEIRI dává UE určitý stupeň autonomie, aby mohlo síť proaktivně informovat, což umožňuje rychlejší optimalizační smyčky.

Motivace vychází z případů užití vyžadujících nízkou latenci a vysokou efektivitu, jako je ultra-spolehlivá komunikace s nízkou latencí ([URLLC](/mobilnisite/slovnik/urllc/)), integrované snímání a komunikace a pokročilá mobilita ve vysokofrekvenčních pásmech. Podporuje také IoT zařízení, která mohou mít velmi sporadické komunikační potřeby; namísto neustálého dotazování ze strany sítě mohou hlásit pouze v případě potřeby. Release 19 zavedlo UEIRI jako součást probíhajících vylepšení, která mají učinit RAN inteligentnější a adaptivnější, snížit režii řízení a zlepšit celkový výkon systému.

## Klíčové vlastnosti

- Umožňuje UE autonomně iniciovat měřicí/stavová hlášení
- Snižuje latenci hlášení pro kritické změny stavu
- Podporuje dynamickou optimalizaci sítě na základě vstupů od UE v reálném čase
- Lze využít pro vylepšené postupy mobility a handoveru
- Usnadňuje hlášení úspory energie a stavu baterie UE
- Definováno v klíčových specifikacích NR protokolů (RRC, MAC, PHY)

## Související pojmy

- [RRC – Radio Resource Control](/mobilnisite/slovnik/rrc/)

## Definující specifikace

- **TS 38.212** (Rel-19) — NR Multiplexing and Channel Coding
- **TS 38.213** (Rel-19) — NR Physical Layer Control Procedures
- **TS 38.214** (Rel-19) — NR Physical Layer Procedures for Data
- **TS 38.300** (Rel-19) — NG-RAN Overall Description

---

📖 **Anglický originál a plná specifikace:** [UEIRI na 3GPP Explorer](https://3gpp-explorer.com/glossary/ueiri/)
