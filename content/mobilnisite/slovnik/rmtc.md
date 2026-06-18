---
slug: "rmtc"
url: "/mobilnisite/slovnik/rmtc/"
type: "slovnik"
title: "RMTC – RSSI Measurement Timing Configuration"
date: 2025-01-01
abbr: "RMTC"
fullName: "RSSI Measurement Timing Configuration"
category: "Radio Access Network"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/rmtc/"
summary: "RSSI Measurement Timing Configuration (RMTC) je konfigurace poskytovaná sítí, která uživatelskému zařízení (UE) určuje, kdy a na jakých kmitočtech má provádět měření indikátoru síly přijímaného signál"
---

RMTC je konfigurace poskytovaná sítí, která uživatelskému zařízení (UE) určuje, kdy a na jakých kmitočtech má provádět měření RSSI pro vyhodnocení obsazenosti kanálu.

## Popis

[RSSI](/mobilnisite/slovnik/rssi/) Measurement Timing Configuration (RMTC) je klíčový mechanismus definovaný ve specifikacích 3GPP pro umožnění funkce Naslouchej-před-mluvením ([LBT](/mobilnisite/slovnik/lbt/)) a měření obsazenosti kanálu v nelicencovaném a sdíleném spektru. Jedná se o konfigurační zprávu odesílanou sítí (prostřednictvím signalizace [RRC](/mobilnisite/slovnik/rrc/)) uživatelskému zařízení (UE), která definuje konkrétní měřicí okno pro provádění širokopásmových měření RSSI na jednom nebo více kmitočtech nosné. Primárním cílem je snímání rádiového prostředí za účelem zjištění, zda je kanál volný nebo obsazený, než síť nebo UE začne vysílat, což je regulatorní požadavek v mnoha nelicencovaných pásmech (např. 5 GHz).

Konfigurace RMTC zahrnuje několik klíčových parametrů: kmitočet nosné (nebo jejich seznam) pro měření, šířku pásma měření, načasování měřicího okna (určené jako offset a délka vůči referenčnímu [SFN](/mobilnisite/slovnik/sfn/)) a periodicitu těchto měřicích příležitostí. UE tuto konfiguraci používá k aktivaci svého přijímače ve stanovených časech a na stanovených kmitočtech, změří celkový přijímaný výkon (RSSI) v rámci nakonfigurovaného pásma a výsledky zpracuje. Měření je typicky mechanismem detekce energie, nevyžaduje synchronizaci s žádným konkrétním signálem. UE následně hlásí výsledky měření zpět síti, často ve formě statistik obsazenosti kanálu (např. procento času, kdy RSSI překročilo určitou prahovou hodnotu).

Síť tyto hlášení využívá pro dynamický výběr kanálu a procedury přístupu ke kanálu. Například v přístupu s licenční podporou ([LAA](/mobilnisite/slovnik/laa/)) a [NR-U](/mobilnisite/slovnik/nr-u/) (NR v nelicencovaném spektru) může gNB nakonfigurovat UE pomocí RMTC k průzkumu volných kanálů v nelicencovaném pásmu. Na základě souhrnných hlášení od více UE se pak gNB může rozhodnout, kterou nosnou použít pro aktivaci sekundární buňky (SCell), čímž zlepšuje celkový výkon systému a koexistenci s jinými systémy, jako je Wi-Fi. Mechanismus RMTC umožňuje síti delegovat úlohu snímání na UE, čímž poskytuje distribuovaný pohled na rádiové prostředí bez nutnosti, aby základnová stanice sama neustále monitorovala všechny potenciální kanály.

## K čemu slouží

RMTC bylo zavedeno ve verzi 3GPP Release 13 jako součást pracovní položky LTE-LAA (License-Assisted Access) pro umožnění provozu LTE v nelicencovaném pásmu 5 GHz. Hlavní problém, který řešilo, bylo, jak efektivně splnit regulatorní požadavky Naslouchej-před-mluvením ([LBT](/mobilnisite/slovnik/lbt/)) při zachování síťové kontroly. Na rozdíl od Wi-Fi, které používá distribuovaný přístup s řízením kolizí ([CSMA/CA](/mobilnisite/slovnik/csma-ca/)), přijal LAA centralizovanější přístup, kdy síť (eNodeB) koordinuje přístup ke kanálu. RMTC poskytlo nástroj pro tuto koordinaci tím, že umožnilo síti instruovat UE – zařízení již vybavená přijímači – aby za ni prováděla potřebné snímání kanálu.

Tento přístup řešil několik omezení. Za prvé poskytl síti širší a přesnější pohled na podmínky rušení v různých místech uvnitř buňky, čehož jediné měření základnové stanice nemohlo dosáhnout. Za druhé umožnil efektivní využití prostředků UE konfigurací měření pouze v případě potřeby a na konkrétních kmitočtech zájmu. Za třetí byl nezbytný pro spravedlivou koexistenci s jinými technologiemi, jako je Wi-Fi, protože umožnil systému LTE/5G přesně vyhodnotit obsazenost kanálu před vysíláním. Koncept byl později přenesen do 5G NR-U (Release 16 a novější), kde zůstává základním prvkem pro provoz NR ve sdíleném a nelicencovaném spektru a podporuje případy užití jako rozšířené mobilní širokopásmové připojení a nasazení privátních sítí.

## Klíčové vlastnosti

- Konfiguruje měřicí okna RSSI na straně UE pro snímání kanálu.
- Zahrnuje parametry pro kmitočet nosné, šířku pásma, časový offset, délku a periodicitu.
- Nezbytné pro splnění regulatorních požadavků Naslouchej-před-mluvením (LBT) v nelicencovaném spektru.
- Umožňuje síťově koordinovaný výběr kanálu pro LAA a NR-U.
- Podporuje hlášení měření pro statistiky obsazenosti kanálu.
- Umožňuje distribuované snímání prostředí využitím více UE.

## Související pojmy

- [LAA – Licensed-Assisted Access](/mobilnisite/slovnik/laa/)
- [NR-U – New Radio Unlicensed](/mobilnisite/slovnik/nr-u/)
- [LBT – Listen Before Talk](/mobilnisite/slovnik/lbt/)
- [RSSI – Received Signal Strength Indication](/mobilnisite/slovnik/rssi/)

## Definující specifikace

- **TS 36.300** (Rel-19) — E-UTRAN Radio Interface Protocol Architecture Overview
- **TS 36.331** (Rel-19) — LTE RRC Protocol Specification
- **TS 38.331** (Rel-19) — NR Radio Resource Control (RRC) Protocol Specification

---

📖 **Anglický originál a plná specifikace:** [RMTC na 3GPP Explorer](https://3gpp-explorer.com/glossary/rmtc/)
