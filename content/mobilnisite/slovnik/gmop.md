---
slug: "gmop"
url: "/mobilnisite/slovnik/gmop/"
type: "slovnik"
title: "GMOP – Group Management OPeration"
date: 2025-01-01
abbr: "GMOP"
fullName: "Group Management OPeration"
category: "Management"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/gmop/"
summary: "GMOP je protokol pro správu skupin zařízení v sítích Machine-Type Communication (MTC) a IoT. Umožňuje operátorům sítí efektivně hromadně konfigurovat, monitorovat a řídit velký počet MTC zařízení namí"
---

GMOP je protokol pro správu skupin zařízení v sítích Machine-Type Communication a IoT, který umožňuje efektivní hromadnou konfiguraci, monitorování a řízení za účelem snížení signalizační režie.

## Popis

Skupinová managementová operace (Group Management OPeration, GMOP) je protokol definovaný 3GPP pro efektivní správu skupin zařízení Machine-Type Communication ([MTC](/mobilnisite/slovnik/mtc/)), známých také jako zařízení Internetu věcí (IoT). Funguje jako součást architektury MTC a umožňuje hromadné operace na zařízeních patřících do definované skupiny. GMOP je specifikován pro komunikaci mezi MTC serverem (často aplikačním serverem v síti nebo cloudu) a funkcí MTC Interworking Function ([MTC-IWF](/mobilnisite/slovnik/mtc-iwf/)) nebo přímo s entitami sítě 3GPP. Jeho hlavní funkcí je umožnit operátorům sítí nebo poskytovatelům služeb provádět úlohy správy na základě skupiny, což je zásadní pro škálovatelnost vzhledem k potenciálně obrovskému počtu IoT zařízení.

Protokol podporuje sadu skupinových managementových operací. Ty zahrnují skupinové doručování zpráv (Group Message Delivery) pro odesílání downlink zpráv (jako jsou aktualizace firmwaru nebo konfigurační příkazy) všem zařízením ve skupině současně nebo podle plánu. Dále zahrnuje skupinovou konfiguraci (Group Configuration), při které lze parametry, jako jsou intervaly hlášení, nastavení QoS nebo bezpečnostní politiky, nasadit na celou skupinu. GMOP také umožňuje skupinové monitorování a diagnostiku (Group Monitoring and Diagnostics), což umožňuje sbírat agregované stavové hlášky nebo indikátory alarmů ze skupiny zařízení a poskytovat celkový přehled o stavu skupiny bez nutnosti dotazovat každé zařízení jednotlivě.

Z architektonického hlediska jsou zprávy GMOP přenášeny přes standardizovaná rozhraní, jako je Tsp odkazované ve specifikaci 24.481. MTC-IWF funguje jako brána, která překládá požadavky GMOP z MTC serveru na odpovídající signalizaci sítě 3GPP (např. směrem k [HSS](/mobilnisite/slovnik/hss/), [MME](/mobilnisite/slovnik/mme/) nebo [SGSN](/mobilnisite/slovnik/sgsn/)) nebo spouští procedury spouštění zařízení (device triggering). Klíčovým konceptem je identifikátor MTC skupiny (MTC Group Identifier), který jednoznačně identifikuje sadu zařízení sdílejících společné charakteristiky nebo předplatná. Použitím tohoto identifikátoru může síť efektivně aplikovat politiky, směrovat zprávy a spravovat prostředky pro celou skupinu. GMOP významně snižuje zátěž signalizace řídicí roviny v jádru sítě, která by jinak vznikla, pokud by se každé z tisíců či milionů zařízení spravovalo pomocí individuálních relací, což činí rozsáhlá nasazení IoT proveditelnými a nákladově efektivními.

## K čemu slouží

GMOP byl vytvořen, aby řešil výzvy škálovatelnosti spojené se správou obrovského počtu zařízení Machine-Type Communication v celulárních IoT sítích. Tradiční paradigma správy zařízení, navržené pro mobilní telefony zaměřené na člověka, zahrnuje signalizaci na jedno zařízení pro konfiguraci, aktualizace a monitoring. Aplikace tohoto modelu na IoT s projekcí desítek miliard zařízení by způsobila nepřijatelnou signalizační zahlcení v jádru sítě a přetížila systémy operační podpory.

Řeší problém provozní efektivity a síťového zatížení pro hromadná nasazení IoT. Umožněním hromadných operací – například odeslání jediného příkazu ke konfiguraci celé skupiny senzorů – GMOP drasticky snižuje počet požadovaných individuálních transakcí. Tím se snižuje signalizační režie na síťových uzlech, jako jsou [MME](/mobilnisite/slovnik/mme/), [SGSN](/mobilnisite/slovnik/sgsn/) a [HSS](/mobilnisite/slovnik/hss/), šetří se rádiové zdroje a snižuje latence úloh správy. Zjednodušuje také pracovní postupy pro poskytovatele IoT služeb, kteří tak mohou spravovat flotily zařízení jako logické entity.

Jeho vývoj byl motivován prací 3GPP na vylepšeních MTC počínaje Release 10 a dále zpřesňován v pozdějších releasech. GMOP, představený v Release 13, je součástí sady funkcí (společně se spouštěním zařízení, přenosem malých dat a režimem úspory energie) navržených pro optimalizaci celulárních sítí pro IoT. Odráží posun od správy na bázi jednotlivých zařízení ke správě orientované na skupiny, což je zásadní pro ekonomickou a technickou životaschopnost rozsáhlých IoT služeb nad sítěmi 3GPP.

## Klíčové vlastnosti

- Hromadná aktualizace konfigurace pro skupiny zařízení
- Skupinové doručování zpráv pro downlink příkazy nebo aktualizace
- Agregované stavové monitorování a hlášení ze skupin zařízení
- Podpora plánovaných skupinových operací
- Použití identifikátoru MTC skupiny pro adresování
- Snížení signalizační režie na jednotlivá zařízení

## Související pojmy

- [MTC – Machine Type Communications](/mobilnisite/slovnik/mtc/)
- [MTC-IWF – Machine Type Communications - InterWorking Function](/mobilnisite/slovnik/mtc-iwf/)

## Definující specifikace

- **TS 24.481** (Rel-19) — Mission Critical Services (MCS) group management

---

📖 **Anglický originál a plná specifikace:** [GMOP na 3GPP Explorer](https://3gpp-explorer.com/glossary/gmop/)
