---
slug: "c-rnc"
url: "/mobilnisite/slovnik/c-rnc/"
type: "slovnik"
title: "C-RNC – Controlling Radio Network Controller"
date: 2025-01-01
abbr: "C-RNC"
fullName: "Controlling Radio Network Controller"
category: "Radio Access Network"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/c-rnc/"
summary: "C-RNC je klíčový síťový prvek v UTRAN, který spravuje rádiové zdroje a řídí jeden nebo více Node B. Zajišťuje správu rádiových zdrojů, řízení přístupu a funkce mobility pro připojená UE, čímž zajišťuj"
---

C-RNC je řídicí radiový síťový kontrolér (Controlling Radio Network Controller) v UTRAN, který spravuje rádiové zdroje, řídí Node B a provádí řízení přístupu (admission control) a správu mobility pro připojená UE.

## Popis

Řídicí radiový síťový kontrolér (C-RNC) je základní součást architektury UMTS Terrestrial Radio Access Network ([UTRAN](/mobilnisite/slovnik/utran/)), definované ve 3GPP Release 99 a novějších. Slouží jako řídicí entita pro jeden nebo více Node B (obdoba základnové stanice v UMTS). C-RNC je zodpovědný za správu a alokaci rádiových zdrojů v buňkách pod jeho kontrolou. Ukončuje rozhraní Iub směrem k Node B a rozhraní Iur směrem k ostatním [RNC](/mobilnisite/slovnik/rnc/), což umožňuje mobilitu mezi RNC a koordinaci zdrojů. Jeho primární rolí je sloužit jako přístupový bod služeb (service access point) pro všechny služby, které UTRAN poskytuje jádru sítě (Core Network, CN), například správu spojení k uživatelskému zařízení (UE).

Operačně C-RNC provádí kritické algoritmy správy rádiových zdrojů (Radio Resource Management, [RRM](/mobilnisite/slovnik/rrm/)). To zahrnuje funkce jako řízení přístupu (Admission Control), kde C-RNC vyhodnocuje, zda lze nový rádiový přístupový bearer vytvořit bez ohrožení kvality stávajících spojení. Provádí také řízení zahlcení (Congestion Control) pro zmírnění přetížení, řízení výkonu (Power Control) pro správu vysílacího výkonu v uplinku a downlinku a řízení předávání spojení (Handover Control) pro správu mobility UE mezi buňkami, včetně měkkého předání (soft handover), kdy je UE připojeno k více Node B současně. C-RNC spravuje makrodiverzitní kombinování a rozdělování (macro-diversity combining and splitting) pro tyto měkké handovery, což je charakteristický rys WCDMA-based UMTS.

Z pohledu protokolů hostuje C-RNC vrstvy radiové síťové vrstvy (Radio Network Layer, [RNL](/mobilnisite/slovnik/rnl/)). Implementuje protokol řízení rádiových zdrojů (Radio Resource Control, [RRC](/mobilnisite/slovnik/rrc/)), který je zodpovědný za vytváření, konfiguraci, údržbu a uvolňování RRC spojení mezi UE a UTRAN. C-RNC také zpracovává vrstvy řízení rádiového spoje (Radio Link Control, [RLC](/mobilnisite/slovnik/rlc/)) a řízení přístupu k médiu (Medium Access Control, [MAC](/mobilnisite/slovnik/mac/)) pro uživatelská a řídicí data. Je to bod, kde se typicky aplikuje šifrování a ochrana integrity pro komunikaci na rádiovém rozhraní. Funkcionalita C-RNC se liší od funkce obsluhujícího RNC (Serving RNC, S-RNC) nebo driftujícího RNC (Drift RNC, D-RNC), ačkoli jedna fyzická RNC jednotka často plní více logických rolí (C-RNC, S-RNC) pro dané spojení UE.

## K čemu slouží

C-RNC byl vytvořen jako součást architektury UMTS za účelem centralizace a inteligentní správy komplexních funkcí rádiových zdrojů a mobility vyžadovaných technologií [WCDMA](/mobilnisite/slovnik/wcdma/). Předchozí systémy 2G, jako GSM, se spoléhaly na řadič základnových stanic (Base Station Controller, BSC), ale zavedení CDMA s jeho schopností měkkého předání a přísnějšími požadavky na řízení výkonu si vyžádalo sofistikovanější řadič. C-RNC řeší problém koordinace více Node B, řízení interference v CDMA systému a umožnění plynulé mobility.

Jeho vytvoření bylo motivováno potřebou oddělit komplexní funkce řídicí roviny a správy zdrojů od jednodušších úkolů přenosu/příjmu rádiového signálu v Node B. Toto hierarchické rozdělení umožňuje efektivnější sdružování zdrojů, lepší škálovatelnost a centralizovanou implementaci pokročilých RRM algoritmů. Koncept C-RNC spolu s rozhraním Iur také řešil omezení starších architektur tím, že umožnil přímou komunikaci RNC-RNC, která je klíčová pro efektivní měkká a tvrdá předání spojení mezi RNC bez nutnosti vždy zapojovat jádro sítě, čímž se snižuje latence a signalizační zátěž.

## Klíčové vlastnosti

- Ukončuje rozhraní Iub a řídí jeden nebo více Node B
- Provádí funkce správy rádiových zdrojů (RRM) včetně řízení přístupu (Admission Control) a řízení zahlcení (Congestion Control)
- Spravuje specifické pro WCDMA měkké předání spojení (soft handover) a makrodiverzitní kombinování
- Implementuje algoritmy řízení výkonu (Power Control) pro uplink a downlink
- Hostuje vrstvu protokolu RRC pro vytváření spojení a správu mobility
- Poskytuje šifrování a ochranu integrity pro komunikaci na rádiovém rozhraní

## Definující specifikace

- **TS 25.425** (Rel-19) — UTRAN Iur Interface User Plane Protocols

---

📖 **Anglický originál a plná specifikace:** [C-RNC na 3GPP Explorer](https://3gpp-explorer.com/glossary/c-rnc/)
